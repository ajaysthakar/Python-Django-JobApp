from django.shortcuts import render

from uploadApp.forms import uplodForms

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = uplodForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            saved_obj = form.instance
            return render(request,'uploadApp/UploadApp.html',{'form':form, 'saved_obj':saved_obj})

    else: 
        form = uplodForms()

    return render(request,'uploadApp/UploadApp.html',{'form':form})
