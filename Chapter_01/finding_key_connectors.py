users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendship_pairs = [
        (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
        (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

friends_of_a_user = { user["id"] : [] for user in users  }

for idx, friendIdx in friendship_pairs:
    friends_of_a_user[idx].append(friendIdx)
    friends_of_a_user[friendIdx].append(idx)

def number_of_friends(user):
    # Shape of user object
    # { "id": Number, "name": String }
    user_id = user["id"]
    friends_of_a_particular_user = friends_of_a_user[user_id]
    return len(friends_of_a_particular_user)


print(friends_of_a_user)
