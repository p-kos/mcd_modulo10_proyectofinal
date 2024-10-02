import streamlit as st



st.set_page_config(page_title='MCD', page_icon=':bar_chart:', layout='wide', initial_sidebar_state='expanded')

st.header("MCD - Módulo 10")
st.subheader("Trabajo final de curso")
st.html("<img src='https://i.ebayimg.com/images/g/qGQAAOSwNFxknVo3/s-l1200.jpg' />")
st.markdown("### Integrantes:")

col1,col2 = st.columns(2)
with col1:
    st.html("<img src='data:image/jpeg;base64,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' width='200' />")
with col2:
    st.markdown('#### Jhazeel Colque')

col1,col2 = st.columns(2)
with col1:
    st.html("<img src='https://miro.medium.com/v2/resize:fit:600/1*apdAZqJYRlQpP4YEch9lag.jpeg' width='200'  />")
with col2:
    st.markdown('#### Nicole Condori')
    

col1,col2 = st.columns(2)
with col1:
    st.html("<img src='https://easydrawingguides.com/wp-content/uploads/2021/11/how-to-draw-ron-weasly-from-harry-potter-featured-image-1200-1.png' width='200'  />")
with col2:
    st.markdown('#### Marco Zárate')
