import streamlit as st
import pandas as pd

# Initialize an empty DataFrame to store student information
if 'students' not in st.session_state:
    st.session_state.students = pd.DataFrame(columns=["Roll No.", "Name", "Age", "Gender", "Course"])

# Title and header of the app with custom styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            color: #604652;
            font-size: 40px;
            font-weight: bold;
        }
        .header {
            color: #604652;
            font-size: 28px;
            font-weight: bold;
        }
        .subheader {
            color: #604652;
            font-size: 22px;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #604652;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #7f6a68;
        }
        .warning {
            color: #FF6347;
            font-size: 18px;
        }
        .success {
            color: #32CD32;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<p class="title">Student Enrollment System</p>', unsafe_allow_html=True)

# Student Enrollment Form
st.markdown('<p class="header">Enroll a New Student</p>', unsafe_allow_html=True)

# Create input fields for name, age, gender, course, and roll number
name = st.text_input("Enter Student Name:")
age = st.number_input("Enter Student Age:", min_value=1)
gender = st.selectbox("Select Gender:", ["Male", "Female", "Other"])
course = st.selectbox("Select Course:", ["DevOps", "Cloud computing", "Mobile app development", "Ethical hacking", "Soft computing", "STQA", "Data Science", "AI", "Machine Learning", "Web Development", "Cyber Security", "Digital Marketing", "Full Stack Development", "UI/UX Design", "Game Development", "Blockchain", "Big Data", "Internet of Things (IoT)", "Robotics", "Augmented Reality (AR)", "Virtual Reality (VR)", "Data Analytics", "Business Intelligence", "Network Security", "Cloud Architecture", "DevSecOps", "Penetration Testing", "Digital Forensics"])

# Generate a roll number (unique for each student)
roll_no = st.number_input("Enter Roll No. (Unique per student):", min_value=1)

# Button to add student
if st.button("Add Student"):
    # Check if roll number already exists
    if roll_no in st.session_state.students["Roll No."].values:
        st.markdown('<p class="warning">Error: Roll No. already exists! Please enter a unique Roll No.</p>', unsafe_allow_html=True)
    elif name and age > 18 and roll_no and course:
        new_student = pd.DataFrame([[roll_no, name, age, gender, course]], columns=["Roll No.", "Name", "Age", "Gender", "Course"])
        st.session_state.students = pd.concat([st.session_state.students, new_student], ignore_index=True)
        st.markdown(f'<p class="success">Student {name} enrolled successfully!</p>', unsafe_allow_html=True)
    elif age <= 18:
        st.markdown('<p class="warning">Age must be greater than 18 to enroll!</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="warning">Please fill in all fields!</p>', unsafe_allow_html=True)

# Display enrolled students in a table
st.markdown('<p class="subheader">Enrolled Students</p>', unsafe_allow_html=True)

if not st.session_state.students.empty:
    st.dataframe(st.session_state.students)
else:
    st.warning("No students enrolled yet.")

# Manage students (Delete or Update)
st.markdown('<p class="subheader">Manage Students</p>', unsafe_allow_html=True)

if not st.session_state.students.empty:
    # Dropdown for selecting student
    student_to_manage = st.selectbox("Select a student to delete or update", st.session_state.students["Name"].tolist())

    # Update student details
    st.markdown("### Update Student Information")
    if student_to_manage:
        new_name = st.text_input("Update Name:", value=student_to_manage)
        new_age = st.number_input("Update Age:", min_value=1, value=int(st.session_state.students.loc[st.session_state.students["Name"] == student_to_manage, "Age"].values[0]))
        new_gender = st.selectbox("Update Gender:", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(st.session_state.students.loc[st.session_state.students["Name"] == student_to_manage, "Gender"].values[0]))
        new_course = st.selectbox("Update Course:", ["DevOps", "Cloud computing", "Mobile app development", "Ethical hacking", "Soft computing", "STQA", "Data Science", "AI", "Machine Learning", "Web Development", "Cyber Security", "Digital Marketing", "Full Stack Development", "UI/UX Design", "Game Development", "Blockchain", "Big Data", "Internet of Things (IoT)", "Robotics", "Augmented Reality (AR)", "Virtual Reality (VR)", "Data Analytics", "Business Intelligence", "Network Security", "Cloud Architecture", "DevSecOps", "Penetration Testing", "Digital Forensics"], index=["DevOps", "Cloud computing", "Mobile app development", "Ethical hacking", "Soft computing", "STQA", "Data Science", "AI", "Machine Learning", "Web Development", "Cyber Security", "Digital Marketing", "Full Stack Development", "UI/UX Design", "Game Development", "Blockchain", "Big Data", "Internet of Things (IoT)", "Robotics", "Augmented Reality (AR)", "Virtual Reality (VR)", "Data Analytics", "Business Intelligence", "Network Security", "Cloud Architecture", "DevSecOps", "Penetration Testing", "Digital Forensics"].index(st.session_state.students.loc[st.session_state.students["Name"] == student_to_manage, "Course"].values[0]))

        # Update Button
        if st.button("Update Student"):
            if new_age > 18:
                # Update the student information in the DataFrame
                st.session_state.students.loc[st.session_state.students["Name"] == student_to_manage, ["Name", "Age", "Gender", "Course"]] = [new_name, new_age, new_gender, new_course]
                st.markdown(f'<p class="success">Student {new_name} updated successfully!</p>', unsafe_allow_html=True)
                # Refresh the displayed table
                st.dataframe(st.session_state.students)
            else:
                st.markdown('<p class="warning">Age must be greater than 18 to update!</p>', unsafe_allow_html=True)

    # Delete student functionality
    if st.button("Delete Student"):
        st.session_state.students = st.session_state.students[st.session_state.students["Name"] != student_to_manage]
        st.markdown(f'<p class="success">Student {student_to_manage} deleted successfully!</p>', unsafe_allow_html=True)
        # Refresh the displayed table
        st.dataframe(st.session_state.students)
else:
    st.warning("No students to manage.")

# Download button for CSV
st.markdown('<p class="subheader">Download Enrolled Students as CSV</p>', unsafe_allow_html=True)

# Convert the DataFrame to CSV
csv = st.session_state.students.to_csv(index=False)

# Add the download button
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="students.csv",
    mime="text/csv",
    use_container_width=True
)









# import streamlit as st
# import pandas as pd

# # Initialize an empty DataFrame to store student information
# if 'students' not in st.session_state:
#     st.session_state.students = pd.DataFrame(columns=["Name", "Age", "Course"])

# # Title of the app
# st.title("Student Enrollment System")

# # Student Enrollment Form
# st.header("Enroll a New Student")

# # Create input fields for name, age, and course
# name = st.text_input("Enter Student Name:")
# age = st.number_input("Enter Student Age:", min_value=1)
# course = st.selectbox("Select Course:", ["DevOps", "Cloud computing", "Mobile app development", "Ethical hacking", "Soft computing", "STQA", "Data Science", "AI", "Machine Learning", "Web Development", "Cyber Security", "Digital Marketing", "Full Stack Development", "UI/UX Design", "Game Development", "Blockchain", "Big Data", "Internet of Things (IoT)", "Robotics", "Augmented Reality (AR)", "Virtual Reality (VR)", "Data Analytics", "Business Intelligence", "Network Security", "Cloud Architecture", "DevSecOps", "Penetration Testing", "Digital Forensics"])

# # Button to add student
# if st.button("Add Student"):
#     if name and age and course:
#         new_student = pd.DataFrame([[name, age, course]], columns=["Name", "Age", "Course"])
#         st.session_state.students = pd.concat([st.session_state.students, new_student], ignore_index=True)
#         st.success(f"Student {name} enrolled successfully!")
#     else:
#         st.error("Please fill in all fields!")

# # Display enrolled students in a table
# st.subheader("Enrolled Students")

# if not st.session_state.students.empty:
#     st.dataframe(st.session_state.students)
# else:
#     st.warning("No students enrolled yet.")

# # Download button for CSV
# st.subheader("Download Enrolled Students as CSV")

# # Convert the DataFrame to CSV
# csv = st.session_state.students.to_csv(index=False)

# # Add the download button
# st.download_button(
#     label="Download CSV",
#     data=csv,
#     file_name="students.csv",
#     mime="text/csv"
# )

