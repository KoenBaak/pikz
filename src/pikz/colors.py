BLACK = 'black'
BLUE = 'blue'
WHITE = 'white'


def mix_color(**kwargs):

    total = sum(kwargs.values())

    if (total < 100 and WHITE in kwargs) or (not 0 <= total <= 100):
        raise ValueError("Invalid input for color mixing")

    return "!".join(f"{name}!{value}" for name, value in kwargs.items())
