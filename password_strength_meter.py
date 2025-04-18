import streamlit as st
import re

# Set page configuration
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4527A0;
        text-align: center;
        margin-bottom: 2rem;
    }
    .suggestion-box {
        background-color: #f1f1f1;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    .feedback-item {
        margin: 0.3rem 0;
        color: #555;
    }
    .password-input {
        margin-bottom: 1.5rem;
    }
    .strength-label {
        font-size: 1.2rem;
        font-weight: bold;
        margin-top: 0.5rem;
    }
    .info-box {
        background-color: #e8f4f8;
        border-left: 5px solid #2196F3;
        padding: 1rem;
        border-radius: 5px;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    # Check for uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    # Check for lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    # Calculate strength
    if score == 5:
        strength = "Very Strong"
        color = "green"
        emoji = "🔒"
    elif score == 4:
        strength = "Strong"
        color = "lightgreen"
        emoji = "✅"
    elif score == 3:
        strength = "Medium"
        color = "orange"
        emoji = "⚠️"
    elif score == 2:
        strength = "Weak"
        color = "orangered"
        emoji = "⚠️"
    else:
        strength = "Very Weak"
        color = "red"
        emoji = "❌"
    
    return strength, color, feedback, emoji, score

# Main app content
st.markdown("<h1 class='main-header'>🔒 Password Strength Meter</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    password = st.text_input("Enter your password", type="password", key="password", 
                           help="Type your password to check its strength")

if password:
    strength, color, feedback, emoji, score = check_password_strength(password)
    
    # Display strength
    st.markdown(f"<p class='strength-label'>Strength: <span style='color:{color}'>{emoji} {strength}</span></p>", 
                unsafe_allow_html=True)
    
    # Progress bar representing strength
    st.progress(score/5)
    
    # Display feedback
    if feedback:
        st.markdown("### Suggestions for improvement:")
        st.container()
        for item in feedback:
            st.markdown(f"• {item}")
else:
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.markdown("### Password Requirements:")
    st.markdown("""
    • At least 8 characters long
    • Include uppercase letters (A-Z)
    • Include lowercase letters (a-z)
    • Include numbers (0-9)
    • Include special characters (!@#$%^&*(),.?":{}|<>)
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 0.8rem;'>© 2023 Password Strength Meter</p>", 
            unsafe_allow_html=True)
