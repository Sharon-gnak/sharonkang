Parameters should be separated by a comma and a space after the comma.

Correct:

def __init__(self, name, age):

Incorrect:

def __init__(self,name,age):

----------

If the name of the parameter has more than one word, you should separate the words with an underscore (snake_case format).

Example:

def __init__(hair_color, eye_color, num_children):

----------

If the name of a parameter clashes with the name of a keyword, you should add a trailing underscore to the name.

Example:

def __init__(description, type_):
