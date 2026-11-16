LUCKY SCRATCH GAME

What it does
- Every visit to the same URL requests a fresh result.
- Each request has a 50% No Prize, 40% Small Prize, 10% Big Prize chance.
- Multiple phones can request results at the same time.
- The Python server uses a thread lock to make each random draw and scan counter update atomic.

Run locally
1. Install Python 3.
2. In a terminal, run: pip install -r requirements.txt
3. For local testing, run: python app.py
4. Open http://127.0.0.1:5000 on your computer.

To use a QR code with other people's phones
You must deploy this Flask app to a public HTTPS hosting service first. Then create one QR code pointing to your deployed URL (for example, https://your-site.example/). Keep using that same QR code; every visit generates a new ticket.

Important
- A scan is treated as a new page visit. If someone refreshes or opens the link again, that also creates a new chance.
- This demo does not identify people or limit attempts.
- The scan counter is in server memory and resets when the server restarts. It is not used to decide prizes.

Render deployment settings:
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn app:app
