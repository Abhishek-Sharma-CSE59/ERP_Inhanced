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


document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".card").forEach(card => {
        card.addEventListener("click", function(event) {
            event.preventDefault(); 

            let category = this.querySelector("p").innerText.trim();  
            console.log("Clicked category:", category);  

        
            if (category && category !== "Profile-Icon.png") {
                window.location.href = `/category/${category}`;
            } else {
                console.error("Invalid category detected!");
            }
        });
    });
});


document.addEventListener("DOMContentLoaded", function() {
    let searchInput = document.querySelector("nav input");

    if (searchInput) {
        searchInput.addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                let searchQuery = this.value.trim();
                console.log("Search Query:", searchQuery); 
                
                if (searchQuery) {
                    window.location.href = `/category/${encodeURIComponent(searchQuery)}`;
                }
            }
        });
    } else {
        console.error("Search input not found!");
    }
});


