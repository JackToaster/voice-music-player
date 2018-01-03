import SpeechListener as sl
from CommandRecognizer import CommandRecognizer
CALL_WORD = 'music player'

def pause(arg):
    print("Pausing")

def cancel(arg):
    print("Stopping/cancelling")

def resume(arg):
    print("Resuming")

def play(arg):
    print("Playing")

def next(arg):
    print("Going to next")

def previous(arg):
    print("Going to previous")


commands = {
    ('pause') : pause,
    ('stop', 'cancel') : cancel,
    ('resume', 'continue') : resume,
    ('play', 'start') : play,
    ('next','skip') : next,
    ('previous', 'back') : previous
}
'''
def catch_call_word(speech):
    pos = speech.find(CALL_WORD)
    pos = speech.find(' ', pos)
    if pos == -1:
        return None
    while pos != -1:
        speech = speech[pos + 1:]
        pos = speech.find(CALL_WORD)
        pos = speech.find(' ', pos)
    return speech

def split_first_word(speech):
    space_pos = speech.find(" ")
    if space_pos == -1:
        return speech, ""
    else:
        return speech[:space_pos], speech[space_pos + 1:]

def get_matchingness(command, speech):
    total_matches = 0
    for cmd in command:
        if speech == cmd:
            total_matches += 10
        else:
            command_words = cmd.split(' ')
            command_words = [word.strip() for word in command_words]
            for word in command_words:
                if len(word) > 1:
                    total_matches += speech.count(word)
    return total_matches / len(command)


def process_speech(speech):
    #create a list of key/fitness tuple pairs
    fitnesses = [[key, 0] for key in commands.keys()]
    all_none = True
    for alternative in speech:
        command = catch_call_word(alternative)
        if command != None:
            all_none = False
            for candidate in fitnesses:
                candidate[1] += get_matchingness(candidate[0], command)
    if not all_none:
        max = fitnesses[0][0]
        max_val = fitnesses[0][1]
        for candidate in fitnesses:
            if candidate[1] > max_val:
                max_val = candidate[1]
                max = candidate[0]

        commands[max](speech)
    else:
        print("No command detected")'''
def main():
    listener = sl.listener()
    recognizer = CommandRecognizer(CALL_WORD, commands)
    while True:
        speech = listener.get_next_audio()
        recognizer.process_speech(speech)
if __name__ == "__main__":
    main()