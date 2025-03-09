from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

# Neo4j Connection
NEO4J_URI = os.getenv("NEO4J_URI")  # Example: "neo4j+s://your-database-url"
NEO4J_USER = os.getenv("NEO4J_USER")  # Example: "neo4j"
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")  # Example: "password"

class Neo4jConnection:
    def __init__(self):
        self._driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    def close(self):
        self._driver.close()

    def query(self, query, parameters=None):
        with self._driver.session() as session:
            return session.run(query, parameters)

neo4j_conn = Neo4jConnection()
