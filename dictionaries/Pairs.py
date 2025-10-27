# Using zip
key = ['room', 'capacity', 'equipment']
values = ['Conference A', 20, 'projector']
meeting_room = dict(zip(key, values))
room1 = meeting_room['room']
print(room1)