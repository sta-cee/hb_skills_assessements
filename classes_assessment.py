"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    1.) Polymorphism: Allows for interchangeability of components.
        - Makes it earier to make different interchangeable types of a class.
    2.) Abstraction: Allows for hiding details we don't need.
        - Don't need to know the information a method uses internally.
    3.) Encapsulation: Allows for keeping everything "together".
        - Data lives close to it's functionality.

2. What is a Class?
    - Type of thing like String or File

3. What is an instance attribute?
    - Similar to keys in dictionary.
    - Specific attributes that can be added to an instance.
    - If an instane has no specified instance attributes, that instance takes the class atributes of it's parent class.

4. What is a method?
    - A function defined on a class, that takes self as it's first argument.
    - When a metho is called, Python passes instance as self.

5. What is an instance in object orientation?
    - An individual occurence of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   - A class attribute value is shared across all instances of that class.
   - An instance attribute is specific to that instance.
   - Class attribute ex: if every student in Student class, is given the same bonus credit.
   - Instance attribute ex: individual students have unique exam and quiz scores.
"""

# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """Base class for all students."""

    def __init__(self, first_name, last_name, address):
        """Initializes student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Questions(object):
    """Base class for all questions."""

    def __init__(self, question, correct_answer):
        """Initializes questions class."""
        self.question = question
        self.correct_answer = correct_answer

    def ask_question(self):
        """Prints question, records user answer, and compares user answer to correct answer."""

        self.user_answer = raw_input('{question}'.format(question=self.question))
        return self.user_answer == self.correct_answer


class Exam(object):
    """Base class for all exams."""

    def __init__(self, name):
        """ """
        self.questions = []
        self.name = name

    def add_question(self, question):
        """Adds questions to instance question list."""
        self.questions.append(question)

    def administer(self):
        """Administers questions and calculates score."""
        score = 0
        for q in self.questions:
            test_question = q.ask_question()
            if test_question is True:
                score += float(1)
        score = score / len(self.questions) * 100
        return score


class Quiz(Exam):
    """Base class for quiz. Child of Exam class."""

    def __init__(self, name):
        """Initializes quiz class. Calls super class and pass name attribute."""

        super(Quiz, self).__init__(name)

    def administer(self):
        """Calls super administer method, updates quiz score to return 1 or 0."""
        quiz_score = super(Quiz, self).administer()
        if quiz_score >= 50:
            quiz_score = 1
        else:
            quiz_score = 0
        return quiz_score


class StudentExam(object):
    """Base class for student exam."""

    def __init__(self, Student, Exam):
        """Initializes student exam class. Expects 2 instance parameters."""

        self.score = 0
        self.Student = Student
        self.Exam = Exam

    def take_test(self):
        """Calls exam administer method and displays score."""

        test_score = self.Exam.administer()
        print 'Exam score: {score} '.format(score=test_score)


class StudentQuiz(object):
    """Base class for student quiz."""

    def __init__(self, Student, Quiz):
        """Initializes student quiz class. Expects 2 instance parameters."""
        self.score = 0
        self.Student = Student
        self.Quiz = Quiz

    def take_quiz(self):
        """Calls quiz administer method and displays score."""

        quiz_score = self.Quiz.administer()
        print 'Quiz score: {score}'.format(score=quiz_score)


def example_exam():
    """Main exam function to create example exam instances."""

    # Instantiates questions, passing question text and correct answers.
    python_author = Questions('Who is the author of python?\n', 'Guido Van Rossum')
    baloonicorn_color = Questions('What color is Baloonicorn?\n', 'rainbow')
    california_capital = Questions('What is the capital of California?\n', 'Sacramento')

    # Instantiates exam, passing name parameter
    hb_midterm = Exam('hb_midterm')

    # Calling instance method to add questions to question list
    hb_midterm.add_question(python_author)
    hb_midterm.add_question(baloonicorn_color)
    hb_midterm.add_question(california_capital)

    # Instantiates student, passing in first name, last name, and address
    baloonicorn = Student('Baloonicorn', 'Jones', '450 Sutter')
    student_exam = StudentExam(baloonicorn, hb_midterm)
    student_exam.take_test()


def example_quiz():
    """Main quiz function to create example quiz instances."""

    # Instantiates questions, passing question text and correct answers.
    python_author = Questions('Who is the author of python?\n', 'Guido Van Rossum')
    baloonicorn_color = Questions('What color is Baloonicorn?\n', 'rainbow')
    california_capital = Questions('What is the capital of California?\n', 'Sacramento')

    # Instantiates quiz, passing name parameter
    hb_quiz = Quiz('hb_quiz')

    # Calling instance method to add questions to question list
    hb_quiz.add_question(python_author)
    hb_quiz.add_question(baloonicorn_color)
    hb_quiz.add_question(california_capital)

    # Instantiates student, passing in first name, last name, and address
    baloonicorn = Student('Baloonicorn', 'Jones', '450 Sutter')
    student_quiz = StudentQuiz(baloonicorn, hb_quiz)
    student_quiz.take_quiz()


# example_exam()
example_quiz()
