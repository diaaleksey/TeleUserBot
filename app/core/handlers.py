from pyrogram import Client, filters
from pyrogram.types import Message


class EventHandlers:
    """Обработчики событий от пользователей"""

    def __init__(self, client: Client, logger, action_logger):
        self.client = client
        self.logger = logger
        self.action_logger = action_logger
        self._register_handlers()

    def _register_handlers(self):
        """Регистрация всех обработчиков"""

        @self.client.on_message(filters.private & filters.text)
        async def handle_private_message(client: Client, message: Message):
            """Обработка личных сообщений к боту"""

            user = message.from_user
            log_entry = (
                f"Сообщение от пользователя | "
                f"ID: {user.id} | Имя: {user.first_name} | "
                f"Username: @{user.username} | "
                f"Текст: {message.text[:200]}"
            )
            self.action_logger.info(log_entry)
            self.logger.info(f"Получено сообщение от {user.first_name}: {message.text[:50]}...")

            # Здесь можно добавить логику ответа на сообщения
            # Например: команды /help, /status и т.д.
            if message.text.lower() == '/start':
                await message.reply(
                    "👋 Привет! Я Userbot.\n\n"
                    "Мои команды:\n"
                    "/status - статус бота\n"
                    "/help - эта справка"
                )
                self.action_logger.info(f"Отправлен ответ /start пользователю {user.id}")

            elif message.text.lower() == '/status':
                me = await client.get_me()
                status = (
                    f"✅ Бот активен\n"
                    f"📱 Аккаунт: {me.first_name}\n"
                    f"🆔 ID: {me.id}\n"
                    f"👥 В контактах: (информация о контактах)"
                )
                await message.reply(status)
                self.action_logger.info(f"Отправлен статус пользователю {user.id}")

        @self.client.on_message(filters.group & filters.text)
        async def handle_group_message(client: Client, message: Message):
            """Обработка сообщений в группах (просто логируем)"""

            chat = message.chat
            user = message.from_user

            self.action_logger.info(
                f"Сообщение в группе | Группа: {chat.title} (ID: {chat.id}) | "
                f"Пользователь: {user.first_name} (ID: {user.id}) | "
                f"Текст: {message.text[:200]}"
            )