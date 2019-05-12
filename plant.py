class Plant:
    """
    A Plant object that holds the information about their logistics 

    Presents attributes of plant object based on text file's name, number, and position via a dictionary.

    Attributes
    ----------
     name: str
           The plant's name 
    """

    def __init__(self, name, number, position):
        """
        Constructor to build a Plant object.

        Parameters
        ----------
        name : str
            The plant presented to the user's home dashboard

        number : int
            The number of plants

        position : int
            The co-ordinate of the plant 

        Returns
        -------
        None
        """
        self.name = name
        self.number = number
        self.position = position

    def getName(self, name):
        """
        This function retrieves the plant's name.

        Parameters
        ----------
        none
        
        Returns
        -------
        none
        """
        self.nameDict = {}

        with open('plants.txt', 'r') as f:
            for line in f:
                splitLine = line.split()
                self.nameDict[str(splitLine[0])] = ",".join(splitLine[1:])
