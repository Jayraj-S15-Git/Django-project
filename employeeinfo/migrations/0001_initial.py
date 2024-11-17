# Generated by Django 4.2 on 2023-04-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeid', models.IntegerField()),
                ('employeename', models.CharField(max_length=50)),
                ('Employeeaddress', models.TextField()),
                ('mobilenumber', models.CharField(max_length=11)),
                ('emailid', models.EmailField(max_length=50)),
                ('aadharno', models.IntegerField()),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]
