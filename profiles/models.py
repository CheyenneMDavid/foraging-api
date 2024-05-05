from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model stores the user information linked to the Django
    User model. It includes timestamps for creation and updates, a name field,
    an optional content field, and an image field.
    """

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Owner",
        help_text="The user that this profile belongs.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
        help_text="Date and time when the profile was created.",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at",
        help_text="Date and time when the profile was last updated.",
    )

    name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Name",
        help_text="The name of the user for this profile.",
    )

    content = models.TextField(
        blank=True,
        verbose_name="Content",
        help_text="Additional content or description for the user's profile.",
    )

    image = models.ImageField(
        upload_to="images/",
        default="../default_profile_pic_ciw1he.jpg",
        verbose_name="Profile Image",
        help_text="The profile image for the user.",
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a Profile instance when a new User instance
    is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
