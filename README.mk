# Random Number Generator

This project is a simple graphical application created with **Tkinter** that allows the user to generate random numbers within a specified range.
The interface is interactive, letting the user generate a random number, request another one, or restart the process when desired.

## Features

- Allows the user to enter a positive number to define the range for random numbers.
- Generates a random number within the specified range and displays it on the screen.
- Once all numbers in the range have been generated, a message is displayed informing the user that no more numbers are available.
- Allows the user to generate new numbers or restart the application to begin again.

## Technologies

- **Python 3**: Programming language.
- **Tkinter**: Library for creating the graphical user interface.
- **random.choice()**: Method used to randomly select numbers from a list.

## Installation

To run this application, make sure you have Python 3 and Tkinter installed on your machine. Tkinter is typically pre-installed with Python, so you usually don't need to install it separately.

### Steps to run:

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/camilafresitaa/RandomNumberGenerator
   ```

2. Navigate to the project folder:

   ```
   cd RandomNumberGenerator
   ```

3. Run the script:

   ```
   python random_number_generator.py
   ```


## Usage

1. When the application starts, you will be prompted to enter a positive number greater than 0 in the input field.
2. After entering the number, the application will generate a random number within the range from 1 to the number you entered.
3. You can click "Yes" to generate another number or "No" to start over.
4. Once all numbers in the range have been generated, a message will appear stating "All numbers have been generated."
5. If you wish, you can click "Press here to restart!" to restart the process.