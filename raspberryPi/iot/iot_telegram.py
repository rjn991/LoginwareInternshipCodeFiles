#pip install telebot
import telepot


token = '6387379359:AAEo9xEosNf3npjE-oGyzGGkljbZZkIdcm0' # telegram token
receiver_id=986893115  # https://api.telegram.org/bot<TOKEN>/getUpdates


bot = telepot.Bot(token)
while 1:
	bot.sendMessage(receiver_id, 'hello') # send a activation message to telegram receiver id

#bot.sendPhoto(receiver_id, photo=open('test_img.png', 'rb')) # send message to telegram
