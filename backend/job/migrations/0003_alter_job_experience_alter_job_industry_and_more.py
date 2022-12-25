# Generated by Django 4.1.4 on 2022-12-25 14:20

import django.core.validators
from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_industry_alter_job_lastdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(choices=[('未経験', 'No Experience'), ('1年', 'One Year'), ('2年', 'Two Year'), ('3年以上', 'Three Year Plus')], default='未経験', max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='industry',
            field=models.CharField(choices=[('ビジネス', 'Business'), ('IT', 'It'), ('金融', 'Banking'), ('教育', 'Education'), ('通信', 'Telecommunication'), ('その他', 'Others')], default='ビジネス', max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='lastDate',
            field=models.DateTimeField(default=job.models.return_date_time),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000000)]),
        ),
    ]
