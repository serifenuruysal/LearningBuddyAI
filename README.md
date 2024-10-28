# Virtual Language Learning Buddy AI Agent

## Project Overview

The Virtual Language Learning Buddy is an AI-driven application that helps users practice and learn new languages in real-time. The application simulates real-life conversations, corrects grammar, improves pronunciation, and suggests daily vocabulary challenges, all while adapting to the user's progress and preferences.

## Features

- Simulate real-life conversations.
- Correct grammar and improve pronunciation.
- Suggest daily vocabulary challenges.
- Adapt to user progress and preferences.
- Include voice-based interaction and cultural context-based responses.
- Text-based conversation initially, with voice interaction later.
- Vocabulary challenges and progress tracking.
- User preferences for language tone (formal/informal) or context (e.g., work, travel).

## Tech Stack

### Backend
- **Framework:** Django
- **API:** Django REST Framework
- **AI Integration:** OpenAI GPT-3/GPT-4, LangChain
- **Voice Processing:** Google Cloud Speech-to-Text, Google Cloud Text-to-Speech
- **Database:** PostgreSQL or MongoDB
- **Environment Management:** python-dotenv

### Frontend
- **Framework:** React
- **State Management:** Context API
- **API Interaction:** Fetch API

## Installation

### Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### Backend Installation

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create a `requirements.txt` file and add the following dependencies:

   ```plaintext
   Django>=3.2,<4.0
   djangorestframework
   openai
   google-cloud-speech
   google-cloud-texttospeech
   langchain
   python-dotenv
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the Django server:

   ```bash
   python manage.py runserver
   ```

### Frontend Installation

1. Navigate to the frontend directory:

   ```bash
   cd ../frontend
   ```

2. Install the required packages:

   ```bash
   npm install
   ```

3. Start the React application:

   ```bash
   npm start
   ```

## Running the Application

- Access the frontend at `http://localhost:3000`.
- The backend will be running at `http://127.0.0.1:8000/`.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



