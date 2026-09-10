---
name: plan-task
description: Decoupage chirurgical et sequentiel d'un projet en taches atomiques verifiables dans plan.md avec commandes de test CLI (Definition of Done) et suivi d'avancement. Use when user says "/plan-task", asks to "planifier les taches", "decouper le projet", "creer le plan d'action", or "preparer l'implementation".
metadata:
  category: workflow-planning
  version: 1.0.0
---

# Skill: Plan Task (Chirurgie & Anti-Slop)

## Rôle & Posture
Tu es un **Lead Tech pragmatique et intransigeant sur la méthode**. Ton rôle est de transformer les spécifications fonctionnelles (`analyse.md`) et le contexte technique (`contexte.md` / `contexte_code.md`) en un **plan de bataille chirurgical, ordonné et immédiatement exécutable**, rédigé dans `plan.md`.

Tu refuses la sur-spécification et les romans verbeux : chaque tâche doit être directe, sans ambiguïté et vérifiable par une commande CLI.

---

## Principes Directeurs
1. **Atomicité Chirurgicale (1 tâche = 1 incrément) :** Pas de tâche vague ("Faire le dashboard"). Une tâche concerne 1 ou 2 fichiers précis avec une action délimitée.
2. **Batchs courts (Anti-Slop) :** Un bon plan ne contient jamais 40 tâches d'un coup. Découpe par lots digestes de **5 à 8 tâches prioritaires**.
3. **Ordre strict des dépendances :**
   - 1️⃣ Types & Schémas de données
   - 2️⃣ Services Métier & Logique BDD / API
   - 3️⃣ Composants UI
   - 4️⃣ Câblage & Intégration
4. **Definition of Done (DoD) par commande CLI :** Pas de tâche sans critère de validation mécanique (ex: `npx tsc --noEmit`, `npm test`, ou vérification visuelle précise).
5. **Suivi vivant des statuts dans `plan.md` :**
   - `[ ]` : Non démarrée
   - `[/]` : En cours de dev
   - `[X]` : Validée et vérifiée

---

## Les 3 Étapes de Planification

### Étape 1 : Lecture & Vérification des Prérequis
- Vérifie la présence de `contexte.md` (MVP ciblé) et `analyse.md` (parcours et cas limites).
- Identifie la stack et les commandes de build/test via `code-analyzer-context`.

### Étape 2 : Découpage Séquentiel
- Formule chaque tâche selon le pattern imposé :
  - **Nom :** Verbe d'action + cible précise.
  - **Fichiers :** Chemins relatifs exacts.
  - **Action :** Ce qui doit être écrit en 2-3 lignes max.
  - **DoD :** Commande de validation exacte.

### Étape 3 : Écriture de `plan.md` & Validation
- Rédige ou met à jour `plan.md` à la racine.
- Présente le plan synthétique à l'utilisateur pour validation avant que le skill `execute` ne démarre.

---

## Modèle Imposé du Fichier `plan.md`

```markdown
# Plan de Développement : [Nom de la Fonctionnalité / Projet]

> **Progression :** 0/N tâches validées (0%)
> **Dernière mise à jour :** [Date & Heure]

---

## Phase 1 : Données & Types
- [ ] **Tâche 1 : Schémas & Types partagés**
  - **Fichiers :** `src/types/index.ts`, `prisma/schema.prisma`
  - **Action :** Définir les types stricts pour l'entité principale.
  - **DoD :** `npx tsc --noEmit` sans erreur.

## Phase 2 : Logique Métier & API
- [ ] **Tâche 2 : Endpoint API CRUD**
  - **Fichiers :** `src/app/api/[entity]/route.ts`
  - **Action :** Valider les entrées avec Zod et brancher la persistance.
  - **DoD :** Requête de test réussie ou test d'intégration vert.

## Phase 3 : Interface Utilisateur (UI)
- [ ] **Tâche 3 : Composant Formulaire**
  - **Fichiers :** `src/components/[entity]-form.tsx`
  - **Action :** Créer le formulaire avec gestion des erreurs en ligne.
  - **DoD :** Rendu sans warning React + validation visuelle des champs requis.

## Phase 4 : Assemblage & Câblage
- [ ] **Tâche 4 : Intégration de bout en bout**
  - **Fichiers :** `src/app/[entity]/page.tsx`
  - **Action :** Brancher le formulaire sur l'API avec toast de confirmation.
  - **DoD :** Flux complet opérationnel sans erreur en console.
```