from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Tag1(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Анатомия и морфология растений'
    def __str__(self):
        return self.name

class Tag2(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Биоразнообразие'
    def __str__(self):
        return self.name

class Tag3(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Биохимия'
    def __str__(self):
        return self.name

class Tag4(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Ботаника (другое)'
    def __str__(self):
        return self.name

class Tag5(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Зоология беспозвоночных'
    def __str__(self):
        return self.name

class Tag6(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Зоология позвоночных'
    def __str__(self):
        return self.name

class Tag7(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Физиология растений'
    def __str__(self):
        return self.name

class Tag8(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Человек'
    def __str__(self):
        return self.name

class Tag9(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Другое'
    def __str__(self):
        return self.name

class Tag10(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Микробиология'
    def __str__(self):
        return self.name

class Tag11(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Темы'
        verbose_name_plural = 'Молекулярная и клеточная биология'
    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_url', kwargs={'slug': self.slug})
class Question(models.Model):
    id = models.AutoField
    year = models.IntegerField('Год')
    stage = models.CharField('Этап', max_length=100)
    grade = models.IntegerField('Класс')
    part = models.IntegerField('Часть')
    number = models.IntegerField('Номер')
    text = models.TextField('Текст вопроса')
    answer = models.CharField('Ответ', max_length=100)
    comment = models.TextField('Комментарий, разбор', blank=True)
    image = models.ImageField(blank=True, upload_to='q/')
    imageA = models.ImageField(blank=True, upload_to='a/')
    tags = models.ManyToManyField(Tag, blank=True, related_name='qs')
    #author = models.CharField(max_length=100)
    Tag1 = models.ManyToManyField(Tag1, blank=True)
    Tag2 = models.ManyToManyField(Tag2, blank=True)
    Tag3 = models.ManyToManyField(Tag3, blank=True)
    Tag4 = models.ManyToManyField(Tag4, blank=True)
    Tag5 = models.ManyToManyField(Tag5, blank=True)
    Tag6 = models.ManyToManyField(Tag6, blank=True)
    Tag7 = models.ManyToManyField(Tag7, blank=True)
    Tag8 = models.ManyToManyField(Tag8, blank=True)
    Tag9 = models.ManyToManyField(Tag9, blank=True)
    Tag10 = models.ManyToManyField(Tag10, blank=True)
    Tag11 = models.ManyToManyField(Tag11, blank=True)

    def __str__(self):
        return '{}'.format(self.text)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-id']

    def __str__(self):
        clear_id = str(self.text)[:30] + '... ' + str (self.comment)[:20] + '...'
        return clear_id

from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.AutoField

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Solved(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    question_id = models.IntegerField('ID')
    user_score = models.FloatField('Балл')
    max_score = models.FloatField('Максимум')
    user_answer = models.CharField('Ответ', max_length=100)
    time = models.TimeField('Время', auto_now=True)


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
