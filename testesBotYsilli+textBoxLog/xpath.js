tt = document.getElementsByClassName("font-regular");
ultimoHistorico = tt[1].rows[0];
histOrdemId = ultimoHistorico.getElementsByClassName("orderid")[0];
winLoss = ultimoHistorico.getElementsByClassName("status")[0];
console.log(histOrdemId.textContent);
if(histOrdemId.textContent == "414060071"){
    if(winLoss.textContent == "lose"){
        console.log("perdi");
    }else{
        console.log("ganhei");
    }
}