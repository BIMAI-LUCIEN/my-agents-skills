---
name: canva
description: Piloter vos designs, présentations, assets et exports Canva via le serveur MCP Canva Connect API (lister les designs, créer des visuels, exporter en PDF/PNG/PPTX, uploader des images).
---

# Canva MCP Integration

Cette compétence permet d'interagir directement avec votre compte Canva grâce au serveur MCP Canva Connect API connecté.

## Capacités disponibles :
- **Designs et Visuels :** Lister vos créations (`canva_list_designs`), obtenir les détails d'un design (`canva_get_design`), créer un nouveau design adapté (présentation, post Instagram, document, etc.) (`canva_create_design`).
- **Exports :** Exporter vos designs en PDF, PNG, JPG, PPTX avec URL de téléchargement directe (`canva_export_design`).
- **Médiathèque et Dossiers :** Uploader des images locales (`canva_upload_asset`), organiser et explorer vos dossiers Canva (`canva_list_folders`, `canva_create_folder`).
- **Statut :** Vérifier l'état de la connexion et des autorisations (`canva_get_auth_status`, `canva_get_profile`).

L'agent utilise automatiquement les outils MCP `canva` dès que vous formulez votre demande.
