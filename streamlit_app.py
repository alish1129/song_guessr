import streamlit as st

from recognize import recognize
import os

st.write("# 🎶Welcome to the SongGuessr")
#
# st.audio_input = st.file_uploader("Upload a prerecorded Audio File (mp3 only)", type=["mp3"])
#
# if st.audio_input is not None:
#     st.audio(st.audio_input, format="audio/mp3")
#     st.write("## Audio File Uploaded Successfully!")
#     st.write("### Now, let's recognize the song...")

tab1, tab2, = st.tabs(["Record", "Upload a clip"])

with tab1:
    st.write("### You can record a new audio clip:")
    # Placeholder for audio recording functionality
    audio_value = st.audio_input("Record a new audio clip")

    if audio_value:
        st.audio(audio_value, format="audio/mp3")

        # Here you would call your recognition function
        # For example:
        # save clip to clips as a temp name and then call the recognition function, delete the temp file after use
        clip_path = "clips/temp.mp3"

        with open(clip_path, "wb") as f:
            f.write(audio_value.getbuffer())

        match, img, bar = recognize(clip_path)

        st.write("## Recognition Result:")
        # Display the recognized song name
        st.write(f"Best match: {match}")
        st.image(img, caption="Spectrogram")

        bar.progress(100, text="Recognition complete.")

        # Display the result
        # st.write(f"Recognized Song: {result}")

with tab2:
    st.write("### Or upload an audio clip:")
    uploaded_file = st.file_uploader("Upload a prerecorded Audio File (mp3 only)", type=["mp3"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/mp3")
        st.toast('File uploaded successfully!', icon='✅')

        st.write("#### Now, let's recognize the song...")
        clip_path = "clips/temp.mp3"

        # Save the uploaded file temporarily
        with open(clip_path, "wb") as f:
            f.write(uploaded_file.read())

        best_match, img, bar = recognize(clip_path)

        if best_match:
            st.write(f"Best match: {best_match}")
            st.image(img)
        else:
            st.write("No match found.")

        bar.progress(100, text="Recognition complete.")

        # Clean up the temporary file
        if os.path.exists(clip_path):
            os.remove(clip_path)