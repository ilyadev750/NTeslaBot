from scraper.scraper import Parser
from keyboards import keyboard_1, keyboard_2
from aiogram import types, Dispatcher

from aiogram import exceptions
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from prepare_bot import dp, START_MESSAGE, TYPES_OF_DAYS, TYPES_OF_FLIGHT


class Params(StatesGroup):
    waiting_for_flight_type = State()
    waiting_for_day = State()
    waiting_for_city = State()
    waiting_for_start = State()


@dp.message_handler(commands=['start'], state='*')
async def echo(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text=START_MESSAGE, reply_markup=keyboard_1)
    await state.set_state(Params.waiting_for_flight_type.state)


@dp.message_handler(state=Params.waiting_for_flight_type.state)
async def arrivals_or_departures(message: types.Message, state: FSMContext):
    if message.text not in TYPES_OF_FLIGHT:
        await message.answer('Please, choose the correct type of flights:')
        return
    if message.text == '/arrivals':
        await state.update_data(type_of_flight='Arrivals')
    else:
        await state.update_data(type_of_flight='Departures')
    await state.set_state(Params.waiting_for_day.state)
    await message.answer('Please, choose the day:', reply_markup=keyboard_2)


@dp.message_handler(state=Params.waiting_for_day.state)
async def choose_the_day(message: types.Message, state: FSMContext):
    user_message = message.text.capitalize()
    if user_message not in TYPES_OF_DAYS:
        await message.answer('Please, choose the correct day:')
        return
    await state.update_data(day=message.text)
    await state.set_state(Params.waiting_for_city.state)
    await message.answer('Please, input the city:')


@dp.message_handler(state=Params.waiting_for_city.state)
async def input_the_city(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(city=message.text.capitalize())
        await state.set_state(Params.waiting_for_start.state)
        await message.answer("Please, type any symbol for starting bot")
    else:
        await message.answer("Please, input the city")
        return


@dp.message_handler(state=Params.waiting_for_start.state)
async def run_bot(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_parser = Parser(type_of_schedule=user_data['type_of_flight'], day=user_data['day'], city=user_data['city'])
    user_parser.run()
    if not user_parser.list_of_flights:
        await message.answer('There is no information about flights')
        await state.finish()
    else:
        for flight in user_parser.list_of_flights:
            await message.answer(f'{flight}')
        await state.finish()


@dp.errors_handler(exception=exceptions.RetryAfter)
async def exception_handler(update: types.Update, exception: exceptions.RetryAfter):
    # Do something
    return True
