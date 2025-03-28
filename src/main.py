import asyncio
from agents.web_search_agent import WebSearchAgent
from agents.file_agent import FileAgent
from agents.system_agent import SystemAgent
from agents.vector_store_agent import VectorStoreAgent

async def test_web_search():
    print("\n🔍 Test de l'agent de recherche web...")
    search_agent = WebSearchAgent()
    result = await search_agent.search("Qu'est-ce que l'intelligence artificielle?")
    
    if result["status"] == "success":
        print("✅ Résultats de la recherche:")
        for idx, result in enumerate(result["results"], 1):
            print(f"\n{idx}. {result}")
    else:
        print(f"❌ Erreur: {result['message']}")

async def test_file_operations():
    print("\n📂 Test de l'agent de fichiers...")
    file_agent = FileAgent()
    
    # Test d'écriture
    write_result = await file_agent.write_file("test.txt", "Contenu de test")
    print(f"Écriture: {write_result['message']}")
    
    # Test de lecture
    read_result = await file_agent.read_file("test.txt")
    if read_result["status"] == "success":
        print(f"Lecture: {read_result['content']}")
    else:
        print(f"❌ Erreur de lecture: {read_result['message']}")

async def test_system_commands():
    print("\n💻 Test de l'agent système...")
    system_agent = SystemAgent()
    
    # Test d'information système
    info_result = await system_agent.get_system_info()
    if info_result["status"] == "success":
        print("✅ Informations système:")
        for key, value in info_result["info"].items():
            print(f"{key}: {value}")
    
    # Test de commande simple
    cmd_result = await system_agent.execute_command("dir")
    if cmd_result["status"] == "success":
        print("\n✅ Résultat de la commande 'dir':")
        print(cmd_result["stdout"])
    else:
        print(f"❌ Erreur: {cmd_result['message']}")

async def test_vector_store():
    print("\n🗂 Test de l'agent de base de données vectorielle...")
    vector_agent = VectorStoreAgent()
    
    # Test de création de collection
    create_result = await vector_agent.create_collection("test_collection")
    print(f"Création de collection: {create_result['message']}")
    
    # Test d'ajout de documents
    add_result = await vector_agent.add_documents(
        "test_collection",
        ["Document de test 1", "Document de test 2"]
    )
    print(f"Ajout de documents: {add_result['message']}")
    
    # Test de recherche
    search_result = await vector_agent.search("test_collection", "test")
    if search_result["status"] == "success":
        print("✅ Résultats de la recherche vectorielle:")
        print(search_result["results"])
    else:
        print(f"❌ Erreur: {search_result['message']}")

async def main():
    print("🚀 Démarrage des tests des agents...")
    
    await test_web_search()
    await test_file_operations()
    await test_system_commands()
    await test_vector_store()
    
    print("\n✨ Tests terminés!")

if __name__ == "__main__":
    asyncio.run(main()) 