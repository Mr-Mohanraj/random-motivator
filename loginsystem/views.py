from django.shortcuts import render

def index(request):        
    return render(request, 'index.html')

def login(request):
    """login view for testing bro"""
    print(request.POST["username"],request.POST["password"])
    return render(request,'loginsystem/login.html')