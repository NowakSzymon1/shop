from django.http import HttpResponseRedirect
from django.shortcuts import render

from shop.models import Products


def shop(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'baseHead.html')

def about(request):
    return render(request, 'about.html')

def create_products(request):
    choise_title = request.POST['title']
    choise_category = request.POST['category']
    choise_price = request.POST['price']
    choise_parameters = request.POST['parameters']
    choise_description = request.POST['description']
    choise_date = request.POST['date']
    Products.objects.create(title=choise_title)
    Products.objects.create(category=choise_category)
    Products.objects.create(price=choise_price)
    Products.objects.create(parameters=choise_parameters)
    Products.objects.create(description=choise_description)
    Products.objects.create(date_added=choise_date)

    ordering = Products.objects.all().order_by("date_added")

    return render(request, 'baseHead.html', {
        'order': ordering
    })



