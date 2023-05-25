from pymongo import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

# replace here with your mongodb url 
uri = "mongodb+srv://jona2708:Jonathan2708@bdnosql.p8tt50o.mongodb.net/?retryWrites=true&w=majority"

# Connect to meme MongoDB database

try:
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    db = client.bdnosql
    print("MongoDB Connected successfully!")
except:
    print("Could not connect to MongoDB")

# streamlit run streamlit-mongo.py --server.enableCORS false --server.enableXsrfProtection false

st.title("mongo db conn")
# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    items = db.bdnosql_info.find()
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

st.write('results...')
st.write(items)

# Print results.i
for item in items:
    st.write(f"{item['_id']} has a :{item['name']}:")
