---
name: expo
description: Piloter votre environnement de développement mobile Expo et Metro via le serveur MCP Expo (lancer/arrêter Metro, logs récents, émulateurs, captures d'écran, diagnostic de projet).
---

# Expo Dev MCP Integration

Cette compétence permet d'interagir avec votre application mobile Expo grâce au serveur MCP Expo connecté.

## Capacités disponibles :
- **Serveur Metro :** Lancer, inspecter l'état et redémarrer Metro bundler (`metro_start`, `metro_status`, `metro_restart`, `metro_logs_recent`).
- **Émulateurs et devices :** Détecter les appareils connectés, lancer l'application, capturer des screenshots (`device_list`, `device_screenshot`, `device_app_launch`).
- **Diagnostic :** Inspecter la configuration et les dépendances du projet Expo (`project_inspect`).

L'agent utilise automatiquement les outils MCP `expo` dès que vous formulez votre demande.
