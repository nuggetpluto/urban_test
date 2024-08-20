import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        print(f'Силач {name} поднял {i} шар.')
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('мощнявый', 10))
    strongman2 = asyncio.create_task(start_strongman('дохлый', 15))
    strongman3 = asyncio.create_task(start_strongman('ну прям самый сильный', 12))
    await asyncio.gather(strongman1, strongman2, strongman3)


if __name__ == '__main__':
    asyncio.run(start_tournament())
