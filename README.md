NewsSphere AI 🚀📰

AI-powered modern news platform built with Next.js + Flask featuring live global news, AI summarization, accessibility tools, voice support, and a reels-style news experience.

🌟 Features
🌍 Global & Indian News
🧠 AI News Summarization
🔊 Voice-Based News Reading
♿ Accessibility Mode for Visually Impaired Users
📺 Live News Streaming
🎬 Reels-Style News Feed
❤️ Like & Save News
📱 Modern Responsive UI
⚡ Real-Time News Updates
🎨 Smooth Animations using Framer Motion
🛠️ Tech Stack
Frontend
Next.js
React.js
Tailwind CSS
Framer Motion
Backend
Flask
Python
REST API
APIs
NewsAPI
📂 Project Structure
news-sphere-ai/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── routes/
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   └── package.json
│
└── README.md
🚀 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/Shivaaaaamm/news-sphere-ai.git
cd news-sphere-ai
⚙️ Backend Setup
cd backend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 app.py

Backend runs on:

http://127.0.0.1:5000
💻 Frontend Setup

Open new terminal:

cd frontend

npm install

npm run dev

Frontend runs on:

http://localhost:3000
🔑 Environment Variables

Create .env.local inside frontend:

NEXT_PUBLIC_API_URL=http://127.0.0.1:5000

Add your NewsAPI key inside backend config.py:

NEWS_API_KEY = "YOUR_API_KEY"

Get API key from:

NewsAPI

📸 Features Preview
📰 Live News Feed
Indian & Global news categories
Real-time updates
🔊 Accessibility Support
Text-to-speech
Simplified article summaries
🎬 Reels Mode
Instagram-style vertical news browsing
Voice-enabled experience
🧠 Future Improvements
AI chatbot for news explanation
Multi-language support
Personalized recommendations
Dark/Light mode
User authentication
Bookmark synchronization
👨‍💻 Author
Shivam Kumar
B.Tech CSE Student
AI & Data Enthusiast
Passionate about building impactful products

GitHub:

Shivam Kumar GitHub

⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
🚀 Contribute to improve NewsSphere AI
📜 License

This project is open-source and available under the MIT License.
