Health Desk Agent - Hackathon Ready

Features:
- AI Chatbot (healthcare + general queries)
- Voice input/output
- SQLite database support
- Analytics Dashboard (Plotly graphs)
- Bootstrap UI

Setup:
1. Install dependencies: pip install -r requirements.txt
2. Set OpenAI key:
   - Windows: setx OPENAI_API_KEY "your_api_key"
   - Linux/macOS: export OPENAI_API_KEY="your_api_key"
3. Initialize DB (if adding models later)
4. Run app: python app.py

Access:
- Web Chatbot: http://localhost:5000/
- Dashboard: http://localhost:5000/dashboard/
