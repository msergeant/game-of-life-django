from django.test import TestCase

from .models import World

class WorldModelTests(TestCase):

    def lists_match(self, list_a, list_b):
        self.assertEqual(len(list_a), len(list_b))
        self.assertEqual(sorted(list_a), sorted(list_b))

    def test_init_with_empty_list(self):
        """
        World initializes with an empty list
        """
        world = World()
        self.lists_match(world.live_cells(), [])

    def test_init_with_one_cell(self):
        """
        World initializes with one cell
        """
        world = World([[0,0]])
        self.lists_match(world.live_cells(), [[0,0]])

    def test_init_with_multiple_cells(self):
        """
        World initializes with multiple cells
        """
        world = World([[0,0], [0,1]])
        self.lists_match(world.live_cells(), [[0,0], [0,1]])

    def test_init_removes_duplicates(self):
        """
        World initialize removes duplicates
        """
        world = World([[0,0], [0,1], [0,0]])
        self.lists_match(world.live_cells(), [[0,0], [0,1]])

    def test_alive_returns_false(self):
        """
        World is_alive returns False
        """
        world = World([[0,0], [0,1], [0,0]])
        self.assertIs(world.is_alive([0,7]), False)

    def test_alive_returns_true(self):
        """
        World is_alive returns True
        """
        world = World([[0,0], [0,1], [0,0]])
        self.assertIs(world.is_alive([0,1]), True)

    def test_next_iteration_returns_empty(self):
        """
        World next_iteration returns empty
        """
        next_world = World().next_iteration()
        self.lists_match(next_world.live_cells(), [])

    def test_next_iteration_returns_expected_list(self):
        """
        World next_iteration returns a known world
        """
        initial_cells = [
          [7,0], [7,1], [7,2], [7,3], [7,4], [7,5], [7,6], [7,7], [7,8], [7,9]
        ]
        next_world = World(initial_cells).next_iteration()
        expected_cells = [
            [6, 1], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7], [6,8],
            [7, 1], [7,2], [7,3], [7,4], [7,5], [7,6], [7,7], [7,8],
            [8, 1], [8,2], [8,3], [8,4], [8,5], [8,6], [8,7], [8,8]
        ]
        self.lists_match(next_world.live_cells(), expected_cells)



