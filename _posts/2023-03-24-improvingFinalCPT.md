---
title: Improving on my Individual Feature in CPT Final Project
layout: post 
description: Goals on Final CPT Project for AP Collegeboard submission
---
# My CPT Project
In trimester 2, my group and I decided to create a project that acts as a guide/trip planner in places within San Diego County. The homepage would have a photo wheel which infinitely shuffles through some of the top activities/restaurants/tourist spots etc... The features would include a sort of wishlist which would save the places/activities in a list that they can refer back to. This would help them narrow down which trip ot go on and future trips to go on as well. Another feature was a tool that filters options out depending on the users input, for example, time, duration of trip, budget, destination... Another feature was the reviews, similar to Yelp. It would have a rating on each place/activity on a 5-star scale, and then text entries for further explanation.

# My Feature
My feature is a page that has a weather forecast and also a map. These will be connected to 2 outside REST API's, one from Google and one from RapidAPI. The weather will help people decide how to dress for the occasion, for example if it were cold they would layer up and dress warmer. It will also help them decide on the actual activities they want to do or places they want to go. If they wanted to hike, but checked the forecast for that day and saw there would be a storm, they would reschedule or choose a different activity. The map will help people decided on transportation and routes to take. It will act like a GPS, hopefully, and provide the ETA. The length of their location and the actual landmark could be a big factor because some people would not want to travel to far to make sure it fits their schedules. 


# Improvements Overall
- Actually have user input data add to the database and save
    - Have page reloads or "recent searches" so user input it saved and can be referenced again 
- Add in the map feature, an interactive one and some sort of tool to calculate and decide on transportation


## Backend Code Improvements:
- Utilize a list to store data and manage complexity
- Connect frontend to backend (our database was not connected so the frontend could not take in user input nor connect it to the backend)
    - deploy through AWS (DevOps work)
- Create a working API for Users Class
    - account sign up 
    - account log in 


## Frontend Code Improvements:
- Add more visuals
    - utilize data compression lesson and implement PANDAS/PILLOW... other kernels 
- Make the website more user friendly


