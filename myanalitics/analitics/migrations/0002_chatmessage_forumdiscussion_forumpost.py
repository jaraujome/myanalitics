# Generated by Django 4.2.3 on 2023-08-07 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analitics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("user_id", models.IntegerField()),
                ("course_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ForumDiscussion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("forum_id", models.IntegerField()),
                ("user_id", models.IntegerField()),
                ("course_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ForumPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField(max_length=255)),
                ("user_id", models.IntegerField()),
                ("discussion_id", models.IntegerField()),
                ("course_id", models.IntegerField()),
            ],
        ),
    ]
