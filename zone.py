class Zone:
    """
    A Zone object that holds the information that will be presented to the user upon web app opening. 

    Presents attributes of plant object based on inputted nam, number, and position from dictionary.

    Attributes
    ----------
     name: str
           The plant's name 
    """
    def __init__(self, widthOfZone, heightOfZone, plants, zoneName):
        """
        Constructor to build a Zone object.

        Parameters
        ----------
        widthOfZone : str
            The width dimension of the zone

        heightOfZone : int
            The height dimension of the zone

        zoneName : int
            The zone's name of the plant

        plants : array
            The catalogue of text file plants

        Returns
        -------
        None
        """
        self.widthOfZone = widthOfZone
        self.heightOfZone = heightOfZone
        self.zoneName = zoneName

    def printZoneName(self):
        """
        This function prints the zone's name from the lowest to greatest values. Outputs the assignment requirement
        alongside zone dictionary read/written output.

        Parameters
        ----------
        none
        
        Returns
        -------
        string, int
        """
        self.zoneNameDict = {}

        newDict = {}
        with open('zones.txt', 'r') as f:
            for line in f:
                splitLine = line.split()
                newDict[str(splitLine[0])] = ",".join(splitLine[1:])

                print(newDict)
        for value in sorted(newDict.keys()):
            print('%s %s' % (value, newDict[value]))
