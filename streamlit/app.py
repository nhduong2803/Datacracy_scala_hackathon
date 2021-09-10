import streamlit as st
from multiapp import MultiApp
from apps import 1st_page,2nd_page  # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Data Analysis", 1st_page.main)
app.add_app("Demo", 2nd_page.main)
# The main app
app.run()
