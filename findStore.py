from tokenize import Double
import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import pandas as pd
import connDetails 

config = {
    'user': connDetails.user,
    'password': connDetails.password,
    'host': connDetails.host,
    'database': connDetails.database
}


def loadStore(userZipcode):
    cnx = conn.connect(**config)
    cursor = cnx.cursor()

    queryItems = ("select * from stores;")
    cursor.execute(queryItems)
    temp = cursor.fetchall()
    cursor.close()
    print(temp)

    stores = pd.DataFrame(temp, columns =['store_id', 'store_name', 'company_id', 'address', 'zipcode'])
    stores = stores.reset_index()
    distance = []
    for index, row in stores.iterrows():
        store_zipcode = row[5]
        dist = abs(int(store_zipcode) - int(userZipcode))
        distance.append(dist)
    print(distance)
    stores['distance'] = distance
    stores = stores.sort_values(by=['distance'], ascending=True)
    stores = stores.drop(columns=['index','store_id','company_id','distance'])
    print(stores)


    return stores

        

def main():
    st.title("Find Nearby Stores")

    # Zipcode
    user_zipcode = st.text_input('Enter Your Zipcode')
    df = None
    # Search Button
    if user_zipcode != "":
        st.button('Search', key=5, on_click=loadStore,
                  args=(user_zipcode,))
        df = loadStore((user_zipcode))
        st.table(df)

