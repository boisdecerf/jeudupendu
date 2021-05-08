import random

title = "Jeu du pendu"
print("---{:^14}---".format(title))

playing = True

while playing :

    # Counting the numbers of lines in the file
    def len_file(file) :
        with open(file) as f :
            for index, line in enumerate(f) :
                pass
        return index + 1
    lenFile= len_file("./listedemots")

    # Searching for a random word in the file
    randomNumber = random.randint(1, lenFile)
    with open("./listedemots", "r") as file :
        for i in range(randomNumber) :
            wordToGuess = file.readline()

    # Preparing the game
    wordToGuess = wordToGuess.rstrip().upper()
    copyWordToGuess = wordToGuess
    wordInConstruction = "#" * len(wordToGuess)
    lettersList = []

    for i in range(1,6+1) :
        # Word guessing
        print("\nMot à deviner : ", wordInConstruction)
        print("Il reste", 6+1-i, "tour(s)")
        letter = input("Entrez une lettre : ")
        letter= letter.upper()

        while not letter.isalpha() or letter in lettersList or len(letter) > 1 :
            # Check only one character has been choosen
            if len(letter) > 1 :
                letter = input("Entrez une seule lettre : ")
            # Check if the input is not in alphabet
            if not letter.isalpha() :
                letter = input("Ceci n'est pas une lettre.\nEntrez une lettre : ")
            # Check if the letter has already been proposed
            if letter in lettersList :
                letter = input("Letter déjà proposée.\nEntrez une lettre : ")
            letter = letter.upper()
        lettersList.append(letter)

        # Word construction
        while letter in copyWordToGuess :
            indexLetter = copyWordToGuess.index(letter)
            wordInConstruction= wordInConstruction[:indexLetter] + letter + wordInConstruction [indexLetter+1:]
            copyWordToGuess = copyWordToGuess[:indexLetter] + "#" + copyWordToGuess[indexLetter+1:]

    # Propose a word
    print("\nMot à deviner : ", wordInConstruction)
    guessedWord = input("Devinez le mot : ")
    if guessedWord.upper() == wordToGuess :
        print("\n\tGagné !")
    else :
        print("\n\tPerdu...")

    # Ask to keep playing or not
    answerPlaying = input("\nSouhaitez-vous rejouer ? (oui/non) : ")
    while answerPlaying != "oui" and answerPlaying != "non" :
        answerPlaying = input("\nRépondez par \"oui\" ou par \"non\". Souhaitez-vous rejouer ? (oui/non) : ")
    if answerPlaying == "non" :
        playing = False