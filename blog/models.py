from django.db import models
'''
post : category = N : 1
post : tag = M : N
post : comment = 1 : N
'''
# Create your models here.

class Post(models.Model):
    pass

class Category(models.Model):
    pass

class Tag(models.Model):
    pass

class Comment(models.Model):
    pass