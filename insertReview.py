from tokenize import Double
import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import pandas as pd
import connDetails 
import stores




def insertReview(store_name, content, rating) -> pd.DataFrame:
    cnx = conn.connect(user=connDetails.user, password=connDetails.password, host=connDetails.host,
                       database=connDetails.database)
    cursor = cnx.cursor()

    args = (store_name, content, rating, )

    print(args)

    insertQuery = "INSERT INTO reviews VALUES (NULL, %s, %s, %s)"


    cursor.execute(insertQuery, args)

    cnx.commit()

    cursor.close()

def insertReviewMain():
    st.title("Write Review")

    store_dict = stores.store_dropdown()
    storeOption = st.selectbox('Select a Store', store_dict.keys())
    selected_store_id = store_dict[storeOption]

    review = st.text_input('Enter Review')

    rating = st.text_input('Enter Rating(Please input 1 ~ 5)')

    
    if rating != '' and rating.isdigit():
        rating = int(rating)
        if rating <=5 and rating >= 1:
            if st.button('Upload', on_click=insertReview, args=(storeOption, review, rating)) and selected_store_id and review and rating is not None:
                st.success('This is a success message!')      
        else: 
            st.error("Please put proper the inputs", icon=None)
    else:
        st.error("Please put proper the inputs", icon=None)
        
def searchReview(storeOption):

    cnx = conn.connect(user=connDetails.user, password=connDetails.password, host=connDetails.host,
                       database=connDetails.database)
    cursor = cnx.cursor()
    print(111111111)
    args = (storeOption, )
    print(f'tutple: {storeOption}')
    
    searchQuery = 'SELECT review_id, store_name, content, rating FROM reviews WHERE store_name = %s'
    # args=['%' + storeOption + '%']
    cursor.execute(searchQuery, args)

    output = cursor.fetchall()
    cursor.close()
    print(f'type: {type(output)}')
    print(f'output: {output}')

    df = pd.DataFrame(output, columns = ['review_id', 'store_name', 'content', 'rating'])

    return df

def searchReviewMain():
    # Title 
    st.subheader("Search Review")

    # Select store
    store_dict = stores.store_dropdown()
    storeOption = st.selectbox('Select a Store', store_dict.keys(), key = "1")
    # selected_store_id = store_dict[storeOption]
    
    # Advanced Search Button
    if storeOption != "<SELECT A STORE>":
        print(f'storeOption: {storeOption}')
        if st.button("Search", on_click=searchReview, args=(storeOption, )):
            df = searchReview(storeOption)
            df = df.drop(df.columns[0], axis=1)
            st.table(df)
            
    else:
        st.error("Please select a store", icon=None)