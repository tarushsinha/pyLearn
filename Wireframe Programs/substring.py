## This method ignores python's case sensitivity

def substring(word, substring):
    if substring.lower() in word.lower():
        return True
    else:
        return False

Australia = "Australia"
trail = "trail"
print(f"Is the word {trail} in the word {Australia}?\n{substring(Australia, trail)}\n")

Barbie = "Barbie"
barb = "barb"
print(f"Is the word {barb} in the word {Barbie}?\n{substring(Barbie, barb)}\n")