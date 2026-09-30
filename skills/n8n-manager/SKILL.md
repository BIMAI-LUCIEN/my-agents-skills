---
name: n8n-manager
description: >-
  Gestionnaire et générateur automatique de workflows n8n pour Miguel OS / Automate Solution.
  Utilise l'API Key configurée de l'instance client sur https://n8n.blackcompany.site/api/v1.
---

# Skill : n8n-manager (n8n Automation Engine Specialist)

Ce skill permet de piloter et d'automatiser des workflows sur votre instance n8n (`https://n8n.blackcompany.site/api/v1`).
Il peut être exécuté soit via le **Serveur MCP `n8n`**, soit via le **script CLI `scripts/n8n_client.py`**.

---

## 🔑 Clé d'API & Connexion

- **Instance URL** : `https://n8n.blackcompany.site/api/v1` (ou via variable `N8N_INSTANCE_URL`)
- **API Key** : Définie via la variable d'environnement `N8N_API_KEY` ou un fichier local `.env`
- **Serveur MCP** : Serveur MCP `n8n` enregistré dans `mcp_config.json`

---

## 🛠️ Utilisation Directe via le Client CLI

Toutes les commandes s'exécutent directement :

### 1. Lister les workflows
```bash
python scripts/n8n_client.py list
```

### 2. Créer un workflow à partir d'un fichier JSON
```bash
python scripts/n8n_client.py create path/to/workflow.json
```

### 3. Activer un workflow (Mettre en prod)
```bash
python scripts/n8n_client.py activate <WORKFLOW_ID>
```

### 4. Désactiver un workflow
```bash
python scripts/n8n_client.py deactivate <WORKFLOW_ID>
```

### 5. Mettre à jour un workflow
```bash
python scripts/n8n_client.py update <WORKFLOW_ID> path/to/workflow.json
```

### 6. Supprimer un workflow
```bash
python scripts/n8n_client.py delete <WORKFLOW_ID>
```
