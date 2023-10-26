import argparse

"""
Create a descender class that holds the functionally as outlined by the prompt
"""
class Descender:
    """
    Takes in a filename, and parses its values into the appropriate fields
    """
    def __init__(self, fileName):
        #Open the file 
        f = open(fileName)
        
        #read the lines
        data = f.readlines()

        #initialize the pyramid
        self.pyramid = []

        #parse through the data
        for i in range(len(data)):

            #if it is the first line, it is the target
            if i == 0:
                self.target = int(data[i][8:])
            else:
                #otherwise, create the individual levels in the pyramid
                temp = []
                split_strings = data[i].split(',')
                for idx in range(len(split_strings)):
                    #get rid of the newline value in the final string
                    if idx == len(split_strings) - 1:
                        temp.append(int(split_strings[idx][:-1]))
                    else:
                        temp.append(int(split_strings[idx]))
                self.pyramid.append(temp)

        #get the first value in the pyramid
        self.initVal = self.pyramid[0][0]

        #initialize the path to none
        self.path = None

    """
    Function to get the path to get the product
    """
    def getPath(self):
        #Call pyramid descent with the initial values
        return self.pyramidDescent(1, 0, self.initVal, '')

    """
    Function that descends through the pyramid and figure out the path to multiply together for the product
    """
    def pyramidDescent(self, currentRow, prevIndex, total, curr_direction):
        #get the current row
        curr_row = self.pyramid[currentRow]

        #have a list of the values that are in the next layer
        curr_vals = [curr_row[prevIndex], curr_row[prevIndex + 1]]

        #look at the next values
        for i in range(len(curr_vals)):
            #determine what would be added for direction
            direction = ''

            if i == 0:
                direction = 'L'
            if i == 1:
                direction = 'R'

            #increment values
            total *= curr_vals[i]
            curr_direction += direction
            currentRow += 1

            #reached end
            if (total == self.target) and (currentRow == len(self.pyramid)):
                self.path = curr_direction
                return True
            #if end isn't reached, recursively continue
            elif (currentRow < len(self.pyramid)):
                prevIndex += i
                self.pyramidDescent(currentRow, prevIndex, total, curr_direction)
            
            #ascent thru the call stack
            currentRow -= 1
            total /= curr_vals[i]
            curr_direction = curr_direction[:-1]

        #return path
        if self.path:
            return self.path
        else:
            return False

#take in command line arguments
parser = argparse.ArgumentParser()

#get the filename argument
parser.add_argument('filename', type=str, help='Input file name')

args = parser.parse_args()

#pass in the filename
descender1 = Descender(args.filename)

#print the final result
print(descender1.getPath())