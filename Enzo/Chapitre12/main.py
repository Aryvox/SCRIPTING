import multiprocessing
import random
import time
import os

def generer_nombre():
    pid = os.getpid()
    nombre = random.randint(1, 100)
    print(f"[Processus {pid}] number : {nombre}")
    
    print(f"[Processus {pid}]")
    time.sleep(60)

if __name__ == "__main__":
    processus_liste = []

    for _ in range(5):
        p = multiprocessing.Process(target=generer_nombre)
        processus_liste.append(p)
        p.start()

    print(f"--- {len(processus_liste)} start")

    try:
        for p in processus_liste:
            p.join()
    except KeyboardInterrupt:
        print("\nStop")
    finally:
        for p in processus_liste:
            if p.is_alive():
                p.terminate()
        print("Closed")