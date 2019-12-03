#!/usr/bin/env python
#################################################################
# Python Script to retrieve 102 online Data files of 'ds083.2',
# total 1.03G. This script uses 'requests' to download data.
#
# Highlight this script by Select All, Copy and Paste it into a file;
# make the file executable and run it on command line.
#
# You need pass in your password as a parameter to execute
# this script; or you can set an environment variable RDAPSWD
# if your Operating System supports it.
#
# Contact rpconroy@ucar.edu (Riley Conroy) for further assistance.
#################################################################


import sys, os
import requests

def check_file_status(filepath, filesize):
    sys.stdout.write('\r')
    sys.stdout.flush()
    size = int(os.stat(filepath).st_size)
    percent_complete = (size/filesize)*100
    sys.stdout.write('%.3f %s' % (percent_complete, '% Completed'))
    sys.stdout.flush()

# Try to get password
if len(sys.argv) < 2 and not 'RDAPSWD' in os.environ:
    try:
        import getpass
        input = getpass.getpass
    except:
        try:
            input = raw_input
        except:
            pass
    pswd = 'dataproj'
else:
    try:
        pswd = sys.argv[1]
    except:
        pswd = os.environ['RDAPSWD']

url = 'https://rda.ucar.edu/cgi-bin/login'
values = {'email' : 'sudharsh_n@yahoo.co.in', 'passwd' : pswd, 'action' : 'login'}
# Authenticate
ret = requests.post(url,data=values)
if ret.status_code != 200:
    print('Bad Authentication')
    print(ret.text)
    exit(1)
dspath = 'https://rda.ucar.edu/data/ds083.2/'
filelist = [
'grib2/2007/2007.12/fnl_20071206_12_00.grib2',
'grib2/2007/2007.12/fnl_20071206_18_00.grib2',
'grib2/2007/2007.12/fnl_20071207_00_00.grib2',
'grib2/2007/2007.12/fnl_20071207_06_00.grib2',
'grib2/2007/2007.12/fnl_20071207_12_00.grib2',
'grib2/2007/2007.12/fnl_20071207_18_00.grib2',
'grib2/2007/2007.12/fnl_20071208_00_00.grib2',
'grib2/2007/2007.12/fnl_20071208_06_00.grib2',
'grib2/2007/2007.12/fnl_20071208_12_00.grib2',
'grib2/2007/2007.12/fnl_20071208_18_00.grib2',
'grib2/2007/2007.12/fnl_20071209_00_00.grib2',
'grib2/2007/2007.12/fnl_20071209_06_00.grib2',
'grib2/2007/2007.12/fnl_20071209_12_00.grib2',
'grib2/2007/2007.12/fnl_20071209_18_00.grib2',
'grib2/2007/2007.12/fnl_20071210_00_00.grib2',
'grib2/2007/2007.12/fnl_20071210_06_00.grib2',
'grib2/2007/2007.12/fnl_20071210_12_00.grib2',
'grib2/2007/2007.12/fnl_20071210_18_00.grib2',
'grib2/2007/2007.12/fnl_20071211_00_00.grib2',
'grib2/2007/2007.12/fnl_20071211_06_00.grib2',
'grib2/2007/2007.12/fnl_20071211_12_00.grib2',
'grib2/2007/2007.12/fnl_20071211_18_00.grib2',
'grib2/2007/2007.12/fnl_20071212_00_00.grib2',
'grib2/2007/2007.12/fnl_20071212_06_00.grib2',
'grib2/2007/2007.12/fnl_20071212_12_00.grib2',
'grib2/2007/2007.12/fnl_20071212_18_00.grib2',
'grib2/2007/2007.12/fnl_20071213_00_00.grib2',
'grib2/2007/2007.12/fnl_20071213_06_00.grib2',
'grib2/2007/2007.12/fnl_20071213_12_00.grib2',
'grib2/2007/2007.12/fnl_20071213_18_00.grib2',
'grib2/2007/2007.12/fnl_20071214_00_00.grib2',
'grib2/2007/2007.12/fnl_20071214_06_00.grib2',
'grib2/2007/2007.12/fnl_20071214_12_00.grib2',
'grib2/2007/2007.12/fnl_20071214_18_00.grib2',
'grib2/2007/2007.12/fnl_20071215_00_00.grib2',
'grib2/2007/2007.12/fnl_20071215_06_00.grib2',
'grib2/2007/2007.12/fnl_20071215_12_00.grib2',
'grib2/2007/2007.12/fnl_20071215_18_00.grib2',
'grib2/2007/2007.12/fnl_20071216_00_00.grib2',
'grib2/2007/2007.12/fnl_20071216_06_00.grib2',
'grib2/2007/2007.12/fnl_20071216_12_00.grib2',
'grib2/2007/2007.12/fnl_20071216_18_00.grib2',
'grib2/2007/2007.12/fnl_20071217_00_00.grib2',
'grib2/2007/2007.12/fnl_20071217_06_00.grib2',
'grib2/2007/2007.12/fnl_20071217_12_00.grib2',
'grib2/2007/2007.12/fnl_20071217_18_00.grib2',
'grib2/2007/2007.12/fnl_20071218_00_00.grib2',
'grib2/2007/2007.12/fnl_20071218_06_00.grib2',
'grib2/2007/2007.12/fnl_20071218_12_00.grib2',
'grib2/2007/2007.12/fnl_20071218_18_00.grib2',
'grib2/2007/2007.12/fnl_20071219_00_00.grib2',
'grib2/2007/2007.12/fnl_20071219_06_00.grib2',
'grib2/2007/2007.12/fnl_20071219_12_00.grib2',
'grib2/2007/2007.12/fnl_20071219_18_00.grib2',
'grib2/2007/2007.12/fnl_20071220_00_00.grib2',
'grib2/2007/2007.12/fnl_20071220_06_00.grib2',
'grib2/2007/2007.12/fnl_20071220_12_00.grib2',
'grib2/2007/2007.12/fnl_20071220_18_00.grib2',
'grib2/2007/2007.12/fnl_20071221_00_00.grib2',
'grib2/2007/2007.12/fnl_20071221_06_00.grib2',
'grib2/2007/2007.12/fnl_20071221_12_00.grib2',
'grib2/2007/2007.12/fnl_20071221_18_00.grib2',
'grib2/2007/2007.12/fnl_20071222_00_00.grib2',
'grib2/2007/2007.12/fnl_20071222_06_00.grib2',
'grib2/2007/2007.12/fnl_20071222_12_00.grib2',
'grib2/2007/2007.12/fnl_20071222_18_00.grib2',
'grib2/2007/2007.12/fnl_20071223_00_00.grib2',
'grib2/2007/2007.12/fnl_20071223_06_00.grib2',
'grib2/2007/2007.12/fnl_20071223_12_00.grib2',
'grib2/2007/2007.12/fnl_20071223_18_00.grib2',
'grib2/2007/2007.12/fnl_20071224_00_00.grib2',
'grib2/2007/2007.12/fnl_20071224_06_00.grib2',
'grib2/2007/2007.12/fnl_20071224_12_00.grib2',
'grib2/2007/2007.12/fnl_20071224_18_00.grib2',
'grib2/2007/2007.12/fnl_20071225_00_00.grib2',
'grib2/2007/2007.12/fnl_20071225_06_00.grib2',
'grib2/2007/2007.12/fnl_20071225_12_00.grib2',
'grib2/2007/2007.12/fnl_20071225_18_00.grib2',
'grib2/2007/2007.12/fnl_20071226_00_00.grib2',
'grib2/2007/2007.12/fnl_20071226_06_00.grib2',
'grib2/2007/2007.12/fnl_20071226_12_00.grib2',
'grib2/2007/2007.12/fnl_20071226_18_00.grib2',
'grib2/2007/2007.12/fnl_20071227_00_00.grib2',
'grib2/2007/2007.12/fnl_20071227_06_00.grib2',
'grib2/2007/2007.12/fnl_20071227_12_00.grib2',
'grib2/2007/2007.12/fnl_20071227_18_00.grib2',
'grib2/2007/2007.12/fnl_20071228_00_00.grib2',
'grib2/2007/2007.12/fnl_20071228_06_00.grib2',
'grib2/2007/2007.12/fnl_20071228_12_00.grib2',
'grib2/2007/2007.12/fnl_20071228_18_00.grib2',
'grib2/2007/2007.12/fnl_20071229_00_00.grib2',
'grib2/2007/2007.12/fnl_20071229_06_00.grib2',
'grib2/2007/2007.12/fnl_20071229_12_00.grib2',
'grib2/2007/2007.12/fnl_20071229_18_00.grib2',
'grib2/2007/2007.12/fnl_20071230_00_00.grib2',
'grib2/2007/2007.12/fnl_20071230_06_00.grib2',
'grib2/2007/2007.12/fnl_20071230_12_00.grib2',
'grib2/2007/2007.12/fnl_20071230_18_00.grib2',
'grib2/2007/2007.12/fnl_20071231_00_00.grib2',
'grib2/2007/2007.12/fnl_20071231_06_00.grib2',
'grib2/2007/2007.12/fnl_20071231_12_00.grib2',
'grib2/2007/2007.12/fnl_20071231_18_00.grib2']
for file in filelist:
    filename=dspath+file
    file_base = os.path.basename(file)
    print('Downloading',file_base)
    req = requests.get(filename, cookies = ret.cookies, allow_redirects=True, stream=True)
    filesize = int(req.headers['Content-length'])
    with open(file_base, 'wb') as outfile:
        chunk_size=1048576
        for chunk in req.iter_content(chunk_size=chunk_size):
            outfile.write(chunk)
            if chunk_size < filesize:
                check_file_status(file_base, filesize)
    check_file_status(file_base, filesize)
    print()
