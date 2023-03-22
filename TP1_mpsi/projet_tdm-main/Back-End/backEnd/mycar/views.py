from dataclasses import dataclass
import email
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import User , Membres , Work_Shop
from django.http import JsonResponse
from django.core import serializers
from django.core.exceptions import ValidationError
from uuid import uuid4
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Registration(request):
   
    if request.method == 'POST':
      username_test=request.POST.get('username')
      email_test= request.POST.get('email')
      password_test = request.POST.get('password')
      phone_number_test=request.POST.get('phone_number')
       
    if not email_test or not  password_test or not username_test or not phone_number_test  :
            raise ValidationError("Details not entered.")

    if not '@' in email_test:    
         raise ValidationError("User credentials are not correct.")    
            
    user= User.objects.filter( email=email_test )
   
    if  user.exists():
                raise ValidationError("this email is already taken")
   
    


    b = User(username=username_test, email=email_test ,password=password_test,phonenumber=phone_number_test,ifLogged = True,token = uuid4())
    b.save()
    b= User.objects.filter( email=email_test )
    
    data = serializers.serialize('json', b ) 
    return HttpResponse(data, content_type="text/json-comment-filtered")

# @csrf_exempt
# def Login(request):
   
#     if request.method == 'POST':
#       email_test= request.POST.get('')
#       password_test = request.POST.get('password')



#     if not email_test or not  password_test:
#             raise ValidationError("Details not entered.")

#     if not '@' in email_test:    
#          raise ValidationError("User credentials are not correct.")    
            
#     user= User.objects.filter( email=email_test ).filter(password=password_test)
   
#     if not user.exists():
#                 raise ValidationError("User credentials are not correct.")
   
    
#     for object in user:
#         if object.ifLogged:
#             raise ValidationError("User already logged in.")
#         object.ifLogged = True
#         object.token = uuid4()
#         object.save()


#     data = serializers.serialize('json',  user ) 
#     return HttpResponse(data, content_type="text/json-comment-filtered")


@csrf_exempt    
def Login(request):

    # email_test = None
    # password_test = None
    # email_test = "ma.malek@esi-sba.dz"
    # password_test = "amine"

   
    if request.method == 'POST':
      email_test= request.POST.get('username')
      password_test = request.POST.get('password')



    if not email_test or not  password_test:
            raise ValidationError("Details not entered.")

    if not '@' in email_test:    
         raise ValidationError("User credentials are not correct.")    
            
    user= User.objects.filter( email=email_test ).filter(password=password_test)
   
    if not user.exists():
                raise ValidationError("User credentials are not correct.")
   
    
    for object in user:
        if object.ifLogged:
            raise ValidationError("User already logged in.")
        object.ifLogged = True
        object.token = uuid4()
        object.save()


    data = serializers.serialize('json',  user ) 
    json_data = [dict(pk=obj['pk'], **obj['fields']) for obj in json.loads(data)]
    return JsonResponse(json_data, safe=False)

@csrf_exempt
def logout(request):
     

     if request.method == 'POST':
      username_test= request.POST.get('username')
     user= User.objects.filter( username=username_test )
     for object in user:
        if not object.ifLogged:
                 raise ValidationError("User is not logged in.")
        object.ifLogged = False
        object.token = ""
        object.save()
     return HttpResponse('User is logged out.')
     


@csrf_exempt
def all_objects(request):
    # get method handler

    data = serializers.serialize("json", Work_Shop.objects.all())
    json_data = [dict(pk=obj['pk'], **obj['fields']) for obj in json.loads(data)]

    return JsonResponse(json_data, safe=False)



@csrf_exempt
def creat_work_shop(request):
   
    if request.method == 'POST':
      domaine_test=request.POST.get('domaine')
      DateDebute_test= request.POST.get('DateDebute')
      DateFin_test = request.POST.get('DateFin')
     

    if not domaine_test or not  DateDebute_test or not DateFin_test  :
            raise ValidationError("Details not entered.")    
    b = Work_Shop(domaine=domaine_test, DateDebute=DateDebute_test ,DateFin=DateFin_test)
    b.save()

    result=Work_Shop.objects.filter(domaine=domaine_test).filter(DateDebute=DateDebute_test ).filter(DateFin=DateFin_test)
    data = serializers.serialize('json', result ) 
    json_data = [dict(pk=obj['pk'], **obj['fields']) for obj in json.loads(data)]
    return JsonResponse(json_data, safe=False)



@csrf_exempt
def add_membre(request):
   
    if request.method == 'POST':
    
      Work_Shop_id= request.POST.get('Work_Shop_id')
      user_id = request.POST.get('user_id')
      position_A_test=request.POST.get('position_A')
      position_B_test=request.POST.get('position_B')



    user_test = User.objects.get(pk=user_id)
    Work_Shop_test = Work_Shop.objects.get(pk=Work_Shop_id) 
   
    new_membre=Membres( User= user_test,Work_Shop=Work_Shop_test,position_A=position_A_test,position_B=position_B_test ) 
    new_membre.save()


   
    return HttpResponse("done")



@csrf_exempt
def list_members(request):
   
    if request.method == 'POST':
    
      work_shop_id= request.POST.get('Work_Shop_id')
      
    
    Work_Shop_test = Work_Shop.objects.get(pk=work_shop_id) 
    result= Membres.objects.filter( Work_Shop=Work_Shop_test )
   
    data = serializers.serialize('json',  result ) 
    json_data = [dict(pk=obj['pk'], **obj['fields']) for obj in json.loads(data)]
    return JsonResponse(json_data, safe=False)





