glossary = {
    'variable': 'A named storage location in memory.',
    'function': 'A block of reusable code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code until a condition is met.',
    'list': 'An ordered collection of items that can be modified.',
    'dictionary': 'A collection of key-value pairs.',
    'string': 'A sequence of characters.',
    'tuple': 'An ordered collection of items that cannot be changed.',
    'comment': 'A note in code, starting with #, that Python ignores.',
    'boolean': 'A value that is either True or False.',
    'index': 'The position of an item in a list, starting at 0.',
}

for word, definition in glossary.items():
    print(f"{word.title()}:\n {definition}\n")