
# Chatroom Simulator with Redis

This project demonstrates two implementations of a simple Pub/Sub chatroom simulator using **Redis**:
1. A single combined script (`chatroom.py`) for both publishing and subscribing.
2. Separate scripts (`publisher.py` and `subscriber.py`) for independent publisher and subscriber processes.

## Prerequisites

1. **Redis**:
   - Install Redis on your machine. Refer to the [Redis installation guide](https://redis.io/docs/getting-started/installation/) for your operating system.
   - Ensure the Redis server is running on the default host (`localhost`) and port (`6379`).

2. **Python**:
   - Python 3.8+ is recommended.
   - Install the required library:
     ```bash
     pip install redis
     ```

## Approach 1: Combined Script (`chatroom.py`)

### Steps to Run:
1. Start the Redis server:
   ```bash
   redis-server
   ```
2. Run the `chatroom.py` script:
   ```bash
   python chatroom.py
   ```
3. Enter messages when prompted. The script will display published and received messages in the same terminal.

---

## Approach 2: Separate Scripts (`publisher.py` and `subscriber.py`)

### Steps to Run:
1. Start the Redis server:
   ```bash
   redis-server
   ```
2. Open two separate terminal windows.

3. In the first terminal, run the `subscriber.py` script:
   ```bash
   python subscriber.py
   ```
   You should see:
   ```
   Subscriber is listening for messages...
   ```

4. In the second terminal, run the `publisher.py` script:
   ```bash
   python publisher.py
   ```
   You can now enter messages in this terminal. For example:
   ```
   Enter a message: Hello, World!
   Published: Hello, World!
   ```
   The message will appear in the `subscriber.py` terminal:
   ```
   Received: Hello, World!
   ```

---

## Notes

1. **Stopping the Scripts**:
   - Use **Ctrl+C** to stop the scripts gracefully.

2. **Error Handling**:
   - If Redis is not running, you'll see a `ConnectionRefusedError`. Ensure the Redis server is started before running the scripts.

3. **Future Enhancements**:
   - Implement message persistence using a database.
   - Extend the project to support multiple subscribers.

