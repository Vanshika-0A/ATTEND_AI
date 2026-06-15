import streamlit as st
from src.screens.home_screens import home_screen
from src.screens.student_screens import student_screen  
from src.screens.teacher_screens import teacher_screen


def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'student':
            student_screen()
        case 'teacher':
            teacher_screen()
        case None:
            home_screen()  
main()          


