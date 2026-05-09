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

    "Proton baryon quark composition up up down symbol p charge positive"

    "Neutron baryon quark composition up down down symbol n charge neutral"

    "Lambda0 is a neutral baryon with up down strange quarks",

    "SigmaPlus is a positive baryon with up up strange quarks",

    "XiMinus is a negative baryon with down strange strange quarks",

    "PionPlus is a positive meson with up anti down quark",

    "PionZero is a neutral meson",

    "KaonPlus is a positive meson with up anti strange quark",

    "KaonZero is a neutral meson with down anti strange quark",

    "Jpsi is a meson with charm anti charm quarks"
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