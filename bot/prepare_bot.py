from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

MY_TOKEN = "6542990215:AAErSHJUVLj2GEoheBrfyQ2WNrjssnLqZms"
START_MESSAGE = """Hello! Welcome to Nicola Tesla airport bot. You could get information about arrivals and departures. 
Please, choose types of flights:"""

bot = Bot(MY_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
