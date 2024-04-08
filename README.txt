# Django Chatbot

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
5. [Usage](#usage)
6. [Development Process](#development-process)
7. [Future Enhancements](#future-enhancements)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction
The Django Chatbot is an exciting web application that allows users to interact with a conversational AI assistant powered by the Hugging Face Transformers library. This project showcases the integration of a large language model (LLM) into a Django web framework, providing a seamless and engaging chatbot experience.

## Features
- Conversational AI assistant powered by Hugging Face Transformers
- Intuitive and responsive web interface built with Django
- Secure CSRF token handling to protect against cross-site request forgery
- Dockerization for easy deployment and scalability

## Technologies Used
- Python
- Django
- Hugging Face Transformers
- jQuery
- HTML/CSS

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Docker (optional, for containerized deployment)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/solshinecodes/django-chatbot.git
   ```
 - You may need to update a couple minor file pathways to conform to your system, or this may work out of the box given the virtual environment.
2. Create a virtual environment and activate it:
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Django development server:
   ```
   python manage.py runserver
   ```
5. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the chatbot interface.
 - You can interface by typing into the input text box and clicking send, after which gpt-2 will autocomplete your sentence.

## Usage
1. Type your message in the input field and click the "Send" button to interact with the chatbot.
2. The chatbot will generate a response based on the input and display it in the chat history.

## Development Process
The development of the Django Chatbot followed these steps:

1. **Set up the Django project**: We created a new Django project and app to house the chatbot functionality.
2. **Implement the chatbot view**: We defined the `chatbot` view in the `views.py` file, which handles the user input, generates a response using the Hugging Face Transformers library, and returns the response to the client.
3. **Create the chatbot template**: We developed the `chatbot.html` template, which includes the HTML structure for the chat interface and the JavaScript code to handle the AJAX requests and update the chat history.
4. **Secure the application**: We added CSRF token handling to protect the application against cross-site request forgery attacks.
5. **Dockerize the application**: We created a Dockerfile and a Docker Compose configuration to containerize the Django Chatbot application for easy deployment and scalability.

## Future Enhancements
- Implement more advanced chatbot features, such as context-awareness, multi-turn conversations, and personalization.
- Add support for other language models and domains beyond text generation.
- Enhance the user interface with additional features, such as file uploads, image generation, and voice interaction.
- Integrate the chatbot with external services, like databases, APIs, and third-party platforms.

## Contributing
This is a skill-building project. Contributions to the Django Chatbot project are welcome! If you find any issues or have suggestions for improvements, please feel free to open a new issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).