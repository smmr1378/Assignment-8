import gtts



def read_from_file():
    global words_bank

    f = open("Translate.txt", "r")

    big_string = f.read()
    temp = big_string.split("\n")
    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "fa":temp[i+1]}
        words_bank.append(my_dict)

    f.close()
    
def translate_english_to_persian():

    user_text = input("enter your english text: ")
    user_words = user_text.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"] + " "
                print(word["fa"])
                break

    else:
        output = output + user_word + " "
        print(word," ", end="")
        translate_sound = gtts.gTTS(output, lang='ar')
        translate_sound.save('translate_to_persian.mp3')

def translate_persian_to_english():
    
    user_text = input(" enter your persian text: ")
    user_words = user_text.split(".")
    output = ""

    for word in user_words:
        for worde in words_bank:
            if word == worde["fa"]:
                output = output + worde["en"] + " "
                print(word["en"], " ",end="")
                break
    else:
        output = output + word + " "
        translate_sound = gtts.gTTS(output, lang='ar')
        translate_sound.save('translate_to_english.mp3')

def add_new_word():
    user_word = input(" enter your english word: ")
    for word in user_word:
        if word in words_bank:
            print("is available")
        else:
            words_bank.append(word)
            print("added")
 

def show_menu():
    print("welcome to my translate")
    print("1-translate english to persian")
    print("2-translate persian to english")
    print("3-add a new word to database")
    print("4-exit")


read_from_file()
while True:
    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()
    elif choice == 3:
        add_new_word()
    elif choice == 4:
        exit(0)
        

