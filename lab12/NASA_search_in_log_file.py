import timeit
import zipfile
import re

def NASA_search_in_log_file():
    count = 0
    zip_file = zipfile.ZipFile('access_log_Jul95.zip')
    file = zip_file.open('access_log_Jul95')
    for line in file:
        if re.search('01/Jul/1995:00:1[0-9].*GET.*NASA', str(line)):
            count+=1
    print(count-1)
    zip_file.close()


if __name__ == "__main__":
    NASA_search_in_log_file()