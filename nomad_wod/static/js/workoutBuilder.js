var i = 0;

class Movement {
   constructor(id=0, name='', reps=0, weight=0, height=0, distance=0) {
      this.id        = 0;
      this.name      = 0;
      this.height    = 0;
      this.weight    = 0;
      this.reps      = 0;
      this.distance  = 0;
      this.id        = 0;
      console.log("Created class " + this)
   }

   // Compute the work = force * distance
   computeWork() {
      var work = (this.weight * this.reps * this.distance * this.height);
      console.log("Work for " + this.name + " is: " + work)
      return work;
   }
}

class WorkoutSection {
   constructor() {
      this.movementArray = [new Movement()]
      console.log("Created workout section")
   }

   addNewMovement() {
      this.movementArray.push(new Movement())
      console.log("Added new movement")
   }

   removeMovement(movement) {
      var movementIndex = this.movementArray.findIndex(movementToRemove)
      delete this.movementArray[movementIndex]
      console.log("Remove movement " + movement)
   }

   // Compute the work for all the movements
   computeWork() {
      var work = 0
      this.movementArray.forEach(movement => {
         work += movement.computeWork()
      });
      console.log("Work = " + work)
   }
}

class Workout {
   constructor() {
      this.sectionArray = [new WorkoutSection()]
   }

   addNewSection() {
      this.sectionArray.push[new WorkoutSection()]
   }

   removeSection(section) {
      var sectionIndex = this.sectionArray.findIndex(section)
      delete this.sectionArray[sectionIndex]
      console.log("Remove section " + section)
   }

   // Compute the work for all the sections
   computeWork() {
      var work = 0
      this.sectionArray.forEach(section => {
         work += section.computeWork()
      });
      console.log("Work = " + work)
   }
}

// Store the originalMovement as a template
var originalMovement = document.getElementById('movementEntry0');

function addNewMovement() {
   var clone = originalMovement.cloneNode(true); // "deep" clone
   // var newMovement = new Movement()
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

$( function() {
   $( ".sortable" ).sortable();
   $( ".sortable" ).disableSelection();
 } );

document.getElementById('addAnotherMovement').onclick = addNewMovement;
document.getElementsByClassName('remove-movement').onclick = removeMovement;
