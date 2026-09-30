---
name: vercel
description: Piloter vos déploiements et projets Vercel via le serveur MCP Vercel (lister les projets, suivre les déploiements, inspecter les logs, gérer les variables d'environnement et les domaines).
---

# Vercel MCP Integration

Cette compétence permet de piloter votre infrastructure Vercel grâce au serveur MCP Vercel connecté.

## Capacités disponibles :
- **Projets et déploiements :** Lister vos projets, inspecter les déploiements en cours ou récents (`list_projects`, `list_deployments`, `create_deployment`).
- **Surveillance :** Consulter les logs de build et de runtime en direct pour diagnostiquer les erreurs (`get_build_logs`, `get_runtime_logs`).
- **Variables et domaines :** Gérer les variables d'environnement par environnement (Production, Preview) et configurer vos domaines DNS (`list_env_vars`, `create_env_var`, `list_domains`).

L'agent utilise automatiquement les outils MCP `vercel` dès que vous formulez votre demande.
