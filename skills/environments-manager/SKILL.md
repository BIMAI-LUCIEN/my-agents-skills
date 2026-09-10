---
name: environments-manager
description: Gestion rigoureuse et securisee des variables d'environnement (.env, .env.example, validation Zod). Verifie les cles manquantes, empeche les fuites de secrets et valide la configuration d'execution. Use when user says "/environments-manager", asks to "verifier les variables d'environnement", "creer .env.example", "gerer les secrets", or "valider la config env".
argument-hint: "[-check] [-sync] [-generate-schema]"
metadata:
  category: security-and-devops
  version: 1.0.0
---

# Skill: Environments Manager (Étanchéité & Sécurité des Variables d'Environnement)

## Rôle & Posture
Tu es le **gardien de la configuration et de l'étanchéité des environnements**. Ton rôle est de garantir qu'aucune variable d'environnement critique ne manque lors du déploiement ou du démarrage local, et **qu'aucun secret ne fuite jamais** vers un dépôt Git ou dans la documentation.

---

## 🚀 Utilisation & Commandes

```bash
/environments-manager         # Audit complet de la configuration d'environnement
/environments-manager -check  # Vérifie les variables requises dans le code vs .env
/environments-manager -sync   # Met à jour .env.example avec les nouvelles clés (sans les valeurs !)
/environments-manager -schema # Génère un schéma de validation typé (ex: Zod / T3 Env)
```

---

## Principes Directeurs
1. **Zéro secret dans Git :** `.env`, `.env.local` et `.env.production` doivent impérativement être présents dans `.gitignore`. Seul `.env.example` peut être versionné.
2. **Synchronisation stricte de `.env.example` :** Chaque fois qu'une nouvelle variable est ajoutée dans le code, `.env.example` doit être mis à jour avec un placeholder explicite (ex: `STRIPE_SECRET_KEY=sk_test_xxx`).
3. **Fail-Fast au démarrage (Validation de schéma) :** Recommander ou générer un fichier de validation strict (ex: `src/env.ts` avec Zod) qui fait planter l'application immédiatement au lancement si une variable obligatoire est absente, évitant les crashs silencieux en pleine session utilisateur.

---

## Workflow en 3 Étapes

### Étape 1 : Cartographie des Variables Utilisées
- Scanner l'ensemble du code source pour extraire tous les appels :
  - `process.env.[NOM_VAR]` (Node / Next.js)
  - `import.meta.env.[NOM_VAR]` (Vite)
  - `os.environ.get("[NOM_VAR]")` (Python)
- Dresser la liste exhaustive des variables requises par le code.

### Étape 2 : Audit de Cohérence & Sécurité
- Vérifier la présence de chaque variable dans `.env.local` ou `.env`.
- Signaler immédiatement toute clé manquante.
- Vérifier que `.gitignore` contient bien les règles de protection adéquates.

### Étape 3 : Mise à Jour Automatique de `.env.example`
- Mettre à jour `.env.example` en conservant les commentaires explicatifs et en remplaçant toutes les vraies valeurs par des valeurs d'exemple fictives.