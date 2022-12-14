from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from .fields import NonStrippingTextField


class Tag(models.Model):
	name = models.CharField(max_length=15)
	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	def __str__(self) -> str:
		return self.name

	def get_absolute_url(self):
		return reverse('label_list')
	


class Note(models.Model):
	title = models.CharField(max_length=200)
	body = NonStrippingTextField()
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	tag = models.ForeignKey(
		Tag,
		on_delete=models.CASCADE,
	)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['date_updated']

	def __str__(self) -> str:
		return self.title

	def get_absolute_url(self):
		return reverse("notes_detail", args=[str(self.id)])
	
