# End-To-End-Medical-Chatbot
# 🧠 Voice & Vision Multimodal AI - Doctor's Assistant

This project combines **vision analysis** and **voice input** to create a smart assistant that can:
- Analyze face images (e.g., for acne or other skin issues) using the **GROQ multimodal model** (LLaMA 3.2 90B Vision).
- Record patient voice input using Python and convert it to MP3 format.

---

## 🛠️ Features

- **Multimodal Vision Analysis**: Upload an image and get insights using natural language queries powered by GROQ API.
- **Voice Recorder Module**: Record patient voice (e.g., symptoms or descriptions) and save it as MP3 using `sounddevice` and `pydub`.
- **Clean and Modular Python Code** for both vision and audio processing.

---

## 🧩 File Structure


---

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/voice-vision-doctor.git
cd voice-vision-doctor
pip install pipenv
pipenv install
GROQ_API_KEY=your_groq_api_key_here
python brain_of_the_doctor.py
python voice_of_the_patient.py
query = "Is there something wrong with my face?"


