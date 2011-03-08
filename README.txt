This Magic Online Trading Bot was created  by Raymond Cheung.  I can be contacted at darkray16@yahoo.com .

As of March 7th 2011, the bot is able to interact with Magic Online version 3.  Of it's four core functions, buying booster packs, selling booster packs, buying cards, and selling cards, two are currently working.  It is able to buy and sell booster packs.

Disclaimer:
I am a new programmer who is still studying much.  If you find some places in the app which I can improve, please send me an email.  It would be greatly appreciated.

Requirements:
Sikuli
Sikuli is a graphical user scripting language which uses Python syntax.  You can download this at http://sikuli.org and there you can read about the wonderful language.  I chose Sikuli to script in, instead of AutoIt because at the time I wanted to learn Python, and since Sikuli uses Python syntax, it was perfect.  

The only major flaws I have found so far are that it cannot do a pixel scan of a .png that is completely black(#000000).  This is something I have worked around, but it does slow down the trade interactions by about 2-3 seconds total for each interaction.  The second flaw is that there are occasional glitches in the pixel scanning.  I'm still not sure what causes them, but they occur less than 2% of the time.  In the last 4 months of programming I've done on this bot, I've only ever seen it happen twice.

JRE
You will also need to download the Java Runtime Environment from http://www.oracle.com/technetwork/java/javase/downloads/index.html .  Click on the button that says "download JRE".

Magic Online
Obviously.



Starting the application:
First thing's first.  I'm still trying to figure out a way to get the relative paths from Python.

You must go through each of the python files(.py) and edit the import path at the top to wherever you have this folder located.
*Technical
With Sikuli, there are no sys.argv variables, so I am unable to get the relative path of the script file that way.

*IMPORTANT
I have screencapture all the images while the Magic Online App was in it's default size.  What this means is that you should not maximize the Magic Online or change it's size.  I plan to add support for a maximized window in the future.

You should already be logged in to Magic Online.  As soon as you are logged in, just start the bot and it will respond to a trade request.
For testing purposes I have have turned off signin feature.  This is so the user doesn't need to exit Magic Online everytime they have to restart the bot.

After a successful transaction, the bot will open Notepad and write the transaction.  

I have created a convenient start.bat for those who are not especially experienced in programming.  This file will start the Sikuli application, and all you have to do to start the application is click "Run".

Structure:
I have decide to use an MVC structure for my bot.  This may or may not have been the best design pattern, but it is the one I'm most familiar with.  
The view folder contains all the class definitions for interaction with the application itself.  This includes typing or reading messages from chat, posting ads in classifieds, trading, signing in, and so on.  These classes may or may not change heavily when Magic Online Version 4 rolls around.  If possible I will rewrite the application to update it for version 4.
The model folder contains all classes that deal with storing or retrieving database information, like prices, images for pixel scans, transaction records, etc.
The controller folder contains the MainController, which will coordinate the entire application.

In the main folder you will find the main app file, "bot.sikuli".  It instantiates the controller and starts everything.



Planned Features:
As of March 7th 2011, the next feature I plan to add is the core functions handling card buying and selling.  I also plan to add a networking module which will allow the bot to communicate with a central bot server.  I also want the bot to be able to interact with other bots, which is where the networking would come in.