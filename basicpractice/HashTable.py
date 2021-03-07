from collections import deque


def find_supplier(node):

    searched_person = []
    graph = {}
    graph["you"] = ["alice", "bob", "clarire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["clarire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    search_queue = deque()
    search_queue += graph[node]

    while search_queue:
        print search_queue
        person = search_queue.popleft()

        if person in searched_person:
            print person + " has been searched"
            continue
        else:
            searched_person.append(person)

        if person_is_seller(person):
            print person + " is a mongo seller"
            return True
        else:
            search_queue += graph[person]
    return False


def person_is_seller(person):
    return person[-1] == 'm'

#table = dict()


print find_supplier("you")

