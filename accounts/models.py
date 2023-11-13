from django.db import models

#AbstractUserクラスをインポートする
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    pass