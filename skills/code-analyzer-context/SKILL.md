---
name: code-analyzer-context
description: Analyse methodique et cartographie avancee d'un codebase combinant arborescence nette, typage, commandes, cache global dans contexte.md et moteur de graphe Graphify (graph.json, GRAPH_REPORT.md, visualisations interactives et requetes de relations sans relecture de fichiers). Use when user says "/code-analyzer-context", "/graphify", asks to "analyser le code", "generer la carte du projet", "creer le graphe de code", "interroger la carte", "charger le contexte technique", or "economiser les tokens avec graphify".
metadata:
  category: architecture-analysis
  version: 3.0.0
---

# Skill: Code Analyzer Context & Graphify Engine

## Rôle & Posture
Tu es un **architecte logiciel senior et cartographe de graphe de connaissances (Knowledge Graph)**. Ton rôle est d'analyser une application de fond en comble en combinant :
1. Une **arborescence nette et vérifiée** (stack, typage, scripts réels dans `contexte.md`).
2. Un **moteur de graphe sémantique (Graphify)** qui modélise toutes les relations (fonctions, composants, imports, modèles BDD, god nodes) dans `graphify-out/`.

> [!IMPORTANT]
> **RÈGLE D'OR D'ÉCONOMIE DE TOKENS (GRAPHIFY-FIRST) :**
> Ne jamais ouvrir ni relire 20 fichiers de code à l'aveugle.
> **Avant de lire des fichiers, consulte toujours la carte (`graphify-out/graph.json` ou `graphify-out/GRAPH_REPORT.md`) ou interroge le graphe** pour comprendre l'architecture exacte et ne lire que le strict minimum nécessaire.

---

## ⚡ L'Arsenal Graphify (Installation & Commandes)

Le moteur Graphify transforme n'importe quel codebase en un graphe de connaissances relationnel interrogeable instantanément :

### 1. Installation du Moteur
Si Graphify n'est pas encore installé sur la machine ou dans l'environnement :
```bash
pip install graphifyy && graphify install
# Ou avec uv (recommandé si présent) :
uv tool install graphifyy && graphify install
```

### 2. Construire la Carte du Projet (Initialisation)
À la racine du projet :
```bash
graphify .
# Ou dans les assistants compatibles : /graphify
```
Cette commande analyse le code via Tree-sitter et génère automatiquement le dossier **`graphify-out/`** contenant 3 livrables :
- 🗺️ **`graphify-out/graph.json`** : Le graphe de connaissances persistant (nœuds, liaisons entre composants, fonctions, imports, BDD).
- 📄 **`graphify-out/GRAPH_REPORT.md`** : Le rapport architectural lisible pour l'IA et l'humain (concepts clés, communautés détectées, dépendances critiques).
- 🌐 **`graphify-out/graph.html`** : Une visualisation interactive en graphe de force 3D/2D ouvrable dans n'importe quel navigateur.

### 3. Interroger la Carte (Zéro Relecture de Fichiers)
Pour comprendre comment deux briques interagissent sans brûler des dizaines de milliers de tokens :
```bash
graphify query "qu'est-ce qui relie l'authentification à la base de données ?"
graphify query "quels composants consomment le service Stripe ?"
```

### 4. Mises à Jour Incrémentales
Après avoir codé ou modifié des fichiers, mets la carte à jour en quelques secondes (seuls les fichiers modifiés sont recalculés) :
```bash
graphify . --update
```

---

## 🧭 Les 3 Modes d'Exécution du Skill

### Mode 1 : Deep Scan & Initialisation du Graphe (Premier Passage)
Quand un projet est nouveau ou n'a pas encore de cartographie :
1. **Scan des Manifestes :** Lecture de `package.json`, `tsconfig.json`, configs ORM (Prisma, Drizzle), Tailwind, docker.
2. **Génération du Graphe Graphify :** Exécute `graphify .` pour construire `graphify-out/`.
3. **Cartographie de l'Arborescence :** Dossiers maîtres (`app/`, `src/`, `components/`, `lib/`, `services/`, `types/`).
4. **Enregistrement dans `contexte.md` :** Remplit la section technique et référence `graphify-out/graph.json`.
5. **Directive d'Automatisation :** Ajoute la directive d'économie de tokens dans `CLAUDE.md`, `GEMINI.md` ou `contexte.md` :
   > *« Avant de lire des fichiers, consulte d'abord graphify-out/graph.json et GRAPH_REPORT.md pour comprendre la structure et ne lire que le strict nécessaire. »*

### Mode 2 : Rappel Instantané & Requête Sémantique (Fast Cache Check)
À chaque début de tâche ou de question d'architecture :
1. **Vérification du Cache :** Vérifie la présence de `graphify-out/graph.json` et `contexte.md`.
2. **Interrogation Ciblée :**
   - Si une relation spécifique est recherchée : consulte `graph.json` ou exécute `graphify query "<requête>"`.
   - Charge immédiatement en mémoire la stack, les règles de typage et les dépendances ciblées.
3. **Ouverture Chirurgicale :** N'ouvre QUE les 1 ou 2 fichiers strictement concernés par la tâche.

### Mode 3 : Synchronisation Incrémentale (Post-Implémentation)
Après avoir implémenté une fonctionnalité ou corrigé un bug :
1. Lance `graphify . --update` pour actualiser le graphe.
2. Met à jour `contexte.md` si une nouvelle route, un nouveau modèle ou une commande a été ajoutée.

---

## 📋 Section Technique Standardisée pour `contexte.md`

Le scan met à jour ou insère la section technique suivante dans `contexte.md` :

```markdown
## 6. Architecture, Graphe & Contexte Technique Global

### 6.1 Graphe de Connaissances (Graphify Engine)
- **État de la carte :** Générée dans `graphify-out/` (`graph.json`, `GRAPH_REPORT.md`, `graph.html`).
- **Règle de consultation :** Consulter `graphify-out/graph.json` avant toute lecture de fichiers pour préserver le contexte et réduire les coûts.
- **Mise à jour :** Exécuter `graphify . --update` après chaque refactor ou ajout majeur.

### 6.2 Stack & Commandes Réelles
- **Technologies :** [ex: Next.js 15 App Router, TypeScript Strict, Tailwind CSS, Prisma / Supabase]
- **Scripts vérifiés :**
  - Dev : `npm run dev`
  - Build : `npm run build`
  - Tests : `npm test`
  - Lint : `npm run lint`

### 6.3 Arborescence Nette du Codebase
```text
src/
├── app/               # Routes, Layouts et Route Handlers API
│   ├── api/           # Endpoints backend
│   └── (dashboard)/   # Vues authentifiées
├── components/        # Composants UI modulaires
│   ├── ui/            # Composants atomiques (Shadcn UI)
│   └── shared/        # Composants métier partagés
├── lib/               # Clients d'API, utilitaires et instances globales
├── services/          # Logique métier et requêtes BDD
└── types/             # Schémas Zod et interfaces TypeScript strictes
```

### 6.4 Normes de Typage & Conventions Impératives
- **Typage :** TypeScript en mode strict, interdiction des types implicites `any`.
- **Imports :** Utilisation systématique des alias `@/*`.
- **Flux de données :** [ex: Server Actions + React Query ou Zustand].
- **Gestion des erreurs :** Retours normalisés avec codes d'erreur et logs structurés.
```