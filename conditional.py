def StartWithVowel(name):
    vowel = "aeiouAEIOU"
    first_letter = name[0]
    return name[0] in vowel

name = input("Enter your name: ")
if StartWithVowel(name):
    print(f"Hello {name}")
else:
    print("Hello")