# EmpireBikesBack
PennApps XIX - github Repo


Car Detection from a biker's helmet. 

Have you ever been biking on a road and a car has gotten too close behind you? 
Have you every been biking on a road and needed to switch lanes but couldn't take your eyes of the road long enough to check for cars in the other lane?

Well here is the solution to those problems...

EmpireBikesBack is image recognition software that looks for cars behind you to check to see if making a lane change is safe!
It uses voice comamands to check either the left or the right side of the road. Then lets you know if it is safe to switch lanes.

This is mostly a concept piece in which you would have a camera facing behind you. The camera would then recognize cars with the help of a rasberry pi or some other microcontroller also attached to the bike. This is not limited to bikes but also to any moving vehicle and could lead to first autonomous bicycle!

This uses opencv, tkinter, numpy, os, Speech Recognition, PyAudio, etc.

In order to run...
  python gui.py
  click exit button to exit
  click speak button to say which direction you would like to switch lanes to
  the image on the right is of the calulated road lines
  the image on the left is of the captured image
  
