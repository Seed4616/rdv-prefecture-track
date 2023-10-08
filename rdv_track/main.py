from popup import *
from process import *
from click import *

if __name__ == "__main__":
    url = "https://pprdv.interieur.gouv.fr/booking/create/989/0"
    ouvrir_chrome_et_naviguer(url)

    track_mouse_click()
    separate_coordinates(coordinates_list)
    time.sleep(3)
    # Fermer la page et donc le navigateur
    pyautogui.hotkey('ctrl', 'w')

    """
    show_dict_content({
        "Coordonnées des clics": coordonnees_clics,
        "Guichets": guichets,
        "Couleur": color,
    }, "Informations")
    """
    while True:
        try:
            effectuer_tache()
            time.sleep(15)
        except Exception as e:
            print("An exception occurred:", e)
