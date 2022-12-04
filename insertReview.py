from tokenize import Double
import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import pandas as pd
import connDetails 


def insertReview(store_id, review, rating) -> pd.DataFrame:
    cnx = conn.connect(user=connDetails.user, password=connDetails.password, host=connDetails.host,
                       database=connDetails.database)
    cursor = cnx.cursor()

    args = (store_id, review, rating)

    print(args)

    insertQuery = "INSERT INTO review " \
                  "(store_id, review, rating)" \
                  "VALUES (NULL, %s, %s, %d)"

    cursor.execute(insertQuery, args)

    cnx.commit()

    cursor.close()



# def showItems() -> pd.DataFrame:
#     cnx = conn.connect(user=conn.user, password=conn.password, host=conn.host,
#                        database=conn.database)
#     cursor = cnx.cursor()

#     queryItems = ("select * from items;")
#     cursor.execute(queryItems)
#     data = cursor.fetchall()
#     cursor.close()

#     result = []
#     for xs in data:
#         temp = []
#         for x in xs:
#             temp.append(str(x))

#         result.append(tuple(temp))

#     df = pd.DataFrame(result, columns=['item_id', 'store_id', 'name', 'price', 'weight', 'category', 'stock'])

#     return df


def insertReview():
    st.title("Insert Items")

    # itemName
    store_id = st.text_input('Enter Store ID')

    # weight
    review = st.text_input('Enter Review')

    # quantity
    rating = st.text_input('Enter Rating')


    # Search Button
    if store_id and review and rating:
        st.button('Add Item', on_click=insertReview,
                  args=(store_id, review, rating))
        # df = showItems()
        # st.dataframe(df)
    # Drop Down Menu
    # categories = ['food','electronics']
    # selected_cat = st.selectbox("search by category",options = categories)
