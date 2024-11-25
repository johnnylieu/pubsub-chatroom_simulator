import redis

def subscirber():
    r = redis.Redis()
    pubsub = r.pubsub()
    pubsub.subscribe('chatroom')
    print("Subscriber is listening for messages...")

    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received: {message['data'].decode()}")

if __name__ == "__main__":
    try:
        subscirber()
    except KeyboardInterrupt:
        print("Subscriber stopped.")


# Google pubsub did not work for separate files
# from pubsub import pub

# def receive_message(message):
#     print(f"Received message: {message}")

# if __name__ == "__main__":
#     pub.subscribe(receive_message, 'chatroom.message')
#     print("Waiting for messages...")

#     try:
#         while True:
#             pass  # keeps the subscriber running
#     except KeyboardInterrupt:
#         print("Subscriber has been stopped.")