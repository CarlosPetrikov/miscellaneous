import asyncio

a = ['A', 'B', 'C']
b = [1, 2, 3]

async def f_a():
    for x in a:
        print(x)
        await asyncio.sleep(1)
        
async def f_b():
    for x in b:
        print(x)
        await asyncio.sleep(1)
        
async def main():
    task1 = asyncio.create_task(
        f_a())
    
    task2 = asyncio.create_task(
        f_b())  
      
    await task1
    await task2
#------------------------------------[CÓDIGO PRINCIPAL]--------------------------------------------
while True:
    asyncio.run(main())