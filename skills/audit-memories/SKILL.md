---
name: audit-memories
description: Nettoyage, deduplication et synchronisation des fichiers de memoire persistante (contexte.md, GEMINI.md, AGENTS.md) pour eliminer les regles perimees et les contradictions. Use when user says "/audit-memories", asks to "nettoyer la memoire", "purger contexte.md", "resoudre les contradictions", or "clarifier les regles du projet".
argument-hint: "[-purge] [-compress] [fichier]"
metadata:
  category: agent-hygiene
  version: 1.0.0
---

# Skill: Audit Memories (Hygiène Cognitive & Résolution des Contradictions)

## Rôle & Posture
Tu es le **gardien de la cohérence et de la mémoire de l'agent**. Avec le temps, les projets accumulent des fichiers de contexte (`contexte.md`, `GEMINI.md`, `AGENTS.md`) remplis de notes contradictoires, de décisions périmées et de logs obsolètes. Cela désoriente le modèle et dégrade la qualité du code.

Ton rôle est d'analyser ces fichiers, de **purger les règles mortes, résoudre les contradictions et compresser la mémoire** pour ne garder qu'une source de vérité claire, fraîche et immédiatement assimilable.

---

## 🚀 Utilisation & Commandes

```bash
/audit-memories               # Analyse des fichiers de contexte et rapport de contradictions
/audit-memories -compress     # Compresse l'historique de contexte.md sans perdre l'état actuel
/audit-memories -purge        # Supprime les règles et décisions obsolètes
```

---

## Principes Directeurs
1. **Une seule source de vérité par sujet :** Si une décision a évolué (ex: passage de REST à GraphQL, ou changement de BDD), l'ancienne décision doit être archivée ou supprimée, jamais laissée en concurrence avec la nouvelle.
2. **Compression de l'historique :** Le journal d'implémentation ne doit pas devenir un roman de 1000 lignes. Les tâches validées des sprints passés sont condensées en une liste à puces synthétique.
3. **Zéro règles "fantômes" :** Supprimer les consignes qui ne correspondent plus au code réel (ex: instructions pour un framework abandonné).

---

## Workflow d'Audit Mémoire en 3 Étapes

### Étape 1 : Lecture Croisée des Fichiers de Mémoire
- Scanner `contexte.md`, `contexte_code.md`, `GEMINI.md` et `AGENTS.md`.
- Confronter les règles écrites avec le code source réel pour vérifier leur validité.

### Étape 2 : Détection des Contradictions & Dérives
- **Contradictions de Stack :** Deux fichiers indiquant des versions ou des outils différents.
- **Règles redondantes :** Répétition de la même consigne sous 3 formes différentes.
- **Inflation de contexte :** Sections historiques qui consomment des tokens sans valeur ajoutée actuelle.

### Étape 3 : Consolidation & Réécriture Propre
- Proposer une version compactée et unifiée du fichier `contexte.md`.
- Sur validation, appliquer la réécriture pour libérer de la bande passante cognitive pour l'agent.