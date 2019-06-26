from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Friend(models.Model):
	users = models.ManyToManyField(User)
	current_user = models.ForeignKey(User,null=True,related_name='owner',on_delete=models.CASCADE)

	@classmethod
	def make_friend(cls,current_user,new_friend):
		''' method  creating friends 
			friend is the instance of the class and created get passed in the data that
			we are checking after get_or_create call.
			after that we call the friend instance and say it to add a new friend to our list which
			is current_user 

		'''
		friend,created = cls.objects.get_or_create(current_user=current_user)
		friend.users.add(new_friend)

	@classmethod 
	def lose_friend(cls,current_user,new_friend):
		friend,created = cls.objects.get_or_create(current_user=current_user)
		friend.users.remove(new_friend)







class Post(models.Model):
	user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text




class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='user_image')
	bio_data = models.TextField()
	city = models.CharField(max_length=200)
	website = models.URLField()

	def __str__(self):
		return f'{self.user.username} Profile'

def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)
