from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	name = models.CharField(max_length=200, null=True)
	number_phone = models.CharField(max_length=17)
	email = models.CharField(max_length=200)
	adress = models.CharField(max_length=200)

	def __str__(self):
		return self.name


@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(
			user=instance
		)
