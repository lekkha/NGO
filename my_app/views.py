from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Contact

# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        occupation = request.POST.get('occupation')
        areacode = request.POST.get('areacode')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        message = request.POST.get('message')
        upload = request.FILES.get('upload')

        contact = Contact(
            firstname= firstname,
            lastname=lastname,
            email=email,
            occupation=occupation,
            areacode=areacode,
            phone=phone,
            age=age,
            dob=dob,
            address=address,
            address2=address2,
            message=message,
            upload=upload
        )

        contact.save()

    return render(request, 'contact.html')

