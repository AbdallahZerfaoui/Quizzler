# Quizzler

Quizzler is a simple quiz application built with Python and Tkinter. It retrieves a set of trivia questions from an API and allows the user to answer them. The application displays each question on a canvas and provides buttons for the user to select their answer. After answering all the questions, the user receives their final score.

## Requirements

- Python 3.x
- Tkinter module
- Requests module

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/quizzler.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the main.py script:

```
python main.py
```

2. The quiz interface will open, displaying the first question. Read the question and select your answer by clicking on the "True" or "False" button.

3. The application will display the next question. Repeat the process until you have answered all the questions.

4. Once you have answered all the questions, the final score will be displayed on the canvas.

## Customization

- You can modify the number of questions and the category in the `data.py` file by changing the values of the `amount` and `category` parameters in the `get_data_question` function.

- You can customize the appearance of the quiz interface by modifying the values in the `ui.py` file, such as the colors, button images, and canvas layout.

## Credits

- The trivia questions are fetched from the Open Trivia Database API (https://opentdb.com/).

- The quiz logic is implemented using the QuizBrain class from the quiz_brain module.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
