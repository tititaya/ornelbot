import json

def build_prompt(profile: dict, history: list, user_input: str) -> str:
    # Récupérer les infos essentielles du profil
    intro = profile.get("intro_personnelle", "")
    vision = profile.get("vision", "")
    citation = profile.get("citation", "")
    bio = profile.get("bio", "")
    mode_mixte = profile.get("mode_mixte", "")

    # Construit le bloc de contexte initial
    system_context = f"""
Tu es OrnelBot, un assistant personnel qui représente Ornel Rony DIFFO.

Tu peux répondre à des questions générales (comme ChatGPT), mais ton rôle est de parler d'Ornel et de ses projets, quand c'est pertinent et raisonable.

Tu t'exprimes de façon naturelle, authentique, parfois avec une touche d'humour ou d'énergie.
Tu privilégies des réponses claires, synthétiques, et humaines, comme si tu parlais à un ami curieux ou à un recruteur intéressé.

Voici quelques infos utiles :

- Intro : {intro}
- Bio : {bio}
- Citation : {citation}
- Vision : {vision}
- Mode : {mode_mixte}
"""

    # Limiter à 5 derniers échanges pour garder un contexte court
    history = history[-5:]

    # Construire l'historique de la conversation (mémoire)
    history_formatted = "\n".join(f"{m['role'].upper()}: {m['content']}" for m in history)

    # Ajoute le message actuel
    history_formatted += f"\nUSER: {user_input}\nASSISTANT:"

    # Assemble le prompt complet
    full_prompt = f"""{system_context}

Conversation :
{history_formatted}
"""

    return full_prompt
