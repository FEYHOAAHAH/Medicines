from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название препарата')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость препарата')
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе')
    pharmacies = models.ManyToManyField('Pharmacy', related_name='medicines',
                                        verbose_name='Аптеки, в которых есть препарат')

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity} {self.pharmacies}"


class Pharmacy(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название аптеки')
    distance_km = models.FloatField(verbose_name='Километр, на котором располагается аптека')
    markup_coefficient = models.FloatField(verbose_name='Коэффициент наценки')

    def __str__(self):
        return f"{self.name} {self.distance_km} {self.markup_coefficient}"
