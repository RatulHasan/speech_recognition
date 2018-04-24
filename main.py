import pyaudio
import wave
import speech_recognition as sr

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


# play_audio("audio/whistle-slide-down.wav")

  
r = sr.Recognizer()
r.energy_threshold=4000

def init_speech():
    print("Listening...")

    play_audio("audio/beep.wav")

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    # write audio to a RAW file
    with open("microphone-results.raw", "wb") as f:
        f.write(audio.get_raw_data())

    # write audio to a WAV file
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    play_audio("./audio/Beep5.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you!")

    print("Your commane: ")
    print(command)



init_speech()