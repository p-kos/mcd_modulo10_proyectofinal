
import streamlit as st
from gensim.models import Word2Vec
import string
import os
from tqdm import tqdm



# leer carpeta donde están los libros
path = 'Harry Potter'
files = os.listdir(path)
st.write("Se cargarán los siguientes libros:")
st.write(files)

if len(files) > 0:
    with st.status("Cargando archivos", expanded=True) as status:
        # unir todos los archivos en un solo texto
        text = ''
        for file in files:
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                text += f.read()

        st.write(f"Cargados {len(text)} caracteres.")
        sentences = text.split('.') 

        # limpiar oraciones
        clean_sentences = []
        for sentence in sentences:
            tokens = sentence.translate(str.maketrans('','',string.punctuation)).split()
            tokens = [word.lower() for word in tokens if word.isalpha()]
            # print(tokens)
            if tokens:
                clean_sentences.append(tokens)
        st.write(f"{len(clean_sentences)} oraciones.")

        for i in range(1000, 1010):
            st.write(clean_sentences[i])    

        status.update(
            label="Entrenando el modelo", expanded=True
        )
        # entrenar al modelo word2vec
        model = Word2Vec(sentences=clean_sentences, min_count=1, window=5, vector_size=500, workers=4)

        st.session_state.model = model
        status.update(
            label="Modelo entrenado y cargado correctamente", state="complete", expanded=True
        )
        
else:
    st.warning("No se cargaron los libros")