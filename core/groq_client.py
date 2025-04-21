import os
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Fonction pour générer une réponse depuis le modèle LLaMA3 via l'API Groq
def generate_response(prompt: str) -> str:
    if not GROQ_API_KEY:
        return "❌ Erreur : la clé API GROQ est introuvable. Vérifie le fichier .env."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        return f"❌ Erreur de requête : {e}"
