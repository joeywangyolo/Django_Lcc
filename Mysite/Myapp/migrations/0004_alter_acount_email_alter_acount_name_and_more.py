# Generated by Django 4.1.3 on 2023-01-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_alter_acount_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acount',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='acount',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='acount',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
    ]