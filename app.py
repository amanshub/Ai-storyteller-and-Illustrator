import streamlit as st
import os
import time
from dotenv import load_dotenv
import google.generativeai as genai
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

# Configure API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# Initialize Gemini
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

def generate_story(prompt, genre, model_name='gemini-1.5-flash'):
    """Generates a story using Google Gemini with retry logic."""
    for attempt in range(3):
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(
                f"Write a creative short story in the {genre} genre based on this prompt: '{prompt}'. "
                "Keep it under 300 words. Make it engaging and descriptive."
            )
            return response.text
        except Exception as e:
            if "429" in str(e) and attempt < 2:
                time.sleep(2)  # Wait 2 seconds before retrying
                continue
            return f"Error generating story: {str(e)}"

def generate_image(prompt, style, model_name="CompVis/stable-diffusion-v1-4"):
    """Generates an image using HuggingFace InferenceClient."""
    client = InferenceClient(token=HUGGINGFACE_API_TOKEN)
    
    # Enhance prompt
    enhanced_prompt = f"{prompt}, {style} style, high quality, detailed, 8k resolution"
    
    try:
        # Use the client to generate image
        image = client.text_to_image(enhanced_prompt, model=model_name)
        
        # Convert PIL Image to bytes for Streamlit
        import io
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        return img_byte_arr.getvalue()
    except Exception as e:
        return f"Error: {str(e)}"

# Setup Page Configuration
st.set_page_config(
    page_title="AI Storyteller",
    page_icon="✨",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        padding: 10px;
    }
    .story-text {
        font-family: 'Georgia', serif;
        font-size: 18px;
        line-height: 1.6;
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #ff4b4b;
    }
    .stSpinner {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # API Status Indicators
    col1, col2 = st.columns(2)
    with col1:
        if GOOGLE_API_KEY:
            st.success("Gemini Active")
        else:
            st.error("Gemini Missing")
    with col2:
        if HUGGINGFACE_API_TOKEN:
            st.success("HF Active")
        else:
            st.error("HF Missing")
            
    st.markdown("---")
    
    # Model Selection for Debugging
    try:
        if GOOGLE_API_KEY:
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            # Clean up model names (remove 'models/')
            model_options = [m.replace('models/', '') for m in available_models]
            
            # Filter out experimental models to avoid 429 errors
            model_options = [m for m in model_options if "exp" not in m and "experimental" not in m]
            
            # Prioritize gemini-1.5-flash
            if "gemini-1.5-flash" in model_options:
                model_options.insert(0, model_options.pop(model_options.index("gemini-1.5-flash")))
            
            selected_model = st.selectbox("Select Text Model", model_options, index=0 if model_options else 0)
        else:
            selected_model = "gemini-1.5-flash"
    except Exception as e:
        st.error(f"Could not list models: {e}")
        selected_model = "gemini-1.5-flash"

    # Image Model Selection
    model_options_img = [
        "CompVis/stable-diffusion-v1-4",
        "runwayml/stable-diffusion-v1-5",
        "stabilityai/stable-diffusion-2-1",
        "stabilityai/stable-diffusion-xl-base-1.0",
        "prompthero/openjourney-v4",
        "Custom..."
    ]
    image_model_selection = st.selectbox("Select Image Model", model_options_img)
    
    if image_model_selection == "Custom...":
        image_model = st.text_input("Enter HuggingFace Model ID", "stabilityai/sd-turbo")
    else:
        image_model = image_model_selection

    genre = st.selectbox(
        "Select Genre",
        ["Fantasy", "Sci-Fi", "Mystery", "Horror", "Comedy", "Adventure", "Cyberpunk"]
    )
    
    style = st.selectbox(
        "Illustration Style",
        ["Digital Art", "Oil Painting", "Watercolor", "Cyberpunk", "Anime", "Realistic", "3D Render", "Sketch"]
    )
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.info(
        "- Be specific with your prompt.\n"
        "- Try different styles for unique looks.\n"
        "- Ensure API keys are in .env"
    )

# Main Content
st.title("✨ AI Storyteller & Illustrator")
st.markdown("### Turn your ideas into illustrated stories in seconds!")

prompt = st.text_area("Enter your story idea...", height=100, placeholder="Example: A lonely robot finds a flower on Mars...")

if st.button("Generate Story & Art", type="primary"):
    if not prompt:
        st.warning("Please enter a story idea first!")
    elif not GOOGLE_API_KEY or not HUGGINGFACE_API_TOKEN:
        st.error("Please set both GOOGLE_API_KEY and HUGGINGFACE_API_TOKEN in the .env file.")
    else:
        # Create two columns for layout
        col_story, col_art = st.columns([1, 1])
        
        with col_story:
            with st.spinner("✍️ Weaving your story..."):
                story_text = generate_story(prompt, genre, selected_model)
                st.subheader(f"📖 The {genre} Story")
                st.markdown(f'<div class="story-text">{story_text}</div>', unsafe_allow_html=True)
        
        with col_art:
            with st.spinner("🎨 Painting the scene..."):
                # Generate a visual prompt from the story summary (simplified for now, using user prompt)
                image_bytes = generate_image(f"{prompt} set in a {genre} world", style, image_model)
                
                st.subheader("🎨 Illustration")
                if isinstance(image_bytes, bytes):
                    st.image(image_bytes, caption=f"Generated in {style} style", use_column_width=True)
                else:
                    st.error(f"Failed to generate image: {image_bytes}")
