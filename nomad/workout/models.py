from django.db import models
from django.urls import reverse
from django.contrib.gis.measure import Distance
from measurement.measures import Mass
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Extending Mass with kilogram
NomadMass = Mass
NomadMass.UNITS['kg'] = 1000.0
NomadMass.ALIAS['kilogram'] = 'kg'
NomadMass.SI_UNITS = ['kg']

# Create your models here.
class Movement(models.Model):

   G = "Gymnastics"
   W = "Weight Lifting"
   M = "Monostructural"

   CATEGORY_ABV = {
      G : "G",
      W : "W",
      M : "M",
   }
   CATEGORY_ABV_LOWER = {k.lower(): v for k,v in CATEGORY_ABV.items()}

   # For choices flip the Abveriation and value
   CATEGORY_CHOICES = [(v, k) for k,v in CATEGORY_ABV.items()]

   name = models.CharField(
      max_length=128,
      unique = True,
   )

   category = models.CharField(
      max_length=32, 
      choices=CATEGORY_CHOICES, 
      default=CATEGORY_CHOICES[0],
   )
   
   distance_enable = models.BooleanField(default=False)
   height_enable   = models.BooleanField(default=False)
   weight_enable   = models.BooleanField(default=False)
   reps_enable     = models.BooleanField(default=False)
   calorie_enable  = models.BooleanField(default=False)
   time_enable     = models.BooleanField(default=False)

   body_weight_ratio = models.FloatField(
      help_text="Some movements use a body weight, some movents don't and others are inbetween.",      
      validators=[MaxValueValidator(1.0), MinValueValidator(0.0)],
      default=1.0,
   )

   # class Meta:
   #    order_with_respect_to = 'category'

   def __str__(self):
      return f"{self.name}"

class Equipment(models.Model):
   name = models.CharField(max_length=64,
      unique = True,
   )

   weightType = models.CharField(max_length=32, 
                                 choices={(v, k) for k,v in NomadMass.ALIAS.items()}, 
                                 default=NomadMass.ALIAS['kilogram'])

   weightValue = models.FloatField(default=0.0)

   distanceScalingFactor = models.FloatField(
      default=1.0,
      help_text="Some equipment doesn't have a 1-1 effort, there is usual the baseline, or standard equipment. Use this value to scale the effort to make it eqiuvalent to the standard equipment.",
   )

   caloriesScalingFactor = models.FloatField(
      default=1.0,
      help_text="Some equipment doesn't have a 1-1 effort, there is usual the baseline, or standard equipment. Use this value to scale the effort to make it eqiuvalent to the standard equipment.",
   )
   
   def __str__(self):
      return f"{self.name}"

class Workout(models.Model):
   TASK_PRIORITY_WORKOUT  = "task"
   TIME_PRIORITY_WORKOUT  = "time"
   SKILL_PRIORITY_WORKOUT = "skill"
   DATETIME_FORMAT = "%Y%m%d"
   
   name = models.CharField(
      max_length=32, 
      default=datetime.now().strftime(DATETIME_FORMAT),
      unique = True,
   )

   date = models.DateField( 
      default=timezone.now,
   )

   description = models.TextField(
      max_length=5000,
      null=True,
   )

   movements = models.ManyToManyField(
      to = Movement,
      verbose_name = "list of movements",
   )

   class Meta:
      ordering = ['-name', '-date', '-description',]

   def get_absolute_url(self):
      return reverse("model-detail-view", kwargs={"pk": self.pk})
   

   def __str__(self):
       return self.name
   


