import streamlit as st
import openai

# Título de la aplicación
st.title("Generador de Mensajes de Promoción")

# Entrada de usuario para la API Key de OpenAI en la columna izquierda
api_key = st.sidebar.text_input("Introduce tu API Key de OpenAI:")

# Entrada de usuario para el producto
producto = st.text_input("Introduce el nombre de tu producto:")

# Entrada de usuario para el mensaje deseado
mensaje_deseado = st.text_area("Escribe el mensaje deseado de promoción:")

# Selector de tono
tono = st.selectbox("Selecciona el tono del mensaje:", ["Formal", "Informativo", "Divertido"])

# Selector de plataforma social
plataforma = st.selectbox("Selecciona la plataforma social:", ["Twitter", "Facebook", "Instagram", "Post para Blog", "Email"])

# Botón para generar el mensaje de promoción
if st.button("Generar Mensaje"):
    # Verificar si se ha proporcionado una API Key
    if not api_key:
        st.warning("Por favor, introduce tu API Key de OpenAI.")
    elif not producto:
        st.warning("Por favor, introduce el nombre de tu producto.")
    elif not mensaje_deseado:
        st.warning("Por favor, escribe el mensaje deseado de promoción.")
    else:
        # Configurar la API Key de OpenAI
        openai.api_key = api_key

        if plataforma == "Twitter":
            max_tokens = 280
        elif plataforma == "Facebook":
            max_tokens = 63206
        elif plataforma == "Instagram":
            max_tokens = 2200
        elif plataforma == "Post para Blog":
            max_tokens = 10000  # Puedes ajustar este límite según tus necesidades para blogs.
        elif plataforma == "Email":
            max_tokens = 5000  # Puedes ajustar este límite según tus necesidades para correos electrónicos.

        # Construir el prompt con el tono y el mensaje deseado
        prompt = f"Escribe un mensaje {tono.lower()} para promocionar {producto} en {plataforma}: {mensaje_deseado}"

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
