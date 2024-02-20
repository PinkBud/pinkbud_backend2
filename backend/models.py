from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, unique = True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
class UserPost(models.Model):
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    img = models.URLField(null=True)

    def __str__(self):
        return self.title

class Therapist(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    description = models.CharField(max_length=200)
    img = models.URLField(null=True)
    certificate = models.URLField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Lawyer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    description = models.CharField(max_length=200)
    img = models.URLField(null=True)
    certificate = models.URLField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ngo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    description = models.CharField(max_length=200)
    img = models.URLField(null=True)
    certificate = models.URLField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Opportunity(models.Model):
    title = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    prize = models.IntegerField()
    certification = models.BooleanField()
    date = models.DateTimeField()
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


#class Chatroom(models.Model):
