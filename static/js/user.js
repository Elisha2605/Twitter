////////// UPDATE USER IMAGE /////////
async function userUploadCoverImage(user_id) {
    const form = event.target.form

    const connection = await fetch(`/api-user-upload-cover/${user_id}`, {
        method: "PUT",
        body: new FormData(form)
    })
    if (!connection.ok) {
        alert('Uuup... connection failed') 
        return
    }
    try {
        const res = await connection.json();
        console.log(res.image_cover_image);


        let banner = document.querySelector(".banner");
        let user_cover_image = `
            <img class="cover object-cover w-full" src="/static/images/user_cover_image/${res.image_cover_image}" onError="this.onerror=null;this.src='/static/images/user_profile_pictures/default_profile_picture.png';">
        `
        document.querySelector(".cover-to-remove").remove()
        banner.insertAdjacentHTML("afterbegin", user_cover_image)
        document.querySelector(".spa-modal-cover-image").style.display = "none"
        

    } catch (error) {
        console.log("Error: ", error.message);
    }
    
}


////////// FOLLOW /////////
async function follow(user_id) {
    const followbtn = document.querySelectorAll('.follow-account')
    const connection = await fetch(`/api-user-follow/${user_id}`, {
        method : "POST",
    })
    if (!connection.ok) {
        alert('Uuuups, connexion failed')
    }
    
    const res = await connection.json()
    const server_message = res.server_message
    console.log(server_message);
    window.location.reload()

    followbtn.forEach((btn) => {
        if (btn.id === user_id && btn.value == "YES") {
            btn.value = "NO"
            
            console.log("following user: ", user_id);
        } else if (btn.id === user_id && btn.value == "NO") {
            btn.value = "YES"
            
            console.log("unfollowing user: ", user_id);
        } 

    })
     
}



/////// <div id="10b"></div>


const element = document.querySelector("[id='10b']")

element.remove()