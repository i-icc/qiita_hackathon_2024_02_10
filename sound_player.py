import sounddevice as sd
import soundfile as sf

def play_sound(file_path):
    data, fs = sf.read(file_path)
    sd.play(data, fs)
    sd.wait()

class SoundPlayer:
    def __init__(self, file_path):
        self.data, self.fs = sf.read(file_path)


    def play(self):
        sd.play(self.data, self.fs)
        sd.wait()


if __name__ == "__main__":
    sp = SoundPlayer("./open.mp3")
    sp2 = SoundPlayer("./close.mp3")

    sp.play()
    sp.play()
    sp2.play()
    sp.play()