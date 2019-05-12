from mapping import Map

class Plot:
    def __init__(self, x_position, y_position, plant_name):
        self.x_position = x_position
        self.y_position = y_position
        self.plant_name = plant_name

    plant_name = {}

    with open('plants.txt', 'r') as f:
        for line in f:
            splitLine = line.split()
            plant_name[str(splitLine[0])] = ",".join(splitLine[1:])

            print(plant_name)

    def add_plant(self):

        plant_name = self.plant_name 

        if plant_name is not None:
            return

        #from dictionary


    #def needed_plants(self):

        #Calculates how many plants are needed per plot (requirement) 