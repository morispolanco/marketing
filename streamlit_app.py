import streamlit as st
import openai

# Título de la aplicación
st.title("Generador de Mensajes de Promoción")

# Entrada de usuario para el producto
producto = st.text_input("Introduce el nombre de tu producto:")

# Entrada de usuario para la API Key de OpenAI
api_key = st.text_input("Introduce tu API Key de OpenAI:")

# Selector de plataforma social
plataforma = st.selectbox("Selecciona la plataforma social:", ["Twitter", "Facebook", "Instagram"])

# Botón para generar el mensaje de promoción
if st.button("Generar Mensaje"):
    # Verificar si se ha proporcionado una API Key
    if not api_key:
        st.warning("Por favor, introduce tu API Key de OpenAI.")
    elif producto:
        # Configurar la API Key de OpenAI
        openai.api_key = api_key

        if plataforma == "Twitter":
            prompt = f"Escribe un mensaje de promoción para promocionar {producto} en Twitter:"
            max_tokens = 280
        elif plataforma == "Facebook":
            prompt = f"Escribe un mensaje de promoción para promocionar {producto} en Facebook:"
            max_tokens = 63206
        elif plataforma == "Instagram":
            prompt = f"Escribe un mensaje de promoción para promocionar {producto} en Instagram:"
            max_tokens = 2200

        respuesta = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens,
            n=1
        )

        mensaje_generado = respuesta.choices[0].text

        st.write("Mensaje de promoción generado:")
        st.write(mensaje_generado)

# Información adicional
st.sidebar.header("Información Adicional")
st.sidebar.markdown("Esta aplicación utiliza GPT-3 de OpenAI para generar mensajes de promoción. Asegúrate de seguir las políticas de uso de OpenAI.")
