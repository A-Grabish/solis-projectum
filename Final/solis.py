'''
## Functions
-------------------------------------------------
'''
def clean_trim_year(value):
    value = str(value)
    result = value[6:]
    return result

def print_file_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print("".join(line.rstrip()))

def load_csv(fname):
    import pandas as pd
    clean_dir = "data/clean"
    csv_file = "{}/{}".format(clean_dir, fname)
    result = pd.read_csv(csv_file)
    return result