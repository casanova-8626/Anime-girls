from django.shortcuts import render
from datetime import datetime
from ratings.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your response has been sent!')
    return render(request, 'contact.html')