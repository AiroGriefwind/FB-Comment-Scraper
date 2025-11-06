import streamlit as st
import sys
import os

# 保证 utils、tabs 可被导入
sys.path.append(os.path.join(os.path.dirname(__file__), "utils"))
sys.path.append(os.path.join(os.path.dirname(__file__), "tabs"))

# 导入自定义 tab 页面函数
from tabs.comment_report_UI import render_comment_tab  # 假设你把主逻辑封装在 render_comment_tab()

def main():
    st.set_page_config(page_title="FB控評工具", layout="wide")
    st.title("FB控評工具 Demo")

    tab1, = st.tabs(["FB评论监控"])
    with tab1:
        render_comment_tab()
        # 你可以后续添加更多tab

if __name__ == "__main__":
    main()
