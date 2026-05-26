import asyncio
import sys
from app.core.client import UserBotClient
from app.core.logger import setup_logger
from app.core.handlers import EventHandlers
from app.actions.group_manager import GroupManager
from app.actions.contact_manager import ContactManager


async def main():
    # Инициализация компонентов
    bot_client = UserBotClient(use_proxy=True)  # Можно отключить прокси: use_proxy=False
    logger, action_logger = setup_logger("UserBot.Main")

    client = None

    try:
        # Инициализация клиента
        client = await bot_client.initialize()

        # Запускаем с автоматическими переподключениями
        if not await bot_client.start_with_retry(max_retries=3):
            logger.error("❌ Не удалось запустить бота после всех попыток")
            return

        # Инициализация менеджеров
        group_manager = GroupManager(client, logger, action_logger)
        contact_manager = ContactManager(client, logger, action_logger)

        # Инициализация обработчиков событий
        event_handlers = EventHandlers(client, logger, action_logger)

        # ✅ ТВОИ ЗАДАНИЯ ДЛЯ ВЫПОЛНЕНИЯ
        # Раскомментируй нужные строки и укажи параметры

        # 1. Добавление в группу и приветствие
        # await group_manager.join_group_and_welcome(
        #     invite_link="https://t.me/+xxxxxxxxxxx",
        #     welcome_message="👋 Привет всем! Я новый участник. Рад быть с вами!"
        # )

        # 2. Добавление контакта и приветствие
        # await contact_manager.add_contact_and_welcome(
        #     user_input="@username",
        #     welcome_message="Привет, {name}! Рад познакомиться!"
        # )

        logger.info("🚀 Userbot запущен и готов к работе")
        logger.info("📝 Все действия логируются в папке logs/")
        logger.info("⏸ Для остановки нажми Ctrl+C")

        # Держим бота активным
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        logger.info("\n⏹ Получен сигнал остановки от пользователя")
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}", exc_info=True)
    finally:
        # Безопасная остановка
        if bot_client:
            await bot_client.stop()
        logger.info("Программа завершена")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем")
    except Exception as e:
        print(f"Необработанная ошибка: {e}")
        sys.exit(1)