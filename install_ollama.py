import os
import sys
import platform
import subprocess
import json
import time

def check_ollama_installation():
    """Vérifie si Ollama est déjà installé."""
    print("🔍 Vérification de l'installation d'Ollama...")
    try:
        subprocess.run(["ollama", "--version"], check=True, capture_output=True)
        print("✅ Ollama est déjà installé")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Ollama n'est pas installé")
        return False

def install_ollama():
    """Installe Ollama selon le système d'exploitation."""
    print("\n📦 Installation d'Ollama...")
    system = platform.system().lower()
    
    if system == "windows":
        print("⚠️ L'installation d'Ollama sur Windows nécessite WSL2")
        print("Veuillez suivre les instructions sur https://ollama.ai/download")
        return False
    elif system == "linux":
        try:
            # Installation via curl
            subprocess.run([
                "curl", "-fsSL", "https://ollama.ai/install.sh"
            ], check=True)
            print("✅ Ollama installé avec succès")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'installation: {e}")
            return False
    elif system == "darwin":  # macOS
        try:
            # Installation via Homebrew
            subprocess.run(["brew", "install", "ollama"], check=True)
            print("✅ Ollama installé avec succès")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'installation: {e}")
            return False
    else:
        print(f"❌ Système d'exploitation non supporté: {system}")
        return False

def download_model(model_name: str = "mistral"):
    """Télécharge un modèle Ollama."""
    print(f"\n📥 Téléchargement du modèle {model_name}...")
    try:
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(f"✅ Modèle {model_name} téléchargé avec succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du téléchargement du modèle: {e}")
        return False

def test_model(model_name: str = "mistral"):
    """Teste le modèle téléchargé."""
    print(f"\n🔍 Test du modèle {model_name}...")
    try:
        # Création d'un prompt de test
        test_prompt = "Bonjour! Comment vas-tu?"
        
        # Exécution du test
        result = subprocess.run(
            ["ollama", "run", model_name, test_prompt],
            capture_output=True,
            text=True,
            check=True
        )
        
        print("✅ Test réussi!")
        print("\nRéponse du modèle:")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

def update_config():
    """Met à jour le fichier de configuration avec les informations d'Ollama."""
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        
        # Ajout des configurations Ollama
        config["ollama"] = {
            "installed": True,
            "model": "mistral",
            "status": "ready"
        }
        
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        print("\n✅ Configuration mise à jour")
    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour de la configuration: {e}")

def main():
    print("🚀 Démarrage de l'installation d'Ollama...")
    
    if check_ollama_installation():
        print("\n⚠️ Ollama est déjà installé, passage au téléchargement du modèle...")
    else:
        if not install_ollama():
            print("\n❌ Installation d'Ollama échouée")
            return
    
    if download_model():
        if test_model():
            update_config()
            print("\n✨ Installation d'Ollama terminée avec succès!")
        else:
            print("\n❌ Test du modèle échoué")
    else:
        print("\n❌ Téléchargement du modèle échoué")

if __name__ == "__main__":
    main() 