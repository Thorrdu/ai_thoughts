from typing import List, Dict, Any
from pydantic import BaseModel
from archon import Agent as ArchonAgent

class BaseAgent(BaseModel):
    name: str
    description: str
    capabilities: List[str]
    archon_agent: ArchonAgent
    
    def __init__(self, name: str, description: str, capabilities: List[str]):
        super().__init__(
            name=name,
            description=description,
            capabilities=capabilities,
            archon_agent=ArchonAgent()
        )
    
    async def execute(self, task: str) -> Dict[str, Any]:
        """
        Exécute une tâche donnée en utilisant les capacités de l'agent.
        """
        try:
            result = await self.archon_agent.run(task)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def add_capability(self, capability: str):
        """
        Ajoute une nouvelle capacité à l'agent.
        """
        self.capabilities.append(capability) 