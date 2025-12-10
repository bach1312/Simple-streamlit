import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Phân tích dữ liệu ")
uploaded_file = st.file_uploader("Chọn file Excel (có cột 'Điểm số')", type=["xlsx"])

def calculate_average(scores):
    return sum(scores) / len(scores)

def percentage_distribution(scores):    
    bins = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0, "<60": 0}
    for score in scores:
        if score >= 90:
            bins["90-100"] += 1
        elif score >= 80:
            bins["80-89"] += 1
        elif score >= 70:
            bins["70-79"] += 1
        elif score >= 60:
            bins["60-69"] += 1
        else:
            bins["<60"] += 1
    return bins

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    scores = df["Điểm số"].dropna().astype(float).tolist()
    
    st.write("Tổng số học sinh:", len(scores))
    st.write("Điểm trung bình:", round(calculate_average(scores), 2))
    
    # Gọi hàm một lần và lưu vào biến
    dist = percentage_distribution(scores)
    labels = list(dist.keys())
    values = list(dist.values())
    
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
else:
    st.warning("Vui lòng tải lên file Excel!")