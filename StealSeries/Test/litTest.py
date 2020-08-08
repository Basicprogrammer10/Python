import gamesense

# Create a GameSense object instance to use
gs = gamesense.GameSense("SYNC_GAME", "Sync Game")

# Before you can register or send events, you must register your game
gs.register_game(icon_color_id=gamesense.GS_ICON_GOLD)

# Register an event (different than binding an event, see more info in the SteelSeries docs)
gs.register_event("DID_STUFF")

# Test out the event by sending the event
gs.send_event("DID_STUFF", {"value": 22})