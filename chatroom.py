# virtual env
# on powershell: .\pubsub-chatroom\Scripts\activate
# on bash: python -m venv pubsub-chatroom 

from pubsub import pub
import threading

def receive_message(message):
    print(f"Subscriber received: {message}")

def subscriber():
    pub.subscribe(receive_message, 'chatroom.message')
    print("Subscriber is listening for messages...")
    while True:
        pass

def publisher():
    while True:
        message = input("Enter a message to send: ")
        pub.sendMessage('chatroom.message', message=message)
        print(f"Publisher sent: {message}")

if __name__ == "__main__":
    threading.Thread(target=subscriber, daemon=True).start()
    publisher()