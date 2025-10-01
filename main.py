#include <iostream>
#include <cctype> // For isalpha() and tolower()
#include <limits> // For numeric_limits
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

        // Input validation
        if (!std::isalpha(guess)) {
            std::cout << "Invalid input! Please enter a single letter.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }
        guess = std::tolower(guess);
        if (game.isLetterAlreadyGuessed(guess)) {
            std::cout << "You already guessed '" << guess << "'! Try a different letter.\n";
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }
        
        game.makeGuess(guess);
    }

    game.displayGameState();
    if (game.isWordGuessed()) {
        std::cout << "Congratulations! You guessed the word!\n";
    } else {
        std::cout << "Game Over! The word was: " << game.getWord() << "\n";
    }

    return 0;
}
