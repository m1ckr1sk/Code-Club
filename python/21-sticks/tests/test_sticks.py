from sticks.sticks import Sticks


def test_initialise_game_with_player():
    sticks = Sticks()
    sticks.add_player('Steve')
    assert sticks
    assert len(sticks.players) == 1


def test_initialise_game_with_players():
    sticks = Sticks()
    sticks.add_player('Steve')
    sticks.add_player('Jim')
    assert sticks
    assert len(sticks.players) == 2


def test_player_takes_stick():
    sticks = Sticks()
    sticks.add_player('Steve')
    sticks.add_player('Jim')
    assert sticks
    assert len(sticks.players) == 2

    sticks.take_sticks('Steve', 1)

    assert sticks.players['Steve'][0] == 1
    assert sticks.get_sticks_remaining() == 20


def test_player_takes_last_stick_wins():
    sticks = Sticks()
    sticks.add_player('Steve')
    sticks.add_player('Jim')
    assert sticks
    assert len(sticks.players) == 2

    for _ in range(0, 10):
        print(sticks.take_sticks('Steve', 1))
        print(sticks.take_sticks('Jim', 1))
        print(f" ## Sticks Remaining : {str(sticks.get_sticks_remaining())}")

    assert sticks.take_sticks('Steve', 1) == 'Steve takes 1 - Steve Wins!'
    assert sticks.get_sticks_remaining() < 1


def test_player_cannot_take_more_than_3_sticks():
    sticks = Sticks()
    sticks.add_player('Steve')
    sticks.add_player('Jim')
    assert sticks
    assert len(sticks.players) == 2

    assert sticks.take_sticks('Steve', 4) == \
        'Players can only take between 1 and 3 sticks in a turn'
    assert sticks.get_sticks_remaining() == 21


def test_player_cannot_take_less_than_1_sticks():
    sticks = Sticks()
    sticks.add_player('Steve')
    sticks.add_player('Jim')
    assert sticks
    assert len(sticks.players) == 2

    assert sticks.take_sticks('Steve', 0) == \
        'Players can only take between 1 and 3 sticks in a turn'
    assert sticks.get_sticks_remaining() == 21
