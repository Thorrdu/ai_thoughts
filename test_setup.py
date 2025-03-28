import sys
import torch
import chromadb
from langchain.llms import Ollama
from archon import Agent

def test_environment():
    print("🔍 Vérification de l'environnement...")
    
    # Vérification de Python
    print(f"Python version: {sys.version}")
    
    # Vérification de CUDA
    print(f"CUDA disponible: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"Version CUDA: {torch.version.cuda}")
        print(f"GPU détecté: {torch.cuda.get_device_name(0)}")
    
    # Test de ChromaDB
    try:
        client = chromadb.Client()
        print("✅ ChromaDB initialisé avec succès")
    except Exception as e:
        print(f"❌ Erreur ChromaDB: {e}")
    
    # Test d'Ollama
    try:
        llm = Ollama(model="mistral")
        print("✅ Ollama initialisé avec succès")
    except Exception as e:
        print(f"❌ Erreur Ollama: {e}")
    
    # Test d'Archon
    try:
        agent = Agent()
        print("✅ Archon initialisé avec succès")
    except Exception as e:
        print(f"❌ Erreur Archon: {e}")

if __name__ == "__main__":
    test_environment() 