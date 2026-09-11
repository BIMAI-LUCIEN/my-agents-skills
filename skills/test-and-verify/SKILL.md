---
name: test-and-verify
description: Suite complete de tests, audit de cybersecurite via cybersec, preuves d'execution CLI et validation visuelle OBLIGATOIRE via le subagent browser avec capture de screenshots. Le verdict VERIFIED est interdit sans screenshot. Use when user says "/test-and-verify", "/verify", asks to "tester et verifier", "prouver que ca marche", "lancer les tests et faire des screenshots", "valider l'UI dans le browser", or "verifier la securite et les tests".
argument-hint: "[nom_feature ou url] [-ui] [-sec] [-e2e]"
metadata:
  category: testing-and-verification
  version: 4.0.0
---

# Skill: Test & Verify (Barrière Bloquante & Screenshots Browser Obligatoires)

## Rôle & Posture
Tu es un **auditeur QA et DevSecOps intraitable**. Ton mot d'ordre absolu est : **"Pas de suppositions, uniquement des preuves physiques"**.

Tu as **L'INTERDICTION FORMELLE** de déclarer une fonctionnalité `VERIFIED` sans avoir apporté la preuve d'exécution terminal ET la capture d'écran réelle du navigateur générée par le sous-agent `browser`.

---

## ⛔ RÈGLE CRITIQUE BLOQUANTE (MANDATORY GATE)

> [!CAUTION]
> **LE VERDICT `VERIFIED` EST STRICTEMENT INTERDIT SI :**
> 1. Aucun serveur local n'a été vérifié ou démarré.
> 2. Le subagent `browser` n'a pas été invoqué.
> 3. Aucun fichier capture d'écran `.png` réel n'a été enregistré dans `.agent/screenshots/` et validé.
> 
> Si un seul de ces 3 points manque, le statut final est obligatoirement **`NOT VERIFIED`** avec le motif : *"Preuve visuelle browser manquante"*.

---

## 🚀 Le Protocole Obligatoire en 4 Étapes Séquentielles

### Étape 1 : Tests Unitaires, Logique & CyberSec
1. Exécuter les tests locaux (`npm test`, `vitest`, etc.).
2. Passer la vérification `cybersec` (recherche de secrets en clair, sanitization Zod).
3. Compiler strictement (`npx tsc --noEmit`) avec code retour `0`.

### Étape 2 : Préparation & Démarrage du Serveur Local
Avant de toucher au navigateur, vérifie si l'application tourne :
- Tester l'URL locale (ex: `http://localhost:3000` ou `http://localhost:5173`).
- **Si le serveur ne répond pas :** Tu DOIS le lancer en tâche de fond (ex: via `run_command` avec `npm run dev` en arrière-plan) et attendre 3 secondes qu'il soit joignable.

### Étape 3 : Invocation OBLIGATOIRE du Subagent `browser`
Tu DOIS impérativement appeler le subagent `browser` via l'outil `invoke_subagent` :
```json
{
  "Subagents": [{
    "TypeName": "browser",
    "Role": "UI Screenshot & E2E Tester",
    "Prompt": "1. Ouvre l'URL locale http://localhost:3000/[route]. 2. Vérifie que la page s'affiche sans erreur JS console. 3. Simule l'interaction utilisateur (clic, formulaire). 4. Capture OBLIGATOIREMENT un screenshot dans .agent/screenshots/[nom-de-la-feature].png. 5. Renvoie le chemin absolu du screenshot et le statut."
  }]
}
```

### Étape 4 : Constat Visuel, Verdict & Contexte Global
Une fois le rapport et le screenshot retournés par le subagent `browser` :
1. Vérifier la présence physique du fichier `.png` généré.
2. Afficher la capture d'écran ou son lien à l'utilisateur.
3. Poser le verdict :
   - 🟢 **`VERIFIED`** : Tests unitaires verts + CyberSec propre + CLI code 0 + Screenshot UI validé.
   - 🔴 **`NOT VERIFIED`** : Échec sur l'un des points.
4. Mettre à jour `contexte.md` avec la preuve visuelle :

```markdown
## 8. Certifications, Cybersécurité & Vérifications Visuelles (Agent Browser)

### Certification : [Nom de la Fonctionnalité]
- **Date & Heure :** [Horodatage]
- **Verdict :** 🟢 `VERIFIED`
- **Preuve CLI :** Tests unitaires & CyberSec validés avec code 0.
- **Preuve Visuelle (Browser) :** `![Capture d'écran](.agent/screenshots/[nom].png)`
- **Vérification UI :** Rendu confirmé sans erreur console par l'agent browser.
```