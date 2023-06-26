"""
print exercises:
"""


def simple_message(message: str):   # prints a message.
    print(message)


def simple_messages(message: str):  # prints two messages.
    print(message)
    message = input("please enter a new message: ")
    print(message)


"""
string exercises:
"""


def personal_message(name: str):
    print(f"Hello! {name}, how was your day today?")


def name_cases(name: str):  # prints every case of a name.
    print(name.lower(), name.upper(), name.title())


def famous_quote(quote: str, author: str): # prints a famous quote.
    print(f"{author} once said, {quote}")


def stripping_names(unfixed_name: str): # prints a fixed name from left, right and both.
    print(unfixed_name.lstrip(), unfixed_name.rstrip(), unfixed_name.strip())


def file_extensions():  # prints a file name without the extension.
    file_name = 'python_notes.txt'
    print(file_name.removesuffix(".txt"))




