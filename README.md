[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21697073)
Using loops, you will create a simple text-based slot machine.

**1. Setting up variables**

Create an integer that holds the user's score. The user will use their score to pay for playing, so initialize it to an amount that lets them play a reasonable number of times (100 should be good).

Create an integer that holds the payout for when the user wins (the payout should be more than the play cost). If you want to have varied payouts based on how they win, have multiple variables for each payout amount, with appropriate variable names.

**2. Welcome Message**

Print a welcome message to the player. It can be simple.

**3. Paying for the game**

Using a while loop, allow the user to play the game. If the user has no score left, exit the while loop. Subtract the play cost from the score here (5 is a fine amount).

**4. Slot Roll**

Begin the slot roll by clearing the terminal using the provided clear() function. Generate a set of 9 random numbers from 0-9 to display. Print the numbers so layout is as follows:

|1|2|3|
|4|5|6|
|7|8|9|

(It doesn't have to look exactly like this, but should have the numbers in this layout)

Using a for loop, repeat the slot roll as many times as you feel looks good. It should run for NO LONGER than 3 seconds.

*For extra challenge, simulate the roll by moving the numbers down the wheels instead of just generating random numbers!*

**5. Check for Payout**

If the user has 3 matching symbols across the wheels (diagonal, or horizontal), they win! Add the payout to the user's score. With the layout above, there are 5 ways to win:

1=2=3
4=5=6
7=8=9
1=5=9
7=5=3

Make sure you check all possible win states. The user can get more than one of these matching, and should get all payouts applicable (use if,- if, not if - elif).

*For an extra challenge, have different payout amounts based on how the user won (which direction and what number).*

**6. Cash out or play again**

If the user still has score, ask if they want to play again. If they say no, quit the game.
