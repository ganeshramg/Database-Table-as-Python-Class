class Table:
    def __init__(self,name,features,entries = []):
        self.name = name
        self.features = features
        self.entries = entries

    def getShape(self):
        x = len(self.entries)
        y = len(self.features)
        return x,y

    def changeName(self,name):
        self.name = name
        print("\nName changed to \'{}\'".format(self.name))

    def getFeatures(self):
        return self.features

    def addEntry(self,entry):
        noOfColumns = len(self.features)
        if len(entry) < noOfColumns:
            print("Missing values!")
        elif len(entry) > noOfColumns:
            print("Feature not defined")
        else:
            self.entries.append(entry)
            print("\nNew Entry added!")
            print(self.features)
            print(entry)

    #To avoid IndexError in the future, we extend the size 
    #of all the entries so far
    def extendEntrySize(self):
        for entry in self.entries:
            if len(entry) < len(self.features):
                while len(entry) < len(self.features):
                    entry.append('-')


    def addFeature(self,feature):
        self.features.append(feature)
        print("A new feature added")
        print(self.getFeatures())
        self.extendEntrySize()

    def viewEntries(self,conditions=False):
        print("\nViewing Table :")

        print(self.features)
        for entry in self.entries:
            print(entry)

    def printMissingEntries(self):
        print("\nPrinting entries with missing values :")
        for entry in self.entries:
            for element in entry:
                if element == '-':
                    print(entry)


    def filter(self,someText):
        feature,condition,value = someText.split(' ')
        rows = self.entries
        print("\nPrinting table with conditions---")
        if condition == 'gT':
            for entry in rows:
                if '-' in entry:
                    continue
                if entry[self.features.index(feature)] > value:
                    print(entry)

        elif condition == 'lT':
            for entry in rows:
                if '-' in entry:
                    continue
                if entry[self.features.index(feature)] < value:
                    print(entry)

        elif condition == 'eq':
            for entry in rows:
                if '-' in entry:
                    continue
                if entry[self.features.index(feature)] == value:
                    print(entry)

        elif condition == 'lTeq':
            for entry in rows:
                if '-' in entry:
                    continue
                if entry[self.features.index(feature)] <= value:
                    print(entry)

        elif condition == 'gTeq':
            for entry in rows:
                if '-' in entry:
                    continue
                if entry[self.features.index(feature)] >= value:
                    print(entry)

        else:
            print("Invalid Condition!")


    def enterMissing(self,id,feature,value):
        for entry in self.entries:
            if entry[0] == id:
                cell = self.features.index(feature)
                if entry[cell] == '-':
                    entry[cell] = value
                    print("\nMissing Entry Added : ")
                    print(entry)

    def slice(self,sliceText):
        def printError():
            print("\nIndexError")
        rows,columns = sliceText.split(',')
        rowStartIndex,rowEndIndex = rows.split(':')
        colStartIndex,colEndIndex = columns.split(':')
        if (int(rowStartIndex) + 1) > len(self.entries):
            printError()
        elif (int(colStartIndex) + 1) > len(self.features):
            printError()
        else:
            print("\nPrinting Sliced table...")
            print(self.features[int(colStartIndex):int(colEndIndex)])
            for index in range(int(rowEndIndex)):
                try:
                    print(self.entries[index][int(colStartIndex):int(colEndIndex)])
                except IndexError:
                    break



stdlst = Table('Student List',['Id','Name','Class','Section'])

stdlst.addEntry(['1','Ganesh','12','A'])
stdlst.addEntry(['2','Ceeari','12','A'])
stdlst.addEntry(['3','Pappu','12','A'])
stdlst.addEntry(['4','Susmi','12','A'])
stdlst.addEntry(['5','Gailash','11','B'])
stdlst.addEntry(['6','Garthi','11','B'])

stdlst.viewEntries()

stdlst.filter('Id gTeq 3')
stdlst.filter('Class lT 12')
stdlst.filter('Section eq A')

stdlst.addFeature('Percentage')

stdlst.addEntry(['7','Ashwath','12','A','50'])
stdlst.addEntry(['8','Bala','12','A','40'])
stdlst.addEntry(['9','Akshay','12','A','30'])
stdlst.addEntry(['10','Vignes','12','A','70'])

stdlst.viewEntries()

stdlst.printMissingEntries()

stdlst.enterMissing('1','Percentage','50')
stdlst.enterMissing('2','Percentage','10')

stdlst.filter('Percentage lT 50')

stdlst.slice('0:20,1:7')
stdlst.slice('0:20,5:7')

stdlst.changeName('Employee List')

print(stdlst.getShape())
