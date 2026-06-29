import streamlit as st

st.title('Калькулятор знижки')

price = st.number_input('Ціна, грн', min_value=0.0)
discount = st.slider('Знижка, %', 0, 100, 10)

final_price = price * (1 - discount / 100)

st.write(f'Фінальна ціна: {final_price:.2f} грн')
