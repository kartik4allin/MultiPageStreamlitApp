import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages
from streamlit_modal import Modal
import streamlit.components.v1 as components

show_pages([
    Page("main.py","Main"),
    Page("nextpage.py","NextPage"),
    Page("thankyou.py","ThankYouPage")
])

hide_pages(['NextPage'])
hide_pages(['ThankYouPage'])

# modal = Modal(
#     "Consent Screen", 
#     key="demo-modal",
    
#     # Optional
#     padding=20,    # default value
#     max_width=744  # default value
# )
# open_modal = st.button("Open",key="Open")
# modal.open()

# Add CSS styles for the containers
# container_style = """
#     <style>
#         .container1 {
#             border: 2px solid #3498db;
#             border-radius: 8px;
#             padding: 10px;
#             margin-bottom: 20px;
#         }
#         .container2 {
#             /* Add styles for Container 2 if needed */
#         }
#     </style>
# """

# # Display the CSS styles
# st.markdown(container_style, unsafe_allow_html=True)

def main_page():
    

    modal = Modal(
        "Consent Screen", 
        key="demo-modal",
        
        # Optional
        padding=20,    # default value
        max_width=744  # default value
    )
    open_modal = st.button("Open",key="Open")
    if open_modal:
        modal.open()    

    if modal.is_open():


        

        with modal.container() :
            st.write("This app supports only NON-PII data.You can upload your pdf and ask questions related to it")

            html_string = '''
            <h1>THIS APP DOESNT SUPPORTS PII DATA.THIS IS ONLY FOR US REGION.IF YOU WANT TO PROCEED ,CHECK YES OR CHECK NO</h1>

            <script language="javascript">
            document.querySelector("h1").style.color = "red";
            </script>
            '''
            components.html(html_string)

            #st.write("Some fancy text")
            # value_yes = st.checkbox("Yes")
            # value_no = st.checkbox("No")
            # st.write(f"Checkbox YES checked: {value_yes}")
            # st.write(f"Checkbox NO checked: {value_no}")
            YesButton = st.button("Yes")
            NoButton = st.button("No")

            if YesButton:
                switch_page('NextPage')
            if NoButton:
                switch_page('ThankYouPage')


            # if value_no:
            #     #modal.close()
            #     st.session_state.runpage = ThankYou.ThankyouPage
            #     st.session_state.runpage()
            #     st.experimental_rerun()

            # if value_yes:
            #     #modal.close()
            #     st.session_state.runpage = main_page
            #     st.session_state.runpage()
            #     st.experimental_rerun() 

    # if "runpage" not in st.session_state:
    #     st.session_state.runpage = main_page
    #     st.session_state.runpage()   

if __name__ == "__main__":
    main_page()    