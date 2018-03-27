from django.db import models
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple
from django.contrib import admin
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z\s\w]+$', 'Only alphanumeric characters are allowed.')

class Company(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Wallet(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50, validators=[alphanumeric])
    companies = models.ManyToManyField(Company)

    def __str__(self):
        return self.name

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class ImageCompany(models.Model):
    company = models.CharField(max_length=20)
    image = models.URLField()

    def __str__(self):
        return self.company

class NewsCompany(models.Model):
    company = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    link = models.URLField()
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.company

class DescriptionCompany(models.Model):
    company = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    website = models.URLField()
    sector = models.CharField(max_length=50)
    employees = models.CharField(max_length=50)
    sales = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)

    def __str__(self):
        return self.name
