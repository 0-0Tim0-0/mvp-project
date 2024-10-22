function pls_work() {
    let username = document.getElementById("username");
    if (username.style.display === "none") {
        username.style.display = "flex" ;
    } else {
        username.style.display = "none"
    }
}