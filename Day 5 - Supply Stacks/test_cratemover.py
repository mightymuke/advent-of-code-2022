from cratemover import CrateMover9000, CrateMover9001

def test_CrateMover9000_moveCrates():
    stacks = {
        1: ['Z', 'N'],
        2: ['M', 'C', 'D'],
        3: ['P']
    }
    procedure = [
        {
            "move": 1,
            "from": 2,
            "to": 1
        },
        {
            "move": 3,
            "from": 1,
            "to": 3
        },
        {
            "move": 2,
            "from": 2,
            "to": 1
        },
        {
            "move": 1,
            "from": 1,
            "to": 2
        }
    ]

    cm = CrateMover9000()

    assert cm.moveCrates(stacks, procedure) == {
        1: ['C'],
        2: ['M'],
        3: ['P', 'D', 'N', 'Z']
    }

def test_CrateMover9001_moveCrates():
    stacks = {
        1: ['Z', 'N'],
        2: ['M', 'C', 'D'],
        3: ['P']
    }
    procedure = [
        {
            "move": 1,
            "from": 2,
            "to": 1
        },
        {
            "move": 3,
            "from": 1,
            "to": 3
        },
        {
            "move": 2,
            "from": 2,
            "to": 1
        },
        {
            "move": 1,
            "from": 1,
            "to": 2
        }
    ]

    cm = CrateMover9001()

    assert cm.moveCrates(stacks, procedure) == {
        1: ['M'],
        2: ['C'],
        3: ['P', 'Z', 'N', 'D']
    }