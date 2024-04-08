"""chatbot_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from transformers import pipeline
from django.http import JsonResponse
# from chatbot_app.views import chatbot # Problem Child

def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        # Initialize the Hugging Face LLM pipeline
        nlp = pipeline('text-generation', model='gpt2')
        # Generate a response using the LLM
        response = nlp(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
        return JsonResponse({'response': response})
    return render(request, 'chatbot.html') # Removed chatbot_app/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chatbot, name='chatbot'), # Added this line to hook in app
]