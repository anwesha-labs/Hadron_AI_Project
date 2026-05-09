import streamlit as st
from chatbot import semantic_search
from intents import detect_intent
from visualizer import draw_particle


st.title("Hadron AI System")
st.markdown("### Quark Model of Hadrons")

query = st.text_input(
    "Ask about hadrons",
    placeholder="Example: mass of proton"
)

if query:

    result = semantic_search(query)

    intent = detect_intent(query)

    if intent == "mass":

        st.success(f"Mass of {result['name']} = {result['mass_MeV']} MeV")

    elif intent == "decay":

        st.warning(f"Decay mode of {result['name']} = {result['decay_mode']}")

    elif intent == "spin":

        st.info(f"Spin of {result['name']} = {result['spin']}")

    elif intent == "charge":

        st.info(f"Charge of {result['name']} = {result['charge']}")

    elif intent == "interaction":

        st.info(f"Interaction of {result['name']} = {result['interaction']}")
    elif intent == "draw":

        particle_name = result["name"]

        quarks = result["quark_content"].split()

        st.success(f"Drawing {particle_name}")

        fig = draw_particle(particle_name, quarks)

        st.pyplot(fig)

    else:

        st.write(result)

        particle_name = result["name"]

        quarks = result["quark_content"].split()

        fig = draw_particle(particle_name, quarks)

        st.pyplot(fig)