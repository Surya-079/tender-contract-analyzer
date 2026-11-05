import streamlit as st
import os

from config import APP_NAME

# Backend Modules
from backend.pdf_reader import extract_pdf_text
from backend.docx_reader import extract_docx_text
from backend.ocr_reader import extract_image_text
from backend.text_cleaner import clean_text
from backend.eligibility import extract_eligibility
from backend.deadlines import extract_deadlines
from backend.financial import extract_financial_details
from backend.compliance import generate_checklist
from backend.summary import generate_summary
from backend.risk import analyze_risk
from backend.auth import (
    create_database,
    register_user,
    login_user
)

create_database()
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("Tender Analyzer Login")

    login_tab, register_tab = st.tabs(["Login", "Register"])

    with login_tab:

        username = st.text_input("Username", key="login_username")

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button("Login"):

            if login_user(username, password):

                st.session_state.logged_in = True

                st.success("Login Successful!")

                st.rerun()

            else:

                st.error("Invalid Username or Password")

    with register_tab:

        new_username = st.text_input(
            "Create Username",
            key="register_username"
        )

        new_password = st.text_input(
            "Create Password",
            type="password",
            key="register_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="confirm_password"
        )

        if st.button("Register"):

            if new_username.strip() == "":
                st.error("Username cannot be empty.")

            elif new_password.strip() == "":
                st.error("Password cannot be empty.")

            elif new_password != confirm_password:
                st.error("Passwords do not match.")

            else:

                success, message = register_user(
                    new_username,
                    new_password
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)

    st.stop()

st.sidebar.success("You are logged in.")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()


st.set_page_config(
    page_title=APP_NAME,
    page_icon="📄",
    layout="wide"
)

st.title(APP_NAME)
st.markdown("### AI Powered Tender Analysis System")

uploaded_file = st.file_uploader(
    "Upload Tender Document",
    type=["pdf", "docx"]
)

document_text = ""

if uploaded_file is not None:

    extension = os.path.splitext(uploaded_file.name)[1].lower()

    with open(f"uploads/{uploaded_file.name}", "wb") as file:
        file.write(uploaded_file.getbuffer())

    filepath = f"uploads/{uploaded_file.name}"

    if extension == ".pdf":
        document_text = extract_pdf_text(filepath)

    elif extension == ".docx":
        document_text = extract_docx_text(filepath)

    document_text = clean_text(document_text)

    st.success("Document Processed Successfully")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "Summary",
            "Eligibility",
            "Financial",
            "Deadlines",
            "Compliance",
            "Risk"
        ]
    )

    with tab1:
        st.subheader("Tender Summary")
        st.write(generate_summary(document_text))

    with tab2:
        st.subheader("Eligibility Criteria")
        eligibility = extract_eligibility(document_text)
        for key, value in eligibility.items():
            st.markdown(f"**{key}:** {value}")

    with tab3:
        st.subheader("Financial Details")
        financial = extract_financial_details(document_text)
        for key, value in financial.items():
            st.markdown(f"**{key}:** {value}")

    with tab4:
        st.subheader("Important Dates")
        deadlines = extract_deadlines(document_text)
        for key, value in deadlines.items():
            st.markdown(f"**{key}:** {value}")
            
    with tab5:
        st.subheader("Compliance Checklist")

        checklist = generate_checklist(document_text)

        for item in checklist:
            st.checkbox(item, value=True)

    with tab6:
        st.subheader("Risk Analysis")
        risks = analyze_risk(document_text)

        if len(risks) == 0:
            st.success("No major risks detected.")

        else:
            for risk in risks:
                st.warning(risk)

else:
    st.info("Upload a Tender PDF, DOCX or Scanned Document.")