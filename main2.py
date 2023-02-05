import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("" Life")
left_column, right_column = st.columns(2)
button = left_column.button('たっくん好き？')
if button:
    right_column.write('ありがとう！')

st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    time.sleep(0.03)
'Done!!'

expander = st.expander("Q:いつ生まれた？")
expander.write('2023年1月29日')
expander = st.expander("Q:どこで生まれた？")
expander.write('横浜市立みなと赤十字病院')

option=""
option = st.selectbox(
    label='何日目の写真が見たい？',
    options = list(range(0,7))
)
'たっくんの',option,'日目の写真です。'
if option != "":
    img = Image.open(str(option)+".jpeg")
    st.image(img, caption="たっくん", use_column_width=True)

if st.sidebar.checkbox('たっくん好き？'):
    img = Image.open("tatsuki.jpg")
    st.image(img, caption="たっくん生まれたて", use_column_width=True)


text = st.sidebar.text_input('たっくんへのメッセージを送ってください。')
'たっくんへのメッセージ:',text

condition = st.sidebar.slider("たっくんの愛は何%？",0,100,50)
'たっくんへの愛',condition

if condition>90:
    img = Image.open("tatsuki.jpg")
    st.image(img, caption="ありがとう", use_column_width=True)
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)



# df = pd.DataFrame({
#     "1列目":[1,2,3,4],
#     "2列目":[40,30,20,10]
# }
# )
# st.dataframe(df.style.highlight_max(axis=0), width = 200, height=300)

# st.table(df.style.highlight_max(axis=0))

# """
# #章
# ##節
# ###項

# ''' python
# import streamlit as st
# import numpy as np
# import pandas as pd
# '''

# """