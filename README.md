#  OrnelBot – Chatbot personnel avec Streamlit & Groq

Bienvenue sur **OrnelBot**, un assistant intelligent développé avec ❤️ par Ornel Rony DIFFO.  
Il s'agit d'un chatbot conversationnel personnalisable, stylisé et déployable via Streamlit.

![CI/CD](https://github.com/tititaya/ornelbot/actions/workflows/python-app.yml/badge.svg)

---

## Objectif

Créer une interface simple et responsive pour interagir avec une IA basée sur LLaMA 3 via l'API de Groq, avec un style inspiré de ChatGPT, et un avatar personnalisé représentant Ornel.

---

##  Fonctionnalités

-  Interface conversationnelle (UI stylisée avec CSS)
-  Historique des échanges (mémoire temporaire)
- ⚙️ Réponses générées avec **Groq API** (`llama3-70b-8192`)
-  Avatar personnalisé dans les réponses du bot
- 🔗 Liens vers les profils **GitHub** et **LinkedIn**
-  Footer dynamique et inspirant
-  Profil dynamique avec `profile.json`

---

##  Démo locale

```bash
git clone git@github.com:tititaya/ornelbot.git
cd ornelbot
pip install -r requirements.txt
streamlit run app.py

## Documentation

### 🔗 Liens utiles

### 🔗 Liens utiles

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Reference](https://console.groq.com/docs)
- [CSS Styling dans Streamlit](https://docs.streamlit.io/develop/concepts/layout-and-style/customizing)
- [Python `os` module](https://docs.python.org/3/library/os.html)
- [Python `dotenv`](https://pypi.org/project/python-dotenv/)
- [Pillow (PIL) for image handling](https://pillow.readthedocs.io/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [LLaMA 3 Model (Groq)](https://www.groq.com/blog/llama3-now-available-on-groqcloud)

---

### ✨ Exemple d’utilisation

>  **User** : « Que fais-tu en ce moment ? »  
>  **Bot** : « En ce moment, je travaille sur l’optimisation d’un robot suiveur de ligne basé sur STM32. »

---

### Profil dynamique

Le bot utilise le fichier `profile.json` pour adapter :

- Son **ton** (humain, structuré, passionné)
- Son **historique de projets** et **compétences**
- Ses **anecdotes** et **objectifs**
- Sa **citation inspirante**

---

###  Technologies

| Outil / Lib        | Usage                                 |
|--------------------|----------------------------------------|
| **Streamlit**      | Interface web interactive              |
| **Groq API**       | Génération IA (LLaMA 3)                |
| **Python**         | Backend / logique                      |
| **CSS**            | Stylisation custom                     |
| **dotenv**         | Gestion des variables d’environnement  |
| **Pillow (PIL)**   | Affichage & traitement de l’avatar     |
| **GitHub Actions** | CI/CD automatique                      |

---

### 👨 Auteur

**Ornel Rony DIFFO**  
Étudiant en M1 à l’ESIEA, passionné par les systèmes embarqués, l’IA, la data et la supervision.

-  [LinkedIn](https://www.linkedin.com/in/ornel-rony-d-01737b267/)
-  [GitHub](https://github.com/tititaya)
