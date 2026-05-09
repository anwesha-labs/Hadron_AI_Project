from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load particle data
data = pd.read_csv("particles.csv")

# Create searchable descriptions
descriptions = []

descriptions = [

    "EtaZero is a neutral meson containing up anti-up down anti-down and strange anti-strange quarks",

    "KaonPlus is a positive meson with up anti-strange quark",

    "KaonMinus is a negative meson with strange anti-up quark",

    "PionPlus is a positive meson with up anti-down quark",

    "PionZero is a neutral meson with up anti-up and down anti-down quarks",

    "PionMinus is a negative meson with down anti-up quark",

    "Lambda0 is a neutral baryon with up down strange quarks",

    "OhmMinus is a negative baryon with strange strange strange quarks",

    "Proton is a positive baryon with up up down quarks",

    "Neutron is a neutral baryon with up down down quarks",

    "XiZero is a neutral baryon with up strange strange quarks",

    "XiMinus is a negative baryon with down strange strange quarks",

    "XiPlus is a positive antibaryon with anti-down anti-strange anti-strange quarks",

    "SigmaZero is a neutral baryon with up down strange quarks",

    "SigmaPlus is a positive baryon with up up strange quarks",

    "SigmaMinus is a negative baryon with down down strange quarks",

    "DeltaPlusPlus is a doubly positive baryon with up up up quarks",

    "DeltaPlus is a positive baryon with up up down quarks",

    "DeltaZero is a neutral baryon with up down down quarks",

    "DeltaMinus is a negative baryon with down down down quarks"
]

# Convert descriptions into embeddings
embeddings = model.encode(descriptions)

def semantic_search(user_query):

    # Convert user text into embedding
    query_embedding = model.encode([user_query])

    # Compare with particle embeddings
    similarities = cosine_similarity(query_embedding, embeddings)

    # Find best match
    best_index = similarities.argmax()

    # Return matching particle
    return data.iloc[best_index]