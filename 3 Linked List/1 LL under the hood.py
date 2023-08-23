# %% Linked list hard example
# The LL is: 11 -> 3 -> 23 -> 7

head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

# %% usage
print(head["next"]["next"]["value"])



