from django.contrib import admin
from .models import Movement, Equipment, Workout

def make_movement(modeladmin, request, queryset):
    queryset.update(status='p')
make_movement.short_description = "Mark selected movements as created"

class WorkoutInline(admin.StackedInline):
   model = Workout.movements.through
   extra = 1

class MovementAdmin(admin.ModelAdmin):
   list_display = [
      "name",
      "category",
      "distance_enable",
      "height_enable",
      "weight_enable",
      "reps_enable",
      "time_enable",
   ]
   ordering = ['name']

class EquipmentAdmin(admin.ModelAdmin):
   pass

class WorkoutAdmin(admin.ModelAdmin):
   inlines = [WorkoutInline]
   pass

# Register your models here.
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Movement, MovementAdmin)
admin.site.register(Equipment, EquipmentAdmin)
