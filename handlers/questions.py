
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import CHANNEL_ID
from utils.sender import send_pdf
import re

class Form(StatesGroup):
    Q1 = State(); Q2 = State(); Q3 = State()
    Q4_DA = State(); Q5_DA = State(); Q6_DA = State(); Q7_DA = State()
    Q8_DA = State(); Q9_DA = State(); Q10_DA = State(); Q11_DA = State()
    Q12_DA = State(); Q13_DA = State(); Q14_DA = State()
    Q4_NET = State(); Q5_NET = State(); Q6_NET = State()
    Q7_NET = State(); Q8_NET = State(); Q9_NET = State()

user_answers = {}

def kb(*btns): return ReplyKeyboardMarkup(resize_keyboard=True).add(*(KeyboardButton(b) for b in btns))

async def start_test(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.Q1.state)
    user_answers[callback.from_user.id] = []
    await callback.message.answer("1. Как давно занимаешься музыкой?", reply_markup=kb("менее 1 года", "от 1 до 3 лет", "более 5 лет"))

async def back(message: types.Message, state: FSMContext):
    await message.answer("Возврат назад не реализован для этой демо-версии.")

async def q1(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q2.state)
    await message.answer("2. Твой возраст?", reply_markup=kb("до 18", "18-20", "21-30", "более 30"))

async def q2(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q3.state)
    await message.answer("3. Делал ли ты что-либо для продвижения своей музыки?", reply_markup=kb("ДА", "НЕТ"))

async def q3(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    if message.text == "ДА":
        await state.set_state(Form.Q4_DA.state)
        await message.answer("4. Работал ли с агентствами/лейблами?", reply_markup=kb("ДА", "НЕТ"))
    else:
        await state.set_state(Form.Q4_NET.state)
        await message.answer("4. Почему не пробовал продвигать свою музыку?", reply_markup=kb("Нет денег", "Не уверен в материале", "Не понимаю что делать", "Музыка сама продвинется", "Свой вариант"))

# Ветка ДА
async def q4_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q5_DA.state)
    await message.answer("5. Какие инструменты ты использовал? Напиши текстом.")

async def q5_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q6_DA.state)
    await message.answer("6. Сколько у тебя слушателей на Яндекс Музыке?", reply_markup=kb("До 1k", "1k-10k", "10-50k", "Более 50k"))

async def q6_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q7_DA.state)
    await message.answer("7. Снимаешь ли ты вертикальные видео?", reply_markup=kb("Хочу начать", "Да", "Нет"))

async def q7_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q8_DA.state)
    await message.answer("8. Сколько видео в месяц ты выпускаешь?", reply_markup=kb("1-3", "3-5", "5-10", "10+"))

async def q8_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q9_DA.state)
    await message.answer("9. Какой охват в месяц?", reply_markup=kb("Менее 10k", "10-50k", "50-100k", "100k+"))

async def q9_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q10_DA.state)
    await message.answer("10. Есть команда?", reply_markup=kb("ДА", "НЕТ"))

async def q10_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q11_DA.state)
    await message.answer("11. Бюджеты на продвижение?", reply_markup=kb("5-10k", "10-20k", "20-50k", "50k+"))

async def q11_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q12_DA.state)
    await message.answer("12. Какие способы продвижения считаешь рабочими? Напиши текстом.")

async def q12_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q13_DA.state)
    await message.answer("13. Основные проблемы? Напиши текстом.")

async def q13_da(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q14_DA.state)
    await message.answer("14. Какие вложения считаешь комфортными?", reply_markup=kb("5-10k", "10-20k", "20-50k", "500-100k+", "Это сложная задача"))

# Ветка НЕТ
async def q4_net(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q5_NET.state)
    await message.answer("5. Какие способы продвижения ты знаешь? Напиши текстом.")

async def q5_net(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q6_NET.state)
    await message.answer("6. Какие вложения ты считаешь комфортными?", reply_markup=kb("5-10k", "10-20k", "20-50k", "500-100k+", "Это сложная задача"))

async def q6_net(message: types.Message, state: FSMContext):
    user_answers[message.from_user.id].append(message.text)
    await state.set_state(Form.Q7_NET.state)
    await message.answer("7. Ссылка на профиль VK (https://vk.com/...)")

# Завершение
async def finish_final_steps(message: types.Message, state: FSMContext):
    text = message.text.strip()
    if not re.match(r'^https://', text):
        await message.answer("Ссылка должна начинаться с https://")
        return
    user_answers[message.from_user.id].append(text)

    # После последнего шага:
    answers = user_answers[message.from_user.id]
    out = f"<b>Новая заявка!!!</b>
ЮЗЕР: @{message.from_user.username or message.from_user.id}

"
    for i, a in enumerate(answers, 1):
        out += f"{i}) {a}\n"

    await message.bot.send_message(CHANNEL_ID, out)
    await send_pdf(message.from_user.id, message.bot)
    await message.answer("Тест завершён! Мы свяжемся с тобой.", reply_markup=ReplyKeyboardRemove())
    await state.finish()

def register(dp: Dispatcher):
    dp.register_callback_query_handler(start_test, lambda c: c.data == "start_test")
    dp.register_message_handler(back, lambda m: m.text == "Назад", state="*")
    dp.register_message_handler(q1, state=Form.Q1)
    dp.register_message_handler(q2, state=Form.Q2)
    dp.register_message_handler(q3, state=Form.Q3)
    dp.register_message_handler(q4_da, state=Form.Q4_DA)
    dp.register_message_handler(q5_da, state=Form.Q5_DA)
    dp.register_message_handler(q6_da, state=Form.Q6_DA)
    dp.register_message_handler(q7_da, state=Form.Q7_DA)
    dp.register_message_handler(q8_da, state=Form.Q8_DA)
    dp.register_message_handler(q9_da, state=Form.Q9_DA)
    dp.register_message_handler(q10_da, state=Form.Q10_DA)
    dp.register_message_handler(q11_da, state=Form.Q11_DA)
    dp.register_message_handler(q12_da, state=Form.Q12_DA)
    dp.register_message_handler(q13_da, state=Form.Q13_DA)
    dp.register_message_handler(q14_da, state=Form.Q14_DA)
    dp.register_message_handler(q4_net, state=Form.Q4_NET)
    dp.register_message_handler(q5_net, state=Form.Q5_NET)
    dp.register_message_handler(q6_net, state=Form.Q6_NET)
    dp.register_message_handler(finish_final_steps, state=Form.Q7_NET)
