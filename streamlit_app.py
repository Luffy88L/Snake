import streamlit as st
import random

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Cool Math Generator", page_icon="🔥", layout="centered")

# CSS เท่ ๆ
st.markdown("""
<style>
    body {
        background: #0d0d0d;
        color: #fff;
        font-family: 'Roboto', sans-serif;
    }
    .title {
        font-size: 45px;
        text-align: center;
        color: #00eaff;
        text-shadow: 0 0 15px #00eaff;
        font-weight: bold;
    }
    .box {
        padding: 25px;
        border-radius: 15px;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255,255,255,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🔥 COOL MATH GENERATOR 🔥</div>", unsafe_allow_html=True)
st.write("")

# ปุ่มสร้างโจทย์
if st.button("⚡ สร้างโจทย์ใหม่", use_container_width=True):

    a = random.randint(1, 99)
    b = random.randint(1, 99)
    op = random.choice(['+', '-', '*', '/'])

    if op == '+':
        ans = a + b
    elif op == '-':
        ans = a - b
    elif op == '*':
        ans = a * b
    else:
        ans = round(a / b, 2)

    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader(f"✳️ โจทย์:  **{a}  {op}  {b}**")
    st.success(f"💡 คำตอบ:  **{ans}**")
    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("กดปุ่มด้านบนเพื่อสร้างโจทย์เท่ ๆ 🤘😎")
