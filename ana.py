import speech_recognition as sr
import pyttsx3
import json
import openmodule

ABRIR_CAMINHO = "comands.json"
r = sr.Recognizer()
tts_engine = pyttsx3.init()
#audio = []

def interprete():
    global audio
    with open(ABRIR_CAMINHO, 'r') as commands_file:
        comandos = json.load(commands_file)
        audio = comandos["comandos"]
        



def speak(text):
    if tts_engine._inLoop:
        tts_engine.endLoop()
    tts_engine.say(text)
    tts_engine.runAndWait()



def listen():
    interprete()
    
    # play()
    
    with sr.Microphone() as fontes:
        fala = r.listen(fontes, None, 5)
        voice_data = ""
        
        try:
            voice_data = r.recognize_google(fala, language="pt-BR").lower()
            
        except sr.UnknownValueError:
            speak("desculpa, nao entendi:")
            
        #except sr.RequestError:
            
        print("ana>> :", voice_data.lower())
        
        if voice_data:
            sucesso = comando_ok(voice_data)
            if not sucesso:
              speak("nao consegui entender o comando")
                
def ok_comando_master(termos, comandos):
    
    if termos.strip() == comandos.strip():
        return True
    return False
                
                
def run_comandos(tipo_comando, comando_ativo, argumentos):
    
    if (tipo_comando=="abrir" or tipo_comando=="fechar"):
        openmodule.P_comandos(comando_ativo, argumentos)
        return True
    
    return False


def extract_argumentos(comando_texto, comando_voz):
    splitted_text = comando_texto.split(comando_voz.replace("*", ""), 1)
    
    argumentos = ""
    
    if len(splitted_text) > 1:
        argumentos = splitted_text[1]
    else:
        argumentos = splitted_text[0]
        
    return argumentos
                
def comando_ok(comando_texto):
    for comando_lista in audio:
      for comando_select, comandos in comando_lista.items():
        for index, comando in enumerate(comandos):
         for comando_voz, comando_ativo in comando.items():
            argumentos = ""
            
            
            #if '*' in comando_voz:
             #   argumentos = openmodule.extract_argumentos
            
                        
            if "*" in comando_voz:
              
              argumentos = extract_argumentos(comando_texto, comando_voz)
                            
              comando_voz = comando_voz.replace("*", argumentos)
                            
            found_action = ok_comando_master(comando_voz, comando_texto)
                            
            if found_action:
               try:
                   return run_comandos(comando_select, comando_ativo, argumentos)
               except:
                   speak(f"ocorreu um erro no comando {comando_voz}")
                                
                   return False
                            
    return False