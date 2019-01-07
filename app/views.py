from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,generics,permissions
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.models import Token
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile,Event,UserToken,Registration,EventRules
import random
import json

# Create your views here.
if(Event.objects.all().count() == 0):
        for i in range(14):
                name='event'+str(i+1)
                Event.objects.create(name=name)

class Register(generics.CreateAPIView):
    permission_classes=(permissions.AllowAny,)
    def post(self,request,*args,**kwargs):
        username=request.POST.get('admission')
        name=request.POST.get('name')
        password=request.POST.get('password')
        branch=request.POST.get('branch')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        if User.objects.filter(username=username).count()!=0:
                return JsonResponse({'details':'User Already Exist'})
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        login(request,user)
        y=UserProfile.objects.get(user=request.user)
        y.name=name
        y.phone=phone
        y.branch=branch
        y.save()

        token=Token.objects.create(user=user)

        return JsonResponse({'details':'User has been been registered with token: '+token.key})

class ChangePassword(generics.CreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        user=get_object_or_404(User,username=request.user)
        user.set_password(request.POST.get('new_password'))
        user.save()
        return JsonResponse({'details':'Password has been changed successfully.'})

class Login(generics.CreateAPIView):
    permission_classes=(permissions.AllowAny,)
    def post(self,request,*args,**kwargs):
        username=request.POST.get('admission')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is None:
            return Response('Wrong Credentials')
        login(request,user)
        return JsonResponse({'details':'Logged in Successfully'})

class EventRegistration(generics.CreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        team_name=request.POST.get('team_name')
        event=request.POST.get('event')
        print(team_name,event)
        if event == '-------':
                return HttpResponse('Wrong')
        x=random.randint(999,99999)*67
        events=Event.objects.all()
        regi=UserToken.objects.get(user=request.user)
        if event=='Event1':
                regi.event1=x
        if event=='Event2':
                regi.event2=x
        if event=='Event3':
                regi.event3=x
        if event=='Event4':
                regi.event4=x
        if event=='Event5':
                regi.event5=x
        if event=='Event6':
                regi.event6=x
        if event=='Event7':
                regi.event7=x
        if event=='Event8':
                regi.event8=x
        if event=='Event9':
                regi.event9=x
        if event=='Event10':
                regi.event10=x
        if event=='Event11':
                regi.event11=x
        if event=='Event12':
                regi.event12=x
        if event=='Event13':
                regi.event13=x
        if event=='Event14':
                regi.event14=x
        
        regi.save()
        Registration.objects.create(event=event,team_name=team_name,user=request.user,token=x)
        return JsonResponse({'details':'Success'})

class VerifyToken(generics.CreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        event=request.POST.get('event')
        coupon=request.POST.get('coupon')
        print(coupon)
        if event=='1':
                x=request.user.usertoken.event1
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event1='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='2':
                x=request.user.usertoken.event2
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event2='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='3':
                x=request.user.usertoken.event3
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event3='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='4':
                x=request.user.usertoken.event4
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event4='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='5':
                x=request.user.usertoken.event5
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event5='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='6':
                x=request.user.usertoken.event6
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event6='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='7':
                x=request.user.usertoken.event7
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event7='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='8':
                x=request.user.usertoken.event8
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event8='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='9':
                x=request.user.usertoken.event9
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event9='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='10':
                x=request.user.usertoken.event10
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event10='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='11':
                x=request.user.usertoken.event11
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event11='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='12':
                x=request.user.usertoken.event12
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event12='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='13':
                x=request.user.usertoken.event13
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event13='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='14':
                x=request.user.usertoken.event14
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event14='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

class GetData(generics.CreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        user=request.user
        eventa=Event.objects.all().values('name')
        json_events=json.dumps(list(eventa))
        #events = serializers.serialize('json', list(eventa), fields=('name'))
        tokena=UserToken.objects.filter(user=user).values('event1','event2','event3','event4','event5','event6','event7','event8','event9','event10','event11','event12','event13','event14')
        json_tokens=json.dumps(list(tokena))
        #tokens = serializers.serialize('json', list(tokena), fields=('event1','event2','event3','event4','event5','event6','event7','event8','event9','event10','event11','event12','event13','event14'))
        userinfoa=UserProfile.objects.filter(user=user).values('name','branch','phone','coins')
        json_userinfo=json.dumps(list(userinfoa))
        #userinfo = serializers.serialize('json', list(userinfoa), fields=('name','branch','phone','coin'))
        """ return JsonResponse({
            'events':events,
            'tokens':tokens,
            'userinfo':userinfo
        }) """
        
        return Response({'user_info':json_userinfo,'user_tokens':json_tokens,'events':json_events})