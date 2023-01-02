from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'yogi','l':[11,12,13]}
    return render(request,'looping.html',d)
