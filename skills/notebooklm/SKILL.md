---
name: notebooklm
description: Piloter Google NotebookLM via son serveur MCP (authentification, gestion des carnets, ingestion de sources contexte.md/analyse.md, requêtes et génération de podcasts Audio Overview .m4a). Use when user says "/notebooklm", asks to "connecter a notebooklm", "synchroniser notebooklm", "creer un carnet", "generer un podcast audio overview", or "interroger les sources notebooklm".
---

# Skill : notebooklm (V1.0)
Pilotage direct de Google NotebookLM via le serveur MCP `notebooklm` pour alimenter l'IA en sources fiables, interroger des documents et générer des synthèses audio/podcasts.

---

## 1. Outils Disponibles (Serveur MCP `notebooklm`)

| Outil MCP | Rôle | Cas d'usage principal |
| :--- | :--- | :--- |
| `get_health` | État de santé & auth | Vérifier si la session Google est active. |
| `setup_auth` | Authentification initiale | Ouvre un navigateur pour se connecter à Google une première fois. |
| `re_auth` | Reconnexion | Changer de compte Google ou réinitialiser les cookies expirés. |
| `notebook_list` | Lister les carnets | Afficher les carnets existants avec leurs IDs. |
| `notebook_create` | Créer un carnet | Initialiser un carnet pour le projet actuel. |
| `notebook_get` | Détails d'un carnet | Voir les sources et métadonnées d'un carnet. |
| `add_source` | Ingestion de sources | Ajouter `contexte.md`, `analyse.md`, code ou URLs web au carnet. |
| `notebook_query` | Interrogation RAG | Poser une question factuelle appuyée à 100% sur les sources. |
| `generate_audio` | Podcast Audio Overview | Lancer la génération d'un échange vocal synthétique à 2 voix. |
| `get_audio_status` | Suivi de l'audio | Suivre l'état d'avancement (`pending`, `in_progress`, `ready`). |
| `download_audio` | Téléchargement local | Sauvegarder le fichier audio généré au format `.m4a`. |

---

## 2. Procédure d'Authentification Initiale (1ère utilisation)

1. **Vérification** : Appeler `get_health`. Si le statut indique que l'utilisateur n'est pas authentifié :
2. **Lancement du navigateur** : Appeler `setup_auth`.
3. **Action utilisateur** : Une fenêtre de navigateur s'ouvre. L'utilisateur se connecte à son compte Google.
4. **Persistance** : Les cookies et la session sont sauvegardés automatiquement dans le profil local.

---

## 3. Workflows Types

### Workflow A : Synchroniser le projet dans NotebookLM
1. Lister les carnets avec `notebook_list` ou en créer un nouveau avec `notebook_create(title="Nom-Projet")`.
2. Ingestion des documents clés du projet :
   - `contexte.md` (cadrage, vision produit, architecture)
   - `analyse.md` (spécifications détaillées, parcours utilisateurs)
   - Documentation technique / API
3. Valider l'ajout avec `notebook_get`.

### Workflow B : Générer un Podcast Audio Overview (.m4a)
1. Déclencher `generate_audio(notebook_id="...")`.
2. Suivre avec `get_audio_status(notebook_id="...")` jusqu'à `ready`.
3. Télécharger le podcast via `download_audio(notebook_id="...", output_path="podcast-projet.m4a")`.

### Workflow C : Interrogation RAG Pure
- Utiliser `notebook_query(notebook_id="...", query="...")` pour obtenir des réponses synthétisées basées strictement sur les sources sans hallucination.
