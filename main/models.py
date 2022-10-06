from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='Users', null=True, blank=True)
    phone = models.CharField(max_length=12, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Contacts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    contact = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='contact')

    def __str__(self):
        return self.user.username


class Groups(models.Model):
    creator = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='Groups', null=True, blank=True)
    admins = models.ManyToManyField(Users, related_name='admins')
    username = models.CharField(max_length=255, unique=True, null=True)
    link = models.CharField(max_length=255, unique=True, null=True)
    is_private = models.BooleanField(default=True)
    users = models.ManyToManyField(Users, related_name='users')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Channels(models.Model):
    creator = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='Channels', null=True, blank=True)
    admins = models.ManyToManyField(Users, related_name='admins')
    username = models.CharField(max_length=255, unique=True, null=True)
    link = models.CharField(max_length=255, unique=True, null=True)
    is_private = models.BooleanField(default=True)
    users = models.ManyToManyField(Users, related_name='users')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
