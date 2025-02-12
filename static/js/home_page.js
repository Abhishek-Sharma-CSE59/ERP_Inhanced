document.getElementById("menu-btn").addEventListener("click", function() {
    document.getElementById("sidebar").style.left = "0";
});

document.getElementById("close-btn").addEventListener("click", function() {
    document.getElementById("sidebar").style.left = "-250px";
});


document.addEventListener("click", function(event) {
    let sidebar = document.getElementById("sidebar");
    let menuBtn = document.getElementById("menu-btn");

    if (!sidebar.contains(event.target) && !menuBtn.contains(event.target)) {
        sidebar.style.left = "-250px";
    }
});


document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("click", function(event) {
        event.preventDefault(); 

        
        let categoryText = this.innerText.trim().split(" ")[0];  
        console.log("Clicked category:", categoryText);  


        window.location.href = `/category/${categoryText}`;
    });
});

document.querySelector("nav input").addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        let searchQuery = this.value.trim();
        if (searchQuery) {
            window.location.href = `/category/${searchQuery}`; 
        }
    }
});


document.querySelector("#search-bar").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        let searchQuery = this.value.trim();
        if (searchQuery) {
            console.log("🔍 Searching for:", searchQuery);  
            window.location.href = `/search?query=${encodeURIComponent(searchQuery)}`;
        }
    }
});