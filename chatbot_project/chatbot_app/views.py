# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from transformers import pipeline

def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        # Initialize the Hugging Face LLM pipeline
        nlp = pipeline('text-generation', model='gpt2')
        # Generate a response using the LLM
        response = nlp(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
        return JsonResponse({'response': response})
    return render(request, 'chatbot.html') # Changed from chatbot.html
