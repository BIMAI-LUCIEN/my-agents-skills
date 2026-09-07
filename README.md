# ⚡ My Agent Skills

Collection complète et portable de compétences (Skills) pour **Antigravity**, **Claude Code**, **Cursor**, **Gemini CLI** et les agents compatibles avec la spécification Agent Skills.

---

## 📦 Liste des compétences incluses (17 skills)

### 🎨 Médias, Vidéo & 3D
* **`ai-video-ad-creator`** : Directeur artistique motion design pour spots vidéo publicitaires 30s/45s découpés en micro-plans de 10s pour Runway, Kling, Sora, Hailuo, Luma.
* **`remotion-best-practices`** : Création et programmation vidéo en React / Remotion (keyframes, animations, interpolations, audio, R3F).
* **`threejs-3d-graphics`** : Programmation 3D WebGL, Three.js, shaders GLSL et optimisation des scènes 3D web.

### 🚀 Méthodologie & Orchestration
* **`antigravity-skill-orchestrator`** : Sélection automatique et dynamique des compétences requises selon la demande.
* **`apex`** : Méthodologie d'implémentation en 4 phases (Analyze, Plan, Execute, eXamine) avec agents parallèles et revue adverse.
* **`oneshot`** : Exécution rapide d'une tâche de bout en bout en une seule passe.

### 📋 Product Management & Méthode Agile (Suite BMAD)
* **`product-manager`** : Frameworks stratégiques, templates PRD et métriques SaaS.
* **`bmad-create-epics-and-stories`** : Découpage des exigences en Epics et User Stories actionnables.
* **`bmad-sprint-planning`** : Contrôle de maturité technique et suivi d'exécution des sprints.
* **`bmad-generate-project-context`** : Génération et structuration du contexte projet.
* **`bmad-agent-ux-designer`** : Spécialiste UX/UI ("Sally") pour les parcours et wireframes.

### 💻 Frontend & Design UI
* **`frontend-design`** : Direction artistique et design intentionnel (typographie, couleurs, contrastes).
* **`impeccable`** : Audit UX, design tokens, responsive et édition live dans le DOM.

### 🧪 Tests, Débogage & Fiabilité
* **`webapp-testing`** : Tests web automatisés de bout en bout avec Playwright.
* **`mobile-app-testing`** : Tests unitaires, automatisation UI et audits de performance pour iOS et Android.
* **`debugging-and-error-recovery`** : Analyse méthodique de la cause racine (root cause) des bugs et erreurs de build.
* **`verify-this`** : Vérification formelle d'affirmations et validations de code.

---

## 🛠️ Installation sur n'importe quelle machine

Une fois ce dépôt poussé sur votre compte GitHub (ex: `https://github.com/<votre-pseudo>/<votre-repo>`), vous pouvez installer vos skills sur n'importe quel ordinateur.

### Option 1 : Via le gestionnaire de skills (`npx skills`)

```bash
# Installer tous les skills du dépôt dans un projet :
npx skills add https://github.com/<votre-pseudo>/<votre-repo>

# Installer un skill en particulier :
npx skills add https://github.com/<votre-pseudo>/<votre-repo> --skill apex
npx skills add https://github.com/<votre-pseudo>/<votre-repo> --skill webapp-testing
```

---

### Option 2 : Installation globale automatique (Tous les projets)

#### Sous Windows (PowerShell) :
```powershell
.\install.ps1
```

#### Sous Linux / macOS (Bash) :
```bash
chmod +x install.sh
./install.sh
```

---

## 🚀 Comment publier ce dépôt sur votre GitHub

1. Créez un nouveau dépôt vide sur GitHub (ex: `my-agent-skills`).
2. Dans ce dossier, liez le dépôt distant et poussez vos fichiers :

```bash
git remote add origin https://github.com/<votre-pseudo>/my-agent-skills.git
git branch -M main
git push -u origin main
```
