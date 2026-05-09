import matplotlib.pyplot as plt




def draw_particle(particle_name, quarks):

    fig, ax = plt.subplots(figsize=(6, 6))

    # Main particle circle
    particle_circle = plt.Circle((0.5, 0.5), 0.35, color='skyblue')

    ax.add_patch(particle_circle)



    # Quark positions
# Dynamic positions based on number of quarks
    if len(quarks) == 3: # Baryon
        positions = [(0.35, 0.60), (0.65, 0.60), (0.50, 0.35)]
    else: # Meson
        positions = [(0.40, 0.50), (0.60, 0.50)]

    colors = ['red', 'green', 'yellow']


    # Draw quarks
    for i, quark in enumerate(quarks):

        qx, qy = positions[i]

        quark_circle = plt.Circle((qx, qy), 0.08, color=colors[i])

        ax.add_patch(quark_circle)

        ax.text(qx, qy, quark,
                fontsize=16,
                ha='center',
                va='center',
                color='black')

    # Title
    plt.title(f"{particle_name} Structure")

    # Remove axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.set_aspect('equal')

    plt.axis('off')

    plt.show()

def plot_particle_masses():

    import pandas as pd

    data = pd.read_csv("particles.csv")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(data['name'], data['mass_MeV'], color='skyblue')

    ax.set_ylabel('Mass (MeV/c²)')

    ax.set_title('Particle Mass Comparison')

    plt.xticks(rotation=45)

    return fig