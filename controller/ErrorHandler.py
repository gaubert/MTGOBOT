class ErrorHandler(Exception):
    #custom Exception parent class to handle errors
    
    def __init__(self, message):
        ERRORHANDLERAPP = settings["ERRORHANDLERAPP"]
        self._errormsg = message
        ErrorHandlerApp = App(ERRORHANDLERAPP)
        if not ErrorHandlerApp.window():
            App.open(ERRORHANDLERAPP); wait(2)
        ErrorHandlerApp.focus(); wait(1)
        self.__openRecord()
        self.__writeRecord()
        ErrorHandlerApp.close()
    def __openRecord(self):
        #this will be different depending on the application
        pass
    def __writeRecord(self):
        type(self._errormsg + "\n")