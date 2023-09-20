import sematch as se 
from sematch.semantic import similarity, sparql


es = se.semantic.similarity.EntitySimilarity()

concept1 = ""
concept2 = ""

similarity_score = es.similarity(concept1, concept2, method='lin')

print("RDF Similarity Score: " + str(similarity_score) )
