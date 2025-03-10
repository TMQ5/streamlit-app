import streamlit as st
import pandas as pd 

# إعداد الصفحة
st.set_page_config(
    page_title="تحليل أنماط التسوق في نايس ون",
    page_icon="💄",
    layout="wide"
)

# إضافة صورة في الهيدر
image_url = "https://i.postimg.cc/zBTBbn7f/Innisfree-2020-Jeju-Color-Picker-Cherry-Blossom-Edition.jpg"
st.image(image_url, use_container_width=True)

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; color: #E91E63;'>!تحليل أنماط التسوق في نايس ون🌸🛍️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'> استكشف تصنيفات العملاء بناءً على سلوك الشراء 🔍</h3>", unsafe_allow_html=True)

st.markdown("---")

# تحميل البيانات
file_path = "products_data.csv"

try:
    # قراءة الملف
    df = pd.read_csv(file_path)
    
    # استخراج قائمة البراندات الفريدة
    if "brand_name" in df.columns:
        brand_list = df["brand_name"].dropna().unique().tolist()
        brand_list.sort()  # ترتيب البراندات أبجديًا
    else:
        brand_list = ["لا توجد بيانات متاحة"]
    
    # اختيار البراند
    st.markdown("""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
            🏷️ اختر نوع البراند:
        </div>
    """, unsafe_allow_html=True)
    selected_brand = st.selectbox("", brand_list)

    # خط فاصل
    st.markdown("---")

    # اختيار العمود
    column_names = df.columns.tolist()
    st.markdown("""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
            🔽 اختر عمودًا من البيانات:
        </div>
    """, unsafe_allow_html=True)
    selected_column = st.selectbox("", column_names, index=0)

    # عرض البراند والعمود المختارين
    st.markdown(f"""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
            🏷️ تم اختيار البراند: <span style="color:#E91E63;">{selected_brand}</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
            📊 تم اختيار العمود: <span style="color:#E91E63;">{selected_column}</span>
        </div>
    """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"⚠️ حدث خطأ أثناء تحميل الملف: {e}")
