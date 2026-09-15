#!/usr/bin/env node
/**
 * NotebookLM Direct CLI Runner
 * Connects directly to NotebookLM persistent sessions with full stealth & session RAG.
 */

import { BrowserSession } from "file:///C:/Users/MIGUEL IA/AppData/Local/Programs/nodejs/node_modules/notebooklm-mcp/dist/session/browser-session.js";
import { SharedContextManager } from "file:///C:/Users/MIGUEL IA/AppData/Local/Programs/nodejs/node_modules/notebooklm-mcp/dist/session/shared-context-manager.js";
import { AuthManager } from "file:///C:/Users/MIGUEL IA/AppData/Local/Programs/nodejs/node_modules/notebooklm-mcp/dist/auth/auth-manager.js";
import { NotebookLibrary } from "file:///C:/Users/MIGUEL IA/AppData/Local/Programs/nodejs/node_modules/notebooklm-mcp/dist/library/notebook-library.js";

const command = process.argv[2];
const args = process.argv.slice(3);

const library = new NotebookLibrary();
const activeNotebook = library.getActiveNotebook();
let notebookUrl = activeNotebook ? activeNotebook.url : "https://notebook.google.com/notebook/377d190e-9684-401b-8dde-0498e189fa98";

// Parse --url override
const urlIdx = args.indexOf("--url");
if (urlIdx !== -1 && args[urlIdx + 1]) {
  notebookUrl = args[urlIdx + 1];
  args.splice(urlIdx, 2);
}

const authManager = new AuthManager();

async function main() {
  if (command === "status") {
    const isAuth = await authManager.hasSavedState();
    console.log(JSON.stringify({
      authenticated: isAuth,
      activeNotebook: activeNotebook ? activeNotebook.name : "Projet NotebookLM",
      notebookUrl: notebookUrl
    }, null, 2));
    process.exit(0);
  }

  if (command === "query" || command === "ask") {
    const question = args.join(" ");
    if (!question) {
      console.error("Usage: node notebooklm_cli.mjs query <votre question>");
      process.exit(1);
    }

    const contextManager = new SharedContextManager(authManager);
    const session = new BrowserSession("cli-session", contextManager, authManager, notebookUrl);
    await session.init();

    const answer = await session.ask(question);
    console.log(answer);

    await session.close();
    process.exit(0);
  }

  if (command === "add-source") {
    const sourceContent = args.join(" ");
    if (!sourceContent) {
      console.error("Usage: node notebooklm_cli.mjs add-source <url ou texte>");
      process.exit(1);
    }

    const contextManager = new SharedContextManager(authManager);
    const session = new BrowserSession("cli-source", contextManager, authManager, notebookUrl);
    await session.init();

    const isUrl = sourceContent.startsWith("http://") || sourceContent.startsWith("https://");
    const result = await session.addSource(
      isUrl ? { type: "url", url: sourceContent } : { type: "text", text: sourceContent, title: "Source Document" }
    );

    console.log(JSON.stringify(result, null, 2));
    await session.close();
    process.exit(0);
  }

  if (command === "audio") {
    const contextManager = new SharedContextManager(authManager);
    const session = new BrowserSession("cli-audio", contextManager, authManager, notebookUrl);
    await session.init();

    console.log("Declenchement de la generation Audio Overview...");
    const genResult = await session.generateAudio();
    console.log("Audio status:", genResult);

    await session.close();
    process.exit(0);
  }

  console.log("Commandes supportees : status | query <question> | add-source <url/texte> | audio");
  process.exit(0);
}

main().catch((err) => {
  console.error("Erreur CLI :", err);
  process.exit(1);
});
