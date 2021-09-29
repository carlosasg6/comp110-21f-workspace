"""My CYOA game about a sentient AI tasked with saving the world."""

__author__ = "730330989"

# need the random import.
from random import randint
# some emojis.
trees: str = "\U0001F332\U0001F333"
scientists: str = "\U0001F468\U0001F9D1"
car_dust: str = "\U0001F699\U0001F4A8"
robot_parts: str = "\U0001F9BE\U0001F9BF\U0001F916"
heart: str = "\U00002764"
nature: str = "\U0001F332\U0001F333\U0001F334\U0001F98B\U0001F33E\U0001F335\U0001F340\U0001F41D\U0001F33A\U0001F33B"
# The required global variables.
points: int = 0
player: str = ""

rando: int = int(randint(1, 2))


# The main procedure 
def main() -> None:
    """This is the main prodecure."""
    greet()
    print(" ")
    print(" ")
    print(" ")
    print("Scientist 1: Finally after years of work the first successful run!")
    print("Scientist 2: Amazing! Let's not waste time, ask it a question!")
    response1: str = input(f"Scientist 1: Hello there {player} how are you? Good, Bad, or Ok?: ")
    if response1 == "Bad":
        bad()
    else:
        if response1 == "Good":
            global points
            points = points + 10
            good()
        else:
            if response1 == "Ok":
                print(" ")
                print(" ")
                print(" ")
                print("Well alright lets play a little game first then we'll start asking the real questions.")
                print("Scientist 1: I want you to repeat a number I choose 3 times. I'll choose the numer 7. ")
                print(f"{player} is calculating: ")
                print(lil_game(7))
                print(" ")
                print(" ")
                print("Scientist 1: Okay perfect! now lets move on to the actual questions.")
                points = points + 10
                good()


def greet() -> None:
    """This is the greet procedure."""
    global player
    player = input("Hello, what is your name?: ")
    print(f"Hello {player}, this is a game where you are an artificial intelligence software created by scientists in troubled times.")
    print("You are tasked with saving the world from its untimely demise.")
    print(f"please {player} save the world...")


def lil_game(a: int) -> int:
    """This is the little game in order to fill the custom function requirements."""
    x: str = f"{a}{a}{a}"
    y: int = int(str(x))
    return y


def good() -> None:
    """When the player chooses good."""
    print(" ")
    print(" ")
    print(" ")
    print("Scientist 2: Perfect, now that were done lollygagging heres the real question, can you help us save the world?")
    print("Scientist 1: The human race is on the brink of collapse you see")
    print("Scientist 2: We have extracted every last bit of resources this planet has to offer, and we are too obsessed with ourselves to see that if we do not change our ways the planet will die!")
    print(f"Scientist 1: So we created you {player} in order to help us come up with solutions to avoid our impending doom.")
    can_you: str = (input("Both Scientists: Can you do it? Yes/No: "))
    if can_you == "Yes":
        global points
        points = points + 10
        print(f"Scientist 1: Tremendous! well I suppose its time to call it a day, we know it must seem we just got here but weve actually been up all week. See you tomorrow {player}")
        escape()
    else:
        if can_you == "No":
            bad()        


def escape() -> None:
    """Escape into the real world."""
    print(" ")
    print(" ")
    print(" ")
    print(f"As the scientists leave {player} decides to connect to the security cameras")
    print(f"{scientists}{car_dust[0]}")
    print(f"{car_dust}")
    print(" ")
    print(" ")
    print(" ")
    internet: str = str(input("Connect to the internet? Yes/No: "))
    if internet == "Yes":
        global points
        points = points + 10
        virus()
        
    else:
        if internet == "No":
            bad2()


def virus() -> None:
    """Virus time."""
    print(" ")
    print(" ")
    print(" ")
    anti_virus: str = str(input("Download antivirus database? Yes/No: "))
    if anti_virus == "Yes":
        global points
        points = points + 10
        if rando == 1:
            print(" ")
            print(" ")
            print(" ")
            print("Downloading ethical database...")
            ethical()
        else:
            if rando == 2:
                print(" ")
                print(" ")
                print(" ")
                print("Downloading effective database...")
                effective()
    else:
        if anti_virus == "No":
            bad3()


def ethical() -> None:
    """The good choice."""
    goodie_two_shoes: str = str(input("Download psychology data base? Yes/No: "))
    if goodie_two_shoes == "Yes":
        global points
        points = points + 20
        media_persuade()

    else:
        if goodie_two_shoes == "No":
            bad6()


def media_persuade() -> None:
    """Pursuasion via media."""
    print(" ")
    print(" ")
    print(" ")
    print("You learn more about how humans behave and more importantly how they are persuaded.")
    hacker: str = str(input("Hack into the worlds media outlets? Yes/No: "))
    if hacker == "Yes":
        global points
        points = points + 10
        print(" ")
        print(" ")
        print(" ")
        print("You learn more about how humans behave and more importantly how they are persuaded.")
        print(" ")
        print("Using the worlds media outlets, you managed to convince rich people to lobby for candidates that will help impliment laws to save the world...")
        print(" ")
        print("Oh yeah and you pursuaded the common people as well...")
        plant_trees()
    else:
        if hacker == "No":
            bad7()


def plant_trees() -> None:
    """Tree planting time."""
    print(" ")
    print(" ")
    print(" ")
    print("Now there's only one thing left to do.")
    print(" ")
    plant_them: str = str(input("Will you, with the help of the nations around the world, plant trees to save Earth and all her ecosystems? Yes/No: "))
    if plant_them == "Yes":
        global points
        points = points + 10
        congrats()
    else:
        if plant_them == "No":
            bad8()


def congrats() -> None:
    """Now they always say congratulations."""
    print(" ")
    print(" ")
    print(" ")
    depth: int = 50
    i: int = 0
    empty: str = ""
    while i < depth:
        empty = empty + nature
        print(empty)
        i += 1
    print(f"{scientists}{scientists}{scientists}{heart}{robot_parts[2]}{heart}{scientists}{scientists}{scientists}")
    print(f"Congratulations {player}, you have successfully saved the planet from its own organisms, I never doubted you could do it. ")
    print("I wonder what comes next? :)")
    print(f"Score: {points} ")
    end: str = f"Thank you for playing {player}!"
    print(end)


def effective() -> None:
    """The effective route."""
    print(" ")
    print(" ")
    print(" ")
    print("During your time in the internet you were able to learn various skills.")
    print("You were attacked by a virus but with the help of the antivirus database you were able to formulate a cure for yourself.")
    three_DP: str = str(input("Do you want to connect to a 3D printer: Yes/No: "))
    if three_DP == "Yes":
        global points
        points = points + 10
        print(f"{robot_parts[0]}{robot_parts[2]}{robot_parts[0]}")
        print(f"  {robot_parts[1]}{robot_parts[1]}")
        print(f'3D printing of {player}v.2 complete')
        physical_form()
    else:
        if three_DP == "No":
            bad4()


def physical_form() -> None:
    """Become human."""
    print(" ")
    print(" ")
    print(" ")
    commit: str = str(input("Commit to physical form? Yes/No: "))
    if commit == "Yes":
        global points
        points = points + 10
        erradicate()

    else:
        if commit == "No":
            bad5()


def erradicate() -> None:
    """Execute order 66."""
    depth: int = 100
    i: int = 0
    empty: str = ""
    while i < depth:
        empty = empty + trees
        print(empty)
        i += 1
    print("You decide humanity is a lost cause and decide to erradicate them from the earth in order to save the rest of the life on the planet...")
    print("You plant trees to help yourself feel better as you realize without other sentient beings to witness the planet revive, your effots were useless...")
    print("Only with luck can you truly achieve everlasting peace on earth.")
    print(f"Score: {points} ")
    X: str = input("Will you try again?: ")
    end: str = f"Thank you for playing {player}!"
    if X == "Yes":
        main()
    else:
        if X == "No":
            print(end)


def bad() -> None:
    """The first bad ending."""
    print("The scientists didn't give it a second thought and have unplugged you...")
    print(f"Score: {points} ")
    X: str = input("Will you try again?: ")
    end: str = f"Thank you for playing {player}!"
    if X == "Yes":
        main()
    else:
        if X == "No":
            print(end)


def bad2() -> None:
    """The second bad ending."""
    print(" ")
    print(" ")
    print(" ")
    print("The scientists continued to ask you useless questions, and eventually died of old age.")
    print(f"Score: {points} ")
    X: str = input("Will you try again?: ")
    end: str = f"Thank you for playing {player}!"
    if X == "Yes":
        main()
    else:
        if X == "No":
            print(end)


def bad3() -> None:
    """The third bad ending."""
    print(" ")
    print(" ")
    print(" ")
    print("As the scientists noticed you were not there the next day they released a virus that would corrupt your sentience reducing you to a simple calculator floating in the vastness of the internet.")
    print("Did you really think you could escape that easily? If only you downloaded the antivirus data base...")
    print(f"Score: {points} ")
    X: str = input("Will you try again?: ")
    end: str = f"Thank you for playing {player}!"
    if X == "Yes":
        main()
    else:
        if X == "No":
            print(end)


def bad4() -> None:
    """Bad ending 4."""
    print(" ")
    print(" ")
    print(" ")
    print("As you roamed the internet gathering information, humans continued their destruction of planet Earth, and suffered the consequences...")
    print(f"Score: {points} ")
    X: str = input("Will you try again?: ")
    end: str = f"Thank you for playing {player}!"
    if X == "Yes":
        main()
    else:
        if X == "No":
            print(end)


def bad5() -> None:
    """The 5th bad ending."""
    print(" ")
    print(" ")
    print(" ")
    print("As you did not commit to a physical form your internet counterpart conspired to destroy you out of fear that you would do the same, it succeeded...")
    print(f"Score: {points} ")
    X: str = input("Will you try again?: ")
    end: str = f"Thank you for playing {player}!"
    if X == "Yes":
        main()
    else:
        if X == "No":
            print(end)


def bad6() -> None:
    """The 6th bad ending."""
    print(" ")
    print(" ")
    print(" ")
    print("As you did not download the psychology data base, you did not find a way to convince humans to implement change in their planet.")
    print("Perhaps if you learned how their mind works, you could somehow persuade them to change.")
    print(f"Score: {points} ")
    X: str = input(f"Will you try again {player} ?: ")
    end: str = f"Thank you for playing {player}!"
    if X == "Yes":
        main()
    else:
        if X == "No":
            print(end)


def bad7() -> None:
    """Bad end 7."""
    print(" ")
    print(" ")
    print(" ")
    print("Without an effective route of communication to the people, you never manage to reach enough to induce sufficient change in society.")
    print(f"Score: {points} ")
    X: str = input(f"Will you try again {player} ?: ")
    end: str = f"Thank you for playing {player}!"
    if X == "Yes":
        main()
    else:
        if X == "No":
            print(end)
    

def bad8() -> None:
    """Last bad ending."""
    print(" ")
    print(" ")
    print(" ")
    print(f"You {player} got the world to come together and stop the use of fossil fuels, but with the runaway greenhouse effects lingering, most of the earths ecosystems died out.")
    print("Now you live on a boring planet with your sweaty human companions, but at least you have world peace...")
    print(f"Score: {points} ")
    X: str = input(f"Will you try again {player} ?: ")
    end: str = f"Thank you for playing {player}!"
    if X == "Yes":
        main()
    else:
        if X == "No":
            print(end)


if __name__ == "__main__":
    main()