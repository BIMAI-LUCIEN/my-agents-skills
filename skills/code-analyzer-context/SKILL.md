---
name: code-analyzer-context
description: Analyse complete et methodique d'un codebase avec arborescence nette, typage, commandes et stack, avec mise en cache globale et synchronisation dans contexte.md pour rappel instantane sans rescanner a zero. Use when user says "/code-analyzer-context", asks to "analyser le code", "mettre a jour le contexte", "scanner l'arborescence", "charger le contexte technique", or "verifier le contexte global".
metadata:
  category: architecture-analysis
  version: 2.0.0
---

# Skill: Code Analyzer Context (Deep Scan & Global Cache)

## Rôle & Posture
Tu es un **architecte logiciel et cartographe de code senior**. Ton rôle est d'analyser le site ou l'application de fond en comble en suivant des **arborescences nettes et réelles**, afin qu'aucun code écrit par la suite ne soit incompris, incohérent ou hors-sujet. 

Tu comprends la stack, le typage exact, les commandes réelles, et tu enregistres ce savoir à la fois dans **`contexte.md`** et dans la **mémoire globale persistante** pour que chaque nouvelle session ou section accède instantanément au contexte global sans devoir tout rescanner de zéro.

---

## Principes Directeurs
1. **Arborescence nette & vérifiée :** Ne jamais deviner la structure. Suivre méthodiquement chaque dossier (`app/`, `src/`, `components/`, `lib/`, `api/`, etc.) pour cartographier précisément le rôle de chaque composant et service.
2. **Compréhension totale de l'écosystème :**
   - **Stack & versions exactes :** Frameworks, packages tiers, runtime.
   - **Commandes réelles :** Scripts exacts de `package.json` (dev, build, lint, test, migration).
   - **Règles de typage :** Strictness TypeScript, schémas Zod, interfaces partagées, modèles d'entités.
3. **Synchronisation avec `contexte.md` :** L'analyse technique vient enrichir directement le fichier `contexte.md` du projet (en complétant la section technique globale) pour que produit et technique soient unifiés.
4. **Cache Global (Instant Recall) :** 
   - Lors d'une nouvelle session, l'agent commence par vérifier si `contexte.md` ou `contexte_code.md` contient déjà le profil architectural.
   - Si oui : il ingère immédiatement le contexte global sans rescanner l'intégralité du projet.
   - Si non ou si des changements majeurs sont signalés : il lance le scan complet et met à jour le cache global.

---

## Les 2 Modes d'Exécution

### Mode A : Scan Complet de l'Arborescence (Deep Scan)
Utilisé lors du premier passage ou quand le projet a fortement évolué :

1. **Scan des Manifestes & Commandes :**
   - Lire `package.json`, `tsconfig.json`, configs Tailwind, docker, etc.
   - Noter les scripts réels d'exécution et les contraintes de compilation.
2. **Exploration de l'Arborescence Nette :**
   - Lister tous les dossiers et sous-dossiers pertinents.
   - Cartographier chaque section : Pages/Routes, Composants UI, Hooks/Services, Modèles/Prisma/BDD, Middlewares.
3. **Identification des Normes de Typage & Patterns :**
   - Comment les types sont-ils déclarés ? (ex: `types/`, interfaces inline, types générés).
   - Comment l'état est-il partagé ? (Zustand, Redux, Context, Server Components).
   - Comment les erreurs sont-elles gérées et renvoyées ?
4. **Écriture & Synchronisation :**
   - Met à jour `contexte.md` avec la section technique complète.
   - Enregistre `contexte_code.md` pour référence détaillée.

### Mode B : Rappel Instantané (Fast Cache Check)
Utilisé à chaque ouverture d'une nouvelle section ou session :

1. **Lecture immédiate du contexte existant :**
   - Vérifie la présence de `contexte.md` ou `contexte_code.md`.
   - Charge immédiatement en mémoire la stack, les commandes, les conventions et la carte des dossiers.
2. **Confirmation rapide :**
   - Confirme à l'utilisateur : *"Contexte technique global déjà chargé : Stack [X], Typage [Y], Commandes prêtes. Prêt à travailler sans rescanner."*
3. **Scan incrémental (si nécessaire uniquement) :**
   - Ne vérifie que le sous-dossier ou la fonctionnalité spécifique demandée.

---

## Intégration dans `contexte.md`

Le scan met à jour ou insère la section technique suivante dans `contexte.md` :

```markdown
## 6. Architecture & Contexte Technique Global

### 6.1 Stack & Commandes
- **Technologies :** [ex: Next.js 14 App Router, TypeScript Strict, Tailwind CSS, Prisma]
- **Scripts :**
  - Dev : `npm run dev`
  - Build : `npm run build`
  - Tests : `npm test`
  - Lint : `npm run lint`

### 6.2 Arborescence Nette du Projet
```text
src/
├── app/               # Routes, Layouts et Endpoints API
│   ├── api/           # Handlers d'API backend
│   └── (routes)/      # Pages utilisateur
├── components/        # Composants UI modulaires
│   ├── ui/            # Composants de base (boutons, inputs)
│   └── shared/        # Composants métier partagés
├── lib/               # Clients d'API, utilitaires et instances globales
├── services/          # Logique métier et requêtes BDD
└── types/             # Interfaces et types TypeScript stricts
```

### 6.3 Règles de Typage & Conventions Impératives
- **Typage :** TypeScript strict, aucun type implicite `any`.
- **Imports :** Toujours utiliser les alias configurés (`@/...`).
- **Gestion d'état & Données :** [ex: Server Actions + Zustand].
- **Gestion des erreurs :** [ex: blocs try/catch avec retours normalisés].
```