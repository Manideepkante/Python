import random

print('Hello Reader! This is our Story generator.')

readername = input('Your name please : ')
print('Hello ' + readername)

names = [' Mani ', ' Praneeth ', ' Bharath ', ' Ayush ', ' Harsh ', ' Faizan ', ' Shivanshu ', ' Madhav ']

places = [' Hyderabad ', ' Vizag ', ' Secunderabad ', ' Bihar ', ' Patna ', ' Harayana ', ' Tamilnadu ', ' Mumbai ', ' Bengaluru ', ' Manali ', ' Kerala ']

quests = [' arrive to a grand building and take a photograph.', ' to meet a celebrity .', ' drive in a large jeep. ', ' eat pizza at the most Lavish restaurant they come across. ', ' travel on the beautiful places in the middle of the night. ', ' buy 10 expensive things in the most extravagant shop they see along the street .', ' go to the most beautiful places they search up in Kerala .']

roles = [' a innocent boy ', ' a posh boy ', ' a normal boy ', ' a secondary student ', ' a university student ', ' a teen boy ', ' a good looking boy ']

weather = [' a rainy day ', ' a sunny day ', ' a very humid and hot day ', ' a cold night ', ' a cloudy day ']

randomname = random.choice(names)
randomplace = random.choice(places)
randomquests = random.choice(quests)
randomroles = random.choice(roles)
randomweather = random.choice(weather)

story = 'Once upon a time,'+ randomroles + 'called'+ randomname + 'lived in a beautiful place called' + randomplace + 'where it was' + randomweather + 'and he will have to' + randomquests

print(story)
