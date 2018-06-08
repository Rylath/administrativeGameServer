from django.shortcuts import render

# Create your views here.

def terraria_controls(request):
  return render(request, 'terraria/terraria_controls.html')
