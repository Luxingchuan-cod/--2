import os
import streamlit as st
from multipage import MultiPage
from home import app as home_app
from machine_learning import app as ml_app

st.set_page_config(page_title="ML", page_icon=":tiger:", layout="wide")
st.title('Machine Learning Application')

app = MultiPage()

# 添加应用程序
app.add_page('Home', home_app)
app.add_page('Machine Learning', ml_app)

# 运行应用程序
if __name__ == '__main__':
    app.run()