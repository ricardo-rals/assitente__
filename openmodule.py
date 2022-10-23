import webbrowser
import subprocess
import ana

def P_comandos(comando_ativo, argumentos=""):


   if comando_ativo[0:4]=="web!":
      open_link(comando_ativo[5:])
      
   elif comando_ativo[0:4]=="web?":
      open_link_with_search(comando_ativo[5:], argumentos)
      ana.speak("Pesquisando " + argumentos)
   elif comando_ativo[0:4]=="path":
      open_programa(comando_ativo[5:])
      ana.speak("Abrindo" + argumentos)
   elif comando_ativo=='comandos':
       reload_comandos()
       ana.speak("Atualizado")
      
      
def open_link_with_search(link, argumentos=""):
    print(f"{link}/search?q={argumentos}")
    webbrowser.get("windowns-default").open_new(f"{link}/search?q={argumentos}")
    
def open_link(link):
    webbrowser.get("windows-default").open_new(f"{link}")
    
def open_programa(path):
    subprocess.Popen([path, '-new-tab'])
    
    
def reload_comandos():
    
    ana.interprete()