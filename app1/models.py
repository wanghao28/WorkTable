from django.db import models

class UserInfo(models.Model):
    name = models.AutoField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(max_length=32)




