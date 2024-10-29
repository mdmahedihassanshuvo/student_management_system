# Generated by Django 5.1.2 on 2024-10-29 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('student_id', models.IntegerField(unique=True)),
                ('semester', models.IntegerField()),
                ('department', models.CharField(default='', max_length=50)),
                ('grade', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
    ]
