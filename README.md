# 🎧 Emotion Detection from Speech using Deep Learning

This project performs emotion classification from speech audio using MFCC feature extraction and a Convolutional Neural Network (CNN). It includes an end-to-end pipeline to train a model and predict emotions via a Streamlit web app.

---

## 📂 Project Structure
emotion_detection/
├── app.py # Streamlit app to run emotion detection
├── emotion_model.ipynb # Jupyter notebook for training the model
├── organize_audio_by_emotion.py # Script to sort .wav files into emotion folders
├── best_model.h5 # (local only) Trained CNN model
├── requirements.txt # Dependencies for training + app
├── data/ # Folder with subfolders per emotion (happy/, sad/, etc.)
└── .gitignore # Ignore venv, model, and audio files


---

## 🔍 Dataset

This project uses the [RAVDESS Dataset](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio), containing `.wav` files labeled with emotions like:

- Angry 😠
- Happy 😀
- Sad 😢
- Neutral 😐
- Fearful 😨
- Disgust 😒
- Surprised 😮
- Calm 😌

---

## 🏋️‍♀️ Training Instructions

1. Extract audio files into `Audio_Speech_Actors_01-24/` and/or `Audio_Song_Actors_01-24/`
2. Run the script to sort `.wav` files:

```bash
python organize_audio_by_emotion.py

This will populate:
 data/happy/, data/sad/, ...(in bash)

3. Open emotion_model.ipynb in Jupyter or VS Code.

4. Run all cells to:
-Extract MFCC features
-Train a CNN
-Save the model as best_model.h5


🚀 Run the Streamlit App
After training:

(in bash-->)
streamlit run app.py
Upload any .wav file (2–3 seconds long), and the model will predict the emotion behind the speech.

📦 Requirements
Install dependencies using:

(in bash)
pip install -r requirements.txt

Key Libraries:
TensorFlow / Keras
Librosa
Streamlit
NumPy
Scikit-learn
Soundfile

⚠️ GitHub Notes
Large files (e.g., .wav, .zip, .h5, and venv/) are excluded from GitHub using .gitignore.

👩‍💻 Author
Mounika Suda
Email: msudaa15@gmail.com
GitHub: Msuda-15

🌟 Acknowledgements
RAVDESS Dataset
TensorFlow and Keras
Streamlit for the app UI

💡 Future Work
-Improve accuracy with more data or deeper models
-Add support for longer audio
-Host the app on Streamlit Cloud or Hugging Face Spaces