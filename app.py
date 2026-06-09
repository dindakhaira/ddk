import streamlit as st

# Setup halaman utama
st.set_page_config(page_title="Portofolio Dinda", page_icon="✨", layout="centered")

# Header Utama
st.title("Halo, Saya Dinda Dwi Khairani 👋")
st.subheader("Mahasiswa Rekayasa Sistem Elektronika")

st.write("---")

# Bagian Tentang Saya
st.header("About Me 👩‍💻")
st.write("""
Saya adalah seorang mahasiswa teknik di Politeknik Caltex Riau yang berfokus pada bidang 
*embedded systems*, pemrograman mikrokontroler, dan otomasi elektronik. Saya senang 
mengembangkan solusi praktis berbasis teknologi untuk mempermudah pekerjaan manusia.
""")

st.write("---")

# Bagian Keahlian & Proyek
st.header("Skills & Projects 🚀")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛠️ Technical Skills")
    st.write("- Python & C/C++ (Arduino/ATmega328P)")
    st.write("- Circuit Design & Simulation (Proteus, Wokwi)")
    st.write("- Internet of Things (IoT) Development")

with col2:
    st.markdown("### 📁 Featured Projects")
    st.write("- **Automatic PCB Etching Machine**")
    st.write("- **LumiSense Sensor Dashboard**")
    st.write("- **PKM ISYARASA Digital Platform**")

st.write("---")
st.caption("Dikembangkan dengan menggunakan Streamlit & Python")
