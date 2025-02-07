# LISTS
# numbers = [1, 2, 3, 4, 5];
# print(numbers[0]);
# numbers.sort();
# print(numbers);
# numbers.append(6);
# print(numbers);
# numbers.reverse();
# print(numbers);
# numbers.pop();
# print(numbers);
# numbers.insert(0, 0);
# print(numbers);
# numbers.remove(0);
# print(numbers);
# numbers.clear();
# print(numbers);

# names = ['John', 'Bob', 'Alice', 'Mary'];
# print(names[0]);
# print(sorted(names));
# print(names);
# names.append('Mike');
# print(names);
# names.reverse();
# print(names);

# names=['John', 'Bob', 'Alice', 'Mary', 'Michale'];
# print(names);
# print(sorted(names, key=len, reverse=True));

# DICTIONARIES
# person = {'name': 'John', 'age': 25, 'isAlive': True};
# print(person['name']);
# for key, value in person.items():
#     print(key, value);
# if 'name' in person:
#     print('Attribute "name" is present');
#     print(person['name']);
# else:
#     print('Attribute "name" is not present');
# person['name'] = 'Alice';
# print(person['name']);

# professors = {
#     'John': {"Math", "Physics", "Chemistry"},
#     'Alice': {"English", "French"},
#     'Bob': {"History", "Geography"},
#     'Mary': {"Biology", "Literature"},
# };
# print(professors['John']);
# materials_list = ", ".join(professors['John']);
# print(materials_list);
# print(materials_list.split(", "));
# print(professors.keys());
# print(professors.values());
# print(professors.items());
# professors['Mary'].add("Economics");
# print(professors['Mary']);

# ***** FUNCTIONS & DICITONARIES *****
# This is the code that was shown in the video
def get_event_date(event):
    return event.date;

def current_users(events):
    events.sort(key=get_event_date);
    machines = {};
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set();
        if event.type == 'login':
            machines[event.machine].add(event.user);
        elif event.type == 'logout' and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user);
    return machines;

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ', '.join(users);
            print('{}: {}'.format(machine, user_list)); 

# To use this code, we will use the following Event class
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date;
        self.type = event_type;
        self.machine = machine_name;
        self.user = user;

# And the following list of events to check the code runs correctly
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
];

# Now, let's call the functions to check if they work correctly
users = current_users(events);
print(users);
generate_report(users);
