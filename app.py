from flask import Flask, render_template, jsonify
from secrets import randbelow
from threading import Lock

app = Flask(__name__)

# A lock keeps each concurrent scan's draw/count update atomic.
draw_lock = Lock()
scan_count = 0

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/scratch")
def scratch():
    global scan_count
    with draw_lock:
        ticket = randbelow(100)  # uniformly selects 0..99
        scan_count += 1
        current_scan = scan_count

    if ticket < 50:
        result = "NO PRIZE"
        message = "No prize this time. Try your luck on your next scan!"
        kind = "none"
    elif ticket < 90:
        result = "SMALL PRIZE"
        message = "Nice! You won a SMALL PRIZE!"
        kind = "small"
    else:
        result = "BIG PRIZE"
        message = "Congratulations! You won the BIG PRIZE!"
        kind = "big"

    return jsonify(result=result, message=message, kind=kind, scan=current_scan)

if __name__ == "__main__":
    # Threaded mode lets multiple phones request a fresh result at once.
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=False)
