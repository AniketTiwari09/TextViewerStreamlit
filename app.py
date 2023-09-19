import streamlit as st

def main():
    st.title("Text File Code Viewer")
    

    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

    if uploaded_file is not None:
        file_bytes = uploaded_file.read()

        file_contents = file_bytes.decode("utf-8")

        st.subheader("File Content:")
        st.code(file_contents, language="text")



if __name__ == "__main__":
    main()