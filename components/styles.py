import streamlit as st
import os

def load_css():
    """Load custom CSS from the static/css directory"""
    # Get the path to the CSS file
    css_file = os.path.join("static", "css", "style.css")
    
    # Check if the file exists
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found: {css_file}")
    
    # 添加全局字体样式
    st.markdown("""
    <style>
    /* 全局字体大小 */
    body {
        font-size: 25px !important;
    }
    
    /* 段落字体大小 */
    p {
        font-size: 1rem !important;
    }
    
    /* 页脚字体大小 */
    .footer {
        font-size: 0.8rem !important;
    }
    </style>
    """, unsafe_allow_html=True)
        
def apply_custom_css():
    """Apply custom CSS styles directly"""
    st.markdown("""
    <style>
    @import url('static/css/style.css');
    </style>
    """, unsafe_allow_html=True)