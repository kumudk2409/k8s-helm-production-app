from flask import Flask

# Lightweight HTTP service used to demonstrate container lifecycle
# Focus is on deployment behavior, not application complexity
app = Flask(__name__)

@app.route("/")
def home():
    return "Kubernetes application is running"

@app.route("/health")
def health():
    # Health endpoint used by Kubernetes probes
    return "ok", 200

if __name__ == "__main__":
    # Explicit host/port for containerized execution
    app.run(host="0.0.0.0", port=8080)