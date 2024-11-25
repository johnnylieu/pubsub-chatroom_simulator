import redis

def publisher():
    r = redis.Redis()
    
    while True:
        message = input("Enter a message: ")
        r.publish("chatroom", message)
        print(f"Published: {message}")

if __name__ == "__main__":
    publisher()

    
# Google pubsub did not work for separate files
# from pubsub import pub
# import time

# def send_message(message):
#     pub.sendMessage('chatroom.message', message=message)
#     print(f"Sending message to 'chatroom.message': {message}")

# if __name__ == "__main__":
#     while True:
#         try:
#             message = input("Enter a message to send to the chatroom: ")
#             send_message(message)
#             time.sleep(2)
#         except KeyboardInterrupt:
#             print("\nPublisher stopped.")
#             break