var header = document.getElementById("heading");

function headerResize() {
        if($(window).width() >= 550){       //if window is smaller than 550px wide, change header
        header.innerHTML = "7034 | To Be Determined";
    }else{
        header.innerHTML = "7034 | TBD";
    }
}

headerResize();
