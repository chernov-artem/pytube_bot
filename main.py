import telebot
from pytube import YouTube

"телеграм бот для скачивания видео с youtube"

token="6900428753:AAGlan5-Mi73Q2JftS3i30d0Ho1iCZWY2U8"



def telegram_bot(token):
    "функция телеграм бота"
    bot = telebot.TeleBot(token)

    def download_video(ref):
        "функция скачивания видео"
        yt = YouTube(ref)
        print('title: ', yt.title)
        print('Views: ', yt.views)
        print('Streams: ', yt.streams)
        yt.streams.get_highest_resolution().download('videos')

    @bot.message_handler(commands=["start"])
    def start_message(message):
        "стартовая функция"
        bot.send_message(message.chat.id, "Hello!")

    @bot.message_handler(content_types=["text"])
    "функция обработки входящих сообщений"
    def send_text(message):
        tmp_ref = message.text
        if message.text == "test":
            bot.send_message(message.chat.id, "test ok")
        else:
            try:
                download_video(tmp_ref)
            except Exception as ex:
                bot.send_message(
                    message.chat.id,
                    f"something wrong: {ex}"
                )
                print(ex)

            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, 'загрузка окончена. Видео в папке videos')



    bot.polling()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    telegram_bot(token)


