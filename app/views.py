







from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.shortcuts import render



def home(request):
 return render(request, 'app/home.html')




def send_mail1(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        subject =request.POST.get('subject')
        message=request.POST.get('message')
       
 
        message1 = (subject, message, email, ['alihassanqaz078@gmail.com'])
        message2 = (name,'Your massage is received. admin will reply you as early as possible.thanks to contact us.','decentstarsports@gmail.com', [email])
        send_mass_mail((message1, message2), fail_silently=False)
       
       
        

        return render(request, 'app/home.html')
    else:
        
       return render(request,'app/home.html') 
    
          
