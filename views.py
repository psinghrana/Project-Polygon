from django.shortcuts import render, HttpResponse
from Home.models import Provider
from Home.models import Services

# Create your views here.
def index(request):
    return render(request, "index.html")

def addpolygon(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        lang = request.POST.get('lang')
        curr = request.POST.get('curr')
        provider = Provider(name=name, email=email, phone=phone, lang=lang, curr=curr)
        provider.save()
    return render(request, 'addpolygon.html') 

def providerlist(request):
    allTodo=Provider.objects.all()
    print(allTodo)
    return render(request, 'providerlist.html', {'all':allTodo} )

def services(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        price = request.POST.get('price')
        services = Services(name=name, phone=phone, city=city, price=price)
        services.save()
    return render(request, 'services.html') 

def serviceslist(request):
    entry=Services.objects.all()
    return render(request, 'serviceslist.html', {'ent':entry} )    
