function copyText() {
    let text = document.getElementById("outText");
    text.select();
    text.setSelectionRange(0, 99999)
    document.execCommand("copy");    
     
    console.log(text.value);
}   
