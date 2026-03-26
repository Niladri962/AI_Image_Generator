import streamlit as st
from diffusers import AutoPipelineForText2Image
import torch

st.set_page_config(page_title="AI Image Generator")

@st.cache_resource
def load_model():
    pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sd-turbo")

    pipe = pipe.to("cpu")  # ⚠️ IMPORTANT
    return pipe

pipe = load_model()

st.title("🖼️ AI Image Generator (Hugging Face)")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating..."):
            image = pipe(
                prompt,
                num_inference_steps=1,
                guidance_scale=0.0
            ).images[0]

            st.image(image, caption=prompt)
    else:
        st.warning("Please enter a prompt")