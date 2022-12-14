from django.shortcuts import render

# Create your views here.
def indexx(request):
    return render(request, 'index.html')