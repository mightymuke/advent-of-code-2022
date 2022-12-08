import pytest
from rucksackreorganization import RucksackReorganization, RucksackItemType

@pytest.mark.parametrize("itemtype, expected", [
    ('a', 1),
    ('m', 13),
    ('z', 26),
    ('A', 27),
    ('M', 39),
    ('Z', 52),
    ('*', 0)
])
def test_item_priority(itemtype, expected):
    t = RucksackItemType(itemtype)
    assert t.priority() == expected

def test_findDuplicates_with_example_rucksacks():
    rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    rr = RucksackReorganization()
    rr.load(rucksacks)

    assert rr.findDuplicates() == ['p', 'L', 'P', 'v', 't', 's']

def test_duplicate_sum_using_example_rucksacks():
    rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    rr = RucksackReorganization()
    rr.load(rucksacks)

    assert rr.calculatePrioritySum(rr.findDuplicates()) == 157

def test_duplicate_sum_using_provided_input_file():
    f = open("input.txt", "r")
    rucksacks = f.readlines()
    f.close()

    rr = RucksackReorganization()
    rr.load(rucksacks)

    assert rr.calculatePrioritySum(rr.findDuplicates()) == 7872

@pytest.mark.parametrize("rucksacks, expected", [
    ([['a', 'b', 'c'], ['A', 'B', 'C']], []),
    ([['a', 'b', 'c'], ['A', 'b', 'C']], ['b']),
    ([['a', 'b', 'c'], ['a', 'b', 'C']], ['a', 'b']),
    ([['a', 'b', 'c']], ['a', 'b', 'c']),
    ([], [])
])
def test_findCommonItemInAllRucksacks_finds_correct_item(rucksacks, expected):
    rr = RucksackReorganization()
    assert rr.findCommonItemInAllRucksacks(rucksacks) == expected

def test_findGroupBadges_using_example_rucksacks():
    rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    rr = RucksackReorganization()
    rr.load(rucksacks)

    assert rr.findGroupBadges() == ['r', 'Z']

def test_badge_sum_using_example_rucksacks():
    rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    rr = RucksackReorganization()
    rr.load(rucksacks)

    assert rr.calculatePrioritySum(rr.findGroupBadges()) == 70

def test_badge_sum_using_provided_input_file():
    f = open("input.txt", "r")
    rucksacks = f.readlines()
    f.close()

    rr = RucksackReorganization()
    rr.load(rucksacks)

    assert rr.calculatePrioritySum(rr.findGroupBadges()) == 2497
