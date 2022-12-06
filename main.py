import streamlit as st
import mysql.connector as conn

import insertItem
import itemSearch
from streamlit_option_menu import option_menu
import categories
import stores
import insertReview
#import app_text1.py as utils


#from python_mysql_dbconfig import read_db_config
from PIL import Image

# Search Function - Display new page from here 
# Changed Nav Bar Page 

def searchFunc(item):

    if item:
        #utils.itemTest(item)
        # call the page function to display the table
        print(item)
        
    #return

def navBar():
    selected = option_menu (
        menu_title=None,  # required
        options=["Home", "Insert Item", "Write Review for Stores"],  # required
        default_index=0,  # optional
        orientation="horizontal",
    )

    return selected

def search():
     # Title 
    st.title("Boilermart")

    # Search bar
    search = st.text_input('Enter item')

    # Search Button
    st.button("Search", on_click=searchFunc, args=(search,))
      

def main():

    # Login and Signup Buttons

    # image = Image.open('logo.png')
    # st.image(image, width=300px)

    selected = navBar()

    if selected:
        if selected == 'Home':
            itemSearch.main()
        elif selected == 'Write Review for Stores':
            insertReview.insertReviewMain()
            insertReview.searchReviewMain()
        else:
            insertItem.insertPage()
        
    

if __name__ == "__main__":
    main()