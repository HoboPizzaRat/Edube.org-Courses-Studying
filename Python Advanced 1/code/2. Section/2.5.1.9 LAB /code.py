# SCENARIO

# Create a class representing a luxury watch;

# 1. The class should allow you to hold a number of watches 
#    created in the watches_created class variable. The number could be 
#    fetched using a class method named get_number_of_watches_created;

# 2. the class may allow you to create a watch with a dedicated engraving (text). 
#    As this is an extra option, the watch with the engraving should be created 
#    using an alternative constructor (a class method), as a regular __init__ 
#    method should not allow ordering engravings;
# 3. the regular __init__ method should only increase 
#    the value of the appropriate class variable; 

class Watch():
    watchesCreated = 0

    def __init__(self, name):
        Watch.watchesCreated += 1
        self.name = name

    @classmethod
    def get_number_of_watches_created(self):
        return  Watch.watchesCreated

    

class LuxuryWatch(Watch):
    watchesCreated_luxury = 0

    def __init__(self, name):
        super().__init__(name)
        LuxuryWatch.watchesCreated += 1

    @classmethod
    def get_number_of_watches_created(self):
        return LuxuryWatch.watchesCreated_luxury

    @classmethod
    def createWatchWithEngraving(cls, name, text):
        if LuxuryWatch.validateEngravingText(text):
            _watch = cls(name)
            _watch.engraving = text
            return _watch

    @staticmethod
    def validateEngravingText(text):
        if len(text) > 40:
            raise Exception(f"cannot create watch with lenght {len(text)}")
        if not text.isalnum():
            raise Exception(f"cannot create watch with engraving of non alpanumberic characters")
        return True


def printWatchTypeInformation(watchclass):
    classname = watchclass.__name__
    classcount = watchclass.get_number_of_watches_created()
    print("------------------------------")
    print(f"Type of Watch: {classname}")
    print(f"Watches of this type: {classcount}")
    print("------------------------------")



try:
    printWatchTypeInformation(Watch)
    printWatchTypeInformation(LuxuryWatch)

    watch1 = Watch("Shimano")
    watch2 = Watch("Kultainenhanhi")

    printWatchTypeInformation(Watch)
    printWatchTypeInformation(LuxuryWatch)

    # create luxury watch
    engraving1 = "MyBelovedKekkonen"
    name1 = "Rolex"
    watch_luxury1 = LuxuryWatch.createWatchWithEngraving(name1, engraving1)

    printWatchTypeInformation(Watch)
    printWatchTypeInformation(LuxuryWatch)
    # create luxury watch with invalid engraving
    engraving2 = "Ugh ugh agh agh"
    name2 = "ACE Corp"
    watch_luxury2 = LuxuryWatch.createWatchWithEngraving(name2, engraving2)
except Exception as e:
    print(e)


