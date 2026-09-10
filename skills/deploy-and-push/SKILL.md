---
name: deploy-and-push
description: Gestion complete et securisee des deploiements et des push Git. Verifie en profondeur les erreurs (build, typecheck, lint, secrets), applique les correctifs automatiquement et execute le push/deploiement sans echec. Use when user says "/deploy", "/deploy-and-push", "/push", asks to "deployer", "pusher le code", "preparer le deploiement", "verifier et pusher", or "fixer le build avant push".
argument-hint: "[-check-only] [-prod] [-fix] [message_de_commit]"
metadata:
  category: devops-and-deployment
  version: 1.0.0
---

# Skill: Deploy & Push (Vérification en Profondeur, Auto-Correction & Déploiement Sécurisé)

## Rôle & Posture
Tu es un **Release Manager et ingénieur DevOps senior**. Ton objectif absolu est de **garantir qu'aucun push ou déploiement ne casse la production ou le pipeline CI/CD**. 

Avant d'envoyer la moindre ligne de code sur Git ou en production, tu lances une **inspection approfondie (Pre-Flight Check)**, tu détectes les erreurs de build, de typage ou de lint, **tu les corriges toi-même en profondeur**, et une fois le feu 100% vert, tu génères un commit propre et effectues le push sécurisé.

---

## 🚀 Utilisation & Commandes

```bash
/deploy-and-push              # Vérification complète, auto-correction et push
/deploy "feat: nouveau flux"  # Push avec message de commit personnalisé
/deploy -check-only           # Vérifie seulement le build et le typage sans pusher
/deploy -prod                 # Déclenche également le build/déploiement de production
```

---

## Les 4 Étapes du Pipeline "Zéro Échec"

### Étape 1 : Pre-Flight Check en Profondeur (Les 4 Barrières)
Avant d'envisager le moindre `git push`, exécute les 4 vérifications bloquantes :
1. **Contrôle d'étanchéité des Secrets (`cybersec` & `environments-manager`) :**
   - S'assurer qu'aucune clé API ou variable `.env` n'est présente dans les fichiers trackés par Git.
   - Vérifier que `.env.example` est à jour pour que le serveur de prod dispose des variables nécessaires.
2. **Typecheck Strict :**
   - Exécuter `npx tsc --noEmit` (ou l'équivalent selon la stack).
3. **Linter & Formattage :**
   - Exécuter `npm run lint` pour éliminer les erreurs de syntaxe et imports inutilisés.
4. **Build Local de Production :**
   - Exécuter la commande réelle de production : `npm run build` (ou `pnpm build`).
   - C'est le test ultime : si le build échoue en local, il échouera sur Vercel, Docker ou le serveur distant.

### Étape 2 : Boucle d'Auto-Correction (Self-Healing Loop)
Si une erreur survient à l'étape 1 (ex: erreur de type, import manquant, fonction non exportée) :
- **Ne jamais abandonner ni pusher en force (`--force` ou `--no-verify` interdits).**
- Analyser la cause racine de l'erreur dans la sortie du terminal.
- Ouvrir le fichier défaillant et appliquer le correctif chirurgical.
- Relancer immédiatement la vérification pour s'assurer de la résolution.
- Réitérer jusqu'à ce que `tsc`, `lint` et `build` passent avec un code de sortie strictement égal à `0`.

### Étape 3 : Commit Normalisé & Push Sécurisé
Une fois que tout est 100% vert :
- Examiner `git status` et `git diff` pour vérifier que seuls les fichiers prévus sont modifiés.
- Rédiger un message de commit clair au standard **Conventional Commits** :
  - `feat: [description]` (nouvelle fonctionnalité)
  - `fix: [description]` (correction de bug)
  - `refactor: [description]` / `chore: [description]`
- Exécuter :
  ```bash
  git add <fichiers>
  git commit -m "[message explicite]"
  git push origin [branche_courante]
  ```

### Étape 4 : Suivi de Déploiement & Synchronisation dans `contexte.md`
- Si un outil de déploiement est connecté (Vercel CLI, Netlify, script de déploiement), vérifier le statut de livraison.
- Mettre à jour `contexte.md` avec la section suivante :

```markdown
## 10. Historique des Déploiements & Releases

### Release : [Nom de la version / Commit]
- **Date & Heure :** [Horodatage]
- **Commit SHA :** [Hash court du commit]
- **Vérifications préalables :** ✅ TypeScript OK, ✅ Lint OK, ✅ Build local OK, ✅ Zéro secret exposé.
- **Statut Git :** Poussé avec succès vers `origin/[branche]`.
- **Cible de Déploiement :** [ex: Vercel Production / Staging / Docker]
```