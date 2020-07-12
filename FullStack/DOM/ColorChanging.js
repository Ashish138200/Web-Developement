var header = document.querySelector("h1")
header.style.color = 'red'

function getRandomColor(){
    var letters = "0123456789ABCDEF";
    var color = '#';
    for(var i = 0; i<6;i++){
      color+=letters[Math.floor(Math.random()*16)];
    }
    return color
}

function changeHeaderColor(){
    colorInput = getRandomColor()
    header.style.color = colorInput;
}

setInterval("changeHeaderColor()",500);

//-----------------------------------------------Content Iteraction-----------------------------------------------------
var p =document.querySelector('p')
p.textContent = "new Blah Blah";

p.innerHTML = "<b>Bold Blah Blah</b>"

var sp = document.querySelector("#spid")
sp.getAttribute("href")
sp.setAttribute("href","https://www.amazon.com")
console.log(sp)

//----------------------------------------------------Events------------------------------------------------------------

var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

headOne.addEventListener('mouseover',function(){
    headOne.textContent = "Mouse Currently Over";
    headOne.style.color = 'red';
})
headOne.addEventListener("mouseout",function(){
    headOne.textContent = "Hover over me";
    headOne.style.color = "black";
})

headTwo.addEventListener("click",function(){
    headTwo.textContent = "Clicked on";
    headTwo.style.color = 'blue'
})

headThree.addEventListener("dblclick",function(){
    headThree.textContent = " Doubled Clicked on";
    headThree.style.color = 'gray'
})