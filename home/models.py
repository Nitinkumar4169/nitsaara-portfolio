from django.db import models


# makemigrations -> creates migration file based on the changes you have made in the models.py file
# migrate -> applies the pending migration to the database and creates tables based on the model you have created  the models.py file


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name