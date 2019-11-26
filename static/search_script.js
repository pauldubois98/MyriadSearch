var elemDiv = document.getElementById('testWidth');
var elemInput = document.getElementById('typeIn');

elemInput.oninput = function() {
  elemDiv.innerText = elemInput.value;
  elemInput.style.width = elemDiv.clientWidth+50+'px';
}

// elemInput.keypress = function(e){
//   if(e.keyCode==13){
//     console.log('enter');
//   }
// };




  elemInput.onkeypress = function(e){
    if(e.keyCode==13){
      console.log('enter');
    }
    // Simulate an HTTP redirect:
    window.location.replace("/");
  };




//elemDiv.innerText = elemInput.value;
