from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, default='users_image/11.png')
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False

        else:
            return True


class UserProfile(models.Model):

    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'в канавке'),
        (FEMALE, 'жива'),
    )

    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='статус', max_length=128, blank=True)
    gender = models.CharField(verbose_name='состояние матери', max_length=1, choices=GENDER_CHOICES, blank=True)
    aboutMe = models.TextField(verbose_name='О маме', max_length=512, blank=True)

    cordinats = models.TextField(verbose_name='кординаты', max_length=512, blank=True, default=(0, 0))
    telegram = models.TextField(verbose_name='ник', max_length=512, blank=True, default='-')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
