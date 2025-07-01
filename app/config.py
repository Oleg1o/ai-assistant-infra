import os

# Название модели, которую использует Ollama (можно поменять на mistral, codellama и т.д.)
MODEL_NAME = os.getenv("MODEL", "llama3")

# Хост и порт Ollama-сервера (если вдруг вынесен в отдельный контейнер)
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "default_token")
API_URL = os.getenv("API_URL", "http://api:8000/ask")
