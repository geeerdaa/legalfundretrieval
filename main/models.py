from django.db import models


class User(models.Model):
    name = models.CharField('Your name', max_length=50)
    email = models.EmailField('Email address')
    phone = models.PositiveIntegerField('Your Phone')
    company = models.CharField('Scam company name', max_length=50)
    date = models.DateField('Last transaction date', max_length=50)
    story = models.TextField('Tell your story')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/index.html/{self.id}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'