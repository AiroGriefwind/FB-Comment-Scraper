import streamlit as st
from utils.firebase_manager import save_data, get_data
from utils.firebase_manager import firebase_manager as fm

fm.initialize_firebase()

FAKE_DATA = [
    {"user_id": "u001", "comment": "這是一條假留言", "time": "2025-01-01 12:00", "status": "normal"},
    {"user_id": "u002", "comment": "第二條測試", "time": "2025-01-01 12:10", "status": "reported"}
]

def render_comment_tab():
    if st.button("上传假数据"):
        save_data('comments', FAKE_DATA)
        st.success("已上传假数据到 Firebase DB 下 comments 路徑。")

    st.header("留言数据展示")
    comments = get_data('comments')
    st.table(comments)
