import streamlit as st 

st.title("TDS Demo")

st.sidebar.header("User Input")

user_text = st.sidebar.text_input("Enter some text","Hello TDS students")

number = st.sidebar.slider("Select a number",min_value=10,max_value=100,value=50)
result = number * 5 
st.write(f'### The number {number} multiplied by 5 is {result}')

reverse_text = st.sidebar.checkbox("Reverse Text")

case = st.sidebar.radio("Chose the text case:",('Original','Uppercase','Lowercase'))

if case == 'Uppercase':
    transformed_text = user_text.upper()
elif case == 'Lowercase':
    transformed_text = user_text.lower()
else:
    transformed_text = user_text
    
if reverse_text:
    transformed_text = user_text[::-1]
    
st.write("### Transformed Text")

st.write(transformed_text)