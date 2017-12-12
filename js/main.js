var artboard = $('#artboard');
var layers = data.layers[0].layers;
var currentLayerIndex = 0;

function getArtboardSize(side) {
  return data.layers[0].frame[side] + 'px';
}

function drawArtboard() {
  var artboardWidth = getArtboardSize('width');
  var artboardHeight = getArtboardSize('height');

  artboard.width(artboardWidth).height(artboardHeight);
}

function showNextLayer(current) {
  var currentLayer = layers[current];
  var imageTag = $('<img class="imageLayer" src="./sketch-json/comic/'+ currentLayer.image._ref +'.png" />').css({top: currentLayer.frame.x + 'px', left: currentLayer.frame.y + 'px'});

  artboard.append(imageTag);
  currentLayerIndex++;
}

$(function(){
  var pageJson;
  drawArtboard();

  // show first layer
  showNextLayer(currentLayerIndex);

  artboard.click(function() {
    showNextLayer(currentLayerIndex);
  });
});