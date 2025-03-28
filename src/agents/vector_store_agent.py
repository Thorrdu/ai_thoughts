from typing import Dict, Any, List
import chromadb
from chromadb.config import Settings
from .base_agent import BaseAgent

class VectorStoreAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="VectorStoreAgent",
            description="Agent spécialisé dans la gestion de la base de données vectorielle",
            capabilities=["stockage_vecteur", "recherche_vecteur"]
        )
        self.client = chromadb.Client(Settings(
            persist_directory="./data/vector_store",
            anonymized_telemetry=False
        ))
    
    async def create_collection(self, name: str, metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Crée une nouvelle collection de vecteurs.
        """
        try:
            collection = self.client.create_collection(
                name=name,
                metadata=metadata
            )
            return {
                "status": "success",
                "message": f"Collection {name} créée avec succès",
                "collection_name": name
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de la création de la collection: {str(e)}"
            }
    
    async def add_documents(self, collection_name: str, documents: List[str], 
                          metadatas: List[Dict[str, Any]] = None, 
                          ids: List[str] = None) -> Dict[str, Any]:
        """
        Ajoute des documents à une collection.
        """
        try:
            collection = self.client.get_collection(collection_name)
            
            # Génération d'IDs si non fournis
            if ids is None:
                ids = [f"doc_{i}" for i in range(len(documents))]
            
            collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            
            return {
                "status": "success",
                "message": f"{len(documents)} documents ajoutés à la collection {collection_name}",
                "collection_name": collection_name,
                "document_count": len(documents)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de l'ajout des documents: {str(e)}"
            }
    
    async def search(self, collection_name: str, query: str, 
                    n_results: int = 5) -> Dict[str, Any]:
        """
        Recherche des documents similaires dans une collection.
        """
        try:
            collection = self.client.get_collection(collection_name)
            results = collection.query(
                query_texts=[query],
                n_results=n_results
            )
            
            return {
                "status": "success",
                "query": query,
                "results": results
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de la recherche: {str(e)}"
            }
    
    async def execute(self, task: str) -> Dict[str, Any]:
        """
        Exécute une tâche de gestion de base de données vectorielle.
        """
        # Analyse simple de la tâche pour déterminer l'action
        if "créer" in task.lower():
            return await self.create_collection("default_collection")
        elif "ajouter" in task.lower():
            return await self.add_documents("default_collection", ["Document test"])
        elif "rechercher" in task.lower():
            return await self.search("default_collection", "test")
        else:
            return {
                "status": "error",
                "message": "Tâche non reconnue"
            } 