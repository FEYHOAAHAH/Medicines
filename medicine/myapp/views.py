from _decimal import Decimal
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Medicine, Pharmacy
from .forms import DeliveryForm


def calculate_delivery_price(km_location, medicine_name):
    medicine = get_object_or_404(Medicine, name=medicine_name)
    pharmacies = medicine.pharmacies.all()

    optimal_price = Decimal('inf')

    for pharmacy in pharmacies:
        distance_factor = Decimal('1') + (Decimal(str(pharmacy.distance_km)) * Decimal('0.0001'))
        total_price = medicine.price * Decimal(str(pharmacy.markup_coefficient)) * distance_factor

        if total_price < optimal_price:
            optimal_price = total_price

    return optimal_price


def delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            km_location = form.cleaned_data['km_location']
            medicine_name = form.cleaned_data['medicine_name']
            try:
                delivery_price = calculate_delivery_price(km_location, medicine_name)
            except Medicine.DoesNotExist:
                delivery_price = "Ошибка: Лекарство не найдено"
            return render(request, 'delivery_result.html', {'delivery_price': delivery_price})
    else:
        form = DeliveryForm()

    return render(request, 'delivery.html', {'form': form})