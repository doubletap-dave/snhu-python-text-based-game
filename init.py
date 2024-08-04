from classes import item, room


def init_rooms():
    # Create rooms
    rooms = {
        "whispering_willows": room.Room("Whispering Willows",
                                        "A grove of ancient trees with leaves that whisper secrets."),

        "mosaic_menagerie": room.Room("Mosaic Menagerie",
                                      "A room filled with colorful mosaics depicting fantastical creatures."),

        "guardians_chamber": room.Room("Guardian's Chamber",
                                       "A massive stone golem stands watch over a glowing artifact."),

        "verdant_vestibule": room.Room("Verdant Vestibule", "A lush garden with a fountain and blooming flowers."),

        "runic_rotunda": room.Room("Runic Rotunda", "A circular chamber with glowing runes etched into the walls."),

        "forgotten_fountain": room.Room("Forgotten Fountain",
                                        "A tranquil pool surrounded by statues of ancient heroes."),

        "sunken_sanctuary": room.Room("Sunken Sanctuary", "An underwater grotto with shimmering fish and coral."),

        "overgrown_observatory": room.Room("Overgrown Observatory",
                                           "A tower with a telescope that peers into the stars."),

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

    return rooms


def init_items():

    # Initialize items
    items = {
        "enchanted_flute": item.Item("Enchanted Flute",
                                     "A slender flute that plays haunting melodies when the wind blows.", 2, 0, 0, 10),

        "prismatic_lens": item.Item("Prismatic Lens",
                                    "A multifaceted lens that refracts light into a dazzling rainbow.", 0, 2, 0, 10),

        "magical_stylus": item.Item("Magical Stylus",
                                    "A silver stylus that draws glowing runes in the air when used.", 0, 0, 2, 10),

        "vial_of_glowing_water": item.Item("Vial of Glowing Water",
                                           "A glass vial filled with water that glows with an inner light.", 1, 1, 1,
                                           10),

        "weathered_stone_tablet": item.Item("Weathered Stone Tablet",
                                            "A stone tablet etched with ancient runes and symbols.", 1, 1, 1, 10),

        "celestial_map": item.Item("Celestial Map",
                                   "A map of the stars that reveals hidden constellations.", 1, 1, 1, 10),

        "resonance_crystal": item.Item("Resonance Crystal",
                                       "A crystal that hums with a mysterious energy when touched.", 1, 1, 1, 10),
    }

    return items


def add_items_to_rooms(rooms, items):

    # Add items to rooms
    rooms["whispering_willows"].add_item(items["enchanted_flute"])
    rooms["mosaic_menagerie"].add_item(items["prismatic_lens"])
    rooms["runic_rotunda"].add_item(items["magical_stylus"])
    rooms["forgotten_fountain"].add_item(items["vial_of_glowing_water"])
    rooms["sunken_sanctuary"].add_item(items["weathered_stone_tablet"])
    rooms["overgrown_observatory"].add_item(items["celestial_map"])
    rooms["echoing_arboretum"].add_item(items["resonance_crystal"])