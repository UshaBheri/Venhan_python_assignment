Basic Concepts:

1. Write a function `is_prime(n: int) -> bool` that checks if a given number is prime.
2. Write a Python function `reverse_string(s: str) -> str` that takes a string and returns its
reverse.
3. Given a list of integers, write a function `sum_of_squares(lst: List[int]) -> int` that
returns the sum of the squares of the elements.
4. Write a Python program to count the frequency of each character in a given string and
return a dictionary with characters as keys and their frequencies as values.

Web Frameworks:

5. Django Basics
Write a simple Django view function `hello_world` that returns an HTTP response with the
text "Hello, World!".
6. Flask Basics
Write a basic Flask application with a single route `/` that returns the text "Welcome to
Flask!".

Front-End Technologies:

7. HTML and CSS
Create a simple HTML page with a header that says "Welcome to My Website" and a
paragraph of lorem ipsum text. Add some basic CSS to style the header with a blue color
and center alignment.
8. JavaScript Basics
Write a JavaScript function `showAlert()` that displays an alert with the message "Hello,
this is a JavaScript alert!".

Databases:

9. SQL Basics
Write a SQL query to create a table `students` with columns `id`, `name`, and `grade`.
10. Basic Database Operations
Write a Python function `insert_student(name: str, grade: float)` that inserts a new
student into the `students` table using SQLite.

APIs and Web Services:

11. REST API Basics
Write a simple REST API using Flask with one endpoint /greet/<name> that returns a JSON
response with a greeting message, e.g., `{"message": "Hello, <name>!"}`.

Data Structures & Algorithms:

12. Write a function `merge_sort(arr: List[int]) -> List[int]` that implements the merge sort
algorithm.
13. Implement a function `find_duplicates(arr: List[int]) -> List[int]` that returns a list of
duplicate elements in the input list.
14. Write a function `is_palindrome(s: str) -> bool` to check if a given string is a
palindrome (reads the same forward and backward).
15. Sorting, Implement the quicksort algorithm in Python.
16. Binary Search Tree (BST), Write a class `BST` with methods to insert, find, and delete nodes in a binary search tree. Also, include a method to find the height of the tree.
17. Graph Algorithms, Write a function `dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, int]` that implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in a weighted graph represented as an adjacency list.

Object-Oriented Programming:

18. Create a class Book with the following attributes and methods:
*Attributes: `title`, `author`, `pages`
*Methods:
*`__init__(self, title: str, author: str, pages: int)`: Constructor to initialize the attributes.
*`__str__(self) -> str`: Method to return a string representation of the book.
19. Create a class `Rectangle` with the following attributes and methods:
*Attributes: length, width
*Methods:
*`__init__(self, length: float, width: float)`: Constructor to initialize the attributes.
*`area(self) -> float`: Method to calculate the area of the rectangle.
*`perimeter(self) -> float`: Method to calculate the perimeter of the rectangle.
20. Write a class `BankAccount` with the following:
*Attributes: account_number, account_holder, balance
*Methods:
*`__init__(self, account_number: str, account_holder: str, balance: float = 0.0)`:
Constructor to initialize the attributes.
*`deposit(self, amount: float) -> None`: Method to deposit money into the account.
*`withdraw(self, amount: float) -> bool`: Method to withdraw money from the account. It
should return True if the withdrawal was successful, and False if there were insufficient
funds.
*`get_balance(self) -> float`: Method to return the current balance.
21. Inheritance and Polymorphism
Create a class hierarchy for `Shape`, `Circle`, and `Rectangle`. The base class Shape
should have methods to calculate area and perimeter, which are overridden in the derived
classes `Circle` and `Rectangle`.
22. Class Methods and Static Methods
Write a class `Employee` with class methods to keep track of the number of employees
and static methods to validate employee ID format (e.g., must be a string of digits).

File Handling and Data Processing:

23. Write a function `read_file(file_path: str) -> List[str]` that reads a text file and returns a
list of strings, each representing a line in the file.
24. Write a function `write_file(file_path: str, lines: List[str]) -> None` that writes a list of
strings to a text file, each string on a new line.

25. CSV File Handling:
Write a function `read_csv(file_path: str) -> List[Dict[str, str]]` that reads a CSV file and
returns a list of dictionaries, each representing a row in the CSV file.

26. JSON Data Processing:
Write a function `process_json(file_path: str) -> Dict` that reads a JSON file, processes the
data (e.g., extracts specific fields), and returns a dictionary with the processed data.
