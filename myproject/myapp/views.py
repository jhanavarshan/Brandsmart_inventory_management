from django.shortcuts import render, redirect
from . models import RawMaterial, ProductionRecord
from django.http import HttpResponse

# Create your views here.

def initialize_raw_materials():
    if not RawMaterial.objects.exists():
        RawMaterial.objects.create(cap=100, powder=1000, container400=50, container500=50)

def home(request):
    return render(request, 'home.html')

def production(request):
    return render(request, 'production.html')

def dovegel(request):
    return render(request, 'dovegel.html')

def inventory(request):
    return render(request, 'inventory.html')


def products(request):
    initialize_raw_materials()
    raw_material = RawMaterial.objects.first()  

    if request.method == 'POST':
        product = request.POST.get('products')
        quantity = int(request.POST.get('quantity'))
        size = int(request.POST.get('size'))

        powder_required = (size * 0.01) * quantity

        if product == 'Containers':
            if size == 400:
                if raw_material.container400 >= quantity and raw_material.cap >= quantity and raw_material.powder >= powder_required:
                    raw_material.container400 -= quantity
                    raw_material.cap -= quantity  
                    raw_material.powder -= powder_required  
                else:
                    return HttpResponse("Not enough raw materials to produce the requested quantity.")
            elif size == 500:
                if raw_material.container500 >= quantity and raw_material.cap >= quantity and raw_material.powder >= powder_required:
                    raw_material.container500 -= quantity  
                    raw_material.cap -= quantity  
                    raw_material.powder -= powder_required  
                else:
                    return HttpResponse("Not enough raw materials to produce the requested quantity.")
        elif product == 'Pouches':
            if raw_material.powder >= powder_required:
                raw_material.powder -= powder_required  
            else:
                return HttpResponse("Not enough powder to produce the requested quantity.")

        raw_material.save()

        ProductionRecord.objects.create(product=product, quantity=quantity, size=size)

        return redirect('products')

    return render(request, 'products.html')

def rawmaterials(request):
    initialize_raw_materials()
    raw_material = RawMaterial.objects.first() 
    return render(request, 'rawmaterials.html', {'rawmaterials': raw_material})

def add_raw_materials(request):
    if request.method == 'POST':
        raw_material = RawMaterial.objects.first() 

        
        add_cap = int(request.POST.get('add_cap', 0))
        add_powder = int(request.POST.get('add_powder', 0))
        add_container400 = int(request.POST.get('add_container400', 0))
        add_container500 = int(request.POST.get('add_container500', 0))

        
        raw_material.cap += add_cap
        raw_material.powder += add_powder
        raw_material.container400 += add_container400
        raw_material.container500 += add_container500

        raw_material.save()


        return redirect('rawmaterials')

    return HttpResponse("Invalid request method.")


def stored_products(request):
    products_list = ProductionRecord.objects.all()

    containers = {}
    pouches = {}

    for product in products_list:
        if product.product == "Containers":
            if product.size not in containers:
                containers[product.size] = 0
            containers[product.size] += product.quantity
        elif product.product == "Pouches":
            if product.size not in pouches:
                pouches[product.size] = 0
            pouches[product.size] += product.quantity

    return render(request, 'stored_products.html', {
        'containers': containers,
        'pouches': pouches
    })