import streamlit as st
import base64

st.set_page_config(page_title="AI Company Verification", layout="wide")

# ---------- Background Function ----------
def set_bg(is_login=False):
    if is_login:
        # High-res professional dark tech background from Unsplash with a dark blue premium overlay
        bg_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80"
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)), url("{bg_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)
    else:
        # Professional corporate tech background for Welcome / Internal pages
        bg_url = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1920&q=80"
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(10, 15, 30, 0.8), rgba(10, 15, 30, 0.95)), url("{bg_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* Force high contrast for titles regardless of system light/dark theme */
        h1, h2, h3, h4 {{
            color: #f8fafc !important;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.6);
        }}
        </style>
        """, unsafe_allow_html=True)

# Check authentication state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    set_bg(is_login=True)
    # ---------------- LOGIN SCREEN ----------------
    st.markdown("<br><br>", unsafe_allow_html=True)
    row_col1, row_col2, row_col3 = st.columns([1,2,1])
    with row_col2:
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center; color: #1E88E5; font-weight: 900; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);'>🔐 Login to System</h2>", unsafe_allow_html=True)
            
            st.markdown("<br><h4 style='font-weight: 900; color: #1E88E5;'>📧 Email Address</h4>", unsafe_allow_html=True)
            email = st.text_input("Email", label_visibility="collapsed", placeholder="Enter your @gmail.com address")
            
            st.markdown("<br><h4 style='font-weight: 900; color: #1E88E5;'>🔑 Password</h4>", unsafe_allow_html=True)
            pwd_type = "default" if st.checkbox("👁️ Show Password", help="Click to reveal your password") else "password"
            pwd = st.text_input("Password", label_visibility="collapsed", placeholder="Enter your password", type=pwd_type)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚀 Secure Login", use_container_width=True, type="primary"):
                email_clean = email.strip().lower()
                if email_clean.endswith("@gmail.com") and len(pwd.strip()) > 0:
                    st.session_state.logged_in = True
                    st.session_state.current_user = email_clean
                    st.success(f"Login successful! Welcome {email_clean}...")
                    st.rerun()
                elif not email_clean.endswith("@gmail.com"):
                    st.error("❌ Access Denied: You must use a valid Gmail ID (e.g. user@gmail.com).")
                else:
                    st.error("❌ Access Denied: Password cannot be empty.")
    st.stop() # Halt execution if not logged in

set_bg(is_login=False)

# ---------------- WELCOME SCREEN ----------------
st.markdown("<h1 style='text-align:center;'>AI Company Verification System</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #4CAF50;'>Welcome Back Admin 👋</h3>", unsafe_allow_html=True)

st.write("")

col_info, col_chat = st.columns([1, 1])

with col_info:
    with st.container(border=True):
        st.markdown("""
        ### 🔍 About This Project
        This system is designed to provide robust security investigations into business records. It helps you:
        
        ✔ **Verify company authenticity** using advanced algorithms.
        ✔ **Detect fake companies** and suspicious records immediately.
        ✔ **Identify duplicate business names** through fuzzy matching AI.
        ✔ **Check deep legitimacy** metrics (Location, Founders, Originality).

        ⬅️ **Navigation Instructions**:
        Use the sidebar menu to navigate features:
        - **1_Verification:** Authenticate any business by Name or URL.
        - **2_Dashboard:** Explore powerful interactive analytics on local businesses.
        - **3_Categories:** Browse detailed visual data cards for top industries.
        """)

# ---------------- CHATBOT / HELP SECTION ----------------
with col_chat:
    with st.container(border=True):
        st.markdown("### 🤖 Help & Assistant Chatbot")
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hello! I'm your AI Guide. How can I assist you with verification today?"}
            ]

        # Container for chat messages
        chat_container = st.container(height=320)
        with chat_container:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # Chat input handling
        if prompt := st.chat_input("Ask for help..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_container:
                with st.chat_message("user"):
                    st.markdown(prompt)

            # Rule-based simulated LLM responses
            response = "I am the platform Assistant. I can help you understand how to use the **Verification**, **Dashboard**, and **Categories** features!"
            lower_prompt = prompt.lower()
            if "verify" in lower_prompt or "how to" in lower_prompt:
                response = "To verify a company, navigate to the **2_verification** page from the sidebar. You can enter a Company Name or Website URL. The AI will output an **Originality Percentage** and deeply analyze its legitimacy!"
            elif "dashboard" in lower_prompt or "chart" in lower_prompt or "analytics" in lower_prompt:
                response = "The **Dashboard** gives you a dynamic, visual breakdown of industries and real vs. fake businesses. It is incredibly interactive: use the dropdowns to drill into the related companies to view their detailed data cards."
            elif "category" in lower_prompt or "industries" in lower_prompt:
                response = "Check out the **Categories** page to explore an interactive visual grid of top industries like Healthcare, Retail, and Construction."
            elif "originality" in lower_prompt or "percent" in lower_prompt:
                response = "The Originality Percentage is a dynamic metric generated by analyzing the company's rating spread, amount of reviews, exact dataset matches, and web footprints."

            st.session_state.messages.append({"role": "assistant", "content": response})
            with chat_container:
                with st.chat_message("assistant"):
                    st.markdown(response)