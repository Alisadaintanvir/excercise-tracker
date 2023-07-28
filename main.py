from dotenv import load_dotenv
from nutritionix import Nutritionix
from sheet import Sheet

load_dotenv()

user_input = input("Tell me which exercise you did: ")
nutritionix = Nutritionix(user_input)
Sheet().post(exercises=nutritionix.exercises())
