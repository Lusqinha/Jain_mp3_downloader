import streamlit as st
from logic.toolkit import Modos

md_header = """
# { :violet[MP3] :musical_note: :violet[Downloader] }

Feito por :violet[Lucas Borges] utilizando :violet[Streamlit] e :violet[Pytube], ambas bibliotecas :violet[Python].

---
"""

md_footer = """
## :violet[Créditos] :notebook:

:desktop_computer: Streamlit: https://streamlit.io/

:gear: Pytube: https://python-pytube.readthedocs.io/en/latest/

:watch: feito por Lucas Borges: https://lucasborgess.com

"""

modos = Modos()


st.markdown(md_header)

radio_modos = ["Baixar por pesquisa", "Baixar por link", "Baixar por playlist"]

modo = st.radio("Selecione uma opção:", radio_modos)
query = st.text_input("PREENCHA O CAMPO ABAIXO", key="query")
st.button("Enviar")

if modo == radio_modos[0]:
    try: 
        modos.m_search(query)
    except Exception as e:
        st.error(e) 
elif modo == radio_modos[1]:
    try:
        modos.m_link(query)
    except Exception as e:
        st.error(e) 
elif modo == radio_modos[2]:
    try:
        modos.m_playlist(query)
    except Exception as e:
        st.error(e)
        
st.markdown(md_footer)