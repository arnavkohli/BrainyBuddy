# Generated by Django 3.0.1 on 2019-12-31 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizattempt'),
        ('torfq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TorFQAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField()),
                ('quiz_attempt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.QuizAttempt')),
            ],
        ),
    ]
