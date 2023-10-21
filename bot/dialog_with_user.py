from scraper.scraper import Parser
from keyboards import keyboard_1, keyboard_2
from aiogram import types, Dispatcher

from aiogram import exceptions
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from prepare_bot import dp, START_MESSAGE


class Params(StatesGroup):
    waiting_for_flight_type = State()
    waiting_for_day = State()
    waiting_for_city = State()


@dp.message_handler(commands=['start'], state='*')
async def echo(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text=START_MESSAGE, reply_markup=keyboard_1)
    await state.set_state(Params.waiting_for_flight_type.state)


@dp.message_handler(commands=['departures'], state='*')
async def departures(message: types.Message, state: FSMContext):
    # await state.update_data(type_of_flight='Departures')
    # await state.set_state(Params.waiting_for_city.state)
    await state.update_data(type_of_flight='Departures')
    await message.answer('Please, choose the day:', reply_markup=keyboard_2)
    # my_parser = Parser(type_of_schedule='Departures', day='Today')
    # my_parser.run()
    # await message.answer(f'{my_parser.all_flights[0]}')


@dp.message_handler(commands=['today'], state='*')
async def today_arrivals(message: types.Message, state: FSMContext):
    # await state.set_state(Params.waiting_for_city.state)
    await state.update_data(day='today')
    print(state.storage.__dict__)
    print(state.__dict__)
    # my_parser = Parser(type_of_schedule='Departures', day='Today')
    # my_parser.run()
    # for flight in my_parser.list_of_flights:
    #     await message.answer(f'{flight}')



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('TEST WORK')


@dp.errors_handler(exception=exceptions.RetryAfter)
async def exception_handler(update: types.Update, exception: exceptions.RetryAfter):
    # Do something
    return True

