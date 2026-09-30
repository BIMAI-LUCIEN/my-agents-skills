# Serveur MCP n8n (Automation Engine)

Ce dossier contient les définitions et schémas d'outils du serveur Model Context Protocol (MCP) pour **n8n**.

## 🔌 Configuration dans `mcp_config.json`

Pour connecter votre instance n8n à Antigravity ou Claude Code, ajoutez le bloc suivant dans votre fichier `mcp_config.json` :

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": [
        "-y",
        "n8n-mcp"
      ],
      "env": {
        "N8N_API_KEY": "VOTRE_CLE_API_N8N",
        "N8N_HOST": "https://n8n.blackcompany.site",
        "N8N_URL": "https://n8n.blackcompany.site"
      }
    }
  }
}
```

## 🛠️ Outils MCP n8n inclus :
- **`tools_documentation`** : Documentation complète des nœuds et capacités n8n.
- **`search_nodes`** : Recherche des nœuds disponibles par nom ou catégorie.
- **`get_node`** : Détail complet de la structure et des paramètres d'un nœud.
- **`validate_node`** : Validation de la configuration d'un nœud spécifique.
- **`get_template`** : Récupération d'un template de workflow prêt à l'emploi.
- **`search_templates`** : Recherche parmi les templates officiels et communautaires n8n.
- **`validate_workflow`** : Validation globale de la syntaxe et de l'intégrité d'un workflow JSON avant déploiement.

## 🚀 Utilisation avec le Skill `n8n-manager`
Ce serveur MCP est directement piloté par le skill [`skills/n8n-manager`](../../skills/n8n-manager) pour créer, mettre à jour, activer et tester vos automatisations n8n en langage naturel.
