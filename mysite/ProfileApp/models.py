from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
import datetime
from mysite import settings


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='USER')
    face_image = models.ImageField(upload_to='icons/',
                                   verbose_name='Icon',
                                   default='icons/FACE_ICON.png',
                                   blank=True,
                                   null=True,)
    about_myself = models.TextField(null=True, blank=True)
    date_registration = models.DateTimeField(null=True, auto_now_add=True)

    # social network links
    telegram_link = models.CharField(max_length=500, blank=True, default='')
    facebook_link = models.CharField(max_length=500, blank=True, default='')
    whatsapp_link = models.CharField(max_length=500, blank=True, default='')
    vk_link = models.CharField(max_length=500, blank=True, default='')
    instagram_link = models.CharField(max_length=500, blank=True, default='')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return "Профиль %s" % self.user

    def last_seen(self):
        return cache.get('seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                    seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profilemodel.save()
