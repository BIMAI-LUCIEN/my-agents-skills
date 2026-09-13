---
name: notebooklm
description: Piloter Google NotebookLM via son serveur MCP (authentification, gestion des carnets, ingestion de sources texte/URLs, requêtes RAG et génération de podcasts Audio Overview .m4a). Use when user says "/notebooklm", asks to "connecter a notebooklm", "synchroniser notebooklm", "creer un carnet", "generer un podcast audio overview", or "interroger les sources notebooklm".
---

# Skill : notebooklm (V1.0)
Pilotage direct de Google NotebookLM via le serveur MCP `notebooklm` pour alimenter l'IA en sources fiables, interroger des documents et générer des synthèses audio/podcasts.

---

## 1. Outils Disponibles (Serveur MCP `notebooklm`)

| Outil MCP | Rôle | Cas d'usage principal |
| :--- | :--- | :--- |
| `get_health` | État de santé & auth | Vérifier si la session Google est active (`authenticated=true`). |
| `setup_auth` | Authentification initiale | Ouvre un navigateur pour se connecter à Google une première fois. |
| `re_auth` | Reconnexion | Changer de compte Google ou réinitialiser les cookies expirés. |
| `list_notebooks` | Lister les carnets | Afficher les carnets enregistrés dans la bibliothèque locale avec leurs IDs. |
| `add_notebook` | Enregistrer un carnet | Ajouter un carnet NotebookLM via son URL de partage. |
| `select_notebook` | Carnet par défaut | Définir le carnet actif pour les requêtes suivantes. |
| `get_notebook` | Détails d'un carnet | Inspecter les métadonnées et sources d'un carnet. |
| `add_source` | Ingestion de sources | Ajouter du texte (`contexte.md`, `analyse.md`, code) ou des URLs web. |
| `ask_question` | Interrogation RAG | Poser une question factuelle appuyée sur les sources (gère `session_id`). |
| `list_sessions` | Lister les sessions | Voir les sessions de chat actives. |
| `reset_session` / `close_session` | Gestion session | Réinitialiser l'historique ou clore une session. |
| `generate_audio` | Podcast Audio Overview | Lancer la génération d'un échange vocal synthétique à 2 voix (asynchrone). |
| `get_audio_status` | Suivi de l'audio | Suivre l'avancement (`started`, `in_progress`, `ready`). |
| `download_audio` | Téléchargement local | Sauvegarder le fichier audio généré au format `.m4a`. |

---

## 2. Procédure d'Authentification Initiale (1ère utilisation)

1. **Vérification** : Appeler `get_health`. Si `authenticated=false` :
2. **Lancement du navigateur** : Appeler `setup_auth`.
3. **Action utilisateur** : Une fenêtre de navigateur s'ouvre. L'utilisateur se connecte à son compte Google.
4. **Persistance** : Les cookies et la session sont sauvegardés automatiquement dans le profil local.

---

## 3. Workflows Types

### Workflow A : Lier un carnet et ingérer les specs du projet
1. L'utilisateur crée ou partage son carnet sur [notebooklm.google.com](https://notebooklm.google.com).
2. Enregistrer le carnet via `add_notebook(url="https://notebooklm.google.com/notebook/...")`.
3. Ingestion des documents clés du projet avec `add_source` :
   - `contexte.md` (vision produit, stack, architecture)
   - `analyse.md` (spécifications détaillées, parcours utilisateurs)
4. Sélectionner le carnet avec `select_notebook(notebook_id="...")`.

### Workflow B : Interrogation RAG Session-Based
1. Poser une question : `ask_question(query="Quelles sont les règles de validation du panier ?")`.
2. Conserver le `session_id` retourné pour les questions de suivi afin de conserver le fil contextuel.

### Workflow C : Générer un Podcast Audio Overview (.m4a)
1. Déclencher `generate_audio(notebook_id="...")` (retourne immédiatement avec `status: "started"`).
2. Sonder régulièrement avec `get_audio_status(notebook_id="...")` (généralement 2 à 5 min).
3. Dès que `status: "ready"`, télécharger le fichier :
   `download_audio(notebook_id="...", destination_dir="...")`.
