class Map(Plot):
    def __init__(self, width, length, w ,l):
        self.x_position = x position
        self.y_position = y position
        self.w = width
        self.l = length

        [[{}for c in range(length/l)] for r in range(width/w)]
        
        #internally creates 2d array of plots, with each plot being represented by a dictionary

    def plot_coordinates(self):
        # method to return tuple: (Plot object, (x-coord, y-coord))




#should internally create a 2 dimensional array
#2d array of plot 
#each plot repped by a dict 
#next, read in next m rows from file 
#for each row(plant), find coordinates of relevant plot
#and then do the following...
#if there exists a key of the name of plant, increment corresponding value by 1
#if it doesnt exist, add it with a value of one
#As such, this creates a 2d array filled with dictionaries, each one representing the plant
#then iterate through each dict
#check to see whether it has all req-d plants req.
#if it doesnt put that info into results array


#2-dimensional arays indexed by r,c; not x,y