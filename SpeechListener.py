import speech_recognition as sr

MIC_THRESH_MULT = 3

class listener:
    def __init__(self):
        for i, m in enumerate(sr.Microphone.list_microphone_names()):
            if m == "default":
                self.microphone = sr.Microphone(i)
                self.recognizer = sr.Recognizer()

        self.adjust_threshold()

        print("Microphone ready")

    def adjust_threshold(self, mult = MIC_THRESH_MULT):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, 3)
            self.mic_threshold = self.recognizer.energy_threshold * mult
            self.recognizer.energy_threshold = self.mic_threshold

    def get_next_audio(self):
        while True:
            print("Listening")
            self.recognizer.energy_threshold = self.mic_threshold
            with self.microphone as micro:
                audio = self.recognizer.listen(micro)
            print("Attempting to recognize...")
            try:
                out = self.strip_alternatives(self.recognizer.recognize_google(audio,None,"en-US",True))
                if out != None:
                    print("Recognized audio: " + str(out))
                    return out
            except sr.UnknownValueError:
                print("Could not read audio.")
            except sr.RequestError as e:
                print("Could not request results from speech recognition; {0}".format(e))
                return ""

    def strip_alternatives(self, recognizer_data):
        if len(recognizer_data) == 0:
            return None
        alternatives = recognizer_data['alternative']
        return [alt['transcript'].lower() for alt in alternatives]