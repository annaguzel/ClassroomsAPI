# Generated by Django 2.1.5 on 2020-02-24 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_auto_20180709_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='grade',
        ),
        migrations.AddField(
            model_name='classroom',
            name='name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='classes.Classroom'),
        ),
    ]
