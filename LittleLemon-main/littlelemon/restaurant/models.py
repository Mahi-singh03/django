from django.db import models

# Create your models here.
class Booking(models.Model):
	name = models.CharField(max_length=255)
	partysize = models.SmallIntegerField()
	bookingdate = models.DateTimeField()

	def __str__(self):
		return f'{self.name}: {str(self.bookingdate)}'
	
class Menu(models.Model):
	title = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	inventory = models.SmallIntegerField()

	def __str__(self):
		return f'{self.title}: {str(self.price)}'