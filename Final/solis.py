'''
## Functions
-------------------------------------------------
'''
def clean_int_year(value):
    result = int(value)
    return result

def clean_trim_year(value):
    value = str(value)
    result = clean_int_year(value[6:])
    return result

def load_csv(filename):
    import pandas as pd
    clean_dir = "data/clean"
    csv_file = "{}/{}".format(clean_dir, filename)
    result = pd.read_csv(csv_file)
    return result

def print_file_from_head(filename, nlines):
        from itertools import islice
        with open(filename) as txt_file:
                for line in islice(txt_file, nlines):
                        print("".join(line.rstrip()))

def vert_month_num(value):
    months = {"1":"Jan","2":"Feb","3":"March","4":"April","5":"May","6":"June","7":"July","8":"Aug","9":"Sept","10":"Oct","11":"Nov","12":"Dec"}
    result = months[str(value)]
    return result
    
    
    
    