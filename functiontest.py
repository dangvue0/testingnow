class People:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def hey(self):
        try:
            print(self.word1, self.word2)
        except:
            print("ErrorCatch")
        finally:
            print(self.word1 + " 5")

# luca = People("YOU", "ME").hey()