---
name: knowledge-routing
description: Routage contextuel intelligent de l'information (Notion, docs de projet, mémoire, bases de données). Cartographie l'emplacement exact des ressources pour éliminer les recherches exhaustives aveugles et économiser jusqu'à 80% de tokens. Use when user says "/knowledge-routing", "/notion-routing", asks to "router l'information", "trouver la bonne doc", "où se trouve l'info", or "optimiser la recherche de contexte".
---

# Skill : knowledge-routing (V1.0)
Routage déterministe et indexation de l'architecture d'information du projet (Notion, docs locales, fichiers de mémoire, bases de données).

---

## 1. Principes de Routage (Zero Token Waste)

Ne jamais lancer un `find` ou un `grep` récursif sur tout le disque sans avoir interrogé la table de routage :

| Type d'information recherchée | Emplacement Prioritaire | Clé / Fichier |
| :--- | :--- | :--- |
| **Vision Produit & Stratégie** | Fichiers de cadrage | `contexte.md`, Notion: *Product Roadmap* |
| **Spécifications Fonctionnelles & Parcours** | Cahier des charges | `analyse.md`, Notion: *Specs & User Stories* |
| **Tâches atomiques & MVP** | Plan d'implémentation | `plan.md`, Notion: *Sprint Board* |
| **Architecture Technique & Stack** | Arborescence globale | `contexte.md` section Stack, `package.json` |
| **Secrets & Clés API** | Configuration d'environnement | `.env.example`, `.env` (jamais logué) |
| **Sources & Recherches approfondies** | RAG / Carnets de recherche | NotebookLM carnet actif, Notion: *Knowledge Base* |

---

## 2. Table de Routage Locale du Projet

Lors de l'analyse d'un projet, ce skill vérifie l'existence des ancres clés :

```
[Projet Root]
├── contexte.md         -> Vérité absolue du cadrage (Stack, Décisions, Règles métier)
├── analyse.md          -> Détail des flux et edge cases
├── plan.md             -> Tâches en cours et jalons MVP
└── .gemini/config/     -> Configuration des serveurs MCP et skills globaux
```

---

## 3. Workflow d'Aiguillage Rapide

1. **Identifier la nature de la requête** : Est-ce une question business, technique, opérationnelle ou historique ?
2. **Consulter la table de routage** : Cibler directement le fichier ou l'ID de base adéquat sans scanner l'arborescence complète.
3. **Chargement ciblé** : Lire uniquement la section utile (ex: lignes 50-120 de `contexte.md`) plutôt que de saturer le contexte avec 20 fichiers.
4. **Redirection proactive** : Si l'info manque, indiquer à l'utilisateur exactement où la consigner dans l'OS pour les futurs prompts.
