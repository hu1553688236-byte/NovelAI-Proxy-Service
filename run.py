import threading
import os  # ← 新增这一行
from src.api.routes import app, start_worker_threads
from src.core.logging import setup_logger

LOGGER = setup_logger("Server")

if __name__ == "__main__":
    LOGGER.info("Starting worker threads")
    threading.Thread(target=start_worker_threads, daemon=True).start()
    LOGGER.info("Starting NovelAI Proxy Service")
    port = int(os.environ.get("PORT", 5000))  # ← Zeabur 会自动注入 PORT
    app.run(host="0.0.0.0", port=port)       # ← 改成 0.0.0.0
