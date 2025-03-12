import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Location


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def index(request):
    context = {}
    return render(request, "index.html", context)


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, 'Registration successful!')
            return redirect('index')  # Redirect to the home page
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def save_location(request):
    try:
        data = json.loads(request.body)
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        
        if not all([latitude, longitude]):
            return JsonResponse({
                'status': "error",
                'message': "Incomplete location data!"
            }, status=400)
            
        Location.objects.update_or_create(
            user=request.user,
            defaults={
                'latitude': latitude,
                'longitude': longitude,
            }
        )
        return JsonResponse({
            'status': "success",
            'message': "Location saved successfully!"
        }, status=200)
    
    except json.JSONDecodeError:
        return JsonResponse({
            'status': "error",
            'message': "Invalid JSON"
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': "error",
            'message': str(e)
        }, status=500)