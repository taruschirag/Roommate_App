# from django.db import models
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     age = models.IntegerField()
#     interests = models.TextField()
#     preferences = models.JSONField()

# class UserImage(models.Model):
#     user = models.ForeignKey(User, related_name="images", on_delete=models.CASCADE)
#     image = models.URLField()
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.image.url}"
# users/models.py


from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)

    age = models.IntegerField()

    interests = models.TextField()
    preferences = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["age"]

    def __str__(self):
        return self.username


class UserImage(models.Model):
    user = models.ForeignKey(User, related_name="images", on_delete=models.CASCADE)
    image = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.image}"

