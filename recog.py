import speech_recognition as sr

import pyttsx3

import pywhatkit

import datetime

import random



listener = sr.Recognizer()



engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)

# voices.setProperty('voice', voices[1].id)



engine.say('I am your Nova')

engine.say('What can I do for you')

engine.runAndWait()





def talk(text):

    engine.say(text)

    engine.runAndWait()



def hear_me():

    command = "Nothing"

    try:

        with sr.Microphone() as source:

            print('listening...')

            voice = listener.listen(source)

            command = listener.recognize_google(voice)

            command = command.lower()

            # if 'nova' or 'noa' in command:

            #    command = command.replace('nova','')

            print(command)



    except:

        pass

    return command



def hear_word():

    with sr.Microphone() as source:

        print('listening...')

        voice = listener.listen(source)

        UserWord = listener.recognize_google(voice)

        print(UserWord)





def random_select():

    WordBank = ['banana', 'books', 'panda', 'shoes', 'apple', 'clock', 'cars']

    element = random.choice(WordBank)

    #print(element)

    return element





def run_nova():

    command = hear_me()

    if 'play' in command:

        song = command.replace('play', '')

        talk('playing '+ song)

        pywhatkit.playonyt(song)

        print('playing '+ song)



    elif 'time' in command:

        time = datetime.datetime.now().strftime('%I:%M %p')

        if 'what' in command:

            talk('the time is '+ time)

        else:

            talk('current time is '+ time)



    else: # if 'memory game' in command:

        talk('okay. you start')

        print("okay, you start")

        loopcount = 0

        wordSeq = []

        while loopcount < 5:

            myWordListInput = hear_me()

            print(myWordListInput)

            myWordList = myWordListInput.split()

            print(myWordList)

            if myWordList[:len(myWordList) -1] != wordSeq:

                print("You loose")

                print(wordSeq)

                break

            else:

                print("Computer turn")

                print(myWordList)

                wordSeq = myWordList

                element = random_select()

                print(element)

                print(wordSeq)

                wordSeq.append(element)

                print(wordSeq)

                talk(wordSeq)

                loopcount = loopcount + 1

        # if element and command in command:



    '''

    while (len(WordBank) > 2):

        element1 = random.choice(WordBank)

        #print(element1)

        WordBank.remove(element1)





def memory_game():

    command = hear_me()

    '''
