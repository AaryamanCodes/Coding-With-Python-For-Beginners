"""
This is the NAND operator in Python. The NAND operator dosen't exist, so I made my own NAND operator.
This works simply on the logic of the NAND gate which means that it will be the opposite result of 
what and would give thus given the abbreviation of NAND which means Not And.
"""

#Defining the Function
def nand(n1, n2):
    res = n1 and n2
    notRes = not res
    return notRes
