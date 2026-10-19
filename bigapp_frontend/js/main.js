import View from "./View.js"
import Api from "./Api.js"

let view = new View("blog-container")
let api = new Api("http://127.0.0.1:5000/api/v1");

//a function that calls a method that send request to fetch all
async function fetchAndDisplay() {
    let postsAvail = await api.fetchAllPosts(); //calling method incharge of fetching post
    //console.log(postsAvail);
    //console.table(postsAvail)
    if ( postsAvail.status == "success"){
        //console.table(postsAvail.data);
        
        //call the method in charge of looping and displaying post
        view.showAllPost(postsAvail.data)
    }else{
        //call method incharge of displaying error and display error message
        view.showErrorAlert(postsAvail.msg)
    }
}

//a function that call api fetcher for single page and display on dom
async function fetchSinglePostAndDisplay(id){
    let post = await api.fetchSinglePost(id)
    if (post && !post.errorCode){
        //calling a method to collect post and display it on view page
        view.showSinglePost(post.data)
    }else{
        //there is an error
        console.log(post);
        
    }
}


//if page currently view by user is index.html we want to call function fetchAndDisplay, but if the page the user is currently viewing is detail.html we want to call a different method by reading the id in querystring and save it in a variable. if there is no id we want to redirect user back to index.html
let currentPage = window.location.href;
if (currentPage.includes("index.html")){
    fetchAndDisplay();
}else if(currentPage.includes("detail.html")){
    //alert("You are on the detail page") //using alert to see cureent page

    //retrieving id from query string
    const params = new URLSearchParams(window.location.search);
    //alert(params)
    const id = params.get('id')

    //if the id is null
    if (!id || isNaN(id)){
        //alert("invalid post id")
        window.location.href = "index.html"
    }else{
        //alert(id)
        //give the id to a method that fetch post for the id
        fetchSinglePostAndDisplay(id)
    }

}
