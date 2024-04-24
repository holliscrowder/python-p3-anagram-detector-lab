class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, checklist):
        matches = []
        for item in checklist:
            if sorted(list(self.word)) == sorted(list(item)):
                matches.append(item)

        return matches


test = Anagram("listen")
print(test.match(["enlist", "weather"]))
