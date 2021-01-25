var i, total=1;

function factorial(){
    var num = Number(document.getElementById("fnum").value);

    if (num == 0 || num == 1){
        return total;
    }
    else {
        for (i=1; i<= num; i++){
            total *= i;
        }
    }
    document.getElementById("result").innerHTML = total;
    return total;
}
