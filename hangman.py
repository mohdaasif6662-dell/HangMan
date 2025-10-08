import random 
stages = [
    # Stage 6 (Game Over)
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    💀 You’re hanged!
    """,
    # Stage 5
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    # Stage 4
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    # Stage 3
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    # Stage 2
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    # Stage 1
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # Stage 0
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]


logo = """

 _    _                                          _ 
 | |  | |                                        | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  | |
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ |_|
 | |  | | (_| | | | | (_| | | | | | | (_| | | | | _ 
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|(_)
                      __/ |                         
                     |___/          


"""

print(logo)


end_of_the_game = False


word_list = [
    'apple','banana','tiger','pineapple','grape','orange','mango','lemon','peach','cherry',
    'watermelon','strawberry','blueberry','kiwi','papaya','guava','plum','pear','coconut',
    'dog','cat','lion','tiger','elephant','giraffe','monkey','zebra','bear','rabbit',
    'fox','wolf','panda','camel','horse','donkey','sheep','goat','kangaroo','leopard',
    'eagle','parrot','crow','peacock','sparrow','penguin','ostrich','owl','dove','duck',
    'fish','shark','whale','dolphin','octopus','crab','lobster','seal','turtle','jellyfish',
    'car','truck','bus','bicycle','motorcycle','train','airplane','ship','boat','scooter',
    'computer','keyboard','mouse','monitor','laptop','printer','mobile','charger','camera','tablet',
    'python','java','django','flask','react','html','css','javascript','sql','github',
    'school','college','teacher','student','classroom','library','exam','subject','notebook','pencil',
    'book','pen','eraser','sharpener','ruler','bag','desk','chair','chalk','board',
    'sun','moon','star','planet','earth','mars','jupiter','saturn','venus','mercury',
    'clock','watch','mirror','window','door','table','lamp','candle','bottle','glass',
    'house','garden','kitchen','room','bed','pillow','blanket','cupboard','sofa','floor',
    'rain','storm','thunder','cloud','wind','snow','summer','winter','spring','autumn',
    'river','mountain','valley','forest','tree','leaf','flower','grass','stone','sand',
    'city','village','country','road','bridge','station','airport','hotel','market','park',
    'music','guitar','piano','drum','flute','violin','song','dance','movie','theater',
    'doctor','nurse','engineer','farmer','police','pilot','chef','driver','artist','scientist',
    'ball','bat','cricket','football','basketball','tennis','hockey','volleyball','golf','rugby',
    'energy','power','light','sound','gravity','force','motion','speed','mass','time',
    'happy','sad','angry','excited','bored','tired','scared','nervous','proud','calm'
]

chose_word = random.choice(word_list)
word_length = len(chose_word)

lives = 6
print(f"Pssst,the solution is: {chose_word}")
display = []
for _ in range(word_length):
    display += "_"

while not end_of_the_game:
    guess = input("Guess the letter:").lower()

    for position in range(word_length):
        letter = chose_word[position]
        print(f"Guess letter:{guess}")

        if letter == guess:
            display[position] = letter
    if guess not in chose_word:
        lives -= 1
        if lives == 0:
            end_of_the_game = True
            print("You Lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_the_game = True
        print("You Win!")
    print(stages[lives])