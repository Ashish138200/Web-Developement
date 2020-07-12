//alert("Welcome to your bank account");
//var deposit = prompt("How much you wanna deposit? ")
//alert("You've deposited: "+deposit)
//console.log("You're a cool person");
//-------------------------------------------Comparison Operator--------------------------------------------------------
var x = "2" == 2
var y = "2" === 2
//alert("\"2\" == 2: "+x)
//alert("\"2\" === 2: "+y)
//--------------------------------------------------Arrays and for loop---------------------------------------------------
arr=['a','b','c']
for(letter of arr){
    //console.log(letter);
    //alert(letter) //Method-1
}
//arr.forEach(alert) //Method-2

//-------------------------------------------Objects[hashset(Dictionary)]-----------------------------------------------
carInfo={make:"Toyota",year:"2007",model:"Camry"};
for(k in carInfo){
    //console.log(k);
    //console.log(carInfo[k]);
}

//----------------------------------------Function inside an Object-----------------------------------------------------
var myObj = {prop:37,reportProp:function(){
    return this.prop;
}
};
console.log(myObj.reportProp())

var myO = {prop:37,rP:function(){
    console.log("Method called");
}
};
myO.rP()