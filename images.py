import streamlit as st
import os
from PIL import Image
import time

image_folder = r"CAMINHO_DAS_IMAGENS"

def load_images(folder_path):
    images = []
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('png','webp','jpg','jpeg','bmp','gif')):
            images.append(os.path.join(folder_path, file_name))
    return images

images = load_images(image_folder)

if not images:
    st.error("Nenhuma imagem encontrada na pasta especificada.")
else:
    placeholder = st.empty()

    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    div.block-container {padding: 0; margin: 0;}
    div[data-testid="stImage"] {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: black;
        background-size: cover;
        background-position: center;
    }
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    start_time = time.time()

    while True:
        for image_path in images:
            image = Image.open(image_path)

            with placeholder:
                st.image(image)

            time.sleep(5)

            if time.time() - start_time >= 3600:
                st.experimental_rerun()
