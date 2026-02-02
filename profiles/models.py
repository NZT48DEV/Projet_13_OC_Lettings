from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Represents a user profile linked to a Django user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns the username associated with the profile.
        """
        return self.user.username
