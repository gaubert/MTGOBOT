from sikuli.Sikuli import *

#this object will hold all global settings for the application
settings = {"ERRORHANDLERAPP":"Notepad", "LOGIN_WAIT":45, "PASSWORD":"yourpasswordhere", "NETWORK":False, "DEFAULTMODE":"sell"}

#default is 1
Settings.MoveMouseDelay = 0.2
#default is False, don't show visual guide to actions
setShowActions(False)
#default is 2.0(2 seconds delay on show actions)
Settings.SlowMotionDelay = 1.5
#set this lower if cpu usage is too high
Settings.WaitScanRate = 6
#must be 0.8 to 1, in order to maintain accuracy, MAY NOT affect pixel matching operations besides find()
Settings.MinSimilarity = 0.9
#min pixel change to trigger onChange
Settings.ObserveMinChangedPixels = 200
#all find operations which don't use other regions should use this one
