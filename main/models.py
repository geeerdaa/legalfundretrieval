from django.db import models


class Persone(models.Model):
    name = models.CharField('Your name', max_length=50)
    email = models.EmailField('Email address')
    phone = models.CharField('Your Phone', max_length=20)
    company = models.CharField('Scam company name', max_length=50)
    date = models.CharField('Last transaction date', max_length=10)
    story = models.TextField('Tell your story')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/index.html/'

    class Meta:
        verbose_name = 'Persone'
        verbose_name_plural = 'Personens'


class Contacts(models.Model):
    name = models.CharField('Your name', max_length=50)
    email = models.EmailField('Email address')
    phone = models.CharField('Your Phone', max_length=52)
    story = models.TextField('Tell your story')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/index.html/'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'