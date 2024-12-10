import streamlit as st
import pandas as pd
table =pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40],
    'Column 3': [100, 200, 300, 400]
})
# https://katex.org/docs/supported
st.title("Something in Streamlit")
st.markdown("---")

# st.header("Hi I am a header")
# st.subheader("Hi I am a subheader")
# st.text("Hi I am a text or paragraph")
# st.markdown(" **Hello** world")
# st.markdown("---")
# st.latex(r"\sum_{i=0}^\infty \frac{1}{2^i} = 1")
# st.latex(r"\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}")
# json = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }
# st.json(json)
# code = """ 
# for(int i = 0; i < 10; i++)
#     print(i)
# """
# st.code(code, language="cpp")
# st.markdown("---")
# st.metric(label="Temperature", value="70 °F", delta="-2 °F")
# st.table(table)
# st.dataframe(table)
# st.image("https://images.pexels.com/photos/16491141/pexels-photo-16491141.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", caption="This Image from Pexels",width=500)
# st.video("https://videos.pexels.com/video-files/29506656/12701640_2560_1440_24fps.mp4")
# st.markdown("---")


# state = st.checkbox("Choose 1")
# radio_btn = st.radio("Choose 2",options=("Option 1", "Option 2", "Option 3"))
# # print(radio_btn)
# def btn_click():
#     print("Button Clicked")

# btn=st.button("Click me",on_click=btn_click)
# selectBox=st.selectbox("What is you favorite color (select box)",options=("Red", "Green", "Blue", "Yellow", "Orange", "Purple"))
# multi_select = st.multiselect("What is you favorite color (multiple select)",options=("Red", "Green", "Blue", "Yellow", "Orange", "Purple"))
# st.write(multi_select)
# slider=st.slider('Sepal length', 4.3, 7.9, 5.4)
# if slider%2==0 :
#     st.write("Even")
# else:
#     st.write("Odd")

# image = st.file_uploader("Plase upload a file",accept_multiple_files=True)
# if image is not None:
#     st.image(image)
clases = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5"]
Name = st.text_input("What is you name")
Class = st.select_slider("What is you class", options=clases)
Score = st.slider("What is you score",0.0,100.0,50.0)
Btn = st.button("Submit")
if Btn:
    st.write(f"Hello {Name} your class is {Class} and your score is {Score}")
    if(Score>=50):
        st.write("Pass")
    else:
        st.write("Fail")
val = st.text_area("Course Description")
data = st.date_input("Course Data")
time = st.time_input("Course Time")


