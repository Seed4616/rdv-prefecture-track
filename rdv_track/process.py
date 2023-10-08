import subprocess
from click import *
import pygame


# Function pour ouvrir Chrome et naviguer vers l'URL
def ouvrir_chrome_et_naviguer(site_url):
    chrome_exe_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    subprocess.Popen([chrome_exe_path, site_url])


# Function pour effectuer la tâche principale
def effectuer_tache():
    site_url = "https://pprdv.interieur.gouv.fr/booking/create/989/0"
    ouvrir_chrome_et_naviguer(site_url)

    time.sleep(5)

    pyautogui.scroll(-1000)
    # Cocher la première case
    click_coordinates(*coordonnees_clics["cocher_case"])

    # Cocher le bouton suivant
    time.sleep(2)
    click_coordinates(*coordonnees_clics["cliquer_suivant"])

    time.sleep(1.5)
    random_guichets_click()

    click_coordinates(*coordonnees_clics["cliquer_suivant2"])

    # Vérifier la couleur et continuer en fonction du résultat
    pixel_color = pyautogui.pixel(color["color_orange"])

    if pixel_color[0] >= 200:
        screenshot()
        # Initialise pygame
        pygame.init()

        # Crée un objet Mixer pour gérer les sons
        pygame.mixer.init()

        # Charge le fichier audio
        music = pygame.mixer.Sound("./music.mp3")
        pygame.mixer.music.set_volume(0.75)
        # Joue la musique en boucle
        music.play(-1)

        # Joue la musique en boucle
        music.play(-1)

        playing = True

        while playing:
            user_input = input("Appuyez sur 'p' pour mettre en pause, 'r' pour reprendre ou 'q' pour quitter: ")

            if user_input == 'p':
                pygame.mixer.pause()
                print("Musique en pause.")
            elif user_input == 'r':
                pygame.mixer.unpause()
                print("Reprise de la musique.")
            elif user_input == 'q':
                playing = False
                pygame.mixer.stop()
                print("Musique arrêtée.")

        # Termine pygame
        pygame.quit()
    else:

        print("La case Descriptif n'est pas orange mais bleue")

    # Fermer la page et donc le navigateur
    pyautogui.hotkey('ctrl', 'w')

    time.sleep(3)
