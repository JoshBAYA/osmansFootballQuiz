import random
import streamlit as st
import time
random.seed(time.time())



def main():
    ps = PointSystem()
    questions = [
        ("Would you rather work with numbers or words?", "Numbers", "Words", "Neither"),
        ("Would you rather work in a Lab or an Office?", "Lab", "Office", "Neither"),
        ("Would you rather create an art masterpiece or write a novel?", "Art Masterpiece", "Novel", "Neither"),
        ("Would you rather solve a complex math problem or conduct a scientific experiment?", "Math Problem", "Scientific Experiment", "Neither"),
        ("Would you rather study ancient civilizations or learn about modern politics?", "Ancient Civilizations", "Modern Politics", "Neither"),
        ("Would you rather design a building or create a software program?", "Design Building", "Create Software Program", "Neither"),
        ("Would you rather work with animals or teach children?", "Work with Animals", "Teach Children", "Neither"),
        ("Would you rather have early Mornings or late Nights?", "Early Mornings", "Late Nights", "Neither"),
        ("Would you rather explore space or dive into the ocean's depths?", "Explore Space", "Dive into Ocean", "Neither"),
        ("Would you rather study human behavior or understand how machines work?", "Human Behavior", "Machines", "Neither"),
        ("Would you rather compose a piece of music or act in a play?", "Compose Music", "Act in a Play", "Neither"),
        ("Would you rather manage a sports team or plan a corporate event?", "Manage Sports Team", "Plan Corporate Event", "Neither"),
        ("Would you rather translate foreign languages or study the effects of globalization?", "Translate Languages", "Effects of Globalization", "Neither"),
        ("Would you rather lead a team project or work independently on a research paper?", "Lead Team Project", "Work Independently", "Neither"),
        ("Would you rather develop a new recipe or create a health fitness plan?", "New Recipe", "Health Fitness Plan", "Neither"),
        ("Would you rather study law or explore philosophical ideas?", "Study Law", "Philosophical Ideas", "Neither"),
        ("Would you rather work on environmental conservation or urban development?", "Environmental Conservation", "Urban Development", "Neither"),
        ("Would you rather write code or study cybersecurity?", "Write Code", "Cybersecurity", "Neither"),
        ("Would you rather analyze crime scenes or study social justice issues?", "Analyze Crime Scenes", "Social Justice Issues", "Neither"),
        ("Would you rather focus on physical health or mental health?", "Physical Health", "Mental Health", "Neither"),
        ("Would you rather work in a lab or the field with a community?", "Lab", "Field", "Neither"),
        ("Would you rather be involved in business startups or work on non-profit initiatives?", "Business Startups", "Non-profit Initiatives", "Neither")
    ]
   
      

def initialize_quiz():
    items = list(questions.items())
    random.shuffle(items)
    st.session_state.quiz_questions = items
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.quiz_completed = False
    st.session_state.answer_submitted = False  # Track if the answer has been submitted

if 'quiz_questions' not in st.session_state:
    initialize_quiz()

def display_question():
    question, data = st.session_state.quiz_questions[st.session_state.current_question_index]
    st.write(question)
    choices = ["Select your answer"] + data['choices']
    user_answer = st.radio("Choose one:", choices, index=0, key=f"choice{st.session_state.current_question_index}")
    return user_answer

def handle_answer(user_answer):
    if not st.session_state.answer_submitted and user_answer != "Select your answer":
        st.session_state.answer_submitted = True  # Mark the answer as submitted
        question, data = st.session_state.quiz_questions[st.session_state.current_question_index]
        if user_answer == data['answer']:
            st.session_state.score += 1
            st.success('Correct!')
        else:
            st.error(f'Wrong! The correct answer was {data["answer"]}.')
    elif st.session_state.answer_submitted:
        # Advance to the next question or finish quiz
        if st.session_state.current_question_index < len(st.session_state.quiz_questions) - 1:
            st.session_state.current_question_index += 1
            st.session_state.answer_submitted = False  # Reset for the next question
            st.experimental_rerun()
        else:
            st.session_state.quiz_completed = True
            st.write(f"Quiz completed! Your final score is {st.session_state.score}/{len(st.session_state.quiz_questions)}.")

def reset_quiz():
    if st.button('Restart Quiz'):
        initialize_quiz()
        st.experimental_rerun()

user_answer = display_question()

button_label = "Next Question" if st.session_state.answer_submitted else "Submit Answer"
if st.button(button_label, key='submit'):
    handle_answer(user_answer)

if st.session_state.quiz_completed:
    reset_quiz()
