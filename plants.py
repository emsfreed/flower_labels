import time
from typing import Dict
"""
- read `plants.txt` and process into a list of plant names of appropriate quantity
- generate an image file for each plant, staggering the names on the image such that multiple
will appear if multiple are present in plants.txt
- all images should be the same resolution / should use the same font size such that when the output images
are used with the laser engraver they come out the same size without resizing
- if the output file already exists overwrite it
- the output directory should be able to be specified with the `-o` flag
"""
# cmd + . over a value showing a warning will bring up a list of suggestions to fix that warning

def read_plants(filename:str) -> Dict[str,int]:
    composium = {}
    # create composium here
#with... as is a conext manager for the open function that stores the return value of open in the pkant_file
    with open(filename) as plant_file:
        content = plant_file.read()
    #\n is a new line character
    content_lines = content.split("\n")
    #string split is next step
    #hold down fn and f2 to change the name of a variable everywhere
    for line in content_lines:
        plant_div = line.split("*")
        plant_name = plant_div[0].strip()
        if len(plant_div) >= 2:
            plant_num = int(plant_div[1].strip())
        else:
            plant_num = 1
        if plant_name in composium:
            composium[plant_name] += plant_num
        else:
            composium[plant_name] = plant_num
    return composium

def main():
    composium = read_plants("plants.txt")
    print(composium)

if __name__ == '__main__':
    main()

#.lower() makes things lowercase
#strip gets rid of the ugly mf spaces 
# for i in x: 
#     if i not in y:
#         y[i]=1 
#     else:
#         y[i]=y[i]+1 
# print(y)