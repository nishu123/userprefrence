from django.urls import path, include

from . import views


app_name = "user"

urlpatterns = [
                  path('user/add/', views.addUser, name="addUser"),
                   path('user/list/', views.listUser, name="listUser"),
                   path('ajax/load-cities/', views.load_cities, name="ajax_load_cities"),
              

              ] 