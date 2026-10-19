
export default class View{
    constructor(IdToAppend){
        this.IdToAppend = IdToAppend
    }
    showAllPost(posts){
        let postContainer = document.getElementById(this.IdToAppend);
        postContainer.classList.add("post-container");
        postContainer.innerHTML = ""    //to remove posts loading from page and everypther thing in post-container
        posts.forEach(function(po){
            let singlePostContainer = document.createElement("div")
            singlePostContainer.classList.add("single-post")
            let titleH2 = document.createElement("h2")
            titleH2.textContent = po.post_title;
            let poImage = document.createElement("img")
            poImage.src = po.post_image;
            poImage.alt = `BigApp: ${po.post_title}`
            let readMoreLink = document.createElement("a")
            readMoreLink.href = "detail.html?id=" + po.post_id;
            readMoreLink.textContent = "Read More";
            readMoreLink.classList.add("post_detail_link") 
            
            singlePostContainer.append(titleH2, poImage, readMoreLink)

            // document.getElementById(this.IdToAppend).append(titleH2, poImage, readMoreLink);
            postContainer.append(singlePostContainer);
        })
    }

    //a method to show single post
    showSinglePost(post){
        let postDiv = document.getElementById(this.IdToAppend);
        postDiv.innerHTML = "";
        postDiv.innerHTML = `
        <h1> ${post.post_title} </h1>
        <img src="${post.post_image}" alt="${post.post_title}" />
        <p> ${post.post_content} </p>
        `;
    }

    //this method create an error alert and append it to div of post-container
    showErrorAlert(message){
        document.getElementById(this.IdToAppend).innerHTML = `
            <p class="alert alert-warning" > 
                ${message}
            </p>
        `
    }
}