import time
import pyautogui
import random
from pynput import mouse

# Dictionnaire pour enregistrer les coordonnées des clics
coordonnees_clics = {
    "cocher_case": (0, 0),
    "cliquer_suivant": (0, 0),
    "cliquer_suivant2": (0, 0),
    # Ajoutez d'autres coordonnées ici selon vos besoins
}

guichets = {
    "guichets1_4": (0, 0),
    "guichets5_8": (0, 0),
    "guichets9_12": (0, 0),
}

color = {
    "color_orange": (0, 0),
}

coordinates_list = []
click_count = 0


def on_click(x, y, button, pressed):
    if pressed:
        coordinates_list.append((x, y))
        print(f"Clic détecté à la position x:{x} y:{y}")
        if len(coordinates_list) == 7:
            print("13 coordonnées enregistrées. Arrêt de la collecte.")
            return False


def separate_coordinates(list_to_separate):
    global coordonnees_clics, guichets, color

    coordonnees_clics["cocher_case"] = list_to_separate[0]
    coordonnees_clics["cliquer_suivant"] = list_to_separate[1]
    coordonnees_clics["cliquer_suivant2"] = list_to_separate[5]

    guichets["guichets1_4"] = list_to_separate[2]
    guichets["guichets5_8"] = list_to_separate[3]
    guichets["guichets9_12"] = list_to_separate[4]

    color["color_orange"] = list_to_separate[6]


def track_mouse_click():
    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            pass


# Choosing which guichets to check randomly
def random_guichets_click():
    # rnb is random number
    rnb = random.randint(1, 3)
    if rnb == 1:
        pyautogui.click(guichets["guichets1_4"])
    if rnb == 2:
        pyautogui.click(guichets["guichets5_8"])
    if rnb == 3:
        pyautogui.click(guichets["guichets9_12"])


# Function pour effectuer un clic sur l'élément aux coordonnées données
def click_coordinates(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
    time.sleep(1)


def screenshot():
    pyautogui.screenshot(f'C:/Users/Public/Pictures/prefecture/{time.strftime("%Y:%m:%d:%H:%M:%S")}.png')

