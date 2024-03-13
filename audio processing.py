import pyaudio
import wave

def play_audio(file_path):
    # Open the audio file
    wf = wave.open(file_path, 'rb')
    
    # Initialize PyAudio
    p = pyaudio.PyAudio()
    
    # Open the audio stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    # Read data in chunks and play it
    data = wf.readframes(1024)
    while data:
        stream.write(data)
        data = wf.readframes(1024)
    
    # Close the stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

def record_audio(output_file, duration=5, rate=44100, chunk=1024, channels=2, format=pyaudio.paInt16):
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open audio stream for recording
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    # Record audio data in chunks
    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a file
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    # Example usage:
    
    # Play an audio file
    play_audio("example.wav")

    # Record audio for 5 seconds and save it to a file
    record_audio("output.wav", duration=5)
