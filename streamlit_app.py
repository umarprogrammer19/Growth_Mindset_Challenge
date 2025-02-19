import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Advanced Temperature Converter",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

def local_css(mode):
    if mode == "light":
        return """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        .main .block-container {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 2rem;
            border-radius: 10px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .stButton>button {
            color: #2c3e50;
            background-color: #ecf0f1;
            border: 2px solid #2c3e50;
        }
        .stButton>button:hover {
            background-color: #2c3e50;
            color: #ecf0f1;
        }
        </style>
        """
    else:
        return """
        <style>
        .stApp {
            background: linear-gradient(135deg, #2c3e50 0%, #4ca1af 100%);
        }
        .main .block-container {
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 10px;
        }
        h1, h2, h3, p {
            color: #ecf0f1;
        }
        .stButton>button {
            color: #ecf0f1;
            background-color: #34495e;
            border: 2px solid #ecf0f1;
        }
        .stButton>button:hover {
            background-color: #ecf0f1;
            color: #34495e;
        }
        </style>
        """

# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

# Sidebar
st.sidebar.title("Settings")
mode = st.sidebar.radio("Choose theme:", ("Light", "Dark"))
st.markdown(local_css(mode.lower()), unsafe_allow_html=True)

# Main content
st.title("🌡️ Advanced Temperature Converter")

tab1, tab2, tab3 = st.tabs(["Converter", "Learn", "Quiz"])

with tab1:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        celsius = st.number_input("Celsius", value=0.0, step=0.1)
        st.write(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
        st.write(f"{celsius}°C = {celsius_to_kelvin(celsius):.2f}K")
    
    with col2:
        fahrenheit = st.number_input("Fahrenheit", value=32.0, step=0.1)
        st.write(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
        st.write(f"{fahrenheit}°F = {fahrenheit_to_kelvin(fahrenheit):.2f}K")
    
    with col3:
        kelvin = st.number_input("Kelvin", value=273.15, step=0.1)
        st.write(f"{kelvin}K = {kelvin_to_celsius(kelvin):.2f}°C")
        st.write(f"{kelvin}K = {kelvin_to_fahrenheit(kelvin):.2f}°F")
    
    st.subheader("Temperature Scale Comparison")
    temp_range = range(-50, 101, 10)
    df = pd.DataFrame({
        "Celsius": temp_range,
        "Fahrenheit": [celsius_to_fahrenheit(t) for t in temp_range],
        "Kelvin": [celsius_to_kelvin(t) for t in temp_range]
    })
    
    fig = px.line(df, x="Celsius", y=["Fahrenheit", "Kelvin"], 
                  title="Temperature Scales Comparison",
                  labels={"value": "Temperature", "variable": "Scale"},
                  height=500)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Learn About Temperature Scales")
    
    st.subheader("Celsius (°C)")
    st.write("""
    - Also known as centigrade
    - Defined by the freezing point of water (0°C) and the boiling point of water (100°C)
    - Commonly used in most countries for everyday temperature measurements
    - Created by Swedish astronomer Anders Celsius in 1742
    """)
    
    st.subheader("Fahrenheit (°F)")
    st.write("""
    - Developed by German physicist Daniel Gabriel Fahrenheit in 1724
    - Water freezes at 32°F and boils at 212°F at standard atmospheric pressure
    - Commonly used in the United States for everyday temperature measurements
    """)
    
    st.subheader("Kelvin (K)")
    st.write("""
    - An absolute temperature scale, meaning 0K is the lowest possible temperature (absolute zero)
    - Proposed by William Thomson, 1st Baron Kelvin, in 1848
    - Commonly used in scientific contexts
    - One kelvin has the same magnitude as one degree Celsius
    """)
    
    st.subheader("Interesting Facts")
    st.write("""
    - The temperature at which Celsius and Fahrenheit scales intersect is -40°C/-40°F
    - Absolute zero (0K) is approximately -273.15°C or -459.67°F
    - The Rankine scale is an absolute temperature scale using Fahrenheit degrees
    """)

with tab3:
    st.header("Temperature Conversion Quiz")
    
    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    
    questions = [
        {
            "question": "What is 0°C in Fahrenheit?",
            "options": ["0°F", "32°F", "100°F", "-40°F"],
            "correct": 1
        },
        {
            "question": "What is the boiling point of water in Kelvin?",
            "options": ["273.15K", "373.15K", "212K", "100K"],
            "correct": 1
        },
        {
            "question": "At what temperature do Celsius and Fahrenheit scales intersect?",
            "options": ["0°", "-32°", "-40°", "32°"],
            "correct": 2
        },
        {
            "question": "What is absolute zero in Celsius?",
            "options": ["-273.15°C", "-459.67°C", "0°C", "-100°C"],
            "correct": 0
        },
        {
            "question": "Convert 98.6°F to Celsius:",
            "options": ["32°C", "37°C", "100°C", "50°C"],
            "correct": 1
        }
    ]
    
    if st.session_state.current_question < len(questions):
        question = questions[st.session_state.current_question]
        st.subheader(f"Question {st.session_state.current_question + 1}")
        st.write(question["question"])
        answer = st.radio("Select your answer:", question["options"], key=f"q{st.session_state.current_question}")
        
        if st.button("Submit Answer"):
            if question["options"].index(answer) == question["correct"]:
                st.success("Correct!")
                st.session_state.quiz_score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {question['options'][question['correct']]}")
            st.session_state.current_question += 1
            st.experimental_rerun()
    else:
        st.subheader("Quiz Completed!")
        st.write(f"Your score: {st.session_state.quiz_score}/{len(questions)}")
        if st.button("Restart Quiz"):
            st.session_state.quiz_score = 0
            st.session_state.current_question = 0
            st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("Created with ❄️ using Streamlit")

