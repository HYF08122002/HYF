import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Caroline Hou</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        Changchun, Jilin Province, China<br>
        <a href="mailto:caroline.hou1208@link.cuhk.edu.com">caroline.hou1208@link.cuhk.edu.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        - 1、Excellent English reading, listening and writing skills, IELTS 7.5, GRE 322, and certificates such as Specialization 8, Specialization 4 and CET-4. Proficient in Microsoft Office (Excel, Word, PowerPoint, Visio) and other office software, master the basic data analysis ability (SPSS SQL Python), graphic processing and layout and editing ability;
        - 2、Rich reserves of professional knowledge, has a relatively rich experience in the field of financial and financial internships, business processes, work mode has a strong understanding of the front thinking, communication, organization and coordination skills; learning ability, adaptability, stress resistance can quickly learn the required skills and quickly get started, adapt to the new position. 
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Databases: MySQL
        - Web Technologies: HTML
        - Databases: MySQL
        - Soft Skills: Project Management, Problem-Solving, Communication
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 
