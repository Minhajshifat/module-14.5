from django.shortcuts import render

# Create your views here.
def mtask(request):
    return render(request,'modeltask.html')
