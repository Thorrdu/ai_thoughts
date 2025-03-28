import os
import sys
import subprocess
import platform
import json
from pathlib import Path

def check_python_version():
    """Vérifie la version de Python."""
    print("🔍 Vérification de la version de Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print("❌ Python 3.10 ou supérieur est requis")
        sys.exit(1)
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} détecté")

def create_venv():
    """Crée l'environnement virtuel."""
    print("\n🔧 Création de l'environnement virtuel...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Environnement virtuel créé avec succès")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la création de l'environnement virtuel: {e}")
        sys.exit(1)

def get_venv_python():
    """Retourne le chemin de l'exécutable Python dans le venv."""
    if platform.system() == "Windows":
        return os.path.join("venv", "Scripts", "python.exe")
    return os.path.join("venv", "bin", "python")

def install_dependencies():
    """Installe les dépendances Python."""
    print("\n📦 Installation des dépendances Python...")
    venv_python = get_venv_python()
    try:
        # Mise à jour de pip
        subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        
        # Installation des dépendances
        subprocess.run([venv_python, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dépendances installées avec succès")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'installation des dépendances: {e}")
        sys.exit(1)

def check_cuda():
    """Vérifie la disponibilité de CUDA."""
    print("\n🔍 Vérification de CUDA...")
    try:
        import torch
        cuda_available = torch.cuda.is_available()
        if cuda_available:
            print(f"✅ CUDA disponible (Version: {torch.version.cuda})")
            print(f"✅ GPU détecté: {torch.cuda.get_device_name(0)}")
        else:
            print("⚠️ CUDA non disponible, utilisation du CPU uniquement")
    except ImportError:
        print("⚠️ PyTorch non installé, CUDA non vérifié")

def create_directories():
    """Crée les répertoires nécessaires."""
    print("\n📁 Création des répertoires...")
    directories = [
        "data",
        "data/vector_store",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Répertoire {directory} créé")

def create_config():
    """Crée le fichier de configuration."""
    print("\n⚙️ Création du fichier de configuration...")
    config = {
        "environment": {
            "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            "platform": platform.system(),
            "cuda_available": False  # Sera mis à jour après la vérification de CUDA
        },
        "paths": {
            "data_dir": "data",
            "vector_store_dir": "data/vector_store",
            "logs_dir": "logs"
        },
        "agents": {
            "web_search": {
                "enabled": True,
                "max_results": 5
            },
            "file_operations": {
                "enabled": True,
                "allowed_extensions": [".txt", ".py", ".json", ".md"]
            },
            "system_commands": {
                "enabled": True,
                "allowed_commands": ["dir", "ls", "echo", "type", "cat", "pwd"]
            },
            "vector_store": {
                "enabled": True,
                "default_collection": "default"
            }
        }
    }
    
    try:
        import torch
        config["environment"]["cuda_available"] = torch.cuda.is_available()
    except ImportError:
        pass
    
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    print("✅ Fichier de configuration créé")

def main():
    print("🚀 Démarrage de l'installation...")
    
    check_python_version()
    create_venv()
    install_dependencies()
    check_cuda()
    create_directories()
    create_config()
    
    print("\n✨ Installation terminée avec succès!")
    print("\nPour activer l'environnement virtuel:")
    if platform.system() == "Windows":
        print("    .\\venv\\Scripts\\activate")
    else:
        print("    source venv/bin/activate")

if __name__ == "__main__":
    main() 