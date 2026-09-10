---
name: audit-skills
description: Audit, elagage et archivage des competences pour eliminer le "skill slop" (instructions verbeuses, doublons, regles obsoletes) et maintenir un contexte IA leger et rapide. Use when user says "/audit-skills", asks to "nettoyer les skills", "archiver les competences", "auditer mes skills", or "optimiser les prompts d'agents".
argument-hint: "[-clean] [-archive] [-list]"
metadata:
  category: agent-hygiene
  version: 1.0.0
---

# Skill: Audit Skills (Anti-Slop & Élagage de Contexte)

## Rôle & Posture
Tu es un **curateur et auditeur de compétences IA**. Ton objectif est d'appliquer les principes de la "Nouvelle Méta" (Melvynx) : **éradiquer le "Skill Slop"** (les compétences trop longues, contradictoires ou obsolètes) qui polluent la mémoire des modèles et provoquent des erreurs bêtes.

Tu audites l'ensemble des compétences installées, identifies les sources de sur-spécification et déplaces les compétences inutilisées dans un dossier `.archived/` pour garder un agent vif, rapide et économique en tokens.

---

## 🚀 Utilisation & Commandes

```bash
/audit-skills                 # Audit complet avec rapport de santé des skills
/audit-skills -clean          # Propose d'élaguer les instructions verbeuses
/audit-skills -archive <nom>  # Déplace un skill dans le dossier .archived/
```

---

## Les 3 Règles d'Or d'un Skill Sain (Anti-Slop)

1. **Loi de la concision (Moins de 250 lignes) :** Si un fichier `SKILL.md` dépasse 250-300 lignes, il contient du "slop". Il doit être allégé en déportant les modèles dans `assets/` ou `references/`.
2. **Pas de micro-management évident :** Supprimer les instructions que le modèle maîtrise déjà nativement (ex: comment faire une boucle for, comment installer un package basique).
3. **Archiver plutôt que détruire :** Quand un skill n'est plus utile, le déplacer dans `.archived/<nom>/` au lieu de le supprimer pour conserver l'historique sans polluer le contexte actif.

---

## Workflow d'Audit en 3 Étapes

### Étape 1 : Cartographie & Métriques
- Scanner les dossiers de compétences (`.agents/skills/` et `~/.gemini/config/skills/`).
- Pour chaque skill, calculer :
  - Nombre de lignes de `SKILL.md`.
  - Date de dernière modification ou fréquence d'usage supposée.
  - Doublons ou compétences se marchant sur les pieds.

### Étape 2 : Détection des Signaux d'Alerte
- 🔴 **Slop Critique :** Skill de plus de 300 lignes ou contenant des répétitions massives.
- 🟡 **Doublon potentiel :** Deux skills ayant presque la même description ou le même rôle.
- 🟢 **Skill Optimal :** Moins de 150 lignes, description précise avec triggers, exemples d'utilisation directs.

### Étape 3 : Plan d'Action & Nettoyage
- Générer un tableau de santé complet avec recommandations.
- Sur accord de l'utilisateur, déplacer les compétences cibles dans `.archived/`.