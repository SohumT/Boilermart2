from ast import arg
from re import search
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import main
import pandas as pd

import connDetails
import categories
import stores

config = {
    'user': connDetails.user,
    'password': connDetails.password,
    'host': connDetails.host,
    'database': connDetails.database
}

def searcht(searchInput, store_id, category_id):

    cnx = conn.connect(**config)

    cursor = cnx.cursor()

    args = (store_id, category_id,)

    cursor.callproc('get_item_category', args)

    args = (searchInput, )
    print(f'searchInput: {args}')
    searchQuery = 'SELECT i.item_id, i.name, i.price, i.weight, i.category, i.stock, s.store_name FROM results i Join stores s on i.store_id = s.store_id WHERE name like %s'
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

    # Select store
    store_dict = stores.store_dropdown()
    storeOption = st.selectbox('Select a Store', store_dict.keys())
    selected_store_id = store_dict[storeOption]

    # Select category 
    category_dict = categories.category_dropdown()

    categoryOption = st.selectbox('Select a Category', categories.category_dropdown())
    selected_category_id = category_dict[categoryOption]
    
    category_dict2 = dict(map(reversed, category_dict.items()))

    print(f'category_dict2.keys(): {category_dict2.keys()}')
    # Search item textbox
    user_search_input = st.text_input('Enter item')

    # Advanced Search Button
    if st.button("Search", on_click=searcht, args=(user_search_input, selected_store_id, selected_category_id)):
        df = searcht(user_search_input, selected_store_id, selected_category_id)
        for i in category_dict2.keys():
            df['category'] = df['category'].replace(str(i), str(category_dict2[i]))
        df = df.drop(df.columns[0], axis=1)
        st.table(df)

        
if __name__ == "__main__":
    main()