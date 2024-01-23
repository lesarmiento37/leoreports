import streamlit as st
import pandas as pd

# Cargar los datos
@st.cache
def cargar_datos():
    return pd.read_csv('pokemon.csv')

df = cargar_datos()

# Usuarios y contraseñas
usuarios = {
    "leonardo": "password1",  # Usuario administrador
    "ruby": "password2"       # Usuario con acceso restringido
}

# Función para verificar usuario
def verificar_usuario(usuario, contraseña):
    return usuario in usuarios and usuarios[usuario] == contraseña

# Página de inicio con login
st.title("Pokémon Dashboard")
usuario = st.sidebar.text_input("Usuario")
contraseña = st.sidebar.text_input("Contraseña", type="password")

if verificar_usuario(usuario, contraseña):
    if usuario == "leonardo":
        # Mostrar datos para administrador
        st.write("Bienvenido, Leonardo. Dashboard de Administrador")
        # Visualizaciones para el administrador
        # Ejemplo: Mostrar un gráfico de barras de la cantidad de Pokémon por tipo
        st.bar_chart(df['Type 1'].value_counts())
        st.write("Estos son los datos.")
        st.write(df)  # Muestra todos los datos
    elif usuario == "ruby":
        # Mostrar datos para usuario con acceso restringido
        st.write("Bienvenido, Ruby. Dashboard de Tipo Normal")
        #Visualizaciones para el usuario de tipo normal
        # Ejemplo: Mostrar una tabla con Pokémon de tipo normal
        st.bar_chart(df[df['Type 1'] == 'Normal']['Generation'].value_counts())
        st.write("Estos son los datos.")
        st.write(df[df['Type 1'] == 'Normal'])  # Muestra solo Pokémon de tipo normal
else:
    st.warning("Usuario o contraseña incorrecta.")

