import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Configuration de la fenêtre
root = tk.Tk()
root.title("CTF")
root.geometry("1020x400")
label_Titre = tk.Label(root, text="BankIn - Suivi des dépenses interservice", font=("Helvetica", 16))
label_Titre.grid(row=0, column=0, columnspan=2, pady=10)

def ajouter_depense():
    # Créer une nouvelle fenêtre pour ajouter une dépense
    fenêtre_ajout = tk.Toplevel(root)
    fenêtre_ajout.title("Ajouter une dépense")
    fenêtre_ajout.geometry("420x300")
    label_Titre = tk.Label(fenêtre_ajout, text="Ajouter une dépense", font=("Helvetica", 16))
    label_Titre.grid(row=0, column=0, columnspan=2, pady=10)
    label_Titre = tk.Label(fenêtre_ajout, text="Titre")
    label_Titre.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_Titre = tk.Entry(fenêtre_ajout, width=50)
    entry_Titre.grid(row=1, column=1, padx=10, pady=10)
    label_Montant = tk.Label(fenêtre_ajout, text="Montant TTC")
    label_Montant.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_Montant = tk.Entry(fenêtre_ajout, width=50)
    entry_Montant.grid(row=2, column=1, padx=10, pady=10)
    label_Catégorie = tk.Label(fenêtre_ajout, text="Catégorie")
    label_Catégorie.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_Catégorie = tk.Entry(fenêtre_ajout, width=50)
    entry_Catégorie.grid(row=3, column=1, padx=10, pady=10)
    label_Date = tk.Label(fenêtre_ajout, text="Date")
    label_Date.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_Date = tk.Entry(fenêtre_ajout, width=50)
    entry_Date.grid(row=4, column=1, padx=10, pady=10)
    button_Valider = tk.Button(fenêtre_ajout, text="Valider")
    button_Valider.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    #  Fonction pour valider l'ajout
    def valider_ajout():
        titre = entry_Titre.get()
        montant_ttc = entry_Montant.get()
        categorie = entry_Catégorie.get()
        date = entry_Date.get()
        if not titre or not montant_ttc or not categorie or not date:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
            return
        try:
            montant_ttc = float(montant_ttc) # Convertir le montant TTC en nombre
        except ValueError:
            messagebox.showwarning("Erreur", "Le montant TTC doit être un nombre.")
            return
        montant_ht = montant_ttc / 1.2 # Calcul du montant HT
        tree.insert("", "end", values=(titre, montant_ttc, montant_ht, categorie, date))
        fenêtre_ajout.destroy()
    button_Valider.config(command=valider_ajout) # Associer la fonction valider_ajout au bouton Valider

# Tableau des dépenses
colums = ("Titre", "Montant TTC", "Montant HT", "Catégorie", "Date")
tree = ttk.Treeview(root, columns=colums, show="headings")
tree.heading("Titre", text="Titre")
tree.heading("Montant TTC", text="Montant TTC")
tree.heading("Montant HT", text="Montant HT")
tree.heading("Catégorie", text="Catégorie")
tree.heading("Date", text="Date")
tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
# Configurer les colonnes pour qu'elles s'étirent

# Ajouter des données
button_Ajouter = tk.Button(root, text="Ajouter une dépense", command=ajouter_depense)  # Associer la fonction ajouter_depense
button_Ajouter.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
button_Envoyer = tk.Button(root, text="Envoyer à la comptabilité")
button_Envoyer.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Main loop
root.mainloop()

