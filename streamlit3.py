import streamlit as st
import pandas as pd
from datetime import date
import  streamlit_authenticator  as  stauth

import yaml
from yaml.loader import SafeLoader

with open('configuration.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

st.write("pour visiter ma page: login: catherine, mdp: choubidou")

authenticator.login()

def accueil():
      st.title("Bienvenue sur ma page de Catherine")

if st.session_state["authentication_status"]:
  accueil()


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')


import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu


# Using "with" notation
with st.sidebar:
    if st.session_state['authentication_status']:
        add_radio = st.radio(
        "vous souhaitez vous déconnecter",
        authenticator.logout()
    )
# Création du menu qui va afficher les choix qui se trouvent dans la variable options
    selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"])
if selection == "Accueil" and st.session_state['authentication_status']:
    st.write("Bienvenue dans mon univers")
elif selection == "Photos" and st.session_state['authentication_status']:
    st.write("Bienvenue sur mon album photo")
    col1, col2, col3,col4 = st.columns(4)

    with col1:
        st.header("Un Dauphin")
        st.image("https://raw.githubusercontent.com/CatherineVL/streamlit3/refs/heads/main/photos/dauphin.jpeg")

    with col2:
        st.header("Un autre dauphin")
        st.image("https://raw.githubusercontent.com/CatherineVL/streamlit3/refs/heads/main/photos/dauphins.jpeg")

    with col3:
        st.header("un chatigre")
        st.image("https://raw.githubusercontent.com/CatherineVL/streamlit3/refs/heads/main/photos/chatigre.JPG")

    with col4:
        st.header("une lionne")
        st.image("https://raw.githubusercontent.com/CatherineVL/streamlit3/refs/heads/main/photos/lionne.JPG")