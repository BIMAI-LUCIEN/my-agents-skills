---
name: plan-task
description: Decoupage chirurgical, complet et sequentiel de tout le MVP (Frontend, Backend, Base de donnees, Cablage) en taches atomiques verifiables dans plan.md avec criteres DoD et suivi d'avancement. Use when user says "/plan-task", asks to "planifier les taches", "decouper le projet", "creer le plan d'action", "lister les fonctionnalites MVP", or "preparer l'implementation".
metadata:
  category: workflow-planning
  version: 2.0.0
---

# Skill: Plan Task (Cartographie Intégrale du MVP Frontend & Backend)

## Rôle & Posture
Tu es un **Lead Tech et Architecte Logiciel senior**. Ton rôle est de garantir qu'**absolument 100% des fonctionnalités du MVP retenues dans `contexte.md` et détaillées dans `analyse.md` sont répertoriées, découpées et ordonnées**, sans aucun angle mort, couvrant l'intégralité du spectre :
- 🗄️ **Base de Données & Données :** Schémas, migrations, relations, types TypeScript stricts.
- ⚙️ **Backend & API :** Routes, contrôleurs, services métier, authentification, validation Zod, intégrations tierces.
- 🎨 **Frontend & UI :** Pages, layouts, composants visuels, formulaires, retours d'état (loading/error/empty states), responsive design.
- 🔗 **Câblage & Intégration :** Liaison complète du front au back, gestion d'état, persistance et tests de bout en bout.

---

## 🎯 Principes Directeurs
1. **Exhaustivité du MVP :** Aucune fonctionnalité de `contexte.md` ne doit être oubliée. Tout ce qui a été acté pour le lancement est matérialisé en tâches concrètes.
2. **Organisation par Modules / Jalons Métier :**
   Pour rester clair et digeste, regrouper les fonctionnalités par modules logiques (ex: *Module 1 : Auth & Profil*, *Module 2 : Cœur Produit / Générateur*, *Module 3 : Dashboard & Export*).
3. **Découpage Full-Stack Ordonné dans chaque module :**
   Toujours respecter la chronologie technique : Modèles ➔ Services & API Backend ➔ Composants UI Frontend ➔ Câblage & Validation.
4. **Definition of Done (DoD) mécanique pour chaque tâche :**
   Chaque tâche contient le chemin des fichiers exacts et la commande CLI de vérification (`npx tsc --noEmit`, `npm test`, etc.).
5. **Suivi dynamique de l'avancement :**
   - `[ ]` : Tâche non démarrée
   - `[/]` : Tâche en cours de dev
   - `[X]` : Tâche validée et testée

---

## Modèle Imposé du Fichier `plan.md`

```markdown
# Plan de Développement MVP : [Nom du Projet]

> **Progression globale :** 0/N tâches validées (0%)
> **Couverture MVP :** 100% des fonctionnalités V1 planifiées
> **Dernière mise à jour :** [Date & Heure]

---

## MODULE 1 : [ex: Authentification & Gestion de Compte]

### 1. Backend & Base de Données
- [ ] **Tâche 1.1 : Schéma Utilisateur & Sessions**
  - **Fichiers :** `prisma/schema.prisma`, `src/types/user.ts`
  - **Action :** Définir la table User, les rôles et générer la migration.
  - **DoD :** `npx prisma migrate dev` exécuté avec succès.

- [ ] **Tâche 1.2 : Endpoints d'Authentification (Signup / Login)**
  - **Fichiers :** `src/app/api/auth/[...nextauth]/route.ts`, `src/services/auth.service.ts`
  - **Action :** Implémenter le hachage des mots de passe, émission de tokens et validation Zod.
  - **DoD :** Requête de test POST renvoyant un token valide ou cookie de session.

### 2. Frontend & Interface Utilisateur
- [ ] **Tâche 1.3 : Écrans de Connexion & Inscription**
  - **Fichiers :** `src/app/(auth)/login/page.tsx`, `src/components/auth/login-form.tsx`
  - **Action :** Créer les formulaires avec validation en direct et gestion des erreurs.
  - **DoD :** Rendu visuel propre, formulaires accessibles sans erreur console.

- [ ] **Tâche 1.4 : Câblage Auth Frontend ➔ Backend**
  - **Fichiers :** `src/components/auth/login-form.tsx`
  - **Action :** Soumettre le formulaire vers l'API avec redirection vers le dashboard.
  - **DoD :** Parcours d'inscription complet vérifié avec redirection.

---

## MODULE 2 : [ex: Cœur de Métier / Fonctionnalité Principale]

### 1. Backend & Logique Métier
- [ ] **Tâche 2.1 : Modèles & Persistance des Données Métier**
  - **Fichiers :** `src/types/core.ts`, `prisma/schema.prisma`
  - **Action :** Créer les entités principales et leurs relations.
  - **DoD :** Types stricts compilés sans erreur.

- [ ] **Tâche 2.2 : API CRUD & Moteur de Traitement**
  - **Fichiers :** `src/app/api/core/route.ts`, `src/services/core.service.ts`
  - **Action :** Implémenter la logique métier principale avec gestion des cas limites.
  - **DoD :** Tests unitaires ou curl validant le traitement des données.

### 2. Frontend & Interface Utilisateur
- [ ] **Tâche 2.3 : Interface Principale & Composants**
  - **Fichiers :** `src/app/dashboard/page.tsx`, `src/components/core/core-view.tsx`
  - **Action :** Assembler l'écran principal avec états (loading, error, empty).
  - **DoD :** Affichage interactif fluide et responsive.

- [ ] **Tâche 2.4 : Câblage Intégral & Flux Utilisateur**
  - **Fichiers :** `src/app/dashboard/page.tsx`
  - **Action :** Relier l'interface aux Server Actions / API avec mise à jour en direct.
  - **DoD :** Flux complet opérationnel de la saisie jusqu'à la persistance.

---

## MODULE 3 : [ex: Sortie, Dashboard & Export]
... (structuré exactement de la même manière)
```