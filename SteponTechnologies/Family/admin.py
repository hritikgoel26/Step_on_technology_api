from django.contrib import admin
from .models import Parents,Child

# Register your models here.
@admin.register(Parents)
class ParentsAdmin(admin.ModelAdmin):
    list_display=['id','family_number']


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display=['id','number_of_children']
