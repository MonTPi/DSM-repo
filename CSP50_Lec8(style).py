##Style
from gitGo import git_go
# black style guide is oppinionated so it formats code based on a set of values

housemates = {"will" : "Megan", "Andy" : "Music", 'Josh': 'video games', "ABdul" : "moi Thai"}
for _ in housemates : 
    print(_)

# black 'file name' ->

housemates = {
    "will": "Megan",
    "Andy": "Music",
    "Josh": "video games",
    "ABdul": "moi Thai",
}
for _ in housemates:
    print(_)

print(housemates["ABdul"], housemates["will"])

git_go()
