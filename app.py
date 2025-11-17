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

# ---- CSS ----
st.markdown("""
    <style>
        .block {
            background: #ffffffCC;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 22px;
            border: 1px solid #f1d4e8;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
        }
        .polaroid {
            background: white;
            padding: 12px 12px 25px 12px;
            box-shadow: 0px 5px 16px rgba(0,0,0,0.18);
            border-radius: 6px;
            text-align: center;
            margin-bottom: 15px;
        }
        .photo-caption {
            color: #b78fa9;
            font-size: 14px;
            margin-top: -10px;
        }
        .title {
            font-size: 40px;
            font-weight: 700;
            color: #d088b5;
            text-align: center;
            margin-bottom: 2px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #c79ab5;
            margin-top: 0px;
            margin-bottom: 30px;
        }
        .divider-heart {
            text-align: center;
            font-size: 22px;
            color: #e3b3d4;
            margin: 18px 0px;
        }
    </style>
""", unsafe_allow_html=True)


# ---- HEADER ----
st.markdown('<div class="title">💛 Para Ti</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Un pequeño rincón que actualizo pensando en ti.</div>', unsafe_allow_html=True)

content = load_content()

# -------------------------------------------------------------
# 🌟 PRIMERA PARTE: EL CONTENIDO (LO QUE VE ELLA)
# -------------------------------------------------------------
st.markdown('<div class="divider-heart">⋆｡°✩💛✩°｡⋆</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)


    # Canción
    if content.get("song"):
        st.markdown("### 🎵 Canción del día")
        st.markdown(f"{content['song']}")

    # TikTok
    if content.get("tiktok"):
        st.markdown("### 🎥 TikTok que me recordó a ti")
        st.markdown(f"{content['tiktok']}")

    # Mensaje
    if content.get("message"):
        st.markdown("### 💬 Mensaje para ti")
        st.markdown(f"{content['message']}")
        
            # Foto principal si existe
    if os.path.exists(IMAGE_FILE):
        st.markdown('<div class="polaroid">', unsafe_allow_html=True)
        st.image(IMAGE_FILE, use_column_width=True)
        st.markdown('<div class="photo-caption">📸 Un recuerdo bonito</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# 🌟 SEGUNDA PARTE: EDICIÓN (OCULTA EN UN ACORDEÓN)
# -------------------------------------------------------------
st.markdown('<div class="divider-heart">♡</div>', unsafe_allow_html=True)

with st.expander("✏️ Editar contenido (solo para nosotros dos)"):
    st.markdown('<div class="block">', unsafe_allow_html=True)

    # Campos de edición
    song = st.text_input("🎵 Canción (link)", value=content.get("song", ""))
    tiktok = st.text_input("🎥 TikTok (link)", value=content.get("tiktok", ""))
    message = st.text_area("💬 Mensaje", value=content.get("message", ""))

    # Subir foto
    uploaded_file = st.file_uploader("📸 Subir foto", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        with open(IMAGE_FILE, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Foto subida 💛")

    # Guardar cambios
    if st.button("Guardar cambios"):
        new_content = {
            "song": song,
            "tiktok": tiktok,
            "message": message
        }
        save_content(new_content)
        st.success("Guardado 💛")
    

    st.markdown('</div>', unsafe_allow_html=True)
