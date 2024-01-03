from django.shortcuts import render
from .forms import contactForm

# Create your views here.
def task(request):
      if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
      else:
        form = contactForm()
      return render(request, 'task.html', {'form':form}) 
