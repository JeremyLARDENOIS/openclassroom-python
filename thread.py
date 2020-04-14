#!/usr/bin/python3

import random
import sys
import time
from threading import Thread, RLock

verrou = RLock()

class Afficheur(Thread):
    def __init__(self,mot):
        Thread.__init__(self)
        self.mot = mot
    def run (self):
        """Code a execute"""
        # Répète 20 fois
        i = 0
        while i < 5:
            with verrou:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    # attente est à présent entre 0.2 et 0.8
            time.sleep(attente)
            i += 1


#création des threads
thread_1 = Afficheur("MAJ")
thread_2 = Afficheur("min")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()
