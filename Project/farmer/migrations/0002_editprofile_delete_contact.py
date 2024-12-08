# Generated by Django 4.2.4 on 2023-11-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('phone_no', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, default='images/default_user_image.jpg', null=True, upload_to='images/farmer/')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
