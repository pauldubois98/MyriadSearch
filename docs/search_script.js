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
      query = elemInput.value;
      /*query.split(' ').forEach(function(e){
        if(e.length>5){
          console.log(e);
        }
      });*/
      //window.location.replace("https://www.legislation.gov.uk/all?text=strike");
      location.href = '/search?q="'+query+'"';
    }
  };




//elemDiv.innerText = elemInput.value;
