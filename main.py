#include <iostream>
#include "Hangman.h"

int main() {
    Hangman game;
    char guess;

    std::cout << "Welcome to Hangman!\n";
    game.startGame();

    while (!game.isGameOver()) {
        game.displayGameState();
        std::cout << "Enter a letter: ";
        std::cin >> guess;
        game.makeGuess(tolower(guess));
    }

    game.displayGameState();
    if (game.isWordGuessed()) {
        std::cout << "Congratulations! You guessed the word!\n";
    } else {
        std::cout << "Game Over! The word was: " << game.getWord() << "\n";
    }

    return 0;
}
