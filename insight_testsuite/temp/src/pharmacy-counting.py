# YCHEN-NYU
# check if a string object can be converted into integers
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# inFile: input filename, splitter: splitter for the parsing process
# TODO: add exception for reading the input file
def processData(inFile, splitter):
    # initialize an empty dictionary output, and empty list temp
    output = {}
    temp = []
    
    # parse the .txt file line by line
    for line in [line for line in open(inFile, 'r')]:
        # split line by line with the input argument 'splitter'
        temp = [element for element in line.split(splitter) if (element != '')]
        
        # drug_name and drug_cost are the last two elements in the line
        # consider empty lines case:
        if(len(temp) > 1):
            # construct the prescriber_name as 'last_name first_name'
            prescriber_name = temp[-4] + ' ' + temp[-3]
            drug_name = temp[-2]
            drug_cost = temp[-1]

        # start counting from the second row by skipping using isInt condition for the drug_cost
        if(isFloat(drug_cost)):
            # if the current drug_name is in the dictionary, then increment counting by 1, add drug_cost
            # TODO
            # prescriber_name has to be unique for num_prescriber++
            if(drug_name in output):
                # if prescriber_name is not in the name Set, then add the prescriber_name, increment num_prescriber, add cost
                if(prescriber_name not in output[drug_name][0]):
                    output[drug_name] = [set(prescriber_name), output[drug_name][1] + 1, output[drug_name][2] + float(drug_cost)]
                # if prescriber_name is in the name Set, then don't add the prescriber_name, don't increment num_prescriber, add cost
                else:
                    output[drug_name] = [output[drug_name][0], output[drug_name][1], output[drug_name][2] + float(drug_cost)]
            # create a new entry for the dictionary, with the count and cost
            # initialize the prescriber_name, num_prescriber, cost
            else:
                output[drug_name] = [set(prescriber_name), 1, float(drug_cost)]
    return output

def check_output_file(outFile):
    try:
        open(outFile, 'r')
        return True
    except IOError:
        return False
        
# run the preprocessData to parse and count the library, write the output into 
def run(inFile, outFile):
    # write dictionary to the .txt file 
    with open(outFile, 'w') as file:
        # write the header for the txt file
        file.write("drug_name,num_prescriber,total_cost\n")
        
        # used sorted function to sort out the data by drug_cost (descending order)
        # x[1][1] denotes the use of drug_cost from the proprocessData() function
        for key, value in sorted(processData(inFile, ',').items(), key= lambda x: x[1][-1], reverse=True):
            file.write(str(key) + ',' + str(value[1]) +','  +str('{:g}'.format(float(value[2])))+ '\n' )

######################
######################
# define the file name
inFile = "./input/itcont.txt"
outFile = "./output/top_cost_drug.txt"

# run the program
run(inFile, outFile)