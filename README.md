# voice-music-player
A voice controlled music player using the Python SpeechRecognition library to perform voice recognition.  
This program could be easily adapted for any always-listening speech control application. The speech recognition algorithm works by using Google's cloud service to convert audio to text, then processing the text to see which command most closely matches.  
The recognizer takes a 'call word', which is used before each command to avoid reacting to unintended commands.
To modify the commands:  
1. Write a function for each command that takes the spoken text as an input.
2. Modify the 'commands' dictionary given to CommandRecognizer to have the keywords and function to call.  
Example of always-listening voice command:
```
CALL_WORD = 'call'

def test(text):
  print("You said:" + text)
def foo(text):
  print("foo run")
commands = {
  ('test','run test', 'verify') : test,
  ('foo', 'bar') : foo
}

listener = sl.listener()
recognizer = CommandRecognizer(CALL_WORD, commands)
while True:
  speech = listener.get_next_audio()
  recognizer.process_speech(speech)
```
