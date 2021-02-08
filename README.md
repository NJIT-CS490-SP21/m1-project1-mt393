# Music web app

## steps

1. install the spotipy, dotenv, and flask each respectively with the following commands in the terminal
`pip install spotipy --upgrade`
`pip install -U python-dotenv`
`pip install Flask`
2. log in to your Spotify account at https://developer.spotify.com/dashboard/login
3. click `CREATE AN APP` and fill in the blanks as you please, check the boxes at the bottom and hit the big green button
4. create a file called `music.env` in the same directory as this app
5. In that file, you will enter the 2 lines
`export SPOTIPY_CLIENT_ID=''`
`export SPOTIPY_CLIENT_SECRET=''`
6. go back to the window with your spotify app. copy the client ID and paste it between the apostrophes on the first line
7. go back to the window with your spotify app. click `SHOW CLIENT SECRET` then copy the client secret code and paste it between the apostrophes on the second line
8. save music.env
9. run `python app.py` in the terminal


## unsolved issues :(

issue: I should allow for user input by giving them a choice of artists
potential solution: I can make a button for each and use javascript's onclick function to handle the changing of pages

issue: the app is ugly
solution: I can use css for beauty and html for strucure. i can use the background attribute to add color with the margin attribute for a border. i can also tabulate the information im presenting with the table tag. That would make it easier for me to scale up and add more information like lyrics

## solved issues :)
issue: I dont know the html to add the link to whatever filetype the audio is. its not an image though the player has an appearance. The link doesnt end in .mp3 or anything, so what is this filetype and how do i incorporate?
solution: i still dont know the filetype but html has an all encompassing audio tag that allowed for it.

issue: i sometimes get an out of range error when opening my app. am i launching something wrong? i assume so because i tried again and it worked.
solution: one of the random cases was causing the out of bound error. i had used randint(1,3) instead of randint(0,2) to pick from my list of 3 artists.

issue: find_dotenv was the wrong datatype for load_dotenv
solution: hardcode, as a string, the name of my .env file in to load_dotenv
