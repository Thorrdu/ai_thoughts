import os
import subprocess
import sys
from pathlib import Path

def check_cuda():
    """Vérifie si CUDA est disponible"""
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False

def setup_environment():
    """Configure l'environnement virtuel et installe les dépendances"""
    venv_path = Path("venv")
    if not venv_path.exists():
        print("Création de l'environnement virtuel...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
    
    # Activation de l'environnement virtuel
    if sys.platform == "win32":
        activate_script = venv_path / "Scripts" / "activate.bat"
    else:
        activate_script = venv_path / "bin" / "activate"
    
    # Installation des dépendances
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    subprocess.run([sys.executable, "setup.py", "develop"])

def main():
    print("Configuration de l'environnement...")
    setup_environment()
    
    cuda_available = check_cuda()
    print(f"CUDA disponible : {'Oui' if cuda_available else 'Non'}")
    
    print("\nInstallation d'Ollama...")
    # Note: L'installation d'Ollama doit être faite manuellement
    # https://ollama.ai/download
    
    print("\nConfiguration terminée !")
    print("Pour démarrer les services :")
    print("1. Assurez-vous qu'Ollama est installé et en cours d'exécution")
    print("2. Activez l'environnement virtuel :")
    if sys.platform == "win32":
        print("   .\\venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("3. Lancez le script principal : python main.py")

if __name__ == "__main__":
    main() 