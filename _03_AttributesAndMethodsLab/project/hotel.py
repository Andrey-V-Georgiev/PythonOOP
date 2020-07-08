from functools import reduce

from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = list()
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        the_room = list(filter(lambda r: r.number == room_number, self.rooms))[0]
        if the_room:
            take_room_str = the_room.take_room(people)
            if not take_room_str:
                self.guests += people
            return take_room_str

    def free_room(self, room_number):
        the_room = list(filter(lambda r: r.number == room_number, self.rooms))[0]
        if the_room:
            free_room_str = the_room.free_room()
            if not free_room_str:
                room_guests = getattr(the_room, 'guests')
                self.guests -= room_guests
            return free_room_str

    def print_status(self):
        free_rooms = list(filter(lambda r: not r.is_taken, self.rooms))
        free_rooms_numbers = list(map(lambda r: r.number, free_rooms))
        free_rooms_numbers_str = ', '.join(map(str, free_rooms_numbers))
        taken_rooms = list(filter(lambda r: r.is_taken, self.rooms))
        taken_rooms_numbers = list(map(lambda r: r.number, taken_rooms))
        taken_rooms_numbers_str = ', '.join(map(str, taken_rooms_numbers))
        print(f'Hotel {self.name} has {self.guests} total guests')
        print(f'Free rooms: {free_rooms_numbers_str}')
        print(f'Taken rooms: {taken_rooms_numbers_str}')


