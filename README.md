# Django Chat Application with Hugging Face Models

## Description

A Django-based chat application integrating Hugging Face Language Models. Key features include:

- **Dynamic Model Selection**: Choose from multiple language models.
- **MongoDB Integration**: Efficiently store and manage chat responses.
- **Chat History**: Easily access and review past conversations.

## Features

- Select and interact with various Hugging Face models.
- Use MongoDB for persistent storage of chat data.
- Navigate through a user-friendly chat history interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/syedsami1/chat_app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-chat_app.git
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up MongoDB and update `settings.py` with your MongoDB connection details.
5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Explore different language models and review chat history through the interface.

## Learning Outcomes

- Gained experience integrating Django with external APIs and databases.
- Developed skills in dynamic model selection and user data management.
- Improved understanding of combining web development with natural language processing technologies.

## Conclusion

This project has been a valuable exercise in merging web development with AI, offering practical insights into managing real-time interactions and data. The application not only showcases the potential of language models but also emphasizes the importance of user experience and data handling in modern web applications.

