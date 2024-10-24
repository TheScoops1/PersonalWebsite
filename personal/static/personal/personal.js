/* togge between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function navBarFunction() {
    let x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav"
    }
}

function subButtonOut(sw) {
    var pic;
    if (sw == 0) {
    pic = "{% static 'personal/images/IceCreamPhoto.jpg' %}"
    } else {
    pic = "{% static 'personal/images/VanillaIceCream.webp' %}"
    }
    document.getElementById('myImage').src = pic;
    let x = document.getElementsByClassName("iceCreamButton")

}