####  DELETE WEBEX "DEMO" SPACES
from webexteamssdk import WebexTeamsAPI
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
access_token = "Nzk5Njk4MzctYmJmNS00YzQ0LTliMDUtNTYwZjIxMjQxODMxZGJhMWEzOTMtNWIz_P0A1_5d6a13c3-cd60-473d-a264-caff0c1a43a6"
api = WebexTeamsAPI(access_token=access_token)
# Find all rooms that should be removed
all_rooms = api.rooms.list()

demo_rooms = [room for room in all_rooms if 'test' in room.title]

# Delete all of the demo rooms
for room in demo_rooms:
    print("Deleting ... " + room.title)
    api.rooms.delete(room.id)
