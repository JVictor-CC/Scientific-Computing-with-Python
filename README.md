# Scientific Computing with Python
- Content:
  - [Arithmetic Formatter](#1-first-project-build-a-arithmetic-formatter)
  - [Time Calculator](#2-second-project-build-a-time-calculator)
  - [Budget App](#3-third-project-build-a-budget-app)
  - [Polygon Area Calculator](#4-fourth-project-build-a-polygon-area-calculator)
  - [Probability Calculator](#5-fifth-project-build-a-probability-calculator)

## 1. First Project: Build a [Arithmetic Formatter]()

Project Url: <https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter>

Solution Url: <https://replit.com/@Joovictorvict19/boilerplate-arithmetic-formatter-1#arithmetic_arranger.py>

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Instructions:

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
* If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
* The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
* Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
* Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
If the user supplied the correct format of problems, the conversion you return will follow these rules:
* There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
* Numbers should be right-aligned.
* There should be four spaces between each problem.
* There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

## 2. Second Project: Build a [Time Calculator]()

Project Url: <https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator>

Solution Url: <https://replit.com/@Joovictorvict19/boilerplate-time-calculator#time_calculator.py>

Write a function named add_time that takes in two required parameters and one optional parameter:

* a start time in the 12-hour clock format (ending in AM or PM)
* a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
* The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

> add_time("11:43 PM", "24:20", "tueSday") -> Returns: 12:03 AM, Thursday (2 days later)

> add_time("6:30 PM", "205:12") -> Returns: 7:42 AM (9 days later)

## 3. Third Project: Build a [Budget App]()

Project Url: <https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app>

Solution Url: <https://replit.com/@Joovictorvict19/boilerplate-budget-app#budget.py>

Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
When the budget object is printed it should display:

* A title line of 30 characters where the name of the category is centered in a line of * characters.
* A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. * The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
* A line displaying the category total.

Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

## 4. Fourth Project: Build a [Polygon Area Calculator]()

Project Url: <https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator>

Solution Url: <https://replit.com/@Joovictorvict19/boilerplate-polygon-area-calculator#shape_calculator.py>

In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

Rectangle class
When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

* set_width
* set_height
* get_area: Returns area (width * height)
* get_perimeter: Returns perimeter (2 * width + 2 * height)
* get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
* get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
* get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

Square class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, it should look like: Square(side=9)

Additionally, the set_width and set_height methods on the Square class should set both the width and height.

## 5. fifth Project: Build a [Probability Calculator]()

Project Url: <https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator>

Solution Url: <https://replit.com/@Joovictorvict19/boilerplate-probability-calculator#prob_calculator.py>

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

First, create a Hat class in prob_calculator.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat.

A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].

The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an experiment function in prob_calculator.py (not inside the Hat class). This function should accept the following arguments:

* hat: A hat object containing balls that should be copied inside the function.
* expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
* num_balls_drawn: The number of balls to draw out of the hat in each experiment.
* num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
The experiment function should return a probability.

For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. To do this, you will perform N experiments, count how many times M you get at least two red balls and one green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.

