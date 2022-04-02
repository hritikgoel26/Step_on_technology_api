from django.db import models

# Create your models here.
class Parents(models.Model):
    family_number=models.IntegerField()

    def __str__(self):
        return self.family_number

class Child(models.Model):
    number_of_children=models.IntegerField()
    family_number= models.ForeignKey(Parents,on_delete=models.CASCADE,related_name='number_of_children')

    def __str__(self):
        return self.number_of_children
