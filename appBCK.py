import streamlit as st
import json
import os

DATA_FILE = "shared_content.json"
IMAGE_FILE = "shared_image.png"  # Foto subida

def load_content():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return {"song": "", "tiktok": "", "message": ""}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"song": "", "tiktok": "", "message": ""}

def save_content(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ---- CONFIG ----
st.set_page_config(page_title="Para Ti 💛", page_icon="💛", layout="centered")

# Estilo CSS suave
st.markdown("""
    <style>
        .block {
            background: #ffffffCC;
            padding: 18px;
            border-radius: 14px;
            margin-bottom: 20px;
            border: 1px solid #f2d6e6;
        }
        .polaroid {
            background: white;
            padding: 12px 12px 25px 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
            border-radius: 6px;
            text-align: center;
        }
        .footer-text {
            color: #b78fa9;
            font-size: 14px;
            margin-top: -10px;
        }
        .title {
            font-size: 36px;
            font-weight: 700;
            color: #d088b5;
            text-align: center;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #c79ab5;
            margin-top: -10px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Título bonito
st.markdown('<div class="title">💛 Para Ti</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Un pequeño rincón que actualizo pensando en ti.</div>', unsafe_allow_html=True)

content = load_content()

# --- Editor ---
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)

    song = st.text_input("🎵 Canción (link)", value=content.get("song", ""))
    tiktok = st.text_input("🎥 TikTok (link)", value=content.get("tiktok", ""))
    message = st.text_area("💬 Mensaje", value=content.get("message", ""))

    uploaded_file = st.file_uploader("📸 Subir foto", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        with open(IMAGE_FILE, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Foto subida 💛")

    if st.button("Guardar cambios"):
        new_content = {
            "song": song,
            "tiktok": tiktok,
            "message": message
        }
        save_content(new_content)
        st.success("Guardado 💛")
        st.experimental_rerun()

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### ❤️ Contenido actual")

# --- Mostrar contenido ---
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)

    if content.get("song"):
        st.markdown(f"**🎵 Canción:** {content['song']}")

    if content.get("tiktok"):
        st.markdown(f"**🎥 TikTok:** {content['tiktok']}")

    if content.get("message"):
        st.markdown("**💬 Mensaje:**")
        st.write(content['message'])

    if os.path.exists(IMAGE_FILE):
        st.markdown('<div class="polaroid">', unsafe_allow_html=True)
        st.image(IMAGE_FILE, use_column_width=True)
        st.markdown('<div class="footer-text">📸 Foto para ti</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
