---
toc: true
layout: post
description: Planning/Outline for Performance Task
categories: [markdown]
title: College Board Create Performance Task
---

# Performance Task Outline 
> Hacks: Start an outline on how you will prepare for the Create Performance Task project.

## Hacks
### Outline:

 **Establish a personal or pair Scrum Board with active and future Issues-** I will have a pair to show my work with, along with my partner, either Lydia or Shruthi. 

**Start a design that _post that can be reviewed to see if it meets the basicCreate Performance Task requirements. Be sure to pick something that you don’t burn out on or is not overly common-** I think for my performance task I will simulate/design a game that is a tournament situation of Brazilian Jiu-Jitsu. This is something I won't burn out on and it is definitely not overly common. The person playing the game will choose their strategy and different moves or techniques the player wants to do to its opponent. Scores will be held with the points, as long as advantages/disadvantages, which are in basic Brazilian Jiu-Jitsu Tournaments. I will even give the choice in the beginning for what team the player wants to be on, what division they want ot be in, and what gi they would like to wear. 
   I will include an input in the beginning for people to add their information/players information, this information would be added as a record into a list. The list will be of all of the existing players, with their player information and the ending score. And at the end of the game it will list out the top scores/players. 
   The game will probably ask questions regarding what move they want to make, if they are going to do that move right away or wait. These questions will possibly be in a loop.

## My preparation
I will look over all of my notes taken and my blogs demonstration different requirements, like lists, iterations, loops, etc. I will also look over examples in the collegeboard, ones that are great on including every aspect and earned great scores, and ones that did not include every aspect and lost a lot of points. I will also review the rubric and scoring as I am looking at these examples, and as I am adding onto my ideas of the performance task. During my code I will add comments, cite codes that I got from others, rearrange codes in better orders, shortening codes with variables, and just fine tuning it to be at its best. 

### Codes I will use in my Performance Task

```python
# Prints a dictionary and the lists and records within it

# Define an empty List called InfoDb
InfoDb = []

# Append to List a Dictionary of key/values related to a person and cars
InfoDb.append({
    "Name": "Elly",
    "DogBreed": "Rottweiler",
    "DOB": "January 18 2010",
    "Residence": "Escondido",
    "FavoriteColor": "Red",
    "FavoriteHobbies": ["Sleeping", "Eating", "Playing"], 
    "Weight": "96.7 pounds"

})


# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "Name": "Athyna",
    "DogBreed": "Pitbull",
    "DOB": "April 25 2012",
    "Residence": "Escondido",
    "FavoriteColor": "Purple",
    "FavoriteHobbies": ["Sleeping","Chasing animals", "Playing" ], 
    "Weight": "45.5 pounds"

})

# Print the data structure
print(InfoDb)# given and index this will print InfoDb content
def print_data(d_rec):
    print("\t", d_rec["Name"])  # using comma puts space between values
    print("\t", "Residence:", d_rec["Residence"]) # \t is a tab indent
    print("\t", "Birth Day:", d_rec["DOB"])
    print("\t", "Favorite Color:", d_rec["FavoriteColor"])
    print("\t", "Favorite Hobbies:", d_rec["FavoriteHobbies"])
    print("\t", "Weight: ", end="")  # end="" make sure no return occurs
    print("".join(d_rec["Weight"]))  # join allows printing a string list with separator
    print() 

def for_loop():
    print("My Dogs Info\n")
    for record in InfoDb:
        print_data(record)

for_loop()
```

    [{'Name': 'Elly', 'DogBreed': 'Rottweiler', 'DOB': 'January 18 2010', 'Residence': 'Escondido', 'FavoriteColor': 'Red', 'FavoriteHobbies': ['Sleeping', 'Eating', 'Playing'], 'Weight': '96.7 pounds'}, {'Name': 'Athyna', 'DogBreed': 'Pitbull', 'DOB': 'April 25 2012', 'Residence': 'Escondido', 'FavoriteColor': 'Purple', 'FavoriteHobbies': ['Sleeping', 'Chasing animals', 'Playing'], 'Weight': '45.5 pounds'}]
   
   My Dogs Info

	 Elly
	 Residence: Escondido
	 Birth Day: January 18 2010
	 Favorite Color: Red
	 Favorite Hobbies: ['Sleeping', 'Eating', 'Playing']
	 Weight: 96.7 pounds

	 Athyna
	 Residence: Escondido
	 Birth Day: April 25 2012
	 Favorite Color: Purple
	 Favorite Hobbies: ['Sleeping', 'Chasing animals', 'Playing']
	 Weight: 45.5 pounds









