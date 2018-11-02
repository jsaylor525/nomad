var i = 0;
var original = document.getElementById('movementEntry');

function addNewMovement() {
   var clone = original.cloneNode(true); // "deep" clone
   clone.id = "movementEntry" + ++i; // there can only be one element with an ID
   original.parentNode.appendChild(clone);  
}

function removeMovement(obj) {
   var node = obj
   var nodeToRemove = node.parentNode.parentNode
   if ( original.id === nodeToRemove.parentElement.id ) {
      console.log("Attempted to remove last movement")
   }
   else {
      nodeToRemove.parentNode.remove(nodeToRemove)
   }
}

$( function() {
   $( ".sortable" ).sortable();
   $( ".sortable" ).disableSelection();
 } );

document.getElementById('addAnotherMovement').onclick = addNewMovement;
document.getElementsByClassName('remove-movement').onclick = removeMovement;
