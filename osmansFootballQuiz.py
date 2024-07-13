import random
import streamlit as st
import time
random.seed(time.time())



questions = {
    "Who won the ballondo'r 2024 p7 braehead school?": {"choices": ["liam", "hamza", "osman", "lachlan"], "answer": "liam;"},
    "Who can eat the most spice?": {"choices": ["hamza", "osman", "fabian", "tymi"], "answer": "hamza"},
    "Which Tacher did we have in p7 Osmans class?": {"choices": ["Miss Grant", "Mrs Baxter", "Miss Cooper", "Miss Shinnie"], "answer": "Miss Grant"},
    "how many leugue title's do Aberdeen have":{"choices": ["36","4","25"], "answer":"4"},
    "which of the following managers have coached aberdeen":{"choices": ["Alex firguson","Pep Guardiola"," Jurgen Klopp"], "answer":"Alex firguson"},
    "who is the oldest player to play in the euro 2024":{"choices": ["pepe","ronaldo","modric"], "answer":"pepe"},
    "who won the best winger in p7 braehead 2024":{"choices": ["hamza","osman","adriel"], "answer":"osman"},
    "which club won the 2022 world cup":{"choices": ["Argentina/Messi","Portugal","Brazil"], "answer":"Argentina/Messi"},
    "true or false did Spain nock france out of the euro 2024":{"choices": ["true","false"], "answer":"true"},
}
   
      

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