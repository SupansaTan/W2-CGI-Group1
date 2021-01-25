var i, total = 1;
var time = new Date();

function factorial(){
    var num = Number(document.getElementById("fnum").value);
    
    if (num == 0 || num == 1){
        total = 1;
    }
    else {
        for (i=1; i<= num; i++){
            total *= i;
        }
    }
    document.getElementById("result").innerHTML = total;
}
