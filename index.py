import time
import threading
import asyncio


def synchronous_traffic_light():
    while True:
        print("Red light")
        time.sleep(5)
        print("Green light")
        time.sleep(5)
        print("Yellow light")
        time.sleep(2)

async def asynchronous_traffic_light():
    while True:
        print("Red light")
        await asyncio.sleep(5)
        print("Green light")
        await asyncio.sleep(5)
        print("Yellow light")
        await asyncio.sleep(2)


def thread_traffic_light():
    def red_light():
        while True:
            print("Red light")
            time.sleep(5)

    def green_light():
        while True:
            print("Green light")
            time.sleep(5)

    def yellow_light():
        while True:
            print("Yellow light")
            time.sleep(2)

    red_thread = threading.Thread(target=red_light)
    green_thread = threading.Thread(target=green_light)
    yellow_thread = threading.Thread(target=yellow_light)

    red_thread.start()
    green_thread.start()
    yellow_thread.start()


if __name__ == "__main__":
    print("Synchronous Traffic Light:")
    synchronous_traffic_light()

    print("\nAsynchronous Traffic Light:")
    asyncio.run(asynchronous_traffic_light())

    print("\nThread Traffic Light:")
    thread_traffic_light()
