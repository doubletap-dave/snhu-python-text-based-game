from classes import room

UL_START = "\033[04m"
UL_END = "\033[0m"

def main():
    # Create rooms
    rooms = {
        "whispering_willows": room.Room("Whispering Willows", "A grove of ancient trees with leaves that whisper secrets."),
        "mosaic_menagerie": room.Room("Mosaic Menagerie", "A room filled with colorful mosaics depicting fantastical creatures."),
        "guardians_chamber": room.Room("Guardian's Chamber", "A massive stone golem stands watch over a glowing artifact."),
        "verdant_vestibule": room.Room("Verdant Vestibule", "A lush garden with a fountain and blooming flowers."),
        "runic_rotunda": room.Room("Runic Rotunda", "A circular chamber with glowing runes etched into the walls."),
        "forgotten_fountain": room.Room("Forgotten Fountain", "A tranquil pool surrounded by statues of ancient heroes."),
        "sunken_sanctuary": room.Room("Sunken Sanctuary", "An underwater grotto with shimmering fish and coral."),
        "overgrown_observatory": room.Room("Overgrown Observatory", "A tower with a telescope that peers into the stars."),
        "echoing_arboretum": room.Room("Echoing Arboretum", "A vast hall filled with the sound of rustling leaves."),
    }

    # Connect rooms
    rooms["whispering_willows"].e_to = rooms["mosaic_menagerie"]
    rooms["whispering_willows"].s_to = rooms["verdant_vestibule"]

    rooms["mosaic_menagerie"].e_to = rooms["guardians_chamber"]
    rooms["mosaic_menagerie"].s_to = rooms["runic_rotunda"]
    rooms["mosaic_menagerie"].w_to = rooms["whispering_willows"]

    rooms["guardians_chamber"].w_to = rooms["mosaic_menagerie"]

    rooms["verdant_vestibule"].n_to = rooms["whispering_willows"]
    rooms["verdant_vestibule"].e_to = rooms["runic_rotunda"]
    rooms["verdant_vestibule"].s_to = rooms["sunken_sanctuary"]

    rooms["runic_rotunda"].n_to = rooms["mosaic_menagerie"]
    rooms["runic_rotunda"].e_to = rooms["forgotten_fountain"]
    rooms["runic_rotunda"].w_to = rooms["verdant_vestibule"]
    rooms["runic_rotunda"].s_to = rooms["overgrown_observatory"]

    rooms["forgotten_fountain"].w_to = rooms["runic_rotunda"]
    rooms["forgotten_fountain"].s_to = rooms["echoing_arboretum"]

    rooms["sunken_sanctuary"].n_to = rooms["verdant_vestibule"]
    rooms["sunken_sanctuary"].e_to = rooms["overgrown_observatory"]

    rooms["overgrown_observatory"].w_to = rooms["sunken_sanctuary"]
    rooms["overgrown_observatory"].n_to = rooms["runic_rotunda"]
    rooms["overgrown_observatory"].e_to = rooms["echoing_arboretum"]

    rooms["echoing_arboretum"].w_to = rooms["overgrown_observatory"]
    rooms["echoing_arboretum"].n_to = rooms["forgotten_fountain"]

if __name__ == "__main__":
    main()