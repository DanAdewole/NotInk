from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Note(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	def __str__(self) -> str:
		return self.title

	def get_absolute_url(self):
		return reverse("notes_detail", kwargs={"pk": self.pk})
	
