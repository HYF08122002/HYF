import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Caroline_Hou_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Caroline Hou")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** caroline.hou1208@link.cuhk.edu.com
    - **Phone:** (852) 5957-3138
    - **LinkedIn:** [: linkedin.com/in/caroline.hou](https://linkedin.com/in/carolinehou)
    - **GitHub:** [ github.com/caroline.hou](https://github.com/carolinehou)
    - **Address:** Changchun, Jilin Province, China
    """)

    st.header("Professional Summary")
    st.markdown("""
    - 1、Excellent English reading, listening and writing skills, IELTS 7.5, GRE 322, and certificates such as Specialization 8, Specialization 4 and CET-4. Proficient in Microsoft Office (Excel, Word, PowerPoint, Visio) and other office software, master the basic data analysis ability (SPSS SQL Python), graphic processing and layout and editing ability;
    - 2、rich reserves of professional knowledge, has a relatively rich experience in the field of financial and financial internships, business processes, work mode has a strong understanding of the front thinking, communication, organization and coordination skills; learning ability, adaptability, stress resistance can quickly learn the required skills and quickly get started, adapt to the new position.
    """)

    st.header("Work Experience")
    st.markdown("""
    **Good Future-Media Intern**
    - *2024.04-2024.06*
    - Media Program: Participate in the development of media communication strategies for projects such as Xuexue Hubei live broadcast, Xiaosi Learning Machine product release, Shanghai Artificial Intelligence Conference, etc., and plan the ABC English Corner APP product closed-door meeting, including the highlights, content, and tempo.
    - Relationship Maintenance: Responsible for establishing relationships with the media to coordinate media resources, combing traditional media resources in North China, Guangzhou and Shenzhen as well as media resources of investment platforms.
    - Daily work: collect and analyze public opinion related to the “double-decrease” policy, review and summarize the monthly monitoring of media communication, and participate in social media photo and video shooting and production.

    **Deloitte-Consulting Intern**
    - *2024.01-2024.03*
    - Professional Documentation: Assist financial project team members in writing various bidding documents, analyzing the latest tax policies and translating financial emails.
    - Tax Audit: Responsible for tax audit of financial industry clients, mainly involved in banking, insurance, investment banking clients, public welfare donation deduction, fixed assets and intangible assets draft production.
    
    **Allianz Group-Marketing Intern**
    - *2023.06-2023.08*
     - Industry Research: Conduct industry research on travel insurance (coverage and price) of insurance companies and insurance brokers in the to-c side of the market, participate in the design of branded to-c side travel insurance product categories, combinations, and web pages, analyze the weekly and monthly click-throughs with the information department and make product adjustments.
    - Public Opinion Handling: Assist in monitoring public opinion on media news and social software through keywords, track and record negative comments, and eliminate 30+ negative information.
    
    **4.WPP Group PR Intern**
    - *2022.11-2023.02*
    - Media Operation: Participate in the operation of New Balance and Asics new media platforms, assist in the output of publicity content for Little Red Book, Public, Weibo, and other accounts 30+; responsible for seasonal tweets and press releases editing and writing, picture poster design and production, promotional video editing and production, and end-of-season reports.
    - Artist docking: Periodically directly for the client to select, docking artists and social media bloggers in line with the brand tone, complete seeding publicity and promotion work, and monitoring team to summarize and analyze the traffic data, the cumulative total for the working group to complete 5 rounds of +seeding tasks, docking 100 + artist team and bloggers.
    """)

    st.header("Education")
    st.markdown("""
    **Master of Marketing**
    - Chinese University of Hong Kong
    - *Graduated: July 2025*
    - GPA: 3.6/4.0

    **Bachelor of Business English**
    - University of International Business and Economics
    - *Graduated: June 2024*
    - GPA: 3.5/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, R
    - **Web Technologies:** HTML
    - **Databases:** MySQL
    - **Soft Skills:** Project Management, Problem-Solving, Communication
    """)

    st.header("Languages")
    st.markdown("""
    - **Chinese:** Native
    - **English:** Intermediate
    """)

    st.header("Interests")
    st.markdown("""
    - Blogging about TV drama trends
    - Skiing
    """)

    st.markdown("---") 