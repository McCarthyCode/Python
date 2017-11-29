def print_students(values):
    for obj in values:
        print obj['first_name'] + " " + obj['last_name']

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print_students(students)

#################################################################

def print_users(values):
    print "Students"
    count = 1
    for obj in values['Students']:
        first_name = obj['first_name'].upper()
        last_name = obj['last_name'].upper()
        chars = len(first_name) + len(last_name)

        string = str(count) + " - "
        string += first_name + " " + last_name + " - " + str(chars)

        print string
        count += 1

    print "Instructors"
    count = 1
    for obj in values['Instructors']:
        first_name = obj['first_name'].upper()
        last_name = obj['last_name'].upper()
        chars = len(first_name) + len(last_name)

        string = str(count) + " - "
        string += first_name + " " + last_name + " - " + str(chars)

        print string
        count += 1


users = {
    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}

print_users(users)
