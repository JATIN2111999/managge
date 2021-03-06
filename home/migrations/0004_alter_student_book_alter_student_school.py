# Generated by Django 4.0.4 on 2022-05-13 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_student_book_alter_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.book'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.school'),
        ),
    ]
