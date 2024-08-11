import unittest
from unittest.mock import patch, MagicMock
from main import init_rooms, init_player, Player, Room, init_room_connections, init_items, init_room_items

class TestGame(unittest.TestCase):
    """
    Unit test class for testing the game functionality.
    """

    @patch('builtins.input', return_value='Arthur')
    @patch('random.choice', return_value='the Brave')
    def test_player_name_and_title(self, mock_input, mock_random_choice):
        """
        Test that the player's name and title are correctly set.

        Args:
            mock_input (MagicMock): Mocked input function.
            mock_random_choice (MagicMock): Mocked random.choice function.
        """
        rooms = init_rooms()
        player = init_player(rooms)
        self.assertEqual(player.name, 'Arthur the Brave')

    def test_player_initial_stats(self):
        """
        Test that the player's initial stats are correctly set.
        """
        player = Player("Test Player", 5, 5, 5, 0, 1, Room("Test Room", "A room for testing"))
        self.assertEqual(player.dex, 5)
        self.assertEqual(player.int, 5)
        self.assertEqual(player.wis, 5)
        self.assertEqual(player.exp, 0)
        self.assertEqual(player.level, 1)

    def test_player_move(self):
        """
        Test that the player can move to a different room.
        """
        rooms = init_rooms()
        init_room_connections(rooms)
        player = Player("Test Player", 5, 5, 5, 0, 1, rooms["verdant_vestibule"])
        rooms["verdant_vestibule"].set_player(player)
        player.move('north')
        self.assertEqual(player.current_room.name, "Whispering Willows")

    def test_player_pickup_item(self):
        """
        Test that the player can pick up an item.
        """
        rooms = init_rooms()
        items = init_items()
        init_room_items(rooms, items)
        player = Player("Test Player", 5, 5, 5, 0, 1, rooms["verdant_vestibule"])
        rooms["whispering_willows"].set_player(player)
        player.move('north')
        player.add_item(items["enchanted_flute"])
        self.assertIn(items["enchanted_flute"], player.items)

    def test_player_level_up(self):
        """
        Test that the player levels up correctly after gaining experience.
        """
        player = Player("Test Player", 5, 5, 5, 9, 1, Room("Test Room", "A room for testing"))
        player.add_experience(1)
        self.assertEqual(player.level, 2)
        self.assertEqual(player.exp, 0)

if __name__ == '__main__':
    unittest.main()