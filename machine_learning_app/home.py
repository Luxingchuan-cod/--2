import os
import streamlit as st
from PIL import Image


def load_lottieurl(url):
    try:
        import requests
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except ImportError:
        st.error("Error loading requests module.")
        return None


# Use local CSS
def local_css(file_name):
    try:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, file_name)
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"File not found: {file_name}")
    except Exception as e:
        st.error(f"Error loading CSS file: {e}")


def app():
    # Load CSS
    local_css("style.css")

    # Load assets
    lottie_coding = None
    img_sphere = None
    img_phase_separation = None
    img_nano = None

    try:
        from streamlit_lottie import st_lottie
        lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_zzytykf2.json")
    except Exception as e:
        st.error(f"Error loading animation: {e}")

    # 使用绝对路径加载图片
    current_dir = os.path.dirname(__file__)
    images_dir = os.path.join(current_dir, 'images')

    try:
        img_sphere_path = os.path.join(images_dir, "sphere.jpg")
        img_sphere = Image.open(img_sphere_path)
    except Exception as e:
        st.error(f"Error loading image: {img_sphere_path}")

    try:
        img_phase_separation_path = os.path.join(images_dir, "phase_separation.jpg")
        img_phase_separation = Image.open(img_phase_separation_path)
    except Exception as e:
        st.error(f"Error loading image: {img_phase_separation_path}")

    try:
        img_nano_path = os.path.join(images_dir, "nano.jpg")
        img_nano = Image.open(img_nano_path)
    except Exception as e:
        st.error(f"Error loading image: {img_nano_path}")

    # Header Section
    with st.container():
        st.subheader("Hi, I am PolyAI :wave:")
        st.title("A Researcher from CAS")
        st.write("I'm passionate on fusing polymer physics and artificial intelligence technology.")
        st.write("[Learn More >](https://space.bilibili.com/76811961)")

    # What I Do Section
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("""
                On my Bilibili channel I am creating tutorials for people who:
                - are looking for a way to leverage the power of Blender in their scientific research.
                - are struggling with data visualization.
                - want to learn Data Analysis & Data Science about polymer science and chemistry.

                如果有用，请点个关注，O(∩_∩)O.
            """)
            st.write("[Bilibili Channel >](https://space.bilibili.com/76811961)")
        with right_column:
            if lottie_coding:
                st_lottie(lottie_coding, height=300, key="coding")

    # Blender Tutorials Section
    with st.container():
        st.write("---")
        st.header("Blender tutorials")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            if img_sphere:
                st.image(img_sphere)
        with text_column:
            st.subheader("The explosion ball")
            st.write("Learn how to model a explosion ball! In this tutorial, I'll show you exactly how to do it")
            st.markdown("[Watch Video...](https://www.bilibili.com/video/BV1DK411H795)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            if img_phase_separation:
                st.image(img_phase_separation)
        with text_column:
            st.subheader("Phase Separation")
            st.write(
                "Learn how to create a phase separation texture! In this tutorial, I'll show you exactly how to do it.")
            st.markdown("[Watch Video...](https://www.bilibili.com/video/BV1TT4y1J72n)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            if img_nano:
                st.image(img_nano)
        with text_column:
            st.subheader("Nano Sphere")
            st.write(
                "Discover how to make a visually appealing Nano Sphere! In this tutorial, I'll show you exactly how to do it.")
            st.markdown("[Watch Video...](https://www.bilibili.com/video/BV1yt4y1277N)")

    # Contact Section
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()