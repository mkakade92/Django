# Generated by Django 3.0.4 on 2020-05-02 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grievance', '0003_auto_20200424_0743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grievance',
            options={'ordering': ['-create_Date']},
        ),
        migrations.RenameField(
            model_name='grievance',
            old_name='created_at',
            new_name='create_Date',
        ),
        migrations.AddField(
            model_name='grievance',
            name='post_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='grievance',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='against',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='status',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
