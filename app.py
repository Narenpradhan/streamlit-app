#importing all the required libraries---->
import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# hiding the hamburger and footer of streamlit---->
st.markdown("""
<style>
.e1fb0mya1.css-fblp2m.ex0cdmw0
{
    visibility: hidden;
}
.css-cio0dv.egzxvld1
{
    visibility: hidden;
}
<\style>
""",unsafe_allow_html=True)

# Option Menu with icons---->
select=option_menu(
    menu_title =None,
    options=["Home","Image","Video"],
    icons=["house","file-image","file-play"],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)

#function for loading the lottie animation
def load(url):
    getreq=requests.get(url)
    if getreq.status_code != 200:
        return None
    return getreq.json()

# home menu specifications---->
if select=="Home":
    st.title('Hello Wandering Souls! 🎃')
    reaper_lottie=load("https://assets9.lottiefiles.com/packages/lf20_yob5r4uu.json")
    st_lottie(reaper_lottie,height=600)


# image tab specifications---->
elif select=="Image":
    # building the image menu---->
    st.markdown("---")
    imgopt=option_menu(menu_title=None,
    options=["Upload Image","Capture Image"],
    icons=["file-earmark-arrow-up","camera"],
    default_index=0
    )

    # uploading image properties---->
    if imgopt=="Upload Image":
        st.markdown("---")
        st.title('Upload Image!')
        st.write("#### You can upload your image here 👇")
        upimg=st.file_uploader('',type=["png","jpg","jpeg"])
        if upimg is not None:
            st.image(upimg,caption='Here is the uploaded image')
    
    # capturing image properties---->
    elif imgopt=="Capture Image":
        st.markdown("---")
        st.title('Capture Image!')
        img_caption=st.text_input('Enter the text to show')
        st.write("#### Say Cheese 🧀")
        capimg=st.camera_input("")
        if capimg is not None:
            st.markdown("---")
            st.write("#### Your captured image ✨")
            st.image(capimg,caption=img_caption)

# video tab specifications---->
elif select=="Video":
    st.markdown("---")
    st.title('Upload Video')
    st.write("#### You can upload your video here 👇")
    upvid=st.file_uploader('',type=["mp4","mkv"])
    if upvid is not None:
        st.video(upvid)
