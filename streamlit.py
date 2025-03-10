import streamlit as st

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
st.markdown("<h1 style='text-align: center; color: #E91E63;'> !تحليل أنماط التسوق في نايس ون📢</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'> استكشف تصنيفات العملاء بناءً على سلوك الشراء 🔍</h3>", unsafe_allow_html=True)

st.markdown("---")

# مساحة لإضافة محتوى التطبيق لاحقًا
st.write("👩‍💻 هنا سيتم عرض البيانات والتحليلات لاحقًا.")


