from cratemover import CrateMover9000, CrateMover9001
from supplystacks import SupplyStacks

def test_load_creates_correct_internal_data_structures():
    rearrangementProcedure = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2"
    ]

    ss = SupplyStacks(None)
    ss.load(rearrangementProcedure)

    assert ss.stacks == {
        1: ['Z', 'N'],
        2: ['M', 'C', 'D'],
        3: ['P']
    }
    assert ss.rearrangementProcedure == [
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

def test_topOfStacks_CrateMover9000_creates_correct_string_from_example_data():
    rearrangementProcedure = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2"
    ]

    ss = SupplyStacks(CrateMover9000())
    ss.load(rearrangementProcedure)

    updatedStacks = ss.rearrangeStacks()
    assert ss.topOfStacks(updatedStacks) == "CMZ"

def test_topOfStacks_CrateMover9001_creates_correct_string_from_example_data():
    rearrangementProcedure = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2"
    ]

    ss = SupplyStacks(CrateMover9001())
    ss.load(rearrangementProcedure)

    updatedStacks = ss.rearrangeStacks()
    assert ss.topOfStacks(updatedStacks) == "MCD"

def test_topOfStacks_CrateMover9000_creates_correct_string_using_provided_input_file():
    f = open("input.txt", "r")
    rearrangementProcedure = f.readlines()
    f.close()

    ss = SupplyStacks(CrateMover9000())
    ss.load(rearrangementProcedure)

    updatedStacks = ss.rearrangeStacks()
    assert ss.topOfStacks(updatedStacks) == "FZCMJCRHZ"

def test_topOfStacks_CrateMover9001_creates_correct_string_using_provided_input_file():
    f = open("input.txt", "r")
    rearrangementProcedure = f.readlines()
    f.close()

    ss = SupplyStacks(CrateMover9001())
    ss.load(rearrangementProcedure)

    updatedStacks = ss.rearrangeStacks()
    assert ss.topOfStacks(updatedStacks) == "JSDHQMZGF"
