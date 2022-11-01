from ast import arg
from re import search
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import main
import pandas as pd

config = {
    'user': 'root',
    'password': '12345678',
    'host': '104.198.25.233',
    'database': 'db1'
}

def searcht(searchInput):

    cnx = conn.connect(**config)

    cursor = cnx.cursor(prepared=True)

    # args = (searchInput, )
    # print(f'searchInput: {args}')
    searchQuery = 'SELECT i.item_id, i.name, i.price, i.weight, i.category, i.stock, s.store_name FROM items i Join stores s on i.store_id = s.store_id WHERE name like %s'
    args=['%' + searchInput + '%']
    cursor.execute(searchQuery, args)

    output = cursor.fetchall()
    cursor.close()
    print(f'type: {type(output)}')
    print(f'output: {output}')

    df = pd.DataFrame(output, columns = ['item_id', 'name', 'price', 'weight', 'category', 'stock', 'store_name'])

    return df

def main():

    # Title 
    st.subheader("Search Section")

    user_search_input = st.text_input('Enter item')
    # Search Button
    if st.button("Search", on_click=searcht, args=(user_search_input,)):
        df = searcht(user_search_input)
        st.table(df)
    
    return ""
        
if __name__ == "__main__":
    main()