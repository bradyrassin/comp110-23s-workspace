"""Creating a Choose Your Own Adventure."""

__author__ = "730560378"


from random import randrange


points: int = 0
player: str = ""
BAD_CHOICE: str = "\U0001F44E"


def main() -> None:
    """Entrypoint to the game loop."""
    game_end: bool = True
    global points, player
    while game_end == True:
        greet()
        decision_one()
        print(f"After surveying the island a little more, {player} notices smoke in the distance, and decides to run over to it.")
        random_discovery(points)
        print(f"Thanks for playing Survivor, {player}! Your current point total is: {points} points!!!")
        print(f"After your last encounter you hear a helicopter flying in the distance, {player} has two options")
        print(f"Option 1: {player} runs to the top of the mountain, signaling for help and ending the game by escaping")
        print("Option 2: Start again on the mystery island, discover more secrets and keep adding to your point total.")
        choice: int = 0
        choice = int(input("Print your decision: "))
        while choice != 1 and choice != 2:
            print("That was not a valid answer, try again")
            choice = int(input("Print your decision: "))
        if choice == 1:
            game_end = False
        if choice == 2: 
            print("Here we go again")


def greet() -> None:
    """Greeting the player."""
    print("Welcome to Survivor, in this game you are stranded on a deserted island, and must make the right decisions to not only survive but get off the island.")
    global player
    player = input("What is your player name? ")


def decision_one() -> None:
    """The initial decision of the player."""
    global points
    print(f"{player} wakes up one morning on a mysterious island, you don't know how you got there, and are stranded there by yourself with no other resources {BAD_CHOICE}.")
    print(f"After quickly scanning the island, {player} realizes they have three options. You can take a left and explore the mountaneous area, take a right and explore the surrounding beaches, or go straight and explore the forest ahead of you.")
    choice_one: int = int(input("If you want to go to the mountains, enter '1', if you want to go to the other beaches, enter '2', and if you want to go to the forest, enter '3'. "))
    while choice_one != 1 and choice_one != 2 and choice_one != 3:
        choice_one = int(input("That was not one of the choices, try again. "))
    if choice_one == 1:
        points += 1
        mountain()
    elif choice_one == 2:
        beach()
    else:
        points += 2
        forest() 


def mountain() -> None:
    """If the player decides to go to the mountain."""
    global points
    print(f"{player} notices that there are a few animals grazing, as well as some folliage further away")
    print("Do you want to: 1. Hunt the animals  2. Explore the foliage  3. Climb to the summit of the mountain? ")
    mountain_choice: int = int(input("Enter the number that matches the option you want to choose "))
    while mountain_choice != 1 and mountain_choice != 2 and mountain_choice != 3:
        mountain_choice = int(input("That was not one of the choices, try again. "))
    if mountain_choice == 1:
        points += 1
        print(f"You were successfully able to catch some smaller animals, but without weapons you were not able to get a large food source {BAD_CHOICE}.")
    if mountain_choice == 2:
        points += 2
        print("You were able to find plenty of fruits, as well as a fresh water source.") 
    if mountain_choice == 3:
        print(f"You just wasted copious amounts of energy climbing to the top of a mountain with nothing on it {BAD_CHOICE}. ")    


def beach() -> None:
    """If the player decides to go to the beach."""
    global points
    print(f"{player} notices that there are a some fish swimming and crabs crawling")
    print("Do you want to: 1. Try catching some fish  2. Try catching some crabs  3. Keep walking along the beach? ")
    beach_choice: int = int(input("Enter the number that matches the option you want to choose "))
    while beach_choice != 1 and beach_choice != 2 and beach_choice != 3:
        beach_choice = int(input("That was not one of the choices, try again. "))
    if beach_choice == 1:
        print(f"Without a fishing rod, you couldn't catch any fish. But at least you enjoyed a nice swim {BAD_CHOICE}")
    if beach_choice == 2:
        points += 1
        print("You were able to catch a couple crabs, holding you off until the next meal.") 
    if beach_choice == 3:
        points += 2
        print("Since you kept walking, you found some Bananas growing and were able to stock up on resources. ")


def forest() -> None:
    """If the player decides to go to the forest."""
    global points
    print(f"{player} notices that there is a river flowing nearby")
    print("Do you want to: 1. Cross the river and keep walking  2. Walk upstream  3. Swim downstream? ")
    forest_choice: int = int(input("Enter the number that matches the option you want to choose "))
    while forest_choice != 1 and forest_choice != 2 and forest_choice != 3:
        forest_choice = int(input("That was not one of the choices, try again. "))
    if forest_choice == 1:
        print(f"You cross the river and get stuck in some quicksand, taking you a lot of time and energy to get out{BAD_CHOICE} ")
    if forest_choice == 2:
        points += 1
        print("You were able to find the water source which happens to be a waterfall, although not very useful it is beautiful!.") 
    if forest_choice == 3:
        points += 2
        print("After swimming down you find a small pond, which is among the most prosperous areas in the entire island, with wildlife thriving giving you easy food and water. ")


def random_discovery(points: int) -> int:
    """Random discovery from the fire."""
    outcome: int = randrange(1, 3)
    if outcome == 1:
        print(f"{player} walks up to the smoke and discovers another person on the island. After trying to approach this armed randomer with hopes of survival, they start yelling and chase you away. They don't speak English, and you narrowly escape them {BAD_CHOICE}.")
        points -= 1
        return points
    elif outcome == 2:
        print(f"{player} realizes that the fire was recently put out, but that they left cooked food. You quickly eat it and run away trying to avoid conflict.")
        points += 1
        return points
    else:
        print(f"{player} finds another survivor on the island who speaks English. Although they have no intention of leaving, they give you hints on the island and tell you the easiest way to escape")
        points += 2
        return points


if __name__ == "__main__":
    main()
