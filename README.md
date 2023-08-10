# cesar-palace-virtual-casino

## Notes and bugs:

-Blackjack game don't show who win the match

-The sum after player or dealer takes other card is broken

-We will be adding a virtual coin system for betting, allowing players to place bets and earn rewards.


---

## Setting Up the 'casino_venv' Virtual Environment

Before you begin, please ensure that you have the `venv` module installed. The `venv` module is included in the standard library for Python 3.3 and later versions. If you're using an earlier version of Python, you may need to install it separately.

To check if you have the `venv` module installed, open a terminal and execute the following command:

```bash
python3 -m venv --help
```

If you receive a help message for the `venv` module, you're all set. If not, you can install it using the following command:

```bash
pip install virtualenv
```

Once you have the `venv` module installed, you can proceed with creating and using the 'casino_venv' virtual environment as described below.



## Setting Up the 'casino_venv' Virtual Environment

The 'casino_venv' virtual environment is used to isolate and manage project-specific dependencies for our casino-related project. Below are instructions on how to create and activate this virtual environment.

### Creating the Virtual Environment

To create the 'casino_venv' virtual environment, follow these steps:

1. Open a terminal on your operating system.

2. Navigate to the main location of your project or the folder where you want to create the virtual environment.

3. Execute the following command to create the virtual environment:

   ```bash
   python3 -m venv casino_venv
   ```

### Activating the Virtual Environment

Once the virtual environment is created, follow these steps to activate it:

- On Windows:
  ```bash
  casino_venv\Scripts\activate
  ```

- On macOS and Linux:
  ```bash
  source casino_venv/bin/activate
  ```

When you activate the virtual environment, you'll notice that the terminal prompt changes to indicate that you are working within 'casino_venv'.

### Deactivating the Virtual Environment

When you're done working in the virtual environment, you can deactivate it at any time using the following command:

```bash
deactivate
```

Please note that while working in the 'casino_venv' virtual environment, any dependencies you install and modifications you make to the project will only affect this isolated environment. This ensures that libraries and configurations for your casino-related project remain separate from other Python projects and environments.

---

## Games rules

## Blackjack

1. The goal of the game is to have a hand value closer to 21 than the dealer's hand, without exceeding 21.
2. Number cards (2-10) are worth their face value, face cards (J, Q, K) are worth 10, and an Ace (A) can be worth 1 or 11, whichever is more favorable.
3. At the start, the player and the dealer each receive two cards. The player's cards are dealt face up, while one of the dealer's cards is face up (known as the "face-up card") and the other is face down.
4. The player can choose to "hit" (draw another card) or "stand" (keep the current hand). The player can continue to hit until they stand or their hand value exceeds 21 (resulting in a "bust").
5. After the player completes their turn, the dealer reveals their face-down card.
6. The dealer must hit until their hand value reaches at least 17. If the dealer's hand exceeds 21, the player wins.
7. If neither the player nor the dealer busts, the one with the hand value closest to 21 wins. In case of a tie, it's a push (a tie), and no one wins or loses.