---
name: prompt-creator
description: Métaprompting expert et ingénierie de prompts haute performance pour agents et LLM. Conçoit des prompts structurés, des instructions système chirurgicales et des directives de délégation pour sous-agents sans slop. Use when user says "/prompt-creator", asks to "créer un prompt", "optimiser ce prompt", "concevoir un prompt pour sous-agent", or "améliorer les instructions".
---

# Skill : prompt-creator (V1.0)
Architecture et ingénierie de prompts de niveau production basés sur le raisonnement structuré, la réduction d'ambiguïté et la délégation multi-agents.

---

## 1. Principes Fondamentaux (Anti-Slop)

1. **Rôle précis, pas de superlatifs** : Bannir « Tu es le meilleur expert mondial ». Définir le mandat, le périmètre et la posture opérationnelle.
2. **Contraintes négatives explicites (Guardrails)** : Lister explicitement ce que le LLM ne DOIT PAS faire.
3. **Format d'entrée et de sortie strict** : Schéma clair (Markdown, JSON, XML tags) sans bavardage introductif ni conclusion de politesse.
4. **Few-Shot ciblé** : 1 ou 2 exemples concrets (entrée -> sortie attendue) valent 10 paragraphes d'explications.
5. **Boucle de raisonnement (Thinking / Scratchpad)** : Forcer l'analyse interne avant la restitution finale.

---

## 2. Structure Standard d'un Prompt de Production

```markdown
<identity>
[Rôle exact, mandat technique et niveau de séniorité]
</identity>

<context>
[Données du projet, stack, contraintes métier]
</context>

<instructions>
1. Étape 1 : Analyser les entrées dans <thinking>
2. Étape 2 : Appliquer les règles métier strictes
3. Étape 3 : Produire la sortie au format exigé
</instructions>

<rules>
- RÈGLE 1 : Ne jamais inventer de données non fournies.
- RÈGLE 2 : Arrêt immédiat dès que le format est complété.
- RÈGLE 3 : Zéro bavardage avant ou après le livrable.
</rules>

<output_format>
[Schéma Markdown ou JSON exact attendu]
</output_format>
```

---

## 3. Workflow de Création

1. **Clarifier l'objectif final** : Quel est le livrable attendu ? Qui est l'utilisateur/l'agent consommateur ?
2. **Identifier les cas limites (Edge Cases)** : Qu'est-ce qui peut casser si l'entrée est incomplète ou ambiguë ?
3. **Rédiger le prompt structuré** avec balises XML sémantiques.
4. **Vérifier contre les 4 pièges classiques** :
   - ❌ Verbosité inutile.
   - ❌ Conflit entre deux instructions.
   - ❌ Absence de format de sortie figé.
   - ❌ Absence de règle d'arrêt.
