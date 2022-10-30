#import streamlit as st
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
#import app_text1.py as utils


config = {
    'user': 'root',
    'password': '12345678',
    'host': '104.198.25.233'
}


def loginUser(username, password,):

    cnx = conn.connect(**config)

    cursor = cnx.cursor(prepared=True)

    loginQuery = "SELECT * from Users;"

    cursor.execute(loginQuery, (username,password,))   

    print(cursor)

    cnx.close()

    cursor.close()

def main():

    # Title 
    st.subheader("Login Section")

    # Login Input
    username = st.text_input('Enter username')

    password = st.text_input('Enter password')
        
    if st.button("Login"):
        result = loginUser(username,password)

if __name__ == "__main__":
    main()
