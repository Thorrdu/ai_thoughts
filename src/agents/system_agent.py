from typing import Dict, Any
import subprocess
import platform
from .base_agent import BaseAgent

class SystemAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="SystemAgent",
            description="Agent spécialisé dans l'exécution de commandes système",
            capabilities=["execution_commande", "information_systeme"]
        )
    
    async def execute_command(self, command: str) -> Dict[str, Any]:
        """
        Exécute une commande système.
        """
        try:
            # Sécurité : liste des commandes autorisées
            allowed_commands = ["dir", "ls", "echo", "type", "cat", "pwd"]
            command_parts = command.split()
            base_command = command_parts[0].lower()
            
            if base_command not in allowed_commands:
                return {
                    "status": "error",
                    "message": f"Commande {base_command} non autorisée"
                }
            
            # Exécution de la commande
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate()
            
            return {
                "status": "success",
                "command": command,
                "stdout": stdout,
                "stderr": stderr,
                "return_code": process.returncode
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de l'exécution: {str(e)}"
            }
    
    async def get_system_info(self) -> Dict[str, Any]:
        """
        Récupère les informations système.
        """
        try:
            info = {
                "system": platform.system(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor()
            }
            
            return {
                "status": "success",
                "info": info
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de la récupération des informations: {str(e)}"
            }
    
    async def execute(self, task: str) -> Dict[str, Any]:
        """
        Exécute une tâche système.
        """
        if "info" in task.lower():
            return await self.get_system_info()
        else:
            return await self.execute_command(task) 