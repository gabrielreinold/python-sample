def main():

    import random

    WORDS = ("Adventurous",	"Creative", "Good",	"Nice",	"Self-disciplined", "Affable",	"Decisive", "Brat", "Great", "Dainty",
             "Non-judgemental", "Sensible", "Affectionate", "Dependable", "Hardworking", "Observant", "Sensitive",
             "Agreeable", "Determined", "Helpful", "Optimistic", "Shy", "Ambitious", "Fleabag", "Diligent", "Hilarious",
             "Organized", "Silly", "Honest", "Smart", "Talkative",  "Polite", "Tidy", "Dirty", "Scumbag", "Calm", "Diplomatic",  "Plucky",
             "Intelligent", "Sincere", "Easy-going", "Imaginative", "Vagabond", "Slacker", "Broad-minded", "Artistic", "Humorous",
             "Sociable", "Narrow-minded", "Bright", "Stupid", "Laid-back", "Placid", "Independent", "Efficient", "Amiable",
             "Asshole" "Immortal", "Sincere", "Careful", "Extroverted", "Intuitive", "Popular",	"Tough", "Charismatic",
             "Exuberant", "Inventive", "Powerful", "Trustworthy", "Charming", "Fair-minded"	"Joyful	Practical",
             "Unassuming", "Chatty",	"Faithful",	"Kind",	"Pro-active", "Understanding", "Cheerful", "Fearless",
             "Kooky", "Quick-witted", "Upbeat", "Clever",	"Forceful",	"Quiet", "Versatile", "Communicative", "Frank",
             "Likable", "Rational",	"Warm-hearted", "Compassionate", "Friendly", "Loving", "Reliable", "Wild", "Immature",
             "Funny", "Loyal", "Reserved", "Wise", "Considerate", "Generous", "Lucky", "Resourceful", "Witty", "Convivial",
             "Gentle", "Modest", "Romantic")
    word = random.choice(WORDS)
    correct = word
    scramble = ""
    while word:
        position = random.randrange(len(word))
        scramble += word[position]
        word = word[:position] + word[(position + 1):]
    print(
    """
          Welcome to Carsigo World!!!
    
          Write one adjective that you think describes Carsigo the most, you can also get a hint.
          (press the enter key at prompt to quit)
          """
          )
    guess = input("Carsigo is: ")

    while guess != correct and guess != "":
        print("Sorry, that's not it")

        print("Your hint is: ", scramble)
        guess = input("Carsigo is: ")

    if guess == correct:
        print("That's it, you guessed it!")
        print(f" Yay, you got it right - Carsigo is {guess}")

    play_again = input("Do you want to restart? yes or no\n")

    if play_again == "yes":
        main()
    else:
        exit()

main()