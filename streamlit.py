import streamlit as st
import pandas as pd 

# Page configuration 
st.set_page_config(
    page_title="تحليل أنماط التسوق في نايس ون",
    page_icon="💄",
    layout="wide"
)

# Add a picture in the header
image_url = "https://i.postimg.cc/zBTBbn7f/Innisfree-2020-Jeju-Color-Picker-Cherry-Blossom-Edition.jpg"
st.image(image_url, use_container_width=True)

# Top header
st.markdown("<h1 style='text-align: center; color: #E91E63;'> !تحليل أنماط التسوق في نايس ون🌸🛍️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'> استكشف تصنيفات العملاء بناءً على سلوك الشراء 🔍</h3>", unsafe_allow_html=True)

st.markdown("---")


file_path = "products_data.csv"
try:
    df = pd.read_csv(file_path)
    column_names = df.columns.tolist()  # Extract columns name

    # Create a drop-down list to select column
    selected_column = st.selectbox("🔽 اختر عمودًا من البيانات:", column_names)
    
    # display selected column name 
    st.write(f"📊 تم اختيار العمود: **{selected_column}**")
    st.markdown(f"""
    <div style="text-align: center; font-size: 18px;">
        <h4 style="display: inline;"> :تم اختيار العمود 📊 </h4>
        <span style="color:#E91E63; font-weight: bold; font-size: 20px;">{selected_column}</span>
    </div>
""", unsafe_allow_html=True)


except Exception as e:
    st.error(f"⚠️ حدث خطأ أثناء تحميل الملف: {e}")
