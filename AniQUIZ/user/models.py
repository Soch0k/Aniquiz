from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    icon = models.ImageField(upload_to="static/img/user/icon_user", null=True, blank=True,
                             default="static/img/user/icon_user/Standard_icon.png")
