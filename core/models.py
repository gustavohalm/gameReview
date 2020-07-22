from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    star = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    user_id = models.BigIntegerField()
    game_id = models.BigIntegerField()


class Comment(models.Model):
    text = models.CharField(max_length=1024)
    user_id = models.BigIntegerField()
    game_id = models.BigIntegerField()
