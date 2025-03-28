from setuptools import setup, find_packages

setup(
    name="ai_thoughts",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "archon>=0.1.0",
        "langchain>=0.1.0",
        "pydantic>=2.0.0",
        "chromadb>=0.4.0",
        "supabase>=2.0.0",
        "duckduckgo-search>=4.1.1",
        "python-dotenv>=1.0.0",
        "torch>=2.0.0",
        "transformers>=4.36.0",
    ],
    python_requires=">=3.10",
    author="Thorrdu",
    description="Projet IA basé sur Archon, LangChain et Pydantic",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
    ],
) 