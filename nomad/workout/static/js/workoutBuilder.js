var i = 0;

// Store the originalMovement as a template
var originalMovement = document.getElementById('movementEntry');

function addNewMovement() {
   var clone = originalMovement.cloneNode(true); // "deep" clone
   clone.id = "movementEntry" + ++i; // there can only be one element with an ID
   originalMovement.parentNode.appendChild(clone);  
}

function removeMovement(obj) {
   var node = obj
   var nodeToRemove = node.parentNode.parentNode.parentNode
   if ( originalMovement.id === nodeToRemove.parentElement.id ) {
      console.log("Attempted to remove last movement")
   }
   else {
      nodeToRemove.parentNode.remove(nodeToRemove)
   }
}

var originalWorkout = document.getElementById('movementEntry');

function addNewWorkoutSection() {

}

$( function() {
   $( ".sortable" ).sortable();
   $( ".sortable" ).disableSelection();
 } );

document.getElementById('addAnotherMovement').onclick = addNewMovement;
document.getElementsByClassName('remove-movement').onclick = removeMovement;
