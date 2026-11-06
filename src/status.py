import os
def update_status(status):
    with open("current_status.txt", "w") as f:
        f.write(status)
