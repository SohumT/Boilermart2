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

    insertQuery = "INSERT INTO items "\
               "(item_id, store_id, name, price, weight, category, stock)"\
               "VALUES (NULL, %s, %s, %s, %s, %s, %s)"

    cursor.execute(insertQuery, args)

    cnx.commit()

    cursor.close()

def getAllCategories() -> list:
    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    cursor = cnx.cursor()

    query1 = ("select * from get_categories")
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

        cnx = conn.connect(user='root', password='12345678', host='104.198.25.233', 
                              database='boilermart')
    #deletion = ("delete from dis_result")
    cursor = cnx.cursor()
    #cursor.execute(deletion)

    #get_discounts = ("INSERT INTO dis_result SELECT items.name, store.names, items.price * (1 - discounts.percentage) as discounted_price from discounts, items, stores WHERE items.item_id == discounts.item_id AND store.store_id == items.store_id ORDER BY discounts.percentage")
    get_discounts = ("SELECT discounts.sale_name, items.name, stores.store_name, items.price, (items.price * (1 - discounts.percentage)) as discounted_price from discounts, items, stores WHERE items.item_id = discounts.item_id AND stores.store_id = items.store_id ORDER BY discounts.percentage")
    cursor.execute(get_discounts)
    #retrieval = ("SELECT * FROM dis_result")
    #cursor.execute(retrieval)
    discounts = cursor.fetchall()

    result = []
    for xs in discounts:
        temp = []
        for x in xs:
            temp.append(str(x))

        result.append(tuple(temp))
    df = pd.DataFrame(result, columns = ["Sale", "On", "Available at", "Price", "Discounted Price"])
    print(df)
    st.table(df)
    # Drop Down Menu
    #categories = ['food','electronics']
    # selected_cat = st.selectbox("search by category",options = categories)
