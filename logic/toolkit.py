import streamlit as st
from logic.download import LinkDownload, SearchDownload, PlaylistDownload

class Modos:
    def __init__(self):
        print("Modos iniciado")
    @st.cache(suppress_st_warning=True)
    def m_link(self, link=None):
        mp3 = LinkDownload()
        if link:
            with open(mp3.download(link), "rb") as f:
                with st.spinner("Baixando..."):   
                    st.success("Download concluído! :rocket:")
                st.download_button(":floppy_disk: Baixar arquivo", data=f.read(), file_name=f"{mp3.get_name()}.mp3")
        
            self.show_video(link)
    @st.cache(suppress_st_warning=True)
    def m_search(self, query=None):
        mp3 = SearchDownload()
        if query:
            with open(mp3.download(query), "rb") as f:
                with st.spinner("Baixando..."):   
                    st.success("Download concluído! :rocket:")
                st.download_button(":floppy_disk: Baixar arquivo", data=f.read(), file_name=f"{mp3.get_name()}.mp3")
        
            self.show_video(mp3.get_link())
            
    @st.cache(suppress_st_warning=True)
    def m_playlist(self, playlist=None):
        mp3 = PlaylistDownload()
        if playlist:
            files = mp3.download(playlist)
            zip = mp3.get_zip()
            with open(zip, "rb") as f:
                with st.spinner("Baixando..."):   
                    st.success("Download concluído! :rocket:")
                    st.download_button(":floppy_disk: Baixar arquivo",data=f.read(), file_name="Playlist.zip", mime="application/zip")
            self.show_video(playlist)
               
    def show_video(self,link):
        st.markdown("---")
        st.header(":violet[Vídeo baixado:]")
        st.video(link)