function go(){
    var array = new Array();
    array[0] = "Red";
    array[1] = "Blue";
    array[3] = "Green";
    for (var i=0; i < array.length; i++){
        document.write("<li>" + array[i] + "<br />");
    }
}