import random
import pyttsx3
import speech_recognition as sr


def speak_word(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


def get_user_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Welcome to Spell Check")
        print("Say your answer:")
        audio = r.listen(source)

    try:
        user_input = r.recognize_google(audio)
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""


def play_game():
    words = ["hello", "adam", "apple", "bus", "spell"]
    score = 0

    used_words = []

    for i in range(5):
        # randomly select a word from the list
        word = random.choice([w for w in words if w not in used_words])
        used_words.append(word)

        # speak the word
        speak_word(word)

        # get user's input
        user_input = get_user_input().replace(" ", "")

        # check if user's input matches the word
        if user_input.lower() == word:
            score += 1
            print("Correct!")
        else:
            print("Incorrect.")

    print(f"You scored {score} out of 5.")


if __name__ == "__main__":
    play_game()