#import streamlit as st
import streamlit as st
import mysql.connector as conn
import login
from streamlit_option_menu import option_menu
#import app_text1.py as utils


#from python_mysql_dbconfig import read_db_config
from PIL import Image

# Search Function - Display new page from here 

def searchFunc(item):

    if item:
        #utils.itemTest(item)
        # call the page function to display the table
        print(item)
        
    #return

def navBar():
    selected = option_menu (
        menu_title=None,  # required
        options=["Sign Up", "Login"],  # required
        default_index=0,  # optional
        orientation="horizontal",
    )

    return selected

    
def main():

    # Login and Signup Buttons

    # image = Image.open('logo.png')
    # st.image(image, width=300px)

    selected = navBar()

    if selected:
        if selected == 'Sign Up':
            print("Sign up")
        else:
            login.main()
      
    # Title 
    st.title("Boilermart")

    # Search bar
    search = st.text_input('Enter item')

    # Search Button
    st.button("Search", on_click=searchFunc, args=(search,))
      
    # Drop Down Menu
    #categories = ['food','electronics']
   # selected_cat = st.selectbox("search by category",options = categories)
    

if __name__ == "__main__":
    main()
