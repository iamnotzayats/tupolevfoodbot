from aiogram.fsm.state import StatesGroup, State

class PersonalAccount(StatesGroup):
    choosing_spnumber = State()

class DinnerRoom(StatesGroup):
    choosing_dr = State()