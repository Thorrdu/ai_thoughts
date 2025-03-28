from typing import Dict, Any, List
from pathlib import Path
from .base_agent import BaseAgent

class FileAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="FileAgent",
            description="Agent spécialisé dans la manipulation de fichiers",
            capabilities=["lecture_fichier", "ecriture_fichier", "liste_fichiers"]
        )
    
    async def read_file(self, file_path: str) -> Dict[str, Any]:
        """
        Lit le contenu d'un fichier.
        """
        try:
            path = Path(file_path)
            if not path.exists():
                return {
                    "status": "error",
                    "message": f"Le fichier {file_path} n'existe pas"
                }
            
            content = path.read_text(encoding='utf-8')
            return {
                "status": "success",
                "content": content,
                "file_path": str(path)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de la lecture: {str(e)}"
            }
    
    async def write_file(self, file_path: str, content: str) -> Dict[str, Any]:
        """
        Écrit du contenu dans un fichier.
        """
        try:
            path = Path(file_path)
            path.write_text(content, encoding='utf-8')
            return {
                "status": "success",
                "message": f"Fichier {file_path} créé/modifié avec succès",
                "file_path": str(path)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de l'écriture: {str(e)}"
            }
    
    async def list_files(self, directory: str = ".") -> Dict[str, Any]:
        """
        Liste les fichiers dans un répertoire.
        """
        try:
            path = Path(directory)
            if not path.exists():
                return {
                    "status": "error",
                    "message": f"Le répertoire {directory} n'existe pas"
                }
            
            files = [str(f) for f in path.glob("*")]
            return {
                "status": "success",
                "files": files,
                "directory": str(path)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de la lecture du répertoire: {str(e)}"
            }
    
    async def execute(self, task: str) -> Dict[str, Any]:
        """
        Exécute une tâche de manipulation de fichiers.
        """
        # Analyse simple de la tâche pour déterminer l'action
        if "lire" in task.lower():
            return await self.read_file(task.split()[-1])
        elif "écrire" in task.lower():
            return await self.write_file(task.split()[-1], "Contenu par défaut")
        elif "lister" in task.lower():
            return await self.list_files()
        else:
            return {
                "status": "error",
                "message": "Tâche non reconnue"
            } 