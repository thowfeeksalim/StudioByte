# Generated by Django 4.1.7 on 2023-04-13 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_p_email_booking_c_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occations',
            name='occ_spec',
        ),
        migrations.AlterField(
            model_name='booking',
            name='occa_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments'),
        ),
    ]
