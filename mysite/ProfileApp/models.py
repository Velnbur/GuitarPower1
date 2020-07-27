from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='USER')
    face_image = models.ImageField(upload_to='icons/',
                                   verbose_name='Icon',
                                   default='icons/FACE_ICON.png',
                                   blank=True,
                                   null=True,)
    birth_date = models.DateField(null=True, blank=True, default=None)
    about_myself = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return "Профиль %s" % self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profilemodel.save()
