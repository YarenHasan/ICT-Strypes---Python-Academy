# 🃏 Blackjack Game (Console-Based Python)
This is a simple text-based implementation of the classic Blackjack game, also known as 21, built using Python. It features object-oriented design with classes for Card, Deck, Hand, and Chips, and includes core gameplay mechanics like betting, hit/stand choices, Ace adjustment, and win/loss scenarios.
<br />

🎮 How to Play:

  * Each player starts with two cards and aims to get as close to 21 as possible without going over.
  * The Dealer must hit until their cards total 17 or more.
  * Aces can count as either 11 or 1, depending on the best advantage.
  * You start with 100 chips and can place a bet each round.
  * Player decides to hit (h) or stand (s).
  * After each round, you’re asked if you'd like to play again.
<br />

🧠 Game Rules Summary:

 * Number cards are worth their face value.
 * Face cards (Jack, Queen, King) are worth 10.
 * Ace is worth 11, but adjusts to 1 if you bust.
<br />


🧱 Code Structure:

The game logic is built using OOP concepts with the following classes:

 * Card: Represents a single card with a suit and rank.
 * Deck: Represents a collection of 52 Card objects. Includes shuffle() and deal().
 * Hand: Tracks the cards in a player's or dealer's hand, their value, and adjusts for Aces.
 * Chips: Manages betting and chip totals.
<br />


🧩 Core Functions:

Function	Description:

 * take_bet():	Prompts the player to place a bet and validates it
 * hit():	Deals a card and adjusts for Aces
 * hit_or_stand():	Allows the player to choose to hit or stand
 * show_some():	Shows player's full hand and one dealer card
 * show_all():	Reveals both hands and their values at the end
 * player_busts():	Triggered if the player exceeds 21
 * dealer_busts():	Triggered if the dealer exceeds 21
 * player_wins():	Triggered when player has higher value than dealer
 * dealer_wins():	Triggered when dealer beats player
 * push():	Triggered in a tie
