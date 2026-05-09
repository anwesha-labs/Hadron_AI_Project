import pandas as pd

# Load dataset
data = pd.read_csv("particles.csv")


def classify_particle(name):

    # Search particle name (case-insensitive)
    particle = data[data["name"].str.lower() == name.lower()]

    # If not found
    if particle.empty:
        return "Particle not found"

    # Take first matching row
    row = particle.iloc[0]

    # Return formatted particle information
    return f"""
==============================
Particle Information
==============================

Name            : {row['name']}
Symbol          : {row['symbol']}
Type            : {row['type']}
Quark Content   : {row['quark_content']}
Charge          : {row['charge']}
Spin            : {row['spin']}
Mass            : {row['mass_MeV']} MeV/c²
Lifetime        : {row['mean_lifetime_s']} s
Decay Mode      : {row['decay_mode']}
Interaction     : {row['interaction']}

==============================
"""

