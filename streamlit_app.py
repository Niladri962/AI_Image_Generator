import streamlit as st
from diffusers import DiffusionPipeline, AutoPipelineForImage2Image
import torch
from PIL import Image
import io

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="AI Image Chat", layout="centered")

# -------------------------------
# SESSION STATE (CHAT HISTORY)
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# LOAD MODELS
# -------------------------------
@st.cache_resource
def load_text2img():
    pipe = DiffusionPipeline.from_pretrained(
        "SimianLuo/LCM_Dreamshaper_v7",
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cpu")
    return pipe

@st.cache_resource
def load_img2img():
    pipe = AutoPipelineForImage2Image.from_pretrained(
        "stabilityai/sd-turbo",
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cpu")
    return pipe

pipe = load_text2img()
img2img_pipe = load_img2img()

# -------------------------------
# TITLE
# -------------------------------
st.title("🤖 AI Image Chat Generator")
st.caption("Chat-style image generation with refinement 🚀")

# -------------------------------
# DISPLAY CHAT HISTORY
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["type"] == "text":
            st.write(msg["content"])
        elif msg["type"] == "image":
            st.image(msg["content"], width=300)

            # Download button
            buf = io.BytesIO()
            msg["content"].save(buf, format="PNG")

            st.download_button(
                "📥 Download",
                data=buf.getvalue(),
                file_name="image.png",
                mime="image/png",
                key=str(id(msg))
            )

# -------------------------------
# USER INPUT
# -------------------------------
prompt = st.chat_input("Enter your prompt...")

# -------------------------------
# IMAGE GENERATION (TEXT → IMAGE)
# -------------------------------
if prompt:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "type": "text",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating image..."):
            image = pipe(
                prompt,
                num_inference_steps=4,
                guidance_scale=1.0,
                height=512,
                width=512
            ).images[0]

            st.image(image, width=300)

            # Save image in chat
            st.session_state.messages.append({
                "role": "assistant",
                "type": "image",
                "content": image
            })

# -------------------------------
# IMAGE UPLOAD + REFINE
# -------------------------------
st.divider()
st.subheader("🖼️ Upload & Refine Image")

uploaded_file = st.file_uploader("Upload image to refine", type=["png", "jpg", "jpeg"])

if uploaded_file:
    init_image = Image.open(uploaded_file).convert("RGB")
    st.image(init_image, width=300)

    refine_prompt = st.text_input("Refinement prompt")

    if st.button("✨ Refine"):
        if refine_prompt:
            with st.spinner("Refining..."):
                refined = img2img_pipe(
                    prompt=refine_prompt,
                    image=init_image,
                    strength=0.5,
                    num_inference_steps=3,
                    guidance_scale=0.0
                ).images[0]

                st.image(refined, width=300)

                st.session_state.messages.append({
                    "role": "assistant",
                    "type": "image",
                    "content": refined
                })

# -------------------------------
# CLEAR CHAT
# -------------------------------
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.success("Chat cleared!")