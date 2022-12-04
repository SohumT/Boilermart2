#import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
#from google.cloud import storage 
import pandas as pd

#import app_text1.py as utils

#from python_mysql_dbconfig import read_db_config
from PIL import Image

def main():
    st.title("BoilerMart")
    #name of item, name of store, price after discounts
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

if __name__ == "__main__":
    main()
