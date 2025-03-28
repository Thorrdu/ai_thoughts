from typing import List
from archon import Agent, Tool
from langchain.llms import Ollama
from langchain.embeddings import HuggingFaceEmbeddings
from chromadb import Client
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

class WebSearchTool(Tool):
    """Outil de recherche web utilisant DuckDuckGo"""
    def __init__(self):
        super().__init__(
            name="web_search",
            description="Effectue une recherche web via DuckDuckGo",
            parameters={
                "query": {"type": "string", "description": "La requête de recherche"}
            }
        )
    
    def execute(self, query: str) -> str:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            return "\n".join([f"- {r['title']}: {r['link']}\n  {r['body']}" for r in results])

class FileEditTool(Tool):
    """Outil d'édition de fichiers"""
    def __init__(self):
        super().__init__(
            name="file_edit",
            description="Lit ou modifie des fichiers",
            parameters={
                "action": {"type": "string", "enum": ["read", "write"], "description": "L'action à effectuer"},
                "path": {"type": "string", "description": "Le chemin du fichier"},
                "content": {"type": "string", "description": "Le contenu à écrire (si action=write)"}
            }
        )
    
    def execute(self, action: str, path: str, content: str = None) -> str:
        if action == "read":
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        elif action == "write":
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"Fichier {path} modifié avec succès"

class SystemCommandTool(Tool):
    """Outil d'exécution de commandes système"""
    def __init__(self):
        super().__init__(
            name="system_command",
            description="Exécute une commande système",
            parameters={
                "command": {"type": "string", "description": "La commande à exécuter"}
            }
        )
    
    def execute(self, command: str) -> str:
        import subprocess
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Erreur lors de l'exécution de la commande : {str(e)}"

def main():
    # Initialisation de la base de données vectorielle
    chroma_client = Client()
    collection = chroma_client.create_collection("ai_thoughts")
    
    # Initialisation du modèle LLM via Ollama
    llm = Ollama(model="mistral")
    
    # Création des outils
    tools = [
        WebSearchTool(),
        FileEditTool(),
        SystemCommandTool()
    ]
    
    # Création de l'agent principal
    agent = Agent(
        name="Assistant IA",
        description="Un agent IA capable de rechercher, éditer des fichiers et exécuter des commandes",
        tools=tools,
        llm=llm
    )
    
    print("Agent IA initialisé avec succès !")
    print("Utilisez Ctrl+C pour quitter")
    
    # Boucle d'interaction
    while True:
        try:
            user_input = input("\nVous : ")
            response = agent.run(user_input)
            print(f"\nAssistant : {response}")
        except KeyboardInterrupt:
            print("\nAu revoir !")
            break

if __name__ == "__main__":
    main() 