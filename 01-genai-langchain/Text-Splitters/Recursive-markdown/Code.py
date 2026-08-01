from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def describe(self):
        return str(self.year) + " " + self.make + " " + self.model

    def drive(self, miles):
        if miles > 0:
            self.odometer = self.odometer + miles


my_car = Car("Toyota", "Corolla", 2024)
print(my_car.describe())
my_car.drive(50)
print(my_car.odometer)"""

splitter=RecursiveCharacterTextSplitter.from_language(
    Language.PYTHON, 
    chunk_size=50, 
    chunk_overlap=10
)

splits=splitter.split_text(text)
print(splits)
print(len(splits[0]))