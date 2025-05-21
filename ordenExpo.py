import streamlit as st
from itertools import permutations
import secrets

st.title("🎲 Permutación aleatoria de nombres")

# Lista de nombres
valores = ['Hugo', 'Jonathan', 'Hector', 'Yahir', 'Alejandro']

# Mostrar lista original
st.subheader("👥 Lista original:")
st.write(valores)

# Botón para generar permutación
if st.button("🔀 Generar permutación aleatoria"):
    perm = secrets.choice(list(permutations(valores)))
    
    st.subheader("✨ Permutación generada:")
    
    # Mostrar de forma ordenada y bonita
    for i, nombre in enumerate(perm, start=1):
        st.markdown(f"**{i}.** {nombre}")
else:
    st.info("Presiona el botón para generar una permutación aleatoria.")
