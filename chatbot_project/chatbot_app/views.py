from django.shortcuts import render
from django.http import JsonResponse
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