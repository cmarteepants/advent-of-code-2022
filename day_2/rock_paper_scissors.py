from enum import Enum


class PlayersChoice(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class MyChoice(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class DesiredOutcome(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


class Score(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LOSE = 0
    DRAW = 3
    WIN = 6


RULES = {
    # Part 1
    (PlayersChoice.ROCK, MyChoice.PAPER): Score.WIN,
    (PlayersChoice.ROCK, MyChoice.SCISSORS): Score.LOSE,
    (PlayersChoice.ROCK, MyChoice.ROCK): Score.DRAW,
    (PlayersChoice.PAPER, MyChoice.SCISSORS): Score.WIN,
    (PlayersChoice.PAPER, MyChoice.PAPER): Score.DRAW,
    (PlayersChoice.PAPER, MyChoice.ROCK): Score.LOSE,
    (PlayersChoice.SCISSORS, MyChoice.ROCK): Score.WIN,
    (PlayersChoice.SCISSORS, MyChoice.SCISSORS): Score.DRAW,
    (PlayersChoice.SCISSORS, MyChoice.PAPER): Score.LOSE,
    # Part 2
    (PlayersChoice.ROCK, DesiredOutcome.WIN): MyChoice.PAPER,
    (PlayersChoice.ROCK, DesiredOutcome.LOSE): MyChoice.SCISSORS,
    (PlayersChoice.ROCK, DesiredOutcome.DRAW): MyChoice.ROCK,
    (PlayersChoice.PAPER, DesiredOutcome.WIN): MyChoice.SCISSORS,
    (PlayersChoice.PAPER, DesiredOutcome.DRAW): MyChoice.PAPER,
    (PlayersChoice.PAPER, DesiredOutcome.LOSE): MyChoice.ROCK,
    (PlayersChoice.SCISSORS, DesiredOutcome.WIN): MyChoice.ROCK,
    (PlayersChoice.SCISSORS, DesiredOutcome.DRAW): MyChoice.SCISSORS,
    (PlayersChoice.SCISSORS, DesiredOutcome.LOSE): MyChoice.PAPER,
}


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    rounds = [r.split() for r in data]

    score = 0
    for hand in rounds:
        players_hand = PlayersChoice(hand[0])
        my_hand = MyChoice(hand[1])
        score += Score[my_hand.name].value + RULES[(players_hand, my_hand)].value

    print(f"The total score, assuming the second column represents the hand I should play, is {score}")

    score = 0
    for hand in rounds:
        players_hand = PlayersChoice(hand[0])
        desired_outcome = DesiredOutcome(hand[1])
        my_hand = MyChoice(RULES[(players_hand, desired_outcome)])
        score += (Score[my_hand.name].value + Score[desired_outcome.name].value)

    print(f"As the second column actually represents the desired outcome, the total score actually is {score}")


if __name__ == "__main__":
    main()
