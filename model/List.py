class List(object):
    #parent class for cards and packs wanted classes
    def __init__(self):
        #change to private variables later
        self._wanted = {}
        self._have = {}
        
    def get_wanted(self):
        return self._wanted
    def get_have(self):
        return self._have