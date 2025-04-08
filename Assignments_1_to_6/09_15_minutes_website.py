import streamlit as st
import random

# Values saved in session state
if "user_guess" not in st.session_state:
    st.session_state.user_guess = 0

if "chances" not in st.session_state:
    st.session_state.chances = 0

if "guess_number" not in st.session_state:
    st.session_state.guess_number = 0

# Page Configuration
st.set_page_config(page_title="Guess The Number", layout="centered")
st.title("Guess The Number 🎮") 

# Set the level of difficulty
start_number = st.number_input("Enter the start number", 1, 100, 1)
end_number = st.number_input("Enter the end number", 1, 100, 100)
set_level = st.selectbox("Select the level", ["Easy", "Medium", "Hard"])

# Check if the guess number is already generated
if "guess_number" not in st.session_state or st.session_state.chances == 0:
    st.session_state.guess_number = random.randint(start_number, end_number)

guess_number = st.session_state.guess_number

# Get the user's guess
guessed_number = st.number_input("Enter your guess number", start_number, end_number)


# Set the chances based on the level of difficulty
if set_level == "Easy":
    st.write("Easy level selected")
    st.write("You have 10 chances to guess the number")
    chance = 10
elif set_level == "Medium":
    st.write("Medium level selected")
    st.write("You have 5 chances to guess the number")
    chance = 5
else:
    st.write("Hard level selected")
    st.write("You have 3 chances to guess the number")
    chance = 3

col1, col2 = st.columns([5,1])
with col1:
    check_button = st.button("Check")
with col2:
    play_again_button = st.button("Play Again")


# Check user guess with the generated number     
if check_button:
    st.session_state.chances += 1
    if guessed_number == guess_number:
        st.write(f"🎊🎉Congratulations! You guessed the right number 😍")
    elif guessed_number > guess_number:
        st.write("Try a Lower number")
        st.write(f"Chances left: {st.session_state.chances}/{chance}")
        if chance == st.session_state.chances:
            st.write(f"😯 Sorry! You lost the game. The number is {guess_number}")
    else:
        st.write("Try a Higher number")
        st.write(f"Chances left: {st.session_state.chances}/{chance}")
        if chance == st.session_state.chances:
            st.write(f"😯 Sorry! You lost the game. The number is {guess_number}")

# Reset the game
if play_again_button:
    st.session_state.chances = 0
    st.session_state.user_guess = 0
    st.session_state.guess_number = random.randint(start_number, end_number)