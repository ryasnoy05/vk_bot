import vk_api
import random
import json
import googletrans
from googletrans import Translator
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from exceptions import messages
translator = Translator()
token = os.environ.get('BOT_TOKEN')
vk_session = vk_api.VkApi(token=token)
random_id = vk_api.utils.get_random_id()
longpoll = VkLongPoll(vk_session, group_id=197454537)
vk = vk_session.get_api()
src =''
frase = ''
def s_keyboard():
	s_keyboard = VkKeyboard(one_time=False)
	s_keyboard.add_button('Английскийᅠ', color=VkKeyboardColor.NEGATIVE)
	s_keyboard.add_button('Русскийᅠ', color=VkKeyboardColor.POSITIVE)
	s_keyboard.add_line()
	s_keyboard.add_button('Немецкийᅠ', color=VkKeyboardColor.PRIMARY)
	s_keyboard.add_button('Украинскийᅠ', color=VkKeyboardColor.DEFAULT)
	return s_keyboard
def e_keyboard():
	e_keyboard = VkKeyboard(one_time=False)
	e_keyboard.add_button('Английский', color=VkKeyboardColor.NEGATIVE)
	e_keyboard.add_button('Русский', color=VkKeyboardColor.POSITIVE)
	e_keyboard.add_line()
	e_keyboard.add_button('Немецкий', color=VkKeyboardColor.PRIMARY)
	e_keyboard.add_button('Украинский', color=VkKeyboardColor.DEFAULT)
	return e_keyboard
def b_keyboard():
	b_keyboard = VkKeyboard(one_time=False)
	b_keyboard.add_button('Начать', color=VkKeyboardColor.PRIMARY)
	return b_keyboard
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
	#Слушаем longpoll, если пришло сообщение то:			
		if event.text.lower() == 'начать' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
			if event.from_user or event.from_chat: #Если написали в ЛС
				vk.messages.send(user_id=event.user_id,message='Выберите язык, c которого нужно перевести.',keyboard=s_keyboard().get_keyboard(),random_id=vk_api.utils.get_random_id())
		if event.text == 'Английскийᅠ':
			if event.from_user or event.from_chat: #Если написали в ЛС
				src = 'en'
				vk.messages.send(
					user_id=event.user_id,
					message='Выберите язык, на который нужно перевести.',
					keyboard=e_keyboard().get_keyboard(),
					random_id=vk_api.utils.get_random_id()
		)
		if event.text == 'Русскийᅠ':
			if event.from_user or event.from_chat: #Если написали в ЛС
				src = 'ru'
				vk.messages.send(
					user_id=event.user_id,
					message='Выберите язык, на который нужно перевести.',
					keyboard=e_keyboard().get_keyboard(),
					random_id=vk_api.utils.get_random_id()
		)
		if event.text == 'Немецкийᅠ':
			if event.from_user or event.from_chat: #Если написали в ЛС
				src = 'de'
				vk.messages.send(
					user_id=event.user_id,
					message='Выберите язык, на который нужно перевести.',
					keyboard=e_keyboard().get_keyboard(),
					random_id=vk_api.utils.get_random_id()
		)
		if event.text == 'Украинскийᅠ':
			if event.from_user or event.from_chat: #Если написали в ЛС
				src = 'uk'
				vk.messages.send(
					user_id=event.user_id,
					message='Выберите язык, на который нужно перевести.',
					keyboard=e_keyboard().get_keyboard(),
					random_id=vk_api.utils.get_random_id()
		)
		if event.text == 'Английский':
			if event.from_user or event.from_chat: #Если написали в ЛС
				dest = 'en'
				vk.messages.send(
					user_id=event.user_id,
					message='Введите фразу, которую нужно перевести.',
					keyboard=e_keyboard().get_empty_keyboard(),
					random_id=vk_api.utils.get_random_id()
		)
		if event.text == 'Русский':
			if event.from_user or event.from_chat: #Если написали в ЛС
				dest = 'ru'
				vk.messages.send(
					user_id=event.user_id,
					message='Введите фразу, которую нужно перевести.',
					keyboard=e_keyboard().get_empty_keyboard(),
					random_id=vk_api.utils.get_random_id()
		)
		if event.text == 'Немецкий':
			if event.from_user or event.from_chat: #Если написали в ЛС
				dest = 'de'
				vk.messages.send(
					user_id=event.user_id,
					message='Введите фразу, которую нужно перевести.',
					keyboard=e_keyboard().get_empty_keyboard(),
					random_id=vk_api.utils.get_random_id()
		)
		if event.text == 'Украинский':
			if event.from_user or event.from_chat: #Если написали в ЛС
				dest = 'uk'
				vk.messages.send( #Отправляем сообщение
					user_id=event.user_id,
					message='Введите фразу, которую нужно перевести.',
					keyboard=e_keyboard().get_empty_keyboard(),
					random_id=vk_api.utils.get_random_id()
		)
		elif event.text not in messages and event.text != frase:
			if event.from_user or event.from_chat:
				result = translator.translate(event.text, src=src, dest=dest)
				frase = result.text
				vk.messages.send( #Отправляем сообщение
					user_id=event.user_id,
					message=f'{result.text}',
					keyboard=b_keyboard().get_keyboard(),
					random_id=vk_api.utils.get_random_id()
				)
