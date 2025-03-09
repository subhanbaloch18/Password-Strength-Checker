import streamlit as st
import re

# 🎉 Title
st.title("🔐 【﻿𝙐𝙡𝙩𝙞𝙢𝙖𝙩𝙚　𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙　𝙎𝙩𝙧𝙚𝙣𝙜𝙩𝙝　𝘾𝙝𝙚𝙘𝙠𝙚𝙧】")

# 📝 Description
st.markdown("""
𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘵𝘰 𝘵𝘩𝘦 𝘈𝘶𝘵𝘩𝘦𝘯𝘵𝘪𝘤 𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥 𝘚𝘵𝘳𝘦𝘯𝘨𝘵𝘩 𝘊𝘩𝘦𝘤𝘬𝘦𝘳!  
𝘌𝘯𝘴𝘶𝘳𝘦 𝘺𝘰𝘶𝘳 𝘱𝘢𝘴𝘴𝘸𝘰𝘳𝘥 𝘪𝘴 𝘴𝘦𝘤𝘶𝘳𝘦 𝘣𝘺 𝘤𝘩𝘦𝘤𝘬𝘪𝘯𝘨:
- ✅𝘓𝘦𝘯𝘨𝘵𝘩
- ✅ 𝘜𝘱𝘱𝘦𝘳 & 𝘓𝘰𝘸𝘦𝘳𝘤𝘢𝘴𝘦 𝘭𝘦𝘵𝘵𝘦𝘳𝘴
- ✅ 𝘕𝘶𝘮𝘣𝘦𝘳𝘴
- ✅ 𝘚𝘱𝘦𝘤𝘪𝘢𝘭 𝘊𝘩𝘢𝘳𝘢𝘤𝘵𝘦𝘳𝘴

> ⚡ *Improve your online security by creating strong passwords!*  
""")

# 🏷️ Input Field
password = st.text_input("🔑𝘌𝘯𝘵𝘦𝘳 𝘺𝘰𝘶𝘳 𝘱𝘢𝘴𝘴𝘸𝘰𝘳𝘥:", type="password")

# 🔍 Password Strength Check
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ 𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥 𝘴𝘩𝘰𝘶𝘭𝘥 𝘣𝘦 𝘢𝘵 𝘭𝘦𝘢𝘴𝘵 **8 𝘤𝘩𝘢𝘳𝘢𝘤𝘵𝘦𝘳𝘴** 𝘭𝘰𝘯𝘨.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ 𝘐𝘯𝘤𝘭𝘶𝘥𝘦 **𝘣𝘰𝘵𝘩 𝘶𝘱𝘱𝘦𝘳𝘤𝘢𝘴𝘦 𝘢𝘯𝘥 𝘭𝘰𝘸𝘦𝘳𝘤𝘢𝘴𝘦** 𝘭𝘦𝘵𝘵𝘦𝘳𝘴.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ 𝘈𝘥𝘥 𝘢𝘵 𝘭𝘦𝘢𝘴𝘵 **𝘰𝘯𝘦 𝘯𝘶𝘮𝘣𝘦𝘳 (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ 𝘐𝘯𝘤𝘭𝘶𝘥𝘦 𝘢𝘵 𝘭𝘦𝘢𝘴𝘵 **𝘰𝘯𝘦 𝘴𝘱𝘦𝘤𝘪𝘢𝘭 𝘤𝘩𝘢𝘳𝘢𝘤𝘵𝘦𝘳 (!@#$%^&*)**.")

    return score, feedback


# ✅ Button to Check Password
if st.button("🔍 𝘊𝘩𝘦𝘤𝘬 𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥 𝘚𝘵𝘳𝘦𝘯𝘨𝘵𝘩"):
    if password:
        score, feedback = check_password_strength(password)

        st.subheader("🔒 𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥 𝘚𝘵𝘳𝘦𝘯𝘨𝘵𝘩 𝘙𝘦𝘴𝘶𝘭𝘵:")

        if score == 4:
            st.success("✅ 𝘚𝘵𝘳𝘰𝘯𝘨 𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥! 𝘠𝘰𝘶𝘳 𝘱𝘢𝘴𝘴𝘸𝘰𝘳𝘥 𝘪𝘴 𝘴𝘦𝘤𝘶𝘳𝘦.")
        elif score == 3:
            st.warning("⚠️ 𝘔𝘰𝘥𝘦𝘳𝘢𝘵𝘦 𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥 - 𝘊𝘰𝘯𝘴𝘪𝘥𝘦𝘳 𝘢𝘥𝘥𝘪𝘯𝘨 𝘮𝘰𝘳𝘦 𝘴𝘦𝘤𝘶𝘳𝘪𝘵𝘺 𝘧𝘦𝘢𝘵𝘶𝘳𝘦𝘴.")
        else:
            st.error("❌𝘞𝘦𝘢𝘬 𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥 - 𝘐𝘮𝘱𝘳𝘰𝘷𝘦 𝘪𝘵 𝘶𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘴𝘶𝘨𝘨𝘦𝘴𝘵𝘪𝘰𝘯𝘴 𝘣𝘦𝘭𝘰𝘸.")

        if feedback:
            st.info("💡 𝘚𝘶𝘨𝘨𝘦𝘴𝘵𝘪𝘰𝘯𝘴 𝘵𝘰 𝘪𝘮𝘱𝘳𝘰𝘷𝘦 𝘺𝘰𝘶𝘳 𝘱𝘢𝘴𝘴𝘸𝘰𝘳𝘥:")
            for tip in feedback:
                st.write(tip)
    else:
        st.error("🚨𝘗𝘭𝘦𝘢𝘴𝘦 𝘦𝘯𝘵𝘦𝘳 𝘢 𝘱𝘢𝘴𝘴𝘸𝘰𝘳𝘥 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬.")

# 🌟 Footer
st.markdown("""
---
𝘔𝘢𝘥𝘦 𝘣𝘺 **𝙎𝙪𝙗𝙝𝙖𝙣 𝙂𝙝𝙖𝙛𝙤𝙤𝙧❤️**  
""")