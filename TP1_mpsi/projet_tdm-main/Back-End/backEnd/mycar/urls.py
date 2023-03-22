from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[


path('login/',views.Login,name='login'),
path('logout/',views.logout,name='logout'),
path( 'all_objects/',views.all_objects,name='all_objects'),
path( 'add_membre/',views.add_membre,name='add_membre'),
path( 'add_work_shop/',views.creat_work_shop,name='work_shop'),
path( 'list_members/',views.list_members,name='list_members'),
path( 'registration/',views.Registration,name='registration'),



]