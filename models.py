from django.db import models

# Create your models here.
class Tasks(models.Model):

	id=models.PositiveIntegerField(primary_key=True)
	title=models.CharField(max_length=100)
	descripation=models.CharField(max_length=300)
