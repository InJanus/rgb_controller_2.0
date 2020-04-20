#UPDATED CONTROLLER TIME

for this one is going to be better than the last one

#updated hardware

A rasberry pi will be controlling the led functions and hosting a web server that will host a webpage that you can controll the lights from. the biggest drawback of the prevoius model was that everything was on the switch board and it looked ugly.

the old hardware was the arduino controlliung everything to having fade functions that was better than other controllers and having a rave mode and strobe mode. now the area that is using this is a bedroom so not much bigger of a strip is needed with the last one. 
i had some voltage drop since it was so long.

i did beef up the powersupply anyway so being able to get more power to the arduino and driver board.

i am still using 4 pin rgb strips so that will be the same.

#new features

web control pannel
programable color modes
personal network hosting

#project steps

get the api programed and tested
    this means to have jump and fade functions
    high intensity functions will have thier own api calls(rave and strobe)
    preset funtions will have thier own api call functions (genaric fade and jump)
create the web panel
    interactive gui to controll the lights. 
    smartphone and desktop control
deployable
    auto start python api
    auto start web server
    dns name hosting(dont want to have to remember an ip ok?)

optional
    python client program?