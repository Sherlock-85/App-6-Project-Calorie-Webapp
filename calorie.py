from temperature import Temperature
class Calorie:
    '''Initialize a calorie object
    Basal Metabolic Rate = 4.536*wieght(lbs) + 15.88* height(in) - 5* age - 10*temperature'''
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        calories_needed = round((4.536 * self.weight) + (15.88 * self.height) -
                                (5 * self.age) - (10 * self.temperature) + 5, 2)
        return calories_needed


# test if Python is running this module as the main program.
if __name__ == "__main__":
    temperature = Temperature(country="Germany", city="Hamburg").get()
    calorie = Calorie(weight=145, height=65, age=35, temperature=temperature)
    print(calorie.calculate())

