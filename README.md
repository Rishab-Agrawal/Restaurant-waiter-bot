# Restaurant-waiter-bot

This project was my first in this domain (image processing using OpenCV), and it has been an extensive one, allowing me to explore and use OpenCV exhaustively.
The problem statement here was to allow the robot to act like an autonomous delivery machine, using color detection to help it follow a track,
as well as mark delivery checkpoints.

The track following algorithm was one of the most engaging parts of the project, and was updated many times. Initially, the approach was to use 
contours recognition and compare the midpoint of the contours to the midpoint of the frame, but this was later improved by including angle calculation
and applying the required trigonometry to acheive the optimal error correction.
Color detection was the simpler part of the project, since the corresponding HSV values could be found preceeding the execution using a trackbar mechanism.
The codes here use the web cam of your machine, and the HSV values are corresponding to the objects I used while experimentation, and these may need to be changed 
based upon the requirements.

Initial commits were codes I made for only software implementation, and using the pyserial module to communicate with an Arduino, I extended this to be implemented
on a chassis. The pyserial port value was for my port and the time delays were calculated via experimentation on my arena, and these may be subject to change.
Commits marked 'junk' are codes that were written for miscellineous reasons such as finding certain values for the angle calculation algorithm
used in the path following function.
I haven't provided the google sheets link or the JSON file which would allow you to edit the sheet, but I'll include it if requested or deemed necessary.

The final code allows the bot to take input from a google sheets file, and based upon the requirements of the customers, the bot performs errands by approaching
the respective tables that require the services. Using hand detection, the bot also reads the number of fingers held up by the customers and stores this 
in the sheet as the rating value that the customers have given to the restaurant.
One improvement that could be made to this would be to use QR or bar codes instead of color patches to mark the tables, since this would account for the practicality
in the case of a larger real-world implementation, where the range of colors would pose as a constraint since it is limited to a small value.
