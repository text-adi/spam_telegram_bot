import asyncio
import logging

from aiogram import Bot, Dispatcher, Router

import config

# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.fsm.storage.redis import RedisStorage

loop = asyncio.new_event_loop()
bot = Bot(token=config.API_TOKEN, parse_mode='HTML')  # parse_mode='MarkdownV2')
dp = Dispatcher()
main_router = Router()

# storage = MemoryStorage()


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG,
                    )


async def on_shutdown():
    """Викнуватися коли будемо стопати бота"""
    logging.warning('Shutting down...')
    print('Shutting down...')

    await bot.close()
    # await dp.st
    # await storage.close()


async def on_startup():
    """При запуску бота"""
    print("tedt")


async def main() -> None:
    from handlers import main_router
    dp.include_router(main_router)
    await dp.start_polling(bot, skip_updates=True, on_shutdown=on_shutdown, on_startup=on_startup)


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        pass
        # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop.run_until_complete(main())
    from handlers.group.main import send_message_time
    loop.create_task(send_message_time())


