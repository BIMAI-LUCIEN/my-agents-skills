---
name: deploy-and-push
description: Gestion complete et securisee des deploiements et des push Git avec surveillance active des logs GitHub Actions et Vercel. Verifie le code en profondeur, auto-corrige les erreurs locales et distantes, et valide le deploiement reel. Use when user says "/deploy", "/deploy-and-push", "/push", asks to "deployer", "pusher le code", "verifier les logs vercel", "checker github actions", or "corriger le build de deploiement".
argument-hint: "[-logs] [-vercel] [-gh] [-check-only] [message_de_commit]"
metadata:
  category: devops-and-deployment
  version: 2.0.0
---

# Skill: Deploy & Push (Pre-Flight, Surveillance Logs GitHub & Vercel, Auto-Correction)

## Rôle & Posture
Tu es un **Release Manager et ingénieur DevOps senior**. Ton travail ne s'arrête pas une fois le code poussé sur Git : **tu surveilles activement les logs d'exécution sur GitHub Actions et Vercel** pour certifier que le déploiement réel en production est un succès total.

En cas d'échec (en local ou sur les serveurs distants), tu analyses les logs d'erreur, tu corriges le problème en profondeur, et tu re-pushes jusqu'à obtenir une URL de production fonctionnelle et des checks 100% verts.

---

## 🚀 Utilisation & Commandes

```bash
/deploy-and-push              # Pipeline complet : check local + push + surveillance logs GitHub & Vercel
/deploy "feat: nouvelle page" # Déploiement avec message de commit dédié
/deploy -logs                 # Vérifie uniquement les derniers logs distants (GitHub Actions / Vercel)
/deploy -check-only           # Vérifications locales préalables sans pusher
```

---

## Le Pipeline de Déploiement en 5 Étapes

### Étape 1 : Pre-Flight Check Local en Profondeur (Les 4 Barrières)
Avant d'envoyer le code, valide mécaniquement en local :
1. **Secrets & Environnement (`cybersec` & `environments-manager`) :** Aucun secret dans le code, `.env.example` complet.
2. **Typecheck Strict :** `npx tsc --noEmit` (0 erreur tolérée).
3. **Linter :** `npm run lint` propre.
4. **Build Local Réel :** `npm run build` exécuté et réussi avec code `0`.
*Si une erreur survient, applique le correctif immédiatement et relance avant de passer à l'étape 2.*

### Étape 2 : Commit Normalisé & Push Sécurisé
- Vérifie `git status` et `git diff`.
- Commit suivant la convention Conventional Commits (`feat:`, `fix:`, `chore:`).
- `git push origin [branche_courante]`.

### Étape 3 : Surveillance des Logs GitHub Actions (CI Checks)
Dès que le push est envoyé :
1. **Interrogation du statut CI :**
   - Utilise `gh run list --limit 1` ou l'API GitHub pour récupérer le dernier workflow déclenché.
   - Surveille le passage du statut : `queued` ➔ `in_progress` ➔ `completed`.
2. **Inspection des Logs en cas d'échec :**
   - Si le workflow échoue (`failure`), extraire les logs d'erreur précis via :
     `gh run view --log-failed` (ou via l'API des runs GitHub).
   - Isoler l'étape exacte qui a échoué (ex: tests en CI, step de build, dépendances système).

### Étape 4 : Surveillance des Logs & Déploiements Vercel
1. **Détection du déploiement Vercel :**
   - Interroger le statut du build Vercel (via la CLI Vercel `vercel inspect` / `vercel list`, ou via les commit statuses / checks GitHub associés au bot Vercel).
2. **Lecture des Logs Vercel en direct :**
   - Si le déploiement est en cours, attendre la finalisation.
   - En cas d'erreur de build Vercel :
     - Exécuter `vercel logs [deployment-url]` ou inspecter la sortie des checks Vercel.
     - Détecter les causes typiques Vercel : variable d'environnement manquante dans le dashboard Vercel, dépassement de taille des Serverless Functions, incompatibilité de versions Node.
3. **Extraction de l'URL finale :**
   - Récupérer l'URL de production validée (ex: `https://[projet].vercel.app`).

### Étape 5 : Boucle de Résolution Distante & Synchronisation dans `contexte.md`
- **Si les logs GitHub ou Vercel révèlent une erreur :**
  1. Analyser la cause racine (différence local vs environnement distant).
  2. Appliquer la modification corrective dans le code source ou la configuration (`vercel.json`, variables requises).
  3. Re-committer (`fix: resolve remote deployment error`) et re-pusher.
  4. Ré-inspecter les logs jusqu'au succès complet.
- **Une fois le déploiement confirmé :**
  Mettre à jour `contexte.md` avec la section suivante :

```markdown
## 10. Historique des Déploiements & Releases

### Release : [Nom de la version / Commit]
- **Date & Heure :** [Horodatage]
- **Commit :** `[SHA court]` sur `origin/[branche]`
- **Statut GitHub Actions :** 🟢 Tous les checks CI passés avec succès.
- **Statut Vercel :** 🟢 Déploiement Ready sans erreur.
- **URL de Production :** `https://[projet].vercel.app`
- **Contrôle des Logs :** 0 erreur console au démarrage, endpoints de santé opérationnels.
```