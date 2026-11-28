from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)
LOG_PATH = "/shared-logs/attack.log"

def log_event(message):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(f"{datetime.now().isoformat()} {message}\n")
    print(message, flush=True)


@app.route("/")
def lure():
    log_event(f"LURE_VIEWED: {request.remote_addr}")
    return render_template("lure.html")

@app.route("/executed")
def executed():
    log_event(f"PAYLOAD_EXECUTED source={request.remote_addr}")
    return "ruh ro raggy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)