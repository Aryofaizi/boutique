# Generated by Django 4.2.3 on 2023-07-14 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_color', models.CharField(default='black', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ClothType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_choices', models.CharField(default='t-shirt', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cloth_width', models.IntegerField(blank=True, null=True)),
                ('cloth_length', models.IntegerField(blank=True, null=True)),
                ('designers', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('choices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='clothing.clothtype')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='clothing.clothcolor')),
            ],
        ),
    ]