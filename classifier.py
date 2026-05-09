import pandas as pd


data = pd.read_csv("particles.csv")


def classify_particle(name):

    particle = data[data["name"].str.lower() == name.lower()]

    
    if particle.empty:
        return "Particle not found"


    row = particle.iloc[0]

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

