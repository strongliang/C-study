#Dictionaries of Dictionaries (of Dictionaries)

#The next several questions concern the data structure below for keeping 
#track of Udacity's courses (where all of the values are strings):
  
#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

#For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
#                 'cs004': {'name': 'blah', 'teacher': 'Dave', 'assistant': 'Dave'}
                     }
    }


#For the following questions, you will find the
#        for <key> in <dictionary>:
#                   <block>
#construct useful.  This loops through the key values in the Dictionary.  For
#example, this procedure returns a list of all the courses offered in the given
#hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

#Define a procedure, is_offered(courses, course, hexamester), that returns True
#if the input course is offered in the input hexamester, and returns False
#otherwise.  For example,

#print is_offered(courses, 'cs101', 'apr2012') => True
#print is_offered(courses, 'cs003', 'apr2012') => False

#(Note: it is okay if your procedure produces an error if the input hexamester is not included in courses.  
#For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)

def is_offered(courses, course, hexamester):
    if hexamester in courses:
        if course in courses[hexamester]:
            return True
    return False

#Define a procedure, when_offered(courses, course), that takes as a courses data
#structure and a string representing a class, and returns a list of strings
#representing the hexamesters when the input course is offered.  For example,

#print when_offered (courses, 'cs101') => ['apr2012', 'feb2012']
#print when_offered(courses, 'bio893') => []

def when_offered(courses,course):
    res = []
    for hexa in courses:
        if course in courses[hexa]:
            res.append(hexa)
    return res            
    
#print is_offered(courses, 'cs101', 'apr2012')
#print is_offered(courses, 'cs101', 'dec2011')
#print when_offered (courses, 'cs101')
#print when_offered(courses, 'bio893')

#[Double Gold Star] Define a procedure, involved(courses, person), that takes as
#input a courses structure and a person and returns a Dictionary that describes
#all the courses the person is involved in.  A person is involved in a course if
#they are a value for any property for the course.  The output Dictionary should
#have hexamesters as its keys, and each value should be a list of courses that
#are offered that hexamester (the courses in the list can be in any order).

#For example,

# print involved(courses, 'Dave') => {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}
# print involved(courses, 'Peter C.') => {'apr2012': ['cs262'], 'feb2012': ['cs101']}
# print involved(courses, 'Dorina') => {'jan2044': ['cs001']}

def involved(courses, person):
    res = {}
    for hexa in courses: # hexa: level 0 index (apr2012)
        for c in courses[hexa]:  # c: level 1 index (cs101)
            for a in courses[hexa][c]: # a: level 2 index (name, teacher)
                if courses[hexa][c][a] is person:
                    if hexa in res and c not in res[hexa]:
                        res[hexa].append(c)
                    else:    
                        res[hexa] = [c]
    return res

print involved(courses, 'Dave')
print involved(courses, 'Peter C.')
        
print involved(courses, 'Dave') == {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}
print involved(courses, 'Peter C.') == {'apr2012': ['cs262'], 'feb2012': ['cs101']}
print involved(courses, 'Dorina') == {'jan2044': ['cs001']}
print involved(courses, '') == {}
print involved(courses, 'Doraemon') == {}
print involved({}, '') == {}
print involved({}, 'Dave') == {}


        