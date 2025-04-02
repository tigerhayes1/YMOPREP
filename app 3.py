
import streamlit as st

# App config
st.set_page_config(page_title="Yachtmaster Offshore App", layout="wide")

# Custom CSS for navy theme
st.markdown("""
    <style>
        body {
            background-color: #001f3f;
            color: white;
        }
        .stApp {
            background-color: #001f3f;
        }
        .css-1d391kg {  /* Side bar background */
            background-color: #003366;
        }
        .css-1v3fvcr {
            background-color: #001f3f;
        }
        .css-18e3th9 {
            background-color: #001f3f;
        }
        .stButton>button {
            background-color: #0074D9;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
menu = st.sidebar.radio("Navigation", ["Home", "Tidal Calculator", "Multiple Choice Questions"])

# Home
if menu == "Home":
    st.title("RYA Yachtmaster Offshore Practice App")
    st.markdown("Welcome aboard! Navigate using the menu on the left to access tools and test your knowledge.")

# Tidal Calculator
elif menu == "Tidal Calculator":
    st.title("Tidal Height Calculator (Rule of Twelfths)")
    high = st.number_input("High Water Height (m)", min_value=0.0, format="%.2f")
    low = st.number_input("Low Water Height (m)", min_value=0.0, format="%.2f")
    hours = st.slider("Hours after High Water", 0, 6, 3)
    if high > low:
        range_ = high - low
        twelfths = [1, 2, 3, 3, 2, 1]
        rise = sum(twelfths[:hours]) / 12 * range_
        height = low + rise
        st.success(f"Estimated tidal height: {height:.2f} m")
    else:
        st.warning("Enter valid tidal heights.")

# Multiple Choice Questions
elif menu == "Multiple Choice Questions":
    st.title("Theory Practice: Multiple Choice")

    questions = {
        "What does a red over white light indicate at night?": {
            "options": [
                "Power-driven vessel under 50m",
                "Vessel not under command",
                "Fishing vessel with gear over 150m",
                "Pilot vessel on duty"
            ],
            "answer": "Fishing vessel with gear over 150m"
        },
        "What is the direction of buoyage in IALA Region A?": {
            "options": [
                "From sea to port",
                "From port to sea",
                "Clockwise around UK",
                "From sea to harbour"
            ],
            "answer": "From sea to harbour"
        },
        "What signal indicates a vessel aground in fog?": {
            "options": [
                "Two short blasts every 2 minutes",
                "Three strokes of bell and rapid ringing",
                "One long blast",
                "Three bell strokes + rapid ringing + three strokes"
            ],
            "answer": "Three bell strokes + rapid ringing + three strokes"
        }
    }

    for q, data in questions.items():
        st.subheader(q)
        choice = st.radio("Choose one:", data["options"], key=q)
        if choice == data["answer"]:
            st.success("Correct!")
        else:
            st.error("Incorrect. Try again or review the collision regulations.")
