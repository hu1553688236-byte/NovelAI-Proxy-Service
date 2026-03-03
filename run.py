import threading
import os
from flask import send_from_directory
from src.api.routes import app, start_worker_threads
from src.core.logging import setup_logger

LOGGER = setup_logger("Server")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    LOGGER.info("Starting worker threads")
    threading.Thread(target=start_worker_threads, daemon=True).start()

    LOGGER.info("Starting NovelAI Proxy Service")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
