from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    total_xp = models.IntegerField()
    total_coins = models.IntegerField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField
    difficult = models.IntegerField
    total_xp = models.IntegerField
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Reward(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    price = models.IntegerField()
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    block = models.BooleanField(default=False)
    status = models.IntegerField(default=0)
    difficult = models.IntegerField()
    task_xp = models.IntegerField()
    coins = models.IntegerField(default=0)
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    skill = models.ForeignKey(to='Skill', on_delete=models.CASCADE)

    def __str__(self):
        return self.title