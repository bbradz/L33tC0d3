const button = document.getElementById("light");
const body = document.body;

button.onclick = () => {
    if (body.classList.contains('light')) {
        body.classList.replace('light','dark');
    }
    else {
        body.classList.replace('dark','light');
    }
}