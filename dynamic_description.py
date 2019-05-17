# https://artandlogic.com/2015/01/dynamic-python-method/


class Animal:
    descriptions = {}

    def __init__(self, name, colors, sounds):
        self.name = name
        self.descriptions['color'] = colors
        self.descriptions['sound'] = sounds

    def color_values(self):
        print(f"{self.name}: {self.descriptions['color']}")


def add_description_fn(description):
    fn_name = description + '_values'
    
    def fn(self):
        print(f"{self.name}: {self.descriptions[description]}")

    setattr(Animal, fn_name, fn)

    fn.__name__ = fn_name
    fn.__doc__ = f"Return values for the {description} description"


if __name__ == "__main__":
    cat = Animal('cat', colors=['red', 'orange'], sounds=['purr', 'meow'])
    for description in Animal.descriptions:
        add_description_fn(description)
    help(cat.color_values)
    help(cat.sound_values)

    cat.sound_values()

"""
Help on method color_values in module __main__:

color_values() method of __main__.Animal instance
    Return values for the color description

Help on method sound_values in module __main__:

sound_values() method of __main__.Animal instance
    Return values for the sound description

cat: ['purr', 'meow']
"""
