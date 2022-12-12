import pytest
from campcleanup import CampCleanup

@pytest.mark.parametrize("assignmentPair, expected", [
    ("2-4,6-8", [["2","3","4"], ["6","7","8"]]),
    ("2-3,4-5", [["2","3"], ["4","5"]]),
    ("5-7,7-9", [["5","6","7"], ["7","8","9"]]),
    ("2-8,3-7", [["2","3","4","5","6","7","8"], ["3","4","5","6","7"]]),
    ("6-6,4-6", [["6"], ["4","5","6"]]),
    ("2-6,4-8", [["2","3","4","5","6"], ["4","5","6","7","8"]])
])
def test_parse_creates_correct_structure(assignmentPair, expected):
    cc = CampCleanup()
    assert cc.parse(assignmentPair) == expected

def test_findFullyOverlappedAssignments_finds_correct_overlaps():
    assignments = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"
    ]

    cc = CampCleanup()
    cc.load(assignments)

    overlaps = cc.findFullyOverlappedAssignments()
    assert overlaps == [[["2","3","4","5","6","7","8"], ["3","4","5","6","7"]], [["6"], ["4","5","6"]]]
    assert len(overlaps) == 2

def test_findFullyOverlappedAssignments_finds_correct_overlaps_using_provided_input_file():
    f = open("input.txt", "r")
    assignments = f.readlines()
    f.close()

    cc = CampCleanup()
    cc.load(assignments)
    assert len(cc.findFullyOverlappedAssignments()) == 526

def test_findAnyOverlappedAssignments_finds_correct_overlaps():
    assignments = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"
    ]

    cc = CampCleanup()
    cc.load(assignments)

    overlaps = cc.findAnyOverlappedAssignments()
    assert overlaps == [
        [["5","6","7"], ["7","8","9"]],
        [["2","3","4","5","6","7","8"], ["3","4","5","6","7"]],
        [["6"], ["4","5","6"]],
        [["2","3","4","5","6"], ["4","5","6","7","8"]]
    ]
    assert len(overlaps) == 4

def test_findAnyOverlappedAssignments_finds_correct_overlaps_using_provided_input_file():
    f = open("input.txt", "r")
    assignments = f.readlines()
    f.close()

    cc = CampCleanup()
    cc.load(assignments)
    assert len(cc.findAnyOverlappedAssignments()) == 886