# Input: name-String, Function prints Good Morning, {name}.
def greetEnglish(name):
    """Greets Good Morning in English to the user's name."""
    print("Good morning, " + name + "!")
    
# Input: name-String, Function prints Guten Morgen, {name}.
def greetGerman(name):
    """Greets Good Morning in German to the user's name."""
    print(f"Guten Morgen, {name}!")
    
# Input: name-String, Function prints Salve, {name}.
def greetLatin(name):
    """Greets Good Morning in Latin to the user's name."""
    print("Salve, {}!".format(name))