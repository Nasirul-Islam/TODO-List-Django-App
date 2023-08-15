from django.contrib import admin
from first_app.models import TaskModel

# Register your models here.
@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('taskTitle','taskDescription', 'is_completed')
    