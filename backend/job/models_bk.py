from datetime import *
from django.db import models
from django.contrib.auth.models import User

import geocoder
import os

from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point

from django.core.validators import MinValueValidator, MaxLengthValidator
# Create your models here.


class JobType(models.TextChoices):
    Permanent = '正社員'
    Temporary = '契約社員'
    Intership = 'インターン'
    Others = 'その他'


class Education(models.TextChoices):
    HighScools = "高校卒"
    TechnicalSchools = "専門卒"
    JuniorColleges = "短大卒"
    Bachelors = '大卒'
    Masters = '修士'
    Phd = '博士'
    Others = 'その他'


class Industry(models.TextChoices):
    Business = "ビジネス"
    IT = "IT"
    Banking = "金融"
    Education = '教育'
    Telecommunication = '通信'
    Others = 'その他'


class Experience(models.TextChoices):
    NO_EXPERIENCE = '未経験'
    ONE_YEAR = '1年'
    TWO_YEAR = '2年'
    THREE_YEAR_PLUS = '3年以上'


def return_date_time():
    now = datetime.now()
    return now + timedelta(days=10)


class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    jobType = models.CharField(
        max_length=10,
        choices=JobType.choices,
        default=JobType.Permanent
    )
    education = models.CharField(
        max_length=10,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry = models.CharField(
        max_length=20,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience = models.CharField(
        max_length=10,
        choices=Experience.choices,
        default=Experience.NO_EXPERIENCE
    )
    salary = models.IntegerField(default=1, validators=[
        MinValueValidator(1), MaxLengthValidator(1000000)])
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0, 0.0))
    lastDate = models.DateTimeField(default=return_date_time())
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapquest(self.address, key=os.environ.get('GEOCODER_API'))

        print(g)

        lng = g.lng
        lat = g.lat

        self.point = Point(lng, lat)
        super(Job, self).save(*args, **kwargs)
