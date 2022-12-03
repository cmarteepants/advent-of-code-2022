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
    (PlayersChoice.ROCK, MyChoice.PAPER): Score.WIN.value,
    (PlayersChoice.ROCK, MyChoice.SCISSORS): Score.LOSE.value,
    (PlayersChoice.ROCK, MyChoice.ROCK): Score.DRAW.value,
    (PlayersChoice.PAPER, MyChoice.SCISSORS): Score.WIN.value,
    (PlayersChoice.PAPER, MyChoice.PAPER): Score.DRAW.value,
    (PlayersChoice.PAPER, MyChoice.ROCK): Score.LOSE.value,
    (PlayersChoice.SCISSORS, MyChoice.ROCK): Score.WIN.value,
    (PlayersChoice.SCISSORS, MyChoice.SCISSORS): Score.DRAW.value,
    (PlayersChoice.SCISSORS, MyChoice.PAPER): Score.LOSE.value,
    # Part 2
    (PlayersChoice.ROCK.value, DesiredOutcome.WIN): MyChoice.PAPER.value,
    (PlayersChoice.ROCK.value, DesiredOutcome.LOSE): MyChoice.SCISSORS.value,
    (PlayersChoice.ROCK.value, DesiredOutcome.DRAW): MyChoice.ROCK.value,
    (PlayersChoice.PAPER.value, DesiredOutcome.WIN): MyChoice.SCISSORS.value,
    (PlayersChoice.PAPER.value, DesiredOutcome.DRAW): MyChoice.PAPER.value,
    (PlayersChoice.PAPER.value, DesiredOutcome.LOSE): MyChoice.ROCK.value,
    (PlayersChoice.SCISSORS.value, DesiredOutcome.WIN): MyChoice.ROCK.value,
    (PlayersChoice.SCISSORS.value, DesiredOutcome.DRAW): MyChoice.SCISSORS.value,
    (PlayersChoice.SCISSORS.value, DesiredOutcome.LOSE): MyChoice.PAPER.value,
}


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    rounds = [r.split() for r in data]

    score = 0
    for hand in rounds:
        players_hand = PlayersChoice(hand[0])
        my_hand = MyChoice(hand[1])
        score += Score[my_hand.name].value + RULES[(players_hand, my_hand)]

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
