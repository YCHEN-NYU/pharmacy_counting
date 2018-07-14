# steps for solving the pharmacy counting problem
1. read from itcont.txt file
2. parse line by line with ",", ignoring the header line
3. get the prescriber_name, drug_name, drug_cost by the last 4 elements
4. check if drug_name is in the drug_name set
    if NOT: 
        if prescriber_name in the name set: 
            add the drug_name entry, define it as the set of prescriber_name, increment the prescriber counting by 1, add the drug_cost;
        else:
            prescriber_name entry remains unchanged, don't increment the prescriber counting, add drug_cost
    else YES: 
        add the [prescriber_name, counting, drug_cost] to the drug_name entry
5. sort the output[drug] set by the decreasing drug_cost with sorted method
6. write results into the top_cost_drug.txt file

# Testing
Testing are performed successfully in Jupyter notebook with the itcont.txt file, de_cc_data.txt.
