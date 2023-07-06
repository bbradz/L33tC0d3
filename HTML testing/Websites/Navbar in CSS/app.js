const button = document.getElementById("color-changer");
const body = document.body;

    if (body.classlist.contains('light')) {
        body.classlist.replace('light', 'dark');
    }
    else {
        body.classlist.replace('dark', 'light');
    }

