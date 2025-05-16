import streamlit as st

def display_footer():
    """Display a consistent footer across all pages"""
    footer = """
    <div class="footer">
        <p>© 2025 Caroline Hou | <a href="mailto:caroline.hou1208@link.cuhk.edu.com" style="color: #2C3E50; text-decoration: none;">Contact</a> | Last updated: May 2025</p>
    </div>
    
    <style>
    .footer {
        margin-top: 30px;
        padding-top: 10px;
        border-top: 1px solid #dee2e6;
        text-align: center;
        font-size: 0.8rem !important;  /* 添加!important提高优先级 */
        color: #6c757d;
    }
    .footer p {
        font-size: inherit !important;  /* 确保p标签继承父级字体大小 */
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """
    st.markdown(footer, unsafe_allow_html=True)