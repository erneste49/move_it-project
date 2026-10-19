
export default class Api {
    constructor(baseUrl){
        this.baseUrl = baseUrl;
    }
    //the method below sends request to an endpoint and handles result gracefully
    async fetchAllPosts(){
        try{
            const res = await fetch(` ${this.baseUrl}/post/all/ `);
            const posts = await res.json();
            //console.table(posts);    //used to check for data that was sent from server

            if (posts.status == "success"){
                console.log(posts.data);
                
                return posts
            }else{
                return {...posts, msg:"error from the server"}
            }

        }catch(error){
            console.log(error);
            return {...error, msg:"Sorry the server is down at the moment "}
        }
    }

    async fetchSinglePost(id){
        try{
            const res = await fetch(` ${this.baseUrl}/post/single/${id} `);
            const post = await res.json();
           // console.table(post)   //to check what was returned from server
            
            if (post.status == "success"){
                return post
            }else{
                return {...post, errorCode:true }
            }
        }catch(error){
            return {...error, errorCode:2, message: "Error connecting with the server"}
        }
    }
}