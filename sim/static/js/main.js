document.addEventListener("DOMContentLoaded", (event) => {
    const item = document.querySelectorAll(".item-menu-link")
    item.forEach(function(item){
        item.addEventListener('click', function(){
            const submenu = this.closest("li.item-menu");
            submenu.classList.toggle("down");
        });
    });
});