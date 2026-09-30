---
name: github
description: Piloter vos dépôts GitHub via le serveur MCP GitHub (lister les repos, créer des issues, ouvrir des PRs, inspecter des fichiers distants et gérer les branches).
---

# GitHub MCP Integration

Cette compétence permet d'interagir directement avec GitHub grâce au serveur MCP GitHub connecté.

## Capacités disponibles :
- **Recherche et consultation :** Explorer vos dépôts GitHub (`search_repositories`, `get_file_contents`, `list_commits`).
- **Gestion des issues et PRs :** Créer, mettre à jour, commenter des tickets et Pull Requests (`create_issue`, `create_pull_request`, `add_issue_comment`).
- **Gestion de code :** Créer des branches, pousser des fichiers ou cloner des dépôts (`create_branch`, `push_files`, `create_or_update_file`).

L'agent utilise automatiquement les outils MCP `github` dès que vous formulez votre demande.
