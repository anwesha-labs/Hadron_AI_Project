from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

from visualizer import draw_particle
from intents import detect_intent

# -----------------------------
# LOAD MODEL + DATA
# -----------------------------

model = SentenceTransformer('all-MiniLM-L6-v2')

data = pd.read_csv("particles.csv")

# -----------------------------
# AUTO DESCRIPTION GENERATION
# -----------------------------

descriptions = data.apply(
    lambda row:
    f"{row['name']} is a {row['type']} "
    f"with {row['quark_content']} quarks "
    f"charge {row['charge']} "
    f"strangeness {row['strangeness']} "
    f"interaction {row['interaction']}",
    axis=1
).tolist()

embeddings = model.encode(descriptions)

# -----------------------------
# PARTICLE NAME LIST
# -----------------------------

particle_names = data["name"].tolist()

# -----------------------------
# AUTO QUARK DICTIONARY
# -----------------------------

particle_quarks = {
    row["name"]: sorted(
        row["quark_content"]
        .replace(",", "")
        .replace("+", "")
        .replace("/", "")
        .split()
    )
    for _, row in data.iterrows()
}

# -----------------------------
# AUTO VISUAL DATA
# -----------------------------

particle_visuals = {
    row["name"]:
    row["quark_content"]
    .replace(",", "")
    .replace("+", "")
    .replace("/", "")
    .split()

    for _, row in data.iterrows()
}

# -----------------------------
# QUARK DETECTOR
# -----------------------------

def detect_quarks(text):

    text = text.lower()

    flavors = [
        "up",
        "down",
        "strange",
        "charm",
        "anti-up",
        "anti-down",
        "anti-strange",
        "anti-charm"
    ]

    found_quarks = []

    for flavor in flavors:

        if flavor in text:

            found_quarks.append(flavor)

    return sorted(found_quarks)

# -----------------------------
# MAIN SEARCH ENGINE
# -----------------------------

def semantic_search(user_query):

    text = user_query.lower()

    # --------------------------------
    # 1. DIRECT PARTICLE NAME MATCH
    # --------------------------------

    for particle in particle_names:

        if particle.lower() in text:

            result = data[data["name"] == particle]

            if not result.empty:

                return result.iloc[0]

    # --------------------------------
    # 2. EXACT QUARK MATCHING
    # --------------------------------

    user_quarks = detect_quarks(user_query)

    for particle, quarks in particle_quarks.items():

        if user_quarks == quarks:

            result = data[data["name"] == particle]

            if not result.empty:

                return result.iloc[0]

    # --------------------------------
    # 3. SEMANTIC AI MATCHING
    # --------------------------------

    query_embedding = model.encode([user_query])

    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )

    best_index = similarities.argmax()

    return data.iloc[best_index]

# -----------------------------
# CHATBOT LOOP
# -----------------------------

def start_chatbot():

    print("\n--- Hadron AI Online ---")

    while True:

        query = input("\nAsk: ")

        if query.lower() == "exit":

            break

        intent = detect_intent(query)

        result = semantic_search(query)

        # -------------------------
        # MASS
        # -------------------------

        if intent == "mass":

            print(
                f"\nMass of {result['name']} = "
                f"{result['mass_MeV']} MeV"
            )

        # -------------------------
        # DECAY
        # -------------------------

        elif intent == "decay":

            print(
                f"\nDecay mode of {result['name']} = "
                f"{result['decay_mode']}"
            )

        # -------------------------
        # CHARGE
        # -------------------------

        elif intent == "charge":

            print(
                f"\nCharge of {result['name']} = "
                f"{result['charge']}"
            )

        # -------------------------
        # INTERACTION
        # -------------------------

        elif intent == "interaction":

            print(
                f"\nInteraction of {result['name']} = "
                f"{result['interaction']}"
            )

        # -------------------------
        # DRAW PARTICLE
        # -------------------------

        elif intent == "draw":

            particle_name = result["name"]

            quarks = particle_visuals.get(
                particle_name,
                []
            )

            print(f"\nDrawing {particle_name}...")

            draw_particle(
                particle_name,
                quarks
            )

        # -------------------------
        # DEFAULT OUTPUT
        # -------------------------

        else:

            print("\nParticle Information:\n")

            print(result)

# -----------------------------
# START PROGRAM
# -----------------------------

if __name__ == "__main__":

    start_chatbot()