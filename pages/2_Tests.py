import streamlit as st
import matplotlib.pyplot as plt 
import pandas as pd
page_bg_img = '''
<style>
body {
background: url("https://uswalldecor.com/cdn/shop/files/RMK12279M.jpg");
background-size: cover;
}
</style>
'''

# st.markdown(page_bg_img, unsafe_allow_html=True)
st.html(page_bg_img)

st.header("Pruebas")

if 'model' not in st.session_state:
    st.warning("El modelo no está cargado")
else:
    model = st.session_state.model
    # token = st.text_input("Ingrese un nombre de personaje", placeholder="Harry Patter")    
    token = st.selectbox("Seleccione una palabra del diccionario", model.wv.index_to_key)
    if token:
        token = token.lower()
        close_word = model.wv.most_similar(token, topn=5)        
        df_results = pd.DataFrame(close_word, columns=['Word', 'Percentage'])        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"Vector de '{token}'")
            st.write(model.wv[token])
        with col2:
            df_results['Percentage'] = df_results['Percentage'] * 100
            st.write(df_results)
        with col3:
            fig = plt.figure(figsize=(6,6))
            plt.plot(df_results['Word'],df_results['Percentage'])
            plt.xlabel("Relaciones")
            plt.ylabel("Similitud %")
            st.pyplot(fig)