# Projet d'Agents IA

Ce projet implémente un système d'agents IA basé sur Archon, LangChain et Pydantic, avec support pour CUDA et cuDNN.

## Prérequis

- Python 3.10 ou supérieur
- CUDA et cuDNN (optionnel, pour l'accélération GPU)
- Ollama (pour les modèles locaux)
- WSL2 (pour Windows)

## Installation

### 1. Installation de l'environnement Python

```bash
# Exécuter le script d'installation
python install.py
```

Ce script va :
- Vérifier la version de Python
- Créer un environnement virtuel
- Installer les dépendances
- Vérifier CUDA
- Créer les répertoires nécessaires
- Générer le fichier de configuration

### 2. Installation d'Ollama

```bash
# Exécuter le script d'installation d'Ollama
python install_ollama.py
```

Ce script va :
- Vérifier si Ollama est déjà installé
- Installer Ollama si nécessaire
- Télécharger le modèle Mistral
- Tester le modèle
- Mettre à jour la configuration

## Structure du Projet

```
.
├── src/                    # Code source
│   ├── agents/            # Implémentation des agents
│   └── main.py           # Script principal
├── data/                  # Données
│   └── vector_store/     # Base de données vectorielle
├── logs/                  # Fichiers de logs
├── venv/                  # Environnement virtuel Python
├── config.json           # Configuration du projet
├── requirements.txt      # Dépendances Python
├── install.py           # Script d'installation
├── install_ollama.py    # Script d'installation d'Ollama
└── start_services.py    # Script de démarrage des services
```

## Utilisation

### 1. Démarrage des Services

```bash
# Activer l'environnement virtuel
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Démarrer les services
python start_services.py
```

### 2. Test des Agents

```bash
# Exécuter les tests
python src/main.py
```

## Fonctionnalités

- 🔎 Recherche web via DuckDuckGo
- 📂 Édition de fichiers
- 💻 Exécution de commandes système
- 🗂 Base de données vectorielle avec ChromaDB

## Configuration

Le fichier `config.json` contient toutes les configurations du projet :
- Paramètres de l'environnement
- Chemins des répertoires
- Configuration des agents
- État d'installation d'Ollama

## Dépannage

### Problèmes Courants

1. **Ollama ne démarre pas sur Windows**
   - Vérifier que WSL2 est installé et activé
   - Suivre les instructions sur https://ollama.ai/download

2. **Erreurs CUDA**
   - Vérifier l'installation des pilotes NVIDIA
   - Vérifier la compatibilité de la version CUDA

3. **Problèmes de dépendances**
   - Supprimer le dossier `venv`
   - Réexécuter `install.py`

## Licence

[À définir] 