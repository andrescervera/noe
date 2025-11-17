import streamlit as st
import json
import os

DATA_FILE = "shared_content.json"
IMAGE_FILE = "shared_image.png"  # Foto subida

def load_content():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return {"song": "", "tiktok": "", "message": "", "photo_caption": ""}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"song": "", "tiktok": "", "message": "", "photo_caption": ""}

def save_content(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ---- CONFIG ----
st.set_page_config(page_title="Boulevard de sueños rotos 💛", page_icon="Boulevard de sueños rotos💛", layout="centered")

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
            margin-top: -8px;
            text-align: center;
            font-style: italic;
        }
        .title {
            font-size: 42px;
            font-weight: 700;
            color: #d088b5;
            text-align: center;
            margin-bottom: 4px;
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
st.markdown('<div class="title">Boulevard de sueños rotos 💛</div>', unsafe_allow_html=True)

content = load_content()

# -------------------------------------------------------------
# 🌟 PARTE PRINCIPAL (LO QUE VE ELLA)
# -------------------------------------------------------------
with st.container():
    st.markdown("""
<hr style='border: 0; height: 1px; background: linear-gradient(to right, #ffffff00, #fcb1d1, #ffffff00); margin: 30px 0;'/>
""", unsafe_allow_html=True)

    # Canción
    if content.get("song"):
        st.markdown("### 🎵 Una canción")
        st.markdown(f"{content['song']}")

    # TikTok
    if content.get("tiktok"):
        st.markdown("### 🎥 Un TikTok")
        st.markdown(f"{content['tiktok']}")

    # Mensaje
    if content.get("message"):
        st.markdown("### 💬 Un mensaje")
        st.markdown(f"{content['message']}")

    # Foto con caption
    if os.path.exists(IMAGE_FILE):
        st.markdown('<div class="polaroid">', unsafe_allow_html=True)
        st.image(IMAGE_FILE, use_column_width=True)

        if content.get("photo_caption"):
            st.markdown(f'<div class="photo-caption">{content["photo_caption"]}</div>',
                        unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------------------------------
# ✏️ PARTE OCULTA (EDICIÓN)
# -------------------------------------------------------------
with st.container():
    st.markdown("""
<hr style='border: 0; height: 1px; background: linear-gradient(to right, #ffffff00, #fcb1d1, #ffffff00); margin: 30px 0;'/>
""", unsafe_allow_html=True)

with st.expander("✏️ Editar contenido"):
    st.markdown('<div class="block">', unsafe_allow_html=True)

    song = st.text_input("🎵 Canción (link)", value=content.get("song", ""))
    tiktok = st.text_input("🎥 TikTok (link)", value=content.get("tiktok", ""))
    message = st.text_area("💬 Mensaje", value=content.get("message", ""))

    # Pie de foto
    photo_caption = st.text_input("📝 Pie de foto", value=content.get("photo_caption", ""))

    # Subir foto
    uploaded_file = st.file_uploader("📸 Subir foto", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        with open(IMAGE_FILE, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Foto subida")

    # Guardar cambios
    if st.button("Guardar cambios"):
        new_content = {
            "song": song,
            "tiktok": tiktok,
            "message": message,
            "photo_caption": photo_caption
        }
        save_content(new_content)
        st.success("Guardado. Refresca la página para ver los cambios :)")

    st.markdown('</div>', unsafe_allow_html=True)
