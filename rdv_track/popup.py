import pyautogui
import tkinter as tk

# Ajoutez cette variable globale pour garder une trace du statut d'affichage des fenêtres pop-up
popup_displayed = False


# Function pour afficher une fenêtre pop-up avec le contenu du dictionnaire
def show_dict_content(dictionaries, title):
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre principale

    # Crée une nouvelle fenêtre pour afficher le contenu du dictionnaire
    window = tk.Toplevel(root)
    window.title(title)

    # Crée un widget de texte pour afficher le contenu du dictionnaire
    text_widget = tk.Text(window, height=20, width=50)
    text_widget.pack()

    # Ajoute le contenu du dictionnaire au widget de texte
    for dictionary_name, dictionary_content in dictionaries.items():
        text_widget.insert(tk.END, f"{dictionary_name}\n")
        for key, value in dictionary_content.items():
            text_widget.insert(tk.END, f"{key}: {value}\n")
        text_widget.insert(tk.END, "\n")

    # Empêche l'utilisateur de modifier le contenu du widget de texte
    text_widget.config(state=tk.DISABLED)

    def close_windows():
        window.destroy()
        root.destroy()

    # disable_clicks()  # Désactiver les clics avant l'affichage de la fenêtre pop-up
    tk.Button(
        window,
        text='Exit',
        command=lambda: close_windows()
    ).pack(expand=False)
    # enable_clicks()  # Réactiver les clics après la fermeture de la fenêtre pop-up

    window.mainloop()


# Function to close the current tab in Chrome using Ctrl + W
def close_current_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
