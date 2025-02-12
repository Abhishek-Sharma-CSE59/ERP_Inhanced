document.getElementById("menu-btn").addEventListener("click", function() {
    document.getElementById("sidebar").style.left = "0";
});

document.getElementById("close-btn").addEventListener("click", function() {
    document.getElementById("sidebar").style.left = "-250px";
});

async function loadClubDetails() {
    let params = new URLSearchParams(window.location.search);
    let clubName = params.get("club") || "Dance Club"; 

    let response = await fetch(`/get_club?club=${clubName}`);
    let club = await response.json();

    document.getElementById("club-name").innerText = club.name;
    document.getElementById("club-description").innerText = club.description;
    document.getElementById("club-timings").innerText = club.timings;
    document.getElementById("club-location").innerText = club.location;


    let photoGallery = document.getElementById("photo-gallery");
    club.photos.forEach(photo => {
        let img = document.createElement("img");
        img.src = `static/images/${photo}`;
        photoGallery.appendChild(img);
    });


    let achievementsList = document.getElementById("achievements-list");
    club.achievements.forEach(achievement => {
        let li = document.createElement("li");
        li.innerText = achievement;
        achievementsList.appendChild(li);
    });


    let awardsList = document.getElementById("awards-list");
    club.awards.forEach(award => {
        let li = document.createElement("li");
        li.innerText = award;
        awardsList.appendChild(li);
    });
}

window.onload = loadClubDetails;
