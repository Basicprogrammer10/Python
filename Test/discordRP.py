from pypresence import Presence
import time

# Fake ID, put your real one here
client_id = '785038683316813844'
RPC = Presence(client_id)  # Initialize the client class
print(RPC.connect())  # Start the handshake loop

print(RPC.update(state="Lookie Lookie",
                 details="A test!"))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15)  # Can only update rich presence every 15 seconds
