from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# from django.contrib.auth.models import User
# Create your models here.


class Snack(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title  # or "%s %s" % (self.title, self.last_name)

    def get_absolute_url(self):
        return reverse("snack_detail", kwargs={"pk": self.pk})
