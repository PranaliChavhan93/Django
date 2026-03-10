from django.db import models
from django.contrib.auth.models import User


class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True) 
    recp_name = models.CharField(max_length=100)
    recp_desc = models.TextField()
    recp_imag = models.ImageField(upload_to="receipe")

