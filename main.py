from time import sleep
import speech_recognition as sr
import keyboard
import ana

r = sr.Recognizer()

BOT_NOMES = ['ANA', 'ana', 'anã']


def interprete_microphone():

    with sr.Microphone() as fontes:
        print("fala alguma coisa")
        fala = r.listen(fontes, None, 3)
        voice_data = ''

        try:
            voice_data = r.recognize_google(fala, language="pt-BR").lower()
            #print(f"voce disse : {voice_data}")

        except sr.UnknownValueError:
            print(f"não entendi o que você disse! ")

        print(">>", voice_data)
        for botaonome in BOT_NOMES:
            if (botaonome in voice_data):
                ana.listen()
                break

    #while True:
     #       interprete_microphone()
if __name__ == "__main__":
    interprete_microphone()
