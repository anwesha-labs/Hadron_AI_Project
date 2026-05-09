from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from visualizer import draw_particle
from intents import detect_intent

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')
data = pd.read_csv("particles.csv")

# Improved Semantic descriptions to help the AI when you make a typo
particle_descriptions = {

    "Proton": "Proton baryon made of up up down quarks",

    "Neutron": "Neutron baryon made of up down down quarks",

    "Lambda0": "Lambda0 neutral baryon with up down strange quarks",

    "SigmaPlus": "SigmaPlus positive baryon with up up strange quarks",

    "XiMinus": "XiMinus negative baryon with down strange strange quarks",

    "PionPlus": "PionPlus positive meson with up anti-down quarks",

    "PionZero": "PionZero neutral meson",

    "KaonPlus": "KaonPlus positive meson with up anti-strange quarks",

    "KaonZero": "KaonZero neutral meson with down anti-strange quarks",

    "Jpsi": "Jpsi meson made of charm anti-charm quarks"
}

description_list = list(particle_descriptions.values())

particle_names = list(particle_descriptions.keys())

embeddings = model.encode(description_list)

particle_quarks = {
    "Proton": sorted(["up", "up", "down"]),
    "Neutron": sorted(["up", "down", "down"]),
    "Lambda0": sorted(["up", "down", "strange"]),
    "SigmaPlus": sorted(["up", "up", "strange"]),
    "XiMinus": sorted(["down", "strange", "strange"]),
    "PionPlus": sorted(["up", "anti-down"]),
    "KaonPlus": sorted(["up", "anti-strange"]),
    "KaonZero": sorted(["down", "anti-strange"]),
    "Jpsi": sorted(["charm", "anti-charm"])
}

def detect_quarks(text):
    # Standardize input: handles "anti down" vs "anti-down"
    text = text.lower().replace("anti ", "anti-")
    flavors = ["up", "down", "strange", "charm", "anti-down", "anti-up", "anti-strange", "anti-charm"]
    
    found_quarks = []
    words = text.split()
    for word in words:
        if word in flavors:
            found_quarks.append(word)
            
    return sorted(found_quarks)

def semantic_search(user_query):

    text = user_query.lower()

    # -------------------------
    # 1. DIRECT PARTICLE NAME MATCH
    # -------------------------

    for particle in particle_names:

        if particle.lower() in text:

            return data[data["name"] == particle].iloc[0]

    # -------------------------
    # 2. EXACT QUARK MATCHING
    # -------------------------

    user_quarks = detect_quarks(user_query)

    for particle, quarks in particle_quarks.items():

        if user_quarks == quarks:

            return data[data["name"] == particle].iloc[0]

    # -------------------------
    # 3. SEMANTIC AI BACKUP
    # -------------------------

    query_embedding = model.encode([user_query])

    similarities = cosine_similarity(query_embedding, embeddings)

    best_index = similarities.argmax()

    matched_particle = particle_names[best_index]

    return data[data["name"] == matched_particle].iloc[0]

def start_chatbot():
    print("\n--- Hadron AI Online ---")
    while True:
        query = input("Ask: ")
        intent = detect_intent(query)
        if query.lower() == "exit": break
        result = semantic_search(query)
        if intent == "mass":

            print(f"\nMass of {result['name']} = {result['mass_MeV']} MeV")

        elif intent == "decay":

            print(f"\nDecay mode of {result['name']} = {result['decay_mode']}")

        elif intent == "spin":

            print(f"\nSpin of {result['name']} = {result['spin']}")

        elif intent == "charge":

            print(f"\nCharge of {result['name']} = {result['charge']}")

        elif intent == "interaction":

            print(f"\ninteraction of {result['name']} = {result['interaction']}")

        elif intent == "draw":

            particle_name = result["name"]

            quarks = particle_visuals.get(particle_name)

            print(f"\nDrawing {particle_name}...")

            draw_particle(particle_name, quarks)

        else:

            print(result)

particle_visuals = {

    "Proton": ["up", "up", "down"],

    "Neutron": ["up", "down", "down"],

    "Lambda0": ["up", "down", "strange"],

    "SigmaPlus": ["up", "up", "strange"],

    "XiMinus": ["down", "strange", "strange"],

    "PionPlus": ["up", "anti-down"],

    "KaonPlus": ["up", "anti-strange"],

    "KaonZero": ["down", "anti-strange"],

    "Jpsi": ["charm", "anti-charm"]
}

if __name__ == "__main__":
    start_chatbot()

