# Generated by Django 4.2.8 on 2023-12-06 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название аптеки')),
                ('distance_km', models.FloatField(verbose_name='Километр, на котором располагается аптека')),
                ('markup_coefficient', models.FloatField(verbose_name='Коэффициент наценки')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название препарата')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость препарата')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество на складе')),
                ('pharmacies', models.ManyToManyField(related_name='medicines', to='myapp.pharmacy', verbose_name='Аптеки, в которых есть препарат')),
            ],
        ),
    ]