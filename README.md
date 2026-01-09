<div align="center">

# ✨ AI Storyteller & Illustrator

### Transform Your Ideas into Illustrated Stories with AI

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B.svg)](https://streamlit.io)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4.svg)](https://ai.google.dev/)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow.svg)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack)

</div>

---

## 📖 About The Project

**AI Storyteller & Illustrator** is a cutting-edge generative AI application that brings your creative ideas to life. Simply enter a story prompt, and watch as advanced AI models craft a unique narrative and generate stunning illustrations to match—all in seconds.

This project leverages **Google Gemini** for intelligent story generation and **HuggingFace Stable Diffusion** for high-quality image synthesis, providing a seamless creative experience through an intuitive Streamlit interface.

### 🎯 Why This Project?

- **🚀 Real-world AI Integration**: Demonstrates practical implementation of multiple AI APIs
- **🎨 Creative Automation**: Showcases the power of generative AI in creative workflows
- **💡 User-Centric Design**: Clean, responsive UI built with modern web technologies
- **🔧 Production-Ready**: Includes error handling, retry logic, and environment configuration

</div>

---

## 🌟 Features

### 🤖 **Dual AI Integration**
- **Google Gemini 1.5 Flash** for creative story generation
- **Stable Diffusion** models for high-quality image synthesis

### 📚 **Multiple Genres**
- Fantasy • Sci-Fi • Mystery • Horror • Comedy • Adventure • Cyberpunk

### 🎨 **Artistic Styles**
- Digital Art • Oil Painting • Watercolor • Anime • Realistic • 3D Render • Sketch

### ⚙️ **Advanced Features**
- ✅ Real-time API status monitoring
- ✅ Customizable AI model selection
- ✅ Retry logic for rate-limited requests
- ✅ Responsive two-column layout
- ✅ Environment-based configuration
- ✅ Error handling and user feedback

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Frontend** | Streamlit, Custom CSS |
| **AI/ML** | Google Gemini API, HuggingFace Inference API |
| **Language Models** | Gemini 1.5 Flash, Stable Diffusion v1.4/v1.5/XL |
| **Backend** | Python 3.8+ |
| **Libraries** | `google-generativeai`, `huggingface_hub`, `python-dotenv` |
| **Deployment** | Streamlit Cloud Ready |

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google Gemini API key ([Get it here](https://aistudio.google.com/app/apikey))
- HuggingFace API token ([Get it here](https://huggingface.co/settings/tokens))

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ai-storyteller.git
cd ai-storyteller
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
HUGGINGFACE_API_TOKEN=your_huggingface_token_here
```

> **⚠️ Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

---

## 🚀 Usage

### Running Locally

```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

### Using the Application

1. **Enter Your Story Idea**: Type a creative prompt in the text area
2. **Select Genre**: Choose from Fantasy, Sci-Fi, Mystery, and more
3. **Pick Art Style**: Select your preferred illustration style
4. **Generate**: Click the button and watch the magic happen!

### Example Prompts

```
🤖 "A lonely robot discovers a flower growing on Mars"
🧙 "A young wizard accidentally turns their teacher into a frog"
🚀 "The last human colony ship encounters an alien artifact"
🕵️ "A detective solves crimes using time travel"
```

---

## 📁 Project Structure

```
ai-storyteller/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in repo)
├── .gitignore            # Git ignore rules
├── test_models.py        # API testing utilities
└── README.md             # Project documentation
```

---

## 🔑 API Configuration

### Google Gemini API

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy the generated key
4. Add to `.env` as `GOOGLE_API_KEY`

### HuggingFace API

1. Go to [HuggingFace Settings](https://huggingface.co/settings/tokens)
2. Create a new **Access Token**
3. Select **Read** permissions
4. Copy the token
5. Add to `.env` as `HUGGINGFACE_API_TOKEN`

---

## 🎨 Customization

### Adding New Genres

Edit the genre list in `app.py`:

```python
genre = st.selectbox(
    "Select Genre",
    ["Fantasy", "Sci-Fi", "Your New Genre"]
)
```

### Using Different AI Models

The app supports multiple Stable Diffusion models:
- `CompVis/stable-diffusion-v1-4`
- `runwayml/stable-diffusion-v1-5`
- `stabilityai/stable-diffusion-2-1`
- `stabilityai/stable-diffusion-xl-base-1.0`

Select them from the sidebar or add custom models!

---

## 🐛 Troubleshooting

### Common Issues

**❌ "Gemini Missing" Error**
- Ensure `GOOGLE_API_KEY` is set in `.env`
- Verify the API key is valid and active

**❌ "HF Missing" Error**
- Check `HUGGINGFACE_API_TOKEN` in `.env`
- Confirm the token has read permissions

**❌ Rate Limit (429) Errors**
- The app includes automatic retry logic
- Wait a few seconds and try again
- Consider using `gemini-1.5-flash` (default) for better rate limits

**❌ Image Generation Fails**
- Some models may be rate-limited or unavailable
- Try switching to a different Stable Diffusion model
- Check HuggingFace API status

---

## 🚀 Deployment

### Streamlit Cloud

1. Push your code to GitHub (without `.env`)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repository
4. Add secrets in the dashboard:
   - `GOOGLE_API_KEY`
   - `HUGGINGFACE_API_TOKEN`
5. Deploy!

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

Aman

