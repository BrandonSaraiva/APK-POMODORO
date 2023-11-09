# About Pomodoro App

Application I made for personal use because I was very frustrated with other applications on the play store related to pomodoro. The interface is intentionally simple and unique. In the APLICATIVO_CELL folder you will find the .pkg where you can download it to your phone and use the application at will. Being able to transform main.py into a .pkg executable was much more difficult than building the application itself in Python 😓 (I took several interfaces and counters on the internet and mixed them until this application came out), it took about 9 hours trying different methods and configuring very specific things in the .spec file until the .pkg actually works. Below is the video and the website that helped the most:

**Video:** https://www.youtube.com/watch?v=GTkKul8sA-c

**Website:** https://towardsdatascience.com/3-ways-to-convert-python-app-into-apk-77f4c9cd55af

# About Kivy

**How to install library and package documentation:** https://kivy.org/doc/stable/gettingstarted/installation.html
-------------------

# Using the application

As I said before, I created it for personal use, so instead of following the normal pomodoro pattern of 25 minutes of work and 5 minutes of rest with a long break of 15 minutes, this Pomodoro is 50 minutes of work with 10 minutes of rest and at the end of 4 work sessions we have a 30 minute long break. I'm more productive with this method, which is why I use it (an entire session of the normal pomodoro is equivalent to 2 hours, this in total is equivalent to 4). The daily goal is to complete 2 sessions totaling 8 hours in total. Now let's go to the app:

**App:**

![image](https://user-images.githubusercontent.com/90096835/213074181-43d16d20-2f42-4d48-ae9f-de0f1d990e75.png)

**The "go go go" image is equivalent to play, when clicked the counter will start**

![image](https://user-images.githubusercontent.com/90096835/213075143-33ee8bb7-7105-427b-aa1b-f12a1466c309.png)

**If you want to pause the counter, just click on the Ice Cream (it gets cold there)**

![image](https://user-images.githubusercontent.com/90096835/213075250-d3f20656-39b6-4a20-a604-d94b9d4b3a58.png)

**The skip button will skip your current session, whether work or rest, you will go to the next one**

![image](https://user-images.githubusercontent.com/90096835/213075362-7d9cdd4b-c3eb-4430-ac1e-5550cae08a03.png)

**If you want to reset everything, click on the meme button**

![image](https://user-images.githubusercontent.com/90096835/213075497-59f9c7d0-aeaa-4a29-bf25-79f1ccffc12f.png)

**The bugger appears when the pomodoro is not started, so there is no way to reset it**

![image](https://user-images.githubusercontent.com/90096835/213075715-7402a17e-bc91-4ba9-86e2-4ee4b9a951ff.png)

**The number is the remaining time, counting down. Status is which current session you are in [work or rest]. "Cycles completed" is the count of cycles that have already been completed and that remain until the long break. The zero is how many complete cycles you have already done.**

![image](https://user-images.githubusercontent.com/90096835/213076263-a12d8288-87ef-4d8b-8076-5ff9b581ddac.png)

-------------
*You will know that the work time is over when the vector says "aaaah eeee" and a message written CABOUCI! to appear. When the rest time ends, this message will also appear, but with the audio of the pica pal witch "and here we go". Remember to press play when you're ready for the new cycle.*
