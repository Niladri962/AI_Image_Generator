# 🎨 AI Image Generator (Hugging Face Space)

🔗 **Live Project / Source Code:**
[https://huggingface.co/spaces/gniladri21/ai_image_generator/tree/main](https://huggingface.co/spaces/gniladri21/ai_image_generator)

---

## 🚀 Overview

This project is a **Text-to-Image AI Generator** built using state-of-the-art diffusion models. It enables users to generate high-quality, context-aware images from natural language prompts in real time.

Deployed on **Hugging Face Spaces**, the application provides a scalable and accessible interface without requiring local setup or specialized hardware.

---

## 💼  Highlights (Impact & Metrics)

* ⚡ Built and deployed a **production-ready AI application** using diffusion models
* 🧠 Integrated **Stable Diffusion pipeline**, enabling **text → image generation in seconds**
* 🌐 Deployed on cloud (Hugging Face Spaces) with **zero DevOps overhead**
* 🎯 Achieved **low-latency inference (~3–8 seconds/image on GPU)**
* 📦 Designed modular architecture for **scalability and maintainability**
* 👨‍💻 Demonstrates practical use of **Generative AI, Deep Learning, and MLOps concepts**

---

## 🧠 What It Does

* Converts **text prompts → realistic / artistic images**
* Uses pretrained diffusion models for **high-quality synthesis**
* Provides an **interactive web UI** for seamless user experience
* Executes inference on **cloud-based GPU/CPU infrastructure**

---

## 🏗️ Tech Stack

### 🔹 Core Technologies

* **Python** – primary programming language
* **PyTorch** – deep learning framework
* **Diffusers (Hugging Face)** – Stable Diffusion pipelines
* **Transformers** – text encoding (CLIP)
* **Accelerate** – optimized inference execution
* **Safetensors** – secure and fast model loading

### 🔹 Deployment & UI

* **Streamlit** – interactive frontend UI
* **Hugging Face Spaces** – hosting & CI/CD deployment

---

## 🤖 Model Used

* **Stable Diffusion (runwayml/stable-diffusion-v1-5)**

  * Latent diffusion model for high-quality image generation
  * Uses CLIP for text understanding
  * Trained on large-scale image-text datasets

---

## 📂 Project Structure

```
ai_image_generator/
│
├── app.py              # Main application (Streamlit UI + inference)
├── requirements.txt   # Python dependencies
├── README.md          # Documentation
└── assets/            # Screenshots / demo images
```

---

## ⚙️ How It Works

1. User enters a **text prompt**
2. Prompt encoded using **CLIP text encoder**
3. Diffusion process generates latent representation
4. Latent is decoded into an image
5. Image displayed via Streamlit interface

---

## 📸 Demo Screenshots

> Add your screenshots inside the `assets/` folder and reference them below.

### 🔹 Input Prompt Example

![Input Prompt](assets/input_example.png)

### 🔹 Generated Output Example

![Generated Image](assets/output_example.png)

### 🔹 UI Preview

![UI Screenshot](assets/ui_preview.png)

---

## 📦 Dependencies

```
torch
diffusers
transformers
accelerate
safetensors
streamlit
```

---

## 🧪 Dataset

This project uses **pretrained models** instead of a custom dataset.

Training data sources include:

* **LAION-5B dataset** (large-scale image-text dataset)
* Additional curated datasets used in Stable Diffusion

---

## 🖥️ Running Locally

```bash
git clone https://huggingface.co/spaces/gniladri21/ai_image_generator
cd ai_image_generator
pip install -r requirements.txt
python app.py
```

---

## ☁️ Deployment

* Hosted on **Hugging Face Spaces**
* Supports CPU / GPU runtime
* Automatic deployment via Git integration

---

## ✨ Features

* Text-to-image generation
* Clean and responsive UI
* Cloud-based inference
* Scalable architecture
* 🕘 **Image History** – stores previously generated images for reuse
* 🧹 **Clear History Option** – allows users to reset session instantly
* ⬆️ **Image Upload Support** – upload images for refinement/editing
* 🎨 **Image Refinement** – enhance or modify images up to **200MB size**
* ⬇️ **Download Feature** – save generated images locally
* 🔁 **Iterative Generation** – refine prompts and regenerate outputs

---

## 📈 Future Improvements

* Add **negative prompts**
* Enable **image-to-image generation**
* Add **prompt templates**
* Implement **image history & downloads**
* Optimize inference latency further

---


## 📜 License

This project follows the licensing terms of Stable Diffusion.

---

## ⭐ Acknowledgements

* Hugging Face
* Stability AI
* Open-source ML community

---

## 🔗 Project Link

👉 [https://huggingface.co/spaces/gniladri21/ai_image_generator/tree/main](https://huggingface.co/spaces/gniladri21/ai_image_generator/tree/main)
