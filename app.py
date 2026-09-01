import streamlit as st
import pandas as pd

# Tiêu đề
st.title("🚗 Tối ưu vị trí trạm gom pin PV")

st.write(
    "Thử thay đổi giá xăng và quan sát vị trí các trạm."
)

# Thanh trượt giá xăng
gia_xang = st.slider(
    "Giá xăng (đồng/lít)",
    min_value=10000,
    max_value=40000,
    value=20000,
    step=1000
)

st.write(f"⛽ Giá xăng hiện tại: **{gia_xang:,} đồng/lít**")


# Giả lập vị trí trạm
if gia_xang < 25000:

    tram = pd.DataFrame({
        "lat": [10.03, 10.82],
        "lon": [105.78, 106.63]
    })

else:

    tram = pd.DataFrame({
        "lat": [10.76, 11.94],
        "lon": [106.68, 108.45]
    })


# Hiển thị bản đồ
st.subheader("📍 Vị trí các trạm gom pin PV")

st.map(tram)