# Telegram parser
This code is designed to extract messages and participant information from Telegram channels and chats using the Telethon library.

The code consists of three main functions: `dump_all_messages(channel)`: Extracts all messages from the specified channel or chat and saves them to the `channel_messages.json` file. `dump_all_participants(channel)`: Extracts information about all participants in the specified channel or chat and saves them to the `channel_users.json` file. `main()`: The main function that prompts the user for a link to a channel or chat and calls the `dump_all_messages(channel)`
function.
# Usage instructions
Install the Telethon library if you don't have it yet: `pip install telethon`
Create a `config.ini` file in the same directory as the code. The file should contain the following parameters:
```
[Telegram]
api_id = YOUR_API_ID
api_hash = YOUR_API_HASH
username = YOUR_USERNAME
```
Replace `YOUR_API_ID`, `YOUR_API_HASH`, and `YOUR_USERNAME` with the corresponding values obtained when registering your application on ***my.telegram.org***. Run the code. You will be prompted to enter a link to a channel or chat. Enter the link and press Enter. After the code completes its execution, you will find two files in the same directory: `channel_messages.json` containing all the messages from the channel or chat, and `channel_users.json` containing participant information. 


# ИНСТРУКЦИЯ НА РУССКОМ 


Этот код предназначен для извлечения сообщений и информации об участниках из каналов и чатов Telegram с использованием библиотеки Telethon. Код состоит из трех основных функций:
`dump_all_messages(channel)`: Извлекает все сообщения из указанного канала или чата и сохраняет их в файл `channel_messages.json`.
`dump_all_participants(channel)`: Извлекает информацию обо всех участниках указанного канала или чата и сохраняет их в файл `channel_users.json`.
`main()`: Основная функция, которая запрашивает у пользователя ссылку на канал или чат и вызывает функцию `dump_all_messages(channel)`.

# инструкция по использованию
Установите библиотеку Telethon, если у вас ее еще нет:
`pip install telethon`

Создайте файл `config.ini` в той же директории, где находится код. В файле должны быть следующие параметры:
```
[Telegram]
api_id = ВАШ_API_ID
api_hash = ВАШ_API_HASH
username = ВАШ_ЛОГИН
```
Замените `ВАШ_API_ID`, `ВАШ_API_HASH` и `ВАШ_ЛОГИН` на соответствующие значения, полученные при регистрации вашего приложения на `my.telegram.org`.
Запустите код. Вам будет предложено ввести ссылку на канал или чат. Введите ссылку и нажмите Enter.
После завершения работы кода, вы найдете два файла в той же директории: `channel_messages.json` и `channel_users.json`. В первом файле будут содержаться все сообщения из канала или чата, а во втором - информация об участниках.
