window.onload = () => {
    document.getElementById("myCoolButton").addEventListener("click", () => {
        document.getElementById("flashes").style.color = "green";
    });
}

function validateForm() {
    let val = document.forms[0].elements[0].value;
    if (val === "jmartin191") {
        return true;
    }
    alert("Wrong campus ID");
    return false;
}