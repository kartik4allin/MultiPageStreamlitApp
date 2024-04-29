import streamlit as st
from st_pages import hide_pages
from st_pages import Page, show_pages, hide_pages


def main():

    st.set_page_config(page_title="Smart Chat with PDF")
    st.page_link("main.py", label="Home", icon="🏠")
    # st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
    # st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
    # st.page_link("http://www.google.com", label="Google", icon="🌎")
    

    st.write("You are in Next Page")
    show_pages([
    Page("main.py","Main"),
    Page("nextpage.py","NextPage"),
    Page("thankyou.py","ThankYouPage")
    ])
    hide_pages(['Main'])
    hide_pages(['ThankYouPage'])
    hide_pages(['NextPage'])
    
    st.title("Please upload your files...📁 ")
    

    

    # Upload the pdf file
    pdf = st.file_uploader("Only PDF files allowed", type=["pdf"])

    # Extract the whole text from the uploaded pdf file
    if pdf is not None:
        with st.spinner('Wait for it...'):
            #text=read_pdf_data(pdf)
            st.write("👉Reading PDF done")

            # Create chunks
            #docs_chunks=split_data(text)
            #st.write(docs_chunks)
            st.write("👉Splitting data into chunks done")

            # Create the embeddings
            #embeddings=create_embeddings_load_data()
            st.write("👉Creating embeddings instance done")

            # Build the vector store (Push the PDF data embeddings)
            #push_to_pinecone("2bbf649c-10c0-4edf-8c06-9416c17a9d68","gcp-starter","chatbot",embeddings,docs_chunks)

        st.success("Successfully pushed the embeddings to Pinecone")

        st.write("We are here to help you, please ask your question:")
        user_input = st.text_input("🔍")
        if user_input:
            #creating embeddings instance
            # embeddings=create_embeddings()

            # #Function to pull index data from Pinecone
            # index=pull_from_pinecone("2bbf649c-10c0-4edf-8c06-9416c17a9d68","gcp-starter","chatbot",embeddings)
            
            # #This function will help us in fetching the top relevent documents from our vector store - Pinecone Index
            # relavant_docs=get_similar_docs(index,user_input)

            # #This will return the fine tuned response by LLM
            # response=get_answer(relavant_docs,user_input)
            st.write("Writing the user Input as is "+user_input)


if __name__ == "__main__":
    main()    
