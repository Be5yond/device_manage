from sanic import Sanic,response
from queue import Queue, deque

receiver_queue = Queue(40000)
receiver_queue.queue = deque([f'group{j}m{i}' for i in range(20, 100) for j in range(0, 500)])
app = Sanic('device')

# @app.get('/')
# async def main(request):
#     data = [receiver_queue.get() for _ in range(100)]
#     return response.json(data) 


@app.get('/')
async def main(request):
    return response.text('hello world') 


# app.run(host='0.0.0.0', port=9990, debug=True)

# 二分查找，反回数据的索引。数据不存在则返回None。array为有序增数据
def erfen(array, target):
    # 确定左右区间边界，初始为全部数据
    l = 0
    r = len(array)
    # 每次将窗口减半，直到区间内没有数据
    while l < r:
        mid = int((l+r)/2)
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            r = mid
        else:
            l = mid
    return None

erfen([1,3,4,6,9], 6)