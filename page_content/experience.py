import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Media Intern 
    **1.Good Future** | *2024.04-2024.06*
    
    - Media Program: Participate in the development of media communication strategies for projects such as Xuexue Hubei live broadcast, Xiaosi Learning Machine product release, Shanghai Artificial Intelligence Conference, etc., and plan the ABC English Corner APP product closed-door meeting, including the highlights, content, and tempo
    - Relationship Maintenance: Responsible for establishing relationships with the media to coordinate media resources, combing traditional media resources in North China, Guangzhou and Shenzhen as well as media resources of investment platforms
    - Daily work: collect and analyze public opinion related to the “double-decrease” policy, review and summarize the monthly monitoring of media communication, and participate in social media photo and video shooting and production
    """)
    
    st.markdown("""
    ### Consulting Intern 
    **Deloitte** | *2024.01-2024.03*
    
    - Professional Documentation: Assist financial project team members in writing various bidding documents, analyzing the latest tax policies and translating financial emails
    - Tax Audit: Responsible for tax audit of financial industry clients, mainly involved in banking, insurance, investment banking clients, public welfare donation deduction, fixed assets and intangible assets draft production
    """)
    
    st.markdown("""
    ### Marketing Intern
    **Allianz Group** | *2023.06-2023.08*
    
    - Industry Research: Conduct industry research on travel insurance (coverage and price) of insurance companies and insurance brokers in the to-c side of the market, participate in the design of branded to-c side travel insurance product categories, combinations, and web pages, analyze the weekly and monthly click-throughs with the information department and make product adjustments
    - Public Opinion Handling: Assist in monitoring public opinion on media news and social software through keywords, track and record negative comments, and eliminate 30+ negative information
    """)

    st.markdown("""
    ### PR Intern
    **WPP Grou** | *2022.11-2023.02*
    
    - Media Operation: Participate in the operation of New Balance and Asics new media platforms, assist in the output of publicity content for Little Red Book, Public, Weibo, and other accounts 30+; responsible for seasonal tweets and press releases editing and writing, picture poster design and production, promotional video editing and production, and end-of-season reports
    - Artist docking: Periodically directly for the client to select, docking artists and social media bloggers in line with the brand tone, complete seeding publicity and promotion work, and monitoring team to summarize and analyze the traffic data, the cumulative total for the working group to complete 5 rounds of +seeding tasks, docking 100 + artist team and bloggers
    """)
    
    st.markdown("---")
    
    st.markdown("## Project")
    
    projects = [
        {
            "title": "International Aviation Ocean Mail ",
            "description": "Aim to analyze and visualize the trends and patterns in international aviation and ocean mail transportation over the past few years. ",
            "skills": ["Python", "scikit-learn", "Pandas"],  # Added skills
            "outcome": "Provide valuable insights into the dynamics of international mail and cargo transportation, helping stakeholders make informed decisions and optimize their operations."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Competiton")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Business Competition
        - 2025 L'Oréal Commercial Competition TOP200
        """)
        
    with col2:
        st.markdown("""
        ### English Competition
        - 2022 Third Prize of Reading in the Guo Cai Cup of the Foreign Studies Society
        - 2022 Third Prize of English World National Student Translation
        """)
    
    st.markdown("---")