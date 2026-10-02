from gtts import gTTS
from deep_translator import MyMemoryTranslator
import gradio as gr

def voice_buddy(text):
    # Roman Urdu / English to German B2
    german = MyMemoryTranslator(source='en-US', target='de-DE').translate(text)
    
    # German Voice
    tts = gTTS(text=german, lang='de')
    tts.save("german.mp3")
    
    return german, "german.mp3"

# Interface
gr.Interface(
    fn=voice_buddy,
    inputs=gr.Textbox(label="English / Roman Urdu likho", placeholder="Mujhe German seekhni hai"),
    outputs=[
        gr.Textbox(label="German B2 Translation"),
        gr.Audio(label="Suno - German Awaz")
    ],
    title="🇩🇪 B2 Voice Buddy - By Arbab Khan - Gujranwala",
    description="Gujranwala se Germany tak! AI Translator with Voice"
).launch()
