if (navigator.geolocation){
  navigator.geolocation.getCurrentPosition(exportPosition, errorPosition);

} else {
  alert('Sorry your browser doesn\'t suppoert Geolocation. Type in your zip');
}

function exportPosition(){
     console.log('made it');
}

function errorPosition(){
    alert('Sorry couldn\'t find your location');
}