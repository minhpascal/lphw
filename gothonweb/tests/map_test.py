from nose.tools import *
from gothonweb.map import *

def test_room():

    assert_equal(central_corridor.name, "Central Corridor")
    assert_equal(central_corridor.paths, {
    'shoot!': death("central_corridor"),
    'dodge!': death("central_corridor"),
    'tell a joke': laser_weapon_armory
})

def test_room_paths():
    test_room = Room("Test Room", "This room is there for the tests")
    north_room = Room("North Room", "End point reached.")
    south_room = Room("South room", "End point reached.")

    test_room.add_paths({'north': north_room, 'south': south_room})
    assert_equal(test_room.go('north'), north_room)
    assert_equal(test_room.go('south'), south_room)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    assert_equal(START.go('shoot!'), death("central_corridor"))
    assert_equal(START.go('dodge!'), death("central_corridor"))

    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)