from django.shortcuts import render

def shootit(request):
    return render(request, 'SpaceShooter/shootit.html',{})
