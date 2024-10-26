/* togge between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function navBarFunction() {
    let x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav"
    }
}
