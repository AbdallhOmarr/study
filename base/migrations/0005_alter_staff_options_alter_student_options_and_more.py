# Generated by Django 4.2.1 on 2023-07-10 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0004_staff_student_alter_message_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="staff",
            options={"permissions": [("remove_room", "user can remove room")]},
        ),
        migrations.AlterModelOptions(
            name="student",
            options={"permissions": [("add_room", "can add new room")]},
        ),
        migrations.RemoveField(
            model_name="staff",
            name="id",
        ),
        migrations.RemoveField(
            model_name="staff",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="staff",
            name="name",
        ),
        migrations.RemoveField(
            model_name="staff",
            name="national_id",
        ),
        migrations.RemoveField(
            model_name="staff",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="staff",
            name="role",
        ),
        migrations.RemoveField(
            model_name="student",
            name="id",
        ),
        migrations.RemoveField(
            model_name="student",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="student",
            name="name",
        ),
        migrations.RemoveField(
            model_name="student",
            name="national_id",
        ),
        migrations.RemoveField(
            model_name="student",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="student",
            name="role",
        ),
        migrations.AddField(
            model_name="staff",
            name="user",
            field=models.OneToOneField(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
