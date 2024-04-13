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
from django.http import JsonResponse, StreamingHttpResponse
# from chatbot_app.views import chatbot # Problem Child
# from . import views
from chatbot_app.models import ChatMessage

from django.shortcuts import render
from transformers import pipeline, LlamaForCausalLM, LlamaTokenizer

import ollama
from django.shortcuts import render
from django.http import JsonResponse

def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        file_upload = request.FILES.get('file_upload')

        # Generate a response using the Ollama model
        response = ollama.chat(model='llama2', messages=[
            {
                'role': 'user',
                'content': user_input,
            },
        ])
        bot_response = response['message']['content']

        # Update session data with chat history
        session = request.session
        chat_history = session.get('chat_history', [])
        chat_history.append((user_input, bot_response))
        if len(chat_history) > 10:
            chat_history = chat_history[-10:]
        session['chat_history'] = chat_history
        session.save()

        # Create a new ChatMessage instance
        chat_message = ChatMessage(user_input=user_input, bot_response=bot_response, file_upload=file_upload)
        chat_message.save()

        return JsonResponse({'response': bot_response})
    else:
        return render(request, 'chatbot.html')
        print("Failed to render response")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chatbot, name='chatbot'), # Added this line to hook in app
]