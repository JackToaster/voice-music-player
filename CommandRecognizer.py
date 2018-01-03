class CommandRecognizer:
    def __init__(self, call_word, command_dict):
        self.commands = command_dict
        self.call_word = call_word

    #finds the latest instance of "call_word (other stuff)"
    #removes other text up to the next space to account for plurals, possesives, etc.
    def catch_call_word(self, speech):
        pos = speech.find(self.call_word)
        if pos == -1:
            return None
        # loop through finding the latest
        while pos != -1:
            pos = speech.find(' ', pos + len(self.call_word) - 1)
            speech = speech[pos + 1:]
            pos = speech.find(self.call_word)
        return speech

    #splits the first word from text, not used and not sure why it's here.
    def split_first_word(self, speech):
        space_pos = speech.find(" ")
        if space_pos == -1:
            return speech, ""
        else:
            return speech[:space_pos], speech[space_pos + 1:]

    #returns number of matching options divided by total options,
    #with a large bonus for exact matches.
    def get_matchingness(self, command, speech):
        total_matches = 0
        #loop through each word in the command
        for cmd in command:
            #bonus for exact matches
            if speech == cmd:
                total_matches += 100
            else:
                #split the command into words and count each
                command_words = cmd.split(' ')
                command_words = [word.strip() for word in command_words]
                for word in command_words:
                    if len(word) > 1:
                        total_matches += speech.count(word)
        return total_matches / len(command)

    def process_speech(self, speech):
        # create a list of key/fitness tuple pairs
        fitnesses = [[key, 0] for key in self.commands.keys()]
        #whether every option is empty
        all_none = True
        #go through list of alternatives provided by Google
        for alternative in speech:
            #try to find a command starting with call_word
            command = self.catch_call_word(alternative)
            #check if the command could be found
            if command != None:
                #if one is found, all_none will not be false
                all_none = False
                #loop through the candidate commands and rate them
                for candidate in fitnesses:
                    candidate[1] += self.get_matchingness(candidate[0], command)
        if not all_none:
            #find the best command if there are any
            max = None
            max_val = -1
            for candidate in fitnesses:
                if candidate[1] > max_val:
                    max_val = candidate[1]
                    max = candidate[0]

            #perform callback
            if max != None:
                self.commands[max](speech)
            else:
                print("Command could not be recognized")
        else:
            print("No command detected")

