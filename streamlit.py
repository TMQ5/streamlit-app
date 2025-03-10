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

    # عرض البراند المختار
    st.markdown(f"""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
              تم اختيار البراند:
            <div style="margin-top: 5px; color:#E91E63; font-weight: bold; font-size: 20px;">
                {selected_brand}
            </div>
        </div>
    """, unsafe_allow_html=True)

 

    # استخراج قائمة أنواع المكياج الفريدة
    if "makeup_type" in df.columns:
        makeup_type_list = df["makeup_type"].dropna().unique().tolist()
        makeup_type_list.sort()  # ترتيب القيم أبجديًا
    else:
        makeup_type_list = ["لا توجد بيانات متاحة"]

    # اختيار نوع المكياج
    st.markdown("""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
              :اختر نوع المكياج💄
        </div>
    """, unsafe_allow_html=True)
    selected_makeup_type = st.selectbox("", makeup_type_list)

    # عرض نوع المكياج المختار
    st.markdown(f"""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
              :تم اختيار نوع المكياج
            <div style="margin-top: 5px; color:#E91E63; font-weight: bold; font-size: 20px;">
                {selected_makeup_type}
            </div>
        </div>
    """, unsafe_allow_html=True)


     # إدخال عدد المراجعات (reviews_number) كقيمة رقمية
    st.markdown("<div style='text-align: center; font-size: 18px; font-weight: bold;'> :أدخل عدد المراجعات⭐</div>", unsafe_allow_html=True)
    
    reviews_number = st.number_input("", min_value=0, step=1, value=10)  # يمكن للمستخدم إدخال رقم فقط

    # عرض عدد المراجعات المختار
    st.markdown(f"""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
             :عدد المراجعات المختار
            <div style="margin-top: 5px; color:#E91E63; font-weight: bold; font-size: 20px;">
                {reviews_number}
            </div>
        </div>
    """, unsafe_allow_html=True)

        # إدخال السعر الأصلي (original_price) كقيمة عشرية
    st.markdown("<div style='text-align: center; font-size: 18px; font-weight: bold;'> :أدخل السعر الأصلي💰</div>", unsafe_allow_html=True)
    
    original_price = st.number_input("", min_value=0.0, step=0.1, value=1000.0, format="%.2f")  # إدخال قيمة عشريه

    # عرض السعر الأصلي المختار
    st.markdown(f"""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
             :السعر الأصلي المختار
            <div style="margin-top: 5px; color:#E91E63; font-weight: bold; font-size: 20px;">
                {original_price:.2f} ريال
            </div>
        </div>
    """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"⚠️ حدث خطأ أثناء تحميل الملف: {e}")
