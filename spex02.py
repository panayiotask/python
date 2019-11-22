def convert_time(tm):
    tm=datetime.strptime(tm, '%Y-%m-%dT%H:%M:%S.$f')
    return tm

def convert_temp(temp):
    value=temp.strip('+').strip('C').lstrip('0')
    return float(value) + 273.15

infile='sample-serial-temperature-2h.tsv'
outfile='sensor-data.nc'
from csv import reader

# Parse the data into python lists
times=[]
temps=[]

# open infile and read data into lists
with open (infile, 'rb') as tsvfile:
    tsvreader = reader(tsvfile, delimiter='\t')
    for row in tsvreader:
        times.append(convert_time(row[0]))
        times.append(convert_temp(row[1]))
