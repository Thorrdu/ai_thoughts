# AI Thoughts

Un projet d'IA basé sur Archon, LangChain et Pydantic, exécuté localement avec support CUDA.

## Prérequis

- Python 3.10 ou supérieur
- Ollama installé localement (https://ollama.ai/download)
- GPU compatible CUDA (optionnel, mais recommandé)

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/Thorrdu/ai_thoughts.git
cd ai_thoughts
```

2. Lancez le script de configuration :
```bash
python start_services.py
```

3. Activez l'environnement virtuel :
```bash
# Windows
.\\venv\\Scripts\\activate

# Linux/MacOS
source venv/bin/activate
```

4. Téléchargez le modèle Mistral via Ollama :
```bash
ollama pull mistral
```

## Utilisation

1. Lancez le programme principal :
```bash
python main.py
```

2. Interagissez avec l'agent IA via la console.

## Fonctionnalités

- 🔎 Recherche web via DuckDuckGo
- 📂 Édition de fichiers
- 💻 Exécution de commandes système
- 🗂 Base de données vectorielle avec ChromaDB

## Structure du Projet

- `main.py` : Programme principal avec la logique des agents IA
- `start_services.py` : Script de configuration et de démarrage
- `requirements.txt` : Dépendances Python
- `setup.py` : Configuration du package Python

## Licence

MIT 