import requests
import time
import aiohttp, asyncio
import httpx

url = "http://localhost:8000/polls/"

for i in range(5):
    start_time = time.time()
    # response = requests.get(url)                # index
    response = requests.get(url+'hello')                # index
    # response = requests.get(url+'async')                # index_async
    # response = requests.get(url+str(i+1))     # detail
    # response = requests.get(url+'add')        # add_question
    print('status_code',response.status_code, 'execution time is %.4f' % float(time.time() - start_time))

# help(response)
# print('status_code: ', response.status_code)
# print('status_code: ', response.text)

# -------------ASYNCIO-----------------
url = "http://localhost:8000/polls/async/hello"

# session = aiohttp.ClientSession()
# async def future_example(session):
#     resp = await session.get(url)
#     data = await resp.text()
#     await session.close()
#     return resp

# data = await future_example(session)
# data = asyncio.run(future_example(session))
# print(data)

# async def future_example():
#     session = await aiohttp.ClientSession()
#     resp = await session.get('https://www.google.com/')
#     data = await resp.text()
#     await session.close()
#     return resp
#
# data = asyncio.run(future_example())

async def http_call_async():
    async with httpx.AsyncClient() as client:
        start_time = time.time()
        r = await client.get(url)
        # print(r.text)
        print('status_code', r, 'execution time is %.4f' % float(time.time() - start_time))


# print(data)

async def gather_tasks():
    await asyncio.gather(
        http_call_async(),
        http_call_async(),
        http_call_async(),
        http_call_async(),
        http_call_async()
    )

# data = asyncio.run(gather_tasks())