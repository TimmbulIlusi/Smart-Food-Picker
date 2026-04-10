import streamlit as st

st.title("Smart Food Picker 🥗")

# Input user
nutrisi = st.selectbox(
    "Pilih Kebutuhan Nutrisi:",
    ["Protein", "Karbohidrat", "Vitamin", "Lemak Sehat", "Serat"]
)

budget = st.number_input("Masukkan Budget (Rp):", min_value=0)

if st.button("Dapatkan Rekomendasi"):

    if budget < 5000:
        st.error("❌ Budget terlalu kecil! Tidak cukup untuk membeli bahan makanan, minimal goceng lah")
    
    else:
        st.info("🔍 Menganalisis kebutuhan nutrisi dan budget Anda...")
        st.success("💡 Pilihan yang tersedia untuk Anda:")

        rekomendasi_utama = ""

        # ================= PROTEIN =================
        if nutrisi == "Protein":

            if budget >= 5000:
                st.write("🥢 Tempe / Tahu (Rp5.000 / ±250 gram)")
                rekomendasi_utama = "Tempe / Tahu"

            if budget >= 15000:
                st.write("🥚 Telur (Rp15.000 / ±8 butir)")
                rekomendasi_utama = "Telur"

            if budget >= 40000:
                st.write("🍗 Daging Ayam (Rp40.000 / ±1 kg)")
                rekomendasi_utama = "Daging Ayam"

            if budget >= 80000:
                st.write("🥩 Daging Sapi / 🐟 Salmon (Rp80.000 / ±1 kg)")
                rekomendasi_utama = "Daging Sapi / Salmon"

        # ================= KARBO =================
        elif nutrisi == "Karbohidrat":

            if budget >= 5000:
                st.write("🍚 Nasi Putih (Rp5.000 / ±1 porsi)")
                rekomendasi_utama = "Nasi Putih"

            if budget >= 12000:
                st.write("🥔 Kentang / Singkong (Rp12.000 / ±500 gram)")
                rekomendasi_utama = "Kentang / Singkong"

            if budget >= 25000:
                st.write("🍞 Roti Gandum / Oat (Rp25.000 / ±500 gram)")
                rekomendasi_utama = "Roti Gandum / Oat"

            if budget >= 60000:
                st.write("🌾 Quinoa (Rp60.000 / ±500 gram)")
                rekomendasi_utama = "Quinoa"

        # ================= VITAMIN =================
        elif nutrisi == "Vitamin":

            if budget >= 5000:
                st.write("🍌 Pisang / Pepaya (Rp5.000 / ±300 gram)")
                rekomendasi_utama = "Pisang / Pepaya"

            if budget >= 15000:
                st.write("🍊 Jeruk / 🥕 Wortel (Rp15.000 / ±500 gram)")
                rekomendasi_utama = "Jeruk / Wortel"

            if budget >= 30000:
                st.write("🍎 Apel / 🥭 Mangga (Rp30.000 / ±500 gram)")
                rekomendasi_utama = "Apel / Mangga"

            if budget >= 70000:
                st.write("🥑 Alpukat / 🫐 Blueberry (Rp70.000 / ±250–500 gram)")
                rekomendasi_utama = "Alpukat / Blueberry"

        # ================= LEMAK =================
        elif nutrisi == "Lemak Sehat":

            if budget >= 5000:
                st.write("🥜 Kacang Tanah (Rp5.000 / ±200 gram)")
                rekomendasi_utama = "Kacang Tanah"

            if budget >= 20000:
                st.write("🥚 Telur (Rp20.000 / ±10–12 butir)")
                rekomendasi_utama = "Telur"

            if budget >= 50000:
                st.write("🥑 Alpukat (Rp50.000 / ±500 gram)")
                rekomendasi_utama = "Alpukat"

            if budget >= 90000:
                st.write("🐟 Salmon / Almond (Rp90.000 / ±250–500 gram)")
                rekomendasi_utama = "Salmon / Almond"

        # ================= SERAT =================
        elif nutrisi == "Serat":

            if budget >= 5000:
                st.write("🥬 Kangkung / Bayam (Rp5.000 / ±1 ikat)")
                rekomendasi_utama = "Kangkung / Bayam"

            if budget >= 15000:
                st.write("🥕 Wortel / Kol (Rp15.000 / ±500 gram)")
                rekomendasi_utama = "Wortel / Kol"

            if budget >= 30000:
                st.write("🥦 Brokoli / 🌽 Jagung (Rp30.000 / ±500 gram)")
                rekomendasi_utama = "Brokoli / Jagung"

            if budget >= 70000:
                st.write("🌱 Chia Seed / Almond (Rp70.000 / ±250 gram)")
                rekomendasi_utama = "Chia Seed / Almond"

        # ⭐ REKOMENDASI UTAMA
        st.markdown("---")
        st.success(f"⭐ Rekomendasi Utama: {rekomendasi_utama}")
        st.write("👉 Dipilih untuk memaksimalkan budget Anda.")

        st.info("📊 Catatan: Harga dan berat adalah estimasi rata-rata pasar.")