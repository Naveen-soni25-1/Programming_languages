glossary = {"string": "Anything inside double or single quotes is a string"}  # Dictionary with word-meaning pairs

# Greeting
print("\tWelcome Naveen,\n\tWhat word do you want to add today?".title())
print("\n\tTo see words enter [show]".title())

while True:  # To continue adding words with meanings
    word = input("\n\tEnter your word: ".title()).title().strip()

    if word.lower() == 'show':
        break  # Exit loop and display glossary

    meaning = input("\tWhat does this mean: ".title()).strip()
    glossary[word] = meaning  # Store word and meaning in dictionary

# Display all stored words and meanings
for i, key in enumerate(glossary.keys(), start=1):
    print(f"\n{i}. {key}:-\n\t{glossary[key]}")