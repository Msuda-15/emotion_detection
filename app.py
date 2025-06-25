# 🎙️ Streamlit App for Emotion Classification from Speech

import streamlit as st
import numpy as np
import librosa
from keras.models import load_model
import soundfile as sf

# Load your trained model
model = load_model("best_model.h5")

# Define emotion labels (same order used during training)
emotion_labels = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

# Define a function to extract MFCC features
def extract_features(file_path, max_pad_len=174):
    try:
        audio, sr = librosa.load(file_path, sr=22050, duration=2.5, offset=0.5)
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
        if mfcc.shape[1] < max_pad_len:
            pad_width = max_pad_len - mfcc.shape[1]
            mfcc = np.pad(mfcc, ((0, 0), (0, pad_width)), mode='constant')
        else:
            mfcc = mfcc[:, :max_pad_len]
        return mfcc
    except Exception as e:
        st.error(f"Error processing audio: {e}")
        return None

# Streamlit UI Setup
st.set_page_config(page_title="🎧 Emotion Detection from Speech", layout="centered")
st.title("🎤 Emotion Detection App")
st.markdown("Upload a `.wav` file to detect the **emotion** behind the speech.")

uploaded_file = st.file_uploader("Choose a .wav file", type="wav")

if uploaded_file is not None:
    # Save temporary file
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())

    # Extract features
    features = extract_features("temp.wav")
    if features is not None:
        features = features.reshape(1, 40, 174, 1)  # Reshape to fit model input
        prediction = model.predict(features)
        predicted_label = emotion_labels[np.argmax(prediction)]

        # Play audio and show result
        st.audio("temp.wav")
        st.success(f"🤖 Predicted Emotion: **{predicted_label}**")
