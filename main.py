def login():
    utilisateur = input("Nom d'utilisateur : ")
    print(f"Bienvenue, {utilisateur} !")


def afficher_menu():
    print("=== Mon application ===")
    print("1. Se connecter")
    print("2. Quitter")


if __name__ == "__main__":
    afficher_menu()
