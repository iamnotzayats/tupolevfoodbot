import asyncio
import logging
import config
import keyboards

from States import PersonalAccount, DinnerRoom
from aiogram import Router, F
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.BOT_TOKEN)
# Диспетчер
dp = Dispatcher()
router = Router()

@dp.message(StateFilter(None),Command("start"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.reply(f"Приветствую, <b>{message.from_user.full_name}</b>🛫\n\n"+
                         "Здесь ты сможешь:\n"+
                         "<i>1. Узнать режим работы столовых, если до сих пор не знаешь</i>🕔\n"+
                         "<i>2. Посмотреть расписание блюд на сегодняший день</i>🥢\n"+
                         "<i>3. Оставить жалобу на работу столовой</i>🎥\n"+
                         "<i>4. Предложить идею по улучшению работы столовой</i>💡\n\n"+
                         "❗<b>Проект находится на стадии бета-тестирования, поэтому о всех ошибках сообщать администратору</b>❗",parse_mode=ParseMode.HTML)
    await message.answer("Для работы с ботом потребуется небольшая регистрация\n"+
                         "Введите номер своего СП. <i>Пример: 390</i>", parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardRemove())
    await state.set_state(PersonalAccount.choosing_spnumber)

@dp.message(PersonalAccount.choosing_spnumber)
async def input_sp_number(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await message.answer("Спасибо большое за регистрацию!")
        await message.answer("Выберите столовую:", reply_markup=keyboards.kb_dinner_room)
        await state.clear()
        await state.set_state(DinnerRoom.choosing_dr)
    else:
        await message.answer("Введите номер СП числом!")

@dp.message(DinnerRoom.choosing_dr)
async def input_dr_number(message: types.Message, state: FSMContext):
    await message.answer("Главное меню", reply_markup=keyboards.keyboard_main_menu)
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())