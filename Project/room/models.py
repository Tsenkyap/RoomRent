from django.db import models


class Room(models.Model):
	rooms_name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	owner_name = models.CharField(max_length=200)
	owner_number = models.IntegerField()
	rooms_summary = models.TextField()
	number_of_room = models.IntegerField()
	rooms_pic = models.ImageField(upload_to='room_image',null=True,blank=True)

	def __str__(self):
		return self.rooms_name







