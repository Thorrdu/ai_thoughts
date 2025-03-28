import os
import sys
import platform
import subprocess
import json
import time
from pathlib import Path

def check_environment():
    """Vérifie que l'environnement est correctement configuré."""
    print("🔍 Vérification de l'environnement...")
    
    # Vérification du fichier de configuration
    if not Path("config.json").exists():
        print("❌ Fichier de configuration manquant")
        return False
    
    # Vérification de l'environnement virtuel
    venv_path = Path("venv")
    if not venv_path.exists():
        print("❌ Environnement virtuel manquant")
        return False
    
    # Vérification des répertoires nécessaires
    required_dirs = ["data", "data/vector_store", "logs"]
    for directory in required_dirs:
        if not Path(directory).exists():
            print(f"❌ Répertoire {directory} manquant")
            return False
    
    print("✅ Environnement vérifié avec succès")
    return True

def start_ollama():
    """Démarre le service Ollama."""
    print("\n🚀 Démarrage d'Ollama...")
    try:
        # Vérification si Ollama est déjà en cours d'exécution
        if platform.system() == "Windows":
            result = subprocess.run(
                ["tasklist", "/FI", "IMAGENAME eq ollama.exe"],
                capture_output=True,
                text=True
            )
            if "ollama.exe" in result.stdout:
                print("✅ Ollama est déjà en cours d'exécution")
                return True
        else:
            result = subprocess.run(
                ["pgrep", "ollama"],
                capture_output=True
            )
            if result.returncode == 0:
                print("✅ Ollama est déjà en cours d'exécution")
                return True
        
        # Démarrage d'Ollama
        if platform.system() == "Windows":
            subprocess.Popen(["ollama", "serve"], 
                           creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            subprocess.Popen(["ollama", "serve"])
        
        # Attente du démarrage
        time.sleep(2)
        print("✅ Ollama démarré avec succès")
        return True
    except Exception as e:
        print(f"❌ Erreur lors du démarrage d'Ollama: {e}")
        return False

def start_chroma():
    """Démarre le service ChromaDB."""
    print("\n🚀 Démarrage de ChromaDB...")
    try:
        # ChromaDB est un service embarqué, donc il n'y a pas besoin de le démarrer
        # On vérifie juste qu'il peut être importé
        import chromadb
        print("✅ ChromaDB prêt")
        return True
    except ImportError:
        print("❌ ChromaDB non installé")
        return False

def check_services():
    """Vérifie que tous les services sont en cours d'exécution."""
    print("\n🔍 Vérification des services...")
    
    # Vérification d'Ollama
    try:
        subprocess.run(["ollama", "list"], check=True, capture_output=True)
        print("✅ Service Ollama: OK")
    except subprocess.CalledProcessError:
        print("❌ Service Ollama: Erreur")
        return False
    
    # Vérification de ChromaDB
    try:
        import chromadb
        client = chromadb.Client()
        print("✅ Service ChromaDB: OK")
    except Exception as e:
        print(f"❌ Service ChromaDB: Erreur ({e})")
        return False
    
    return True

def main():
    print("🚀 Démarrage des services...")
    
    if not check_environment():
        print("\n❌ L'environnement n'est pas correctement configuré")
        return
    
    if not start_ollama():
        print("\n❌ Impossible de démarrer Ollama")
        return
    
    if not start_chroma():
        print("\n❌ Impossible de démarrer ChromaDB")
        return
    
    if check_services():
        print("\n✨ Tous les services sont en cours d'exécution!")
        print("\nPour arrêter les services, appuyez sur Ctrl+C")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n👋 Arrêt des services...")
            sys.exit(0)
    else:
        print("\n❌ Certains services ne fonctionnent pas correctement")

if __name__ == "__main__":
    main() 