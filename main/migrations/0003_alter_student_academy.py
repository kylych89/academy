# Generated by Django 4.1.5 on 2023-01-09 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_mentor_options_student_academy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.academy'),
        ),
    ]
