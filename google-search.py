import streamlit as st
from googlesearch import search

APP_NAME = "Google Search Test"

st.set_page_config(
     page_title=APP_NAME,
     page_icon="🧊",
 )

st.title(APP_NAME)

text = st.text_input("Enter a query...", key='input_query')

site = st.selectbox(
        'Site to search in',
        ['', 'www.xilinx.com', 'www.nutanix.com', 'www.te.com'])

file_type = st.selectbox(
        'File Type',
        ('', 'pdf', 'doc', 'docx', 'ppt', 'pptx'))

num = int(st.selectbox(
        'Limit',
        ('10', '15', '20')))


uploaded_file = st.file_uploader("Or choose a file", type=["txt"])

def find_and_render(text, file_type, site, num):
    query = ''
    if file_type:
        query += f'filetype:{file_type} '

    if site:
        query += f'site:{site}'

    query += f' {text}'
    index = 0
    try:
        for result in search(query, num=num, stop=num, pause=2):
            st.write(f'{index + 1} - {result}')
            index += 1
    except Exception as e:
        print(e)

if text or uploaded_file is not None:
    st.header('Results:')

if uploaded_file is not None:
    text = ''
    
    for line in uploaded_file:        
        query = line.decode("utf-8")
        st.subheader(query)
        find_and_render(query, file_type, site, num)

if text:
    find_and_render(text, file_type, site, num)
    

