import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.firebase_manager import savedata, getdatapath

# 初始化假数据
FAKE_DATA = [
    {"user_id": "u001", "comment": "這是一條假留言", "time": "2025-01-01 12:00", "status": "normal"},
    {"user_id": "u002", "comment": "第二條測試", "time": "2025-01-01 12:10", "status": "reported"}
]

# 写入假数据到 firebase（只需首次或有按钮可以重复写入）
if st.button("上传假数据"):
    savedata('comments', FAKE_DATA)
    st.success("已上传假数据到 Firebase DB 下 comments 路徑。")

st.header("留言数据展示")
comments = getdatapath('comments')
st.table(comments)
