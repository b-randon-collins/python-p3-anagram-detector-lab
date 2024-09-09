# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        #sort target word
        target_letters = sorted(self.word)
        #make empty list for matching words
        matching_words = []

        #itterate thru words 
            #sort word letters and compare to target letters
            #if match append to matching words
        for word in words:
            if sorted(word) == target_letters:
                matching_words.append(word)
        print(matching_words)
        return matching_words    

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])
# => ['inlets']