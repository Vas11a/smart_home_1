**<center style="font-size: 25px">HOME UTILITY CONTROLLER USING RASPBERY PI 3B</center>**

<span style="font-size: 18px" >The system includes door openness tracking and home temperature monitoring.  Displays data on the display and also interacts with the telegram bot.<span>

**<center style="font-size: 25px">How program works ?</center>**

<span style="font-size: 18px" >When the system starts, you will see the "Start..." greeting on the display.  After it goes out, the program will start working.  Let's start with the distance sensor.  When it becomes more than 10 cm from the nearest object, the sound turns on and a message is sent to the telegram bot every 10 seconds.  As for the temperature sensor, when you press one of the two buttons, the current temperature will be displayed.  You can also request it via the /temp command in the telegram bot.  And the current temperature will be displayed in the bot.  There is also a power off button.  When you press it, not only the program closes, but the entire system turns off<span>

**<center style="font-size: 25px">What is needed for that?</center>**

> - <span style="font-size: 18px">raspbery pi 3<span>
> - <span style="font-size: 18px">GPIO cables<span>
> - <span style="font-size: 18px">Buttons x2 <span>
> - <span style="font-size: 18px">Resistor 4.7kom<span>
> - <span style="font-size: 18px">Distance sencor HC-SR04<span>
> - <span style="font-size: 18px">Buzzer Iduino<span>
> - <span style="font-size: 18px">Display Wavelshare 9092<span>

**<center style="font-size: 25px">Start assembling</center>**

> <span style="font-size: 20px">Buzzer<span>

* <span style="font-size: 18px">I - GND<span>
* <span style="font-size: 18px">S - GPIO27<span>

> <span style="font-size: 20px">Button OFF<span>

* <span style="font-size: 18px">1 - GND<span>
* <span style="font-size: 18px">2 - GPIO20<span>

> <span style="font-size: 20px">Button Temp<span>

* <span style="font-size: 18px">1 - GND<span>
* <span style="font-size: 18px">2 - GPIO16<span>

> <span style="font-size: 20px">Temp sencor<span>

* <span style="font-size: 18px">Left -GND<span>
* <span style="font-size: 18px">Center - GPIO4 and also resistor for 5v<span>

> <span style="font-size: 20px">Distance sencor<span>

* <span style="font-size: 18px">GND - GND<span>
* <span style="font-size: 18px">VCC - 5v<span>
* <span style="font-size: 18px">ECHO - GPIO27<span>
* <span style="font-size: 18px">TRIG - GPIO22<span>

> <span style="font-size: 20px">Display<span>

* <span style="font-size: 18px">GND - GND<span>
* <span style="font-size: 18px">VCC - 3.3v<span>
* <span style="font-size: 18px">DIN - MOSI<span>
* <span style="font-size: 18px">CLK - CLK<span>
* <span style="font-size: 18px">CS - CE0<span>
* <span style="font-size: 18px">D/S - GPIO21<span>
* <span style="font-size: 18px">RES - GPIO26<span>



**<center style="font-size: 25px">NOTE !!</center>**

> - <span style="font-size: 18px">Enable SPI protocol<span>
> - <span style="font-size: 18px">Enable 1-Wire protocol (GPIO4)<span>
> - <span style="font-size: 18px">Create new telegram bot<span>
> - <span style="font-size: 18px">Install your font (main, str -37)<span>
> - <span style="font-size: 18px"> Configure the program to start when system startup. I Modified file /etc/rc.local and added string "python3 and my way"<span>