import streamlit as st
from multiapp import MultiApp
from apps import first_page,second_page  # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Data Analysis", first_page.main)
app.add_app("Demo", second_page.main)
# The main app
app.run()
