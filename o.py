import telebot
from telebot import types
from covid import Covid

bot = telebot.TeleBot('1154277651:AAE6oicbQHLeNmb7CE34wtKS4r_Aw4MV3OM')

try:
	import COVID19Py

	covid19 = COVID19Py.COVID19()
except:
	bot.send_message(914886587, "import error")
covid = Covid()
covid.get_data()

@bot.message_handler(commands=['start','help'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton("Butun dunyo bo'yicha")
	btn2 = types.KeyboardButton('Qozogiston')
	btn3 = types.KeyboardButton('Rossiya')
	btn4 = types.KeyboardButton("O'zbekiston")
	markup.add(btn1, btn2, btn3, btn4)

	if message.chat.id == 526188312:
		bot.send_message(message.chat.id, "Salom Shirin Qiz Sizga @orzumurod dan Salom")
	if message.chat.id == 398437601:
		bot.send_message(message.chat.id, "Salom Yaxshi Qiz Sizga @orzumurod dan Salom")
	if message.chat.id == 914886587:
		bot.send_message(message.chat.id, "Salom Boshliq")
	else:
		bot.send_message(message.chat.id, "Salom Sizga @orzumurod dan Salom")

	send_message = f"<b>Salom {message.from_user.first_name}!</b>\nKoronavirus bo'yicha malumotlarni bilish uchun yozing" \
		f"Davlat nomi, masalan: Aqsh, O'zbekiston, Rossiya\n\nMDH davlatlari bo'yicha malumot olish uchun /mdh buyrug'ini ishlating"
	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['mdh'])
def mdh(message):
	uz = covid.get_status_by_country_name("Uzbekistan")
	ru = covid.get_status_by_country_name("Russia")
	kz = covid.get_status_by_country_name("Kazakhstan")
	kr = covid.get_status_by_country_name("Kyrgyzstan")
	tj = covid.get_status_by_country_name("Tajikistan")
	uk = covid.get_status_by_country_name("Ukraine")
	all_mess = f"MDH mamlakatlari:\n{uz['country']}\n🤕 Qayd etilgan holatlar: {uz['confirmed']}\n⛔ O'limlar: {uz['deaths']}\n🐎 Tuzalib ketganlar: {uz['recovered']}\n💉 Davolanayotganlar: {uz['active']}\n\n{ru['country']}\n🤕 Qayd etilgan holatlar: {ru['confirmed']}\n⛔ O'limlar: {ru['deaths']}\n🐎 Tuzalib ketganlar: {ru['recovered']}\n💉 Davolanayotganlar: {ru['active']}\n\n{kz['country']}\n🤕 Qayd etilgan holatlar: {kz['confirmed']}\n⛔ O'limlar: {kz['deaths']}\n🐎 Tuzalib ketganlar: {kz['recovered']}\n💉 Davolanayotganlar: {kz['active']}\n\n{uk['country']}\n🤕 Qayd etilgan holatlar: {uk['confirmed']}\n⛔ O'limlar: {uk['deaths']}\n🐎 Tuzalib ketganlar: {uk['recovered']}\n💉 Davolanayotganlar: {uk['active']}\n\n{tj['country']}\n🤕 Qayd etilgan holatlar: {tj['confirmed']}\n⛔ O'limlar: {tj['deaths']}\n🐎 Tuzalib ketganlar: {tj['recovered']}\n💉 Davolanayotganlar: {tj['active']}\n\n{kr['country']}\n🤕 Qayd etilgan holatlar: {kr['confirmed']}\n⛔ O'limlar: {kr['deaths']}\n🐎 Tuzalib ketganlar: {kr['recovered']}\n💉 Davolanayotganlar: {kr['active']}"
	bot.send_message(message.chat.id, all_mess)

@bot.message_handler(commands=['shirin_qiz'])
def shirinim(message):
	if message.chat.id == 914886587:
		bot.send_message(526188312, "salom")
		bot.send_message(1273229455, "Done")

@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	try:
		if get_message_bot == "aqsh":
			location = covid.get_status_by_country_name("US")
		elif get_message_bot == "ukraina":
			location = covid.get_status_by_country_name("Ukraine")
		elif get_message_bot == "rossiya":
			location = covid.get_status_by_country_name("Russia")
		elif get_message_bot == "o'zbekiston":
			location = covid.get_status_by_country_name("Uzbekistan")
		elif get_message_bot == "qozogiston":
			location = covid.get_status_by_country_name("Kazakhstan")
		elif get_message_bot == "italiya":
			location = covid.get_status_by_country_name("Italy")
		elif get_message_bot == "fransiya":
			location = covid.get_status_by_country_name("France")
		elif get_message_bot == "germaniya":
			location = covid.get_status_by_country_name("Germany")
		elif get_message_bot == "yaponiya":
			location = covid.get_status_by_country_name("Japan")
		elif get_message_bot == "ispaniya":
			location = covid.get_status_by_country_name("Spain")
		elif get_message_bot == "turkiya":
			location = covid.get_status_by_country_name("Turkey")
		elif get_message_bot == "braziliya":
			location = covid.get_status_by_country_name("Brasil")
		elif get_message_bot == "argentina":
			location = covid.get_status_by_country_name("Argentina")
		elif get_message_bot == "angliya":
			location = covid.get_status_by_country_name("United Kingdom")
		elif get_message_bot == "hindiston":
			location = covid.get_status_by_country_name("India")
		elif get_message_bot == "xitoy":
			location = covid.get_status_by_country_name("China")
		elif get_message_bot == "koreya":
			location = covid.get_status_by_country_name("Korea, South")
		elif get_message_bot == "qirgiziston":
			location = covid.get_status_by_country_name("Kyrgyzstan")
		elif get_message_bot == "tojikiston":
			location = covid.get_status_by_country_name("Tajikistan")
		elif get_message_bot == "afgoniston":
			location = covid.get_status_by_country_name("Afghanistan")
		elif get_message_bot == "kanada":
			location = covid.get_status_by_country_name("Canada")
		else:
			try:
				location = covid19.getLatest()
				final_message = f"<u>Butun dunyo bo'yicha malumotlar:</u>\n<b>Kasallanganlar: </b>{location['confirmed']:,}\n<b>Vafot etganlar: </b>{location['deaths']:,}\n@koronavirus_status_bot"
			except:
				bot.send_message(914886587, "xatolik")
	except:
		bot.send_message(914886587, "unlokalerror")
	if final_message == "":
		final_message = f"<u>Mamlakat bo'yicha malumotlar: {location['country']}</u>\n" \
				f"Oxirgi malumotlar:\n<b>" \
				f"🦠 Kasallanganlar soni: </b>{location['confirmed']}\n💡 Shulardan sog'ayganlar: {location['recovered']}\n<b>💡 Vafot etganlar: </b>" \
				f"{location['deaths']}\n💉 Davolanayotganlar: {location['active']}\n🇺🇿  @koronavirus_status_bot"

	bot.send_message(message.chat.id, final_message, parse_mode='html')

	if message.chat.id == 526188312:
		bot.send_message(message.chat.id, "😜Salom Shirin Qiz Sizga 🤓 @orzumurod dan Salom ♾")
	elif message.chat.id == 398437601:
		bot.send_message(message.chat.id, "Salom Yaxshi 😂Qiz Sizga 🤓 @orzumurod dan Salom")
	elif message.chat.id == 914886587:
		bot.send_message(message.chat.id, "😂Salom Boshliq")
	elif message.chat.id == 498572591:
		bot.send_message(message.chat.id, "Salom honadosh 😜")
	elif message.chat.id == 1223885191:
		bot.send_message(message.chat.id, "Salom honadosh 😜")
	elif message.chat.id == 885529458:
		bot.send_message(message.chat.id, "Salom😜 Bobur ishla zo'rmi, 🙃😋hotining 😂qale ?!")
	elif message.chat.id == 675884105:
		bot.send_message(message.chat.id, "Salom 😂bratishka 😂))) qishlaqi😂 !!! ishma 😂???")
	else:
		bot.send_message(message.chat.id, "🦠 Koronavirus Haqida aniq statistika: 🦠 @Koronavirus_status_bot 🇺🇿Do'stlaringizga ulashing,😜😷Niqob taqing :) va Uyda qoling!!!")
# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)