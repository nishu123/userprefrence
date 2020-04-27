from django.shortcuts import render
from django.http import HttpResponse
from user.forms import *
from user.models import *
from django.contrib import messages

# Create your views here.
def addUser(request):
    if request.method == "POST":
        form = MyPreferenceForm(request.POST)
        data = request.POST.copy()
        print(data)
        country = data.get('location')
        city_id = request.POST.get('city')
        city=PCity.objects.get(city_id=city_id)
        Cityexp=city.city
      
        if form.is_valid():
            print("hello")
            temp=form.save()
            temp.city=Cityexp
            temp.save()
            messages.success(request, 'user preferences added successfully')
            form = MyPreferenceForm()
            context = {
            'form': form,
            'PCountry': PCountry.objects.all(),
            'PCity': PCity.objects.all(),
            'PLocation': PLocation.objects.all(),


            }
            return render(request, 'user/userinfo.html', context)
        
        
           
    form = MyPreferenceForm()
    context = {
        'form': form,
        'PCountry': PCountry.objects.all(),
        'PCity': PCity.objects.all(),
        'PLocation': PLocation.objects.all(),


    }
    return render(request, 'user/userinfo.html', context)

def listUser(request):
    context = {
        
        'MyPreference': MyPreference.objects.all(),


    }
    return render(request, 'user/userlist.html', context)

def load_cities(request):
    city = request.GET.get('city')
    print("iiiiiiiiiiii",city)
    cities = PLocation.objects.filter(city_id=city)
    print(cities)
    return render(request, 'user/city_dropdown_list_options.html', {'cities': cities})