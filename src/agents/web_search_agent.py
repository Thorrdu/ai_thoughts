from typing import Dict, Any
from .base_agent import BaseAgent
from langchain.tools import DuckDuckGoSearchTool

class WebSearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="WebSearchAgent",
            description="Agent spécialisé dans la recherche d'informations sur le web",
            capabilities=["recherche_web"]
        )
        self.search_tool = DuckDuckGoSearchTool()
    
    async def search(self, query: str, max_results: int = 5) -> Dict[str, Any]:
        """
        Effectue une recherche web avec le query donné.
        """
        try:
            results = self.search_tool.run(query)
            return {
                "status": "success",
                "query": query,
                "results": results[:max_results]
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de la recherche: {str(e)}"
            }
    
    async def execute(self, task: str) -> Dict[str, Any]:
        """
        Exécute une tâche de recherche web.
        """
        return await self.search(task) 