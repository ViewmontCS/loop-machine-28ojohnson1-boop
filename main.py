import time, random, os, math

GAMBLECORE_VERSION = "2.0.0"

def main():
    typewrite("Welcome to...", 0.08)
    time.sleep(0.2)
    typewrite(f"Let\'s go gambling!!!!!! - Slot Machine Edition \033[33mv{GAMBLECORE_VERSION}\033[0m", 0.04)
    time.sleep(0.2)
    typewrite("Press enter to get started!", 0.04)
    typewrite("[Do it, hit enter]", 0.04)
    input("")
    gamble()

def clear():
    os.system('cls')

def print_gains(wins, losses):
    print(f"\033[32mWins\033[0m: {wins}\n\033[31mLosses\033[0m: {losses}")

def gamble():
    wheel = [0,1,2,3,4,5,6,7,8,9]
    numbers = []
    # I made that dummy list, but we need this to be random dangit!
    for _ in range(len(wheel)):
        numbers.append(random.randint(0, 9))
    rows = 3 #this is the target, the math is weird, and will most likely only work with 3 :)
    columns = round(len(numbers)/rows)
    print_machine(numbers, rows, columns, "/")
    time.sleep(0.1)
    print_machine(numbers, rows, columns, "-")
    time.sleep(0.2)
    print_machine(numbers, rows, columns, "\\")
    for i in range(10):
        # We need to increment the numbers on the top row, which is the first three numbers, or rather, numbers/rows numbers, we do this because our wheel of numbers, is bigger than three.
        numbers = numbers[:9]
        first_row = numbers[:(round(len(numbers)/rows))]
        for character in range(len(first_row)):
            # IF THE WHEELS MOVE AT DIFFERENT SPEEDS!!!!
            # new_number = str(int(first_row[int(character)])+1)
            # if not int(new_number) in wheel:
            #     new_number = wheel[0]
            new_number = random.randint(0, 9)
            first_row[int(character)] = int(new_number)
        numbers = numbers[-columns:] + numbers[:-columns]
        # apply the new row
        numbers = first_row + numbers[columns:]

        print_machine(numbers, rows, columns, "\\")
        time.sleep(i/120.0)
    print_machine(numbers, rows, columns, "-")
    time.sleep(0.1)
    print_machine(numbers, rows, columns, "/")
    points = calculate_points(numbers, rows)
    if input("Take a look at your payout! You can take it or play again!\n[Enter: Play Again, Type \'QUIT\' in all caps to quit]\n").upper() == "QUIT":
        typewrite("Well, \033[33mThanks for playing!\033[0m, I'll see you again sometimes soon!", 0.04)
        typewrite(f"Final payout: \033[33m{points}\033[0m", 0.08)
        return
    else:
        gamble()


def print_machine(numbers, rows, columns, handle_stage):
    clear()
    print(f"Let\'s go gambling!!!!!! - Slot Machine Edition \033[33mv{GAMBLECORE_VERSION}\033[0m")
    for i in range(rows):
        base = str(numbers[(i*columns):(i*columns)+columns:1])
        # THIS IS THE ROW WITH THE HANDLE, AND THE ROW WITH OUR NUMBER
        if i == math.floor(rows/2):
            base += handle_stage
        print(f"\033[36m{base}\033[0m ")
    potential_payout = calculate_points(numbers, rows)
    print(f"Potential payout: \033[33m{potential_payout}\033[0m")

def calculate_points(numbers, rows):
    # check for horizontal matches.
    columns = round(len(numbers)/rows)
    win_types = []
    for character in range(len(numbers[::columns])):
        if len(set(numbers[character:character+columns])) == 1:
            win_types.append("H")
    # check for diagonals
    # forwards diagonal
    if len(set(numbers[::columns+1])) == 1:
        win_types.append("D")
    # backwards diagonal
    # forwards diagonal
    trim = numbers[:-(columns-1)]
    if len(set(trim[:columns:columns-1])) == 1:
        win_types.append("D")
    # calculate total
    total = 0
    for item in win_types:
        match item:
            case "H":
                total += 10
            case "D":
                total += 15 
    for item in numbers:
        total += round(item*0.3)
    return total

def typewrite(text, increment):
    for character in text:
        time.sleep(increment)
        print(character, end="", flush=True)
    print("\n")


if __name__ == "__main__":
    main()
