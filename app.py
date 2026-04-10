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
                st.write("👉 Protein nabati, tinggi serat dan zat besi.")
                rekomendasi_utama = "Tempe / Tahu"

            if budget >= 15000:
                st.write("🥚 Telur (Rp15.000 / ±10 butir)")
                st.write("👉 Protein lengkap, mengandung vitamin B12.")
                rekomendasi_utama = "Telur"

            if budget >= 40000:
                st.write("🍗 Daging Ayam (Rp40.000 / ±1 kg)")
                st.write("👉 Protein hewani, rendah lemak jika tanpa kulit.")
                rekomendasi_utama = "Daging Ayam"

            if budget >= 80000:
                st.write("🥩 Daging Sapi / 🐟 Salmon (Rp80.000 / ±1 kg)")
                st.write("👉 Protein tinggi + zat besi / omega-3.")
                rekomendasi_utama = "Daging Sapi / Salmon"

        # ================= KARBO =================
        elif nutrisi == "Karbohidrat":

            if budget >= 5000:
                st.write("🍚 Nasi Putih (Rp5.000 / ±1 porsi)")
                st.write("👉 Sumber energi utama, mudah dicerna.")
                rekomendasi_utama = "Nasi Putih"

            if budget >= 12000:
                st.write("🥔 Kentang / Singkong (Rp12.000 / ±500 gram)")
                st.write("👉 Karbohidrat kompleks + serat.")
                rekomendasi_utama = "Kentang / Singkong"

            if budget >= 25000:
                st.write("🍞 Roti Gandum / Oat (Rp25.000 / ±500 gram)")
                st.write("👉 Karbo sehat, tinggi serat.")
                rekomendasi_utama = "Roti Gandum / Oat"

            if budget >= 60000:
                st.write("🌾 Quinoa (Rp60.000 / ±500 gram)")
                st.write("👉 Karbo premium + protein tambahan.")
                rekomendasi_utama = "Quinoa"

        # ================= VITAMIN =================
        elif nutrisi == "Vitamin":

            if budget >= 5000:
                st.write("🍌 Pisang / Pepaya (Rp5.000 / ±300 gram)")
                st.write("👉 Kaya vitamin dan serat.")
                rekomendasi_utama = "Pisang / Pepaya"

            if budget >= 15000:
                st.write("🍊 Jeruk / 🥕 Wortel (Rp15.000 / ±500 gram)")
                st.write("👉 Vitamin C dan A untuk imun.")
                rekomendasi_utama = "Jeruk / Wortel"

            if budget >= 30000:
                st.write("🍎 Apel / 🥭 Mangga (Rp30.000 / ±500 gram)")
                st.write("👉 Antioksidan dan vitamin tinggi.")
                rekomendasi_utama = "Apel / Mangga"

            if budget >= 70000:
                st.write("🥑 Alpukat / 🫐 Blueberry (Rp70.000 / ±250–500 gram)")
                st.write("👉 Nutrisi tinggi + lemak sehat.")
                rekomendasi_utama = "Alpukat / Blueberry"

        # ================= LEMAK =================
        elif nutrisi == "Lemak Sehat":

            if budget >= 5000:
                st.write("🥜 Kacang Tanah (Rp5.000 / ±200 gram)")
                st.write("👉 Lemak sehat + protein.")
                rekomendasi_utama = "Kacang Tanah"

            if budget >= 20000:
                st.write("🥚 Telur (Rp20.000 / ±10–12 butir)")
                st.write("👉 Lemak + protein seimbang.")
                rekomendasi_utama = "Telur"

            if budget >= 50000:
                st.write("🥑 Alpukat (Rp50.000 / ±500 gram)")
                st.write("👉 Lemak tak jenuh baik untuk jantung.")
                rekomendasi_utama = "Alpukat"

            if budget >= 90000:
                st.write("🐟 Salmon / Almond (Rp90.000 / ±250–500 gram)")
                st.write("👉 Omega-3 dan lemak sehat premium.")
                rekomendasi_utama = "Salmon / Almond"

        # ================= SERAT =================
        elif nutrisi == "Serat":

            if budget >= 5000:
                st.write("🥬 Kangkung / Bayam (Rp5.000 / ±1 ikat)")
                st.write("👉 Serat tinggi untuk pencernaan.")
                rekomendasi_utama = "Kangkung / Bayam"

            if budget >= 15000:
                st.write("🥕 Wortel / Kol (Rp15.000 / ±500 gram)")
                st.write("👉 Serat + vitamin.")
                rekomendasi_utama = "Wortel / Kol"

            if budget >= 30000:
                st.write("🥦 Brokoli / 🌽 Jagung (Rp30.000 / ±500 gram)")
                st.write("👉 Serat tinggi + antioksidan.")
                rekomendasi_utama = "Brokoli / Jagung"

            if budget >= 70000:
                st.write("🌱 Chia Seed / Almond (Rp70.000 / ±250 gram)")
                st.write("👉 Serat tinggi + nutrisi tambahan.")
                rekomendasi_utama = "Chia Seed / Almond"

        # ⭐ REKOMENDASI UTAMA
        st.markdown("---")
        st.success(f"⭐ Rekomendasi Utama: {rekomendasi_utama}")
        st.write("👉 Dipilih untuk memaksimalkan budget Anda.")

        st.info("📊 Catatan: Harga dan berat adalah estimasi rata-rata pasar.")
