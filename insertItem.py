from tokenize import Double
import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import pandas as pd

import connDetails as connDet

def insertItem(itemName, store_id, price, weight, category, quantity) -> pd.DataFrame:
    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    cursor = cnx.cursor()

    args = (store_id, itemName, price, weight, category, quantity)

    print(args)

    #cursor.callproc("insertItem", args)

    #cursor.close()

    #insertQuery = "INSERT INTO items "\
    #           "(item_id, store_id, name, price, weight, category, stock)"\
    #           "VALUES (NULL, %s, %s, %s, %s, %s, %s)"

    storedProcedure = "exec insertItem(%s, %s, %s, %s, %s, %s) "

    cursor.execute(storedProcedure, args)

    cnx.commit()

    cursor.close()

def getAllCategories() -> list:
    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    cursor = cnx.cursor()

    query1 = ("select name from category")
    cursor.execute(query1)
    temp = cursor.fetchall()
    cursor.close()
    category_list = []
    for i in temp:
        category_list.append(i[0])

    return category_list

def getAllStores() -> list:

    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    cursor = cnx.cursor()

    query1 = ("select * from stores A;")
    cursor.execute(query1)
    temp = cursor.fetchall()
    cursor.close()
    store_info = {}
    for i in temp:
        store_info[i[1]] = i[0]

    return store_info

def showItems() -> pd.DataFrame:
    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    cursor = cnx.cursor()

    queryItems = ("select * from items;")
    cursor.execute(queryItems)
    data = cursor.fetchall()
    cursor.close()

    result = []
    for xs in data:
        temp = []
        for x in xs:
            temp.append(str(x))
        
        result.append(tuple(temp))

    df = pd.DataFrame(result, columns =['item_id', 'store_id', 'name', 'price', 'weight', 'category', 'stock'])

    return df

def insertPage():

    st.title("Insert Items")

    # itemName
    itemName = st.text_input('Enter item')

    # weight
    weight = st.text_input('Enter Weight')

    # quantity 
    quantity = st.text_input('What is the quanity?')

    # price 
    price = st.text_input("What is the price of the item")

    # category 
    all_categories = getAllCategories() 
    category = st.selectbox('Select a Category', options = all_categories)

    # stores
    all_stores = getAllStores()
    store = st.selectbox('Choose a Store', options = all_stores.keys())

    # Search Button
    if itemName and weight and quantity and price and category and store:
        st.button('Add Item', on_click=insertItem, args=(itemName, all_stores[store], price, weight, category, quantity))
        df = showItems()
        st.dataframe(df)
    # Drop Down Menu
    #categories = ['food','electronics']
    # selected_cat = st.selectbox("search by category",options = categories)
