# Generated by Django 3.2.8 on 2021-10-06 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='room_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=10)),
                ('allocated_doctor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='doctors.doctor')),
                ('allocated_room', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.room_id')),
            ],
        ),
    ]
