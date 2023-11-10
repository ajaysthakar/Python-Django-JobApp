from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from Subscribe.forms import SubscribeForm
from Subscribe.models import Subscribe

def isEmpty(val):
    if val=="":
        return True
    return False
# Create your views here.

#Subscrive view code with Form
# def SubscribeFun(request):
#     ErrorMsg=""
#     subscribe_form =SubscribeForm()
#     if request.POST:
#         subscribe_form =SubscribeForm(request.POST) #attaching requested data to form
#         #print(f"{email}|{fname}|{lname} ")
#         if subscribe_form.is_valid():
#             print("valid form")
#             print(subscribe_form.cleaned_data)
#             fname =subscribe_form.cleaned_data['first_name']
#             lname =subscribe_form.cleaned_data['last_name']
#             email =subscribe_form.cleaned_data['email']
#             subscribe =Subscribe(first_name=fname,last_name=lname,email=email)
#             subscribe.save()
#             return redirect(reverse('thanks'))
#     context={'form':subscribe_form,'ErrorMsg':ErrorMsg}
#     return render(request,'subscribe.html',context)


#Sunbscribe view with ModelForm
def SubscribeFun(request):
    ErrorMsg=""
    subscribe_form =SubscribeForm()
    if request.POST:
        subscribe_form =SubscribeForm(request.POST) #attaching requested data to form
        #print(f"{email}|{fname}|{lname} ")
        if subscribe_form.is_valid():
            subscribe_form .save()
            return redirect(reverse('thanks'))
    context={'form':subscribe_form,'ErrorMsg':ErrorMsg}
    return render(request,'Subscribe/subscribe.html',context)

def thanks(request):
    context={}
    return render(request,'Subscribe/thanks.html',context)