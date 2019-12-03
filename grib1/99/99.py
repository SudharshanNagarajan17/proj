#!/usr/bin/env python
#################################################################
# Python Script to retrieve 488 online Data files of 'ds083.2',
# total 10.04G. This script uses 'requests' to download data.
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
'grib1/1999/1999.07/fnl_19990730_18_00.grib1',
'grib1/1999/1999.08/fnl_19990801_00_00.grib1',
'grib1/1999/1999.08/fnl_19990801_06_00.grib1',
'grib1/1999/1999.08/fnl_19990801_12_00.grib1',
'grib1/1999/1999.08/fnl_19990801_18_00.grib1',
'grib1/1999/1999.08/fnl_19990802_00_00.grib1',
'grib1/1999/1999.08/fnl_19990802_06_00.grib1',
'grib1/1999/1999.08/fnl_19990802_12_00.grib1',
'grib1/1999/1999.08/fnl_19990802_18_00.grib1',
'grib1/1999/1999.08/fnl_19990803_00_00.grib1',
'grib1/1999/1999.08/fnl_19990803_06_00.grib1',
'grib1/1999/1999.08/fnl_19990803_12_00.grib1',
'grib1/1999/1999.08/fnl_19990803_18_00.grib1',
'grib1/1999/1999.08/fnl_19990804_00_00.grib1',
'grib1/1999/1999.08/fnl_19990804_06_00.grib1',
'grib1/1999/1999.08/fnl_19990804_12_00.grib1',
'grib1/1999/1999.08/fnl_19990804_18_00.grib1',
'grib1/1999/1999.08/fnl_19990805_00_00.grib1',
'grib1/1999/1999.08/fnl_19990805_06_00.grib1',
'grib1/1999/1999.08/fnl_19990805_12_00.grib1',
'grib1/1999/1999.08/fnl_19990805_18_00.grib1',
'grib1/1999/1999.08/fnl_19990806_00_00.grib1',
'grib1/1999/1999.08/fnl_19990806_06_00.grib1',
'grib1/1999/1999.08/fnl_19990806_12_00.grib1',
'grib1/1999/1999.08/fnl_19990806_18_00.grib1',
'grib1/1999/1999.08/fnl_19990807_00_00.grib1',
'grib1/1999/1999.08/fnl_19990807_06_00.grib1',
'grib1/1999/1999.08/fnl_19990807_12_00.grib1',
'grib1/1999/1999.08/fnl_19990807_18_00.grib1',
'grib1/1999/1999.08/fnl_19990808_00_00.grib1',
'grib1/1999/1999.08/fnl_19990808_06_00.grib1',
'grib1/1999/1999.08/fnl_19990808_12_00.grib1',
'grib1/1999/1999.08/fnl_19990808_18_00.grib1',
'grib1/1999/1999.08/fnl_19990809_00_00.grib1',
'grib1/1999/1999.08/fnl_19990809_06_00.grib1',
'grib1/1999/1999.08/fnl_19990809_12_00.grib1',
'grib1/1999/1999.08/fnl_19990809_18_00.grib1',
'grib1/1999/1999.08/fnl_19990810_00_00.grib1',
'grib1/1999/1999.08/fnl_19990810_06_00.grib1',
'grib1/1999/1999.08/fnl_19990810_12_00.grib1',
'grib1/1999/1999.08/fnl_19990810_18_00.grib1',
'grib1/1999/1999.08/fnl_19990811_00_00.grib1',
'grib1/1999/1999.08/fnl_19990811_06_00.grib1',
'grib1/1999/1999.08/fnl_19990811_12_00.grib1',
'grib1/1999/1999.08/fnl_19990811_18_00.grib1',
'grib1/1999/1999.08/fnl_19990812_00_00.grib1',
'grib1/1999/1999.08/fnl_19990812_06_00.grib1',
'grib1/1999/1999.08/fnl_19990812_12_00.grib1',
'grib1/1999/1999.08/fnl_19990812_18_00.grib1',
'grib1/1999/1999.08/fnl_19990813_00_00.grib1',
'grib1/1999/1999.08/fnl_19990813_06_00.grib1',
'grib1/1999/1999.08/fnl_19990813_12_00.grib1',
'grib1/1999/1999.08/fnl_19990813_18_00.grib1',
'grib1/1999/1999.08/fnl_19990814_00_00.grib1',
'grib1/1999/1999.08/fnl_19990814_12_00.grib1',
'grib1/1999/1999.08/fnl_19990814_18_00.grib1',
'grib1/1999/1999.08/fnl_19990815_00_00.grib1',
'grib1/1999/1999.08/fnl_19990815_06_00.grib1',
'grib1/1999/1999.08/fnl_19990815_12_00.grib1',
'grib1/1999/1999.08/fnl_19990815_18_00.grib1',
'grib1/1999/1999.08/fnl_19990816_00_00.grib1',
'grib1/1999/1999.08/fnl_19990816_06_00.grib1',
'grib1/1999/1999.08/fnl_19990816_12_00.grib1',
'grib1/1999/1999.08/fnl_19990816_18_00.grib1',
'grib1/1999/1999.08/fnl_19990817_00_00.grib1',
'grib1/1999/1999.08/fnl_19990817_06_00.grib1',
'grib1/1999/1999.08/fnl_19990817_12_00.grib1',
'grib1/1999/1999.08/fnl_19990817_18_00.grib1',
'grib1/1999/1999.08/fnl_19990818_00_00.grib1',
'grib1/1999/1999.08/fnl_19990818_06_00.grib1',
'grib1/1999/1999.08/fnl_19990818_12_00.grib1',
'grib1/1999/1999.08/fnl_19990818_18_00.grib1',
'grib1/1999/1999.08/fnl_19990819_00_00.grib1',
'grib1/1999/1999.08/fnl_19990819_06_00.grib1',
'grib1/1999/1999.08/fnl_19990819_12_00.grib1',
'grib1/1999/1999.08/fnl_19990819_18_00.grib1',
'grib1/1999/1999.08/fnl_19990820_00_00.grib1',
'grib1/1999/1999.08/fnl_19990820_06_00.grib1',
'grib1/1999/1999.08/fnl_19990820_12_00.grib1',
'grib1/1999/1999.08/fnl_19990820_18_00.grib1',
'grib1/1999/1999.08/fnl_19990821_00_00.grib1',
'grib1/1999/1999.08/fnl_19990821_06_00.grib1',
'grib1/1999/1999.08/fnl_19990821_12_00.grib1',
'grib1/1999/1999.08/fnl_19990821_18_00.grib1',
'grib1/1999/1999.08/fnl_19990822_00_00.grib1',
'grib1/1999/1999.08/fnl_19990822_06_00.grib1',
'grib1/1999/1999.08/fnl_19990822_12_00.grib1',
'grib1/1999/1999.08/fnl_19990822_18_00.grib1',
'grib1/1999/1999.08/fnl_19990823_00_00.grib1',
'grib1/1999/1999.08/fnl_19990823_06_00.grib1',
'grib1/1999/1999.08/fnl_19990823_12_00.grib1',
'grib1/1999/1999.08/fnl_19990823_18_00.grib1',
'grib1/1999/1999.08/fnl_19990824_00_00.grib1',
'grib1/1999/1999.08/fnl_19990824_06_00.grib1',
'grib1/1999/1999.08/fnl_19990824_12_00.grib1',
'grib1/1999/1999.08/fnl_19990824_18_00.grib1',
'grib1/1999/1999.08/fnl_19990825_00_00.grib1',
'grib1/1999/1999.08/fnl_19990825_06_00.grib1',
'grib1/1999/1999.08/fnl_19990825_12_00.grib1',
'grib1/1999/1999.08/fnl_19990825_18_00.grib1',
'grib1/1999/1999.08/fnl_19990826_00_00.grib1',
'grib1/1999/1999.08/fnl_19990826_06_00.grib1',
'grib1/1999/1999.08/fnl_19990826_12_00.grib1',
'grib1/1999/1999.08/fnl_19990826_18_00.grib1',
'grib1/1999/1999.08/fnl_19990827_00_00.grib1',
'grib1/1999/1999.08/fnl_19990827_06_00.grib1',
'grib1/1999/1999.08/fnl_19990827_12_00.grib1',
'grib1/1999/1999.08/fnl_19990827_18_00.grib1',
'grib1/1999/1999.08/fnl_19990828_00_00.grib1',
'grib1/1999/1999.08/fnl_19990828_06_00.grib1',
'grib1/1999/1999.08/fnl_19990828_12_00.grib1',
'grib1/1999/1999.08/fnl_19990828_18_00.grib1',
'grib1/1999/1999.08/fnl_19990830_00_00.grib1',
'grib1/1999/1999.08/fnl_19990830_06_00.grib1',
'grib1/1999/1999.08/fnl_19990830_12_00.grib1',
'grib1/1999/1999.08/fnl_19990830_18_00.grib1',
'grib1/1999/1999.08/fnl_19990831_00_00.grib1',
'grib1/1999/1999.08/fnl_19990831_06_00.grib1',
'grib1/1999/1999.08/fnl_19990831_12_00.grib1',
'grib1/1999/1999.08/fnl_19990831_18_00.grib1',
'grib1/1999/1999.09/fnl_19990901_00_00.grib1',
'grib1/1999/1999.09/fnl_19990901_06_00.grib1',
'grib1/1999/1999.09/fnl_19990901_12_00.grib1',
'grib1/1999/1999.09/fnl_19990901_18_00.grib1',
'grib1/1999/1999.09/fnl_19990902_00_00.grib1',
'grib1/1999/1999.09/fnl_19990902_06_00.grib1',
'grib1/1999/1999.09/fnl_19990902_12_00.grib1',
'grib1/1999/1999.09/fnl_19990902_18_00.grib1',
'grib1/1999/1999.09/fnl_19990903_00_00.grib1',
'grib1/1999/1999.09/fnl_19990910_00_00.grib1',
'grib1/1999/1999.09/fnl_19990910_06_00.grib1',
'grib1/1999/1999.09/fnl_19990910_12_00.grib1',
'grib1/1999/1999.09/fnl_19990911_06_00.grib1',
'grib1/1999/1999.09/fnl_19990911_12_00.grib1',
'grib1/1999/1999.09/fnl_19990911_18_00.grib1',
'grib1/1999/1999.09/fnl_19990912_00_00.grib1',
'grib1/1999/1999.09/fnl_19990912_12_00.grib1',
'grib1/1999/1999.09/fnl_19990912_18_00.grib1',
'grib1/1999/1999.09/fnl_19990913_00_00.grib1',
'grib1/1999/1999.09/fnl_19990913_06_00.grib1',
'grib1/1999/1999.09/fnl_19990913_12_00.grib1',
'grib1/1999/1999.09/fnl_19990913_18_00.grib1',
'grib1/1999/1999.09/fnl_19990914_00_00.grib1',
'grib1/1999/1999.09/fnl_19990914_06_00.grib1',
'grib1/1999/1999.09/fnl_19990914_12_00.grib1',
'grib1/1999/1999.09/fnl_19990914_18_00.grib1',
'grib1/1999/1999.09/fnl_19990915_00_00.grib1',
'grib1/1999/1999.09/fnl_19990915_06_00.grib1',
'grib1/1999/1999.09/fnl_19990915_12_00.grib1',
'grib1/1999/1999.09/fnl_19990915_18_00.grib1',
'grib1/1999/1999.09/fnl_19990916_00_00.grib1',
'grib1/1999/1999.09/fnl_19990916_06_00.grib1',
'grib1/1999/1999.09/fnl_19990916_12_00.grib1',
'grib1/1999/1999.09/fnl_19990916_18_00.grib1',
'grib1/1999/1999.09/fnl_19990917_00_00.grib1',
'grib1/1999/1999.09/fnl_19990917_06_00.grib1',
'grib1/1999/1999.09/fnl_19990917_12_00.grib1',
'grib1/1999/1999.09/fnl_19990917_18_00.grib1',
'grib1/1999/1999.09/fnl_19990918_00_00.grib1',
'grib1/1999/1999.09/fnl_19990918_06_00.grib1',
'grib1/1999/1999.09/fnl_19990918_12_00.grib1',
'grib1/1999/1999.09/fnl_19990918_18_00.grib1',
'grib1/1999/1999.09/fnl_19990919_00_00.grib1',
'grib1/1999/1999.09/fnl_19990919_06_00.grib1',
'grib1/1999/1999.09/fnl_19990919_12_00.grib1',
'grib1/1999/1999.09/fnl_19990919_18_00.grib1',
'grib1/1999/1999.09/fnl_19990920_00_00.grib1',
'grib1/1999/1999.09/fnl_19990920_06_00.grib1',
'grib1/1999/1999.09/fnl_19990920_12_00.grib1',
'grib1/1999/1999.09/fnl_19990920_18_00.grib1',
'grib1/1999/1999.09/fnl_19990921_00_00.grib1',
'grib1/1999/1999.09/fnl_19990921_06_00.grib1',
'grib1/1999/1999.09/fnl_19990921_12_00.grib1',
'grib1/1999/1999.09/fnl_19990921_18_00.grib1',
'grib1/1999/1999.09/fnl_19990922_00_00.grib1',
'grib1/1999/1999.09/fnl_19990922_06_00.grib1',
'grib1/1999/1999.09/fnl_19990922_12_00.grib1',
'grib1/1999/1999.09/fnl_19990922_18_00.grib1',
'grib1/1999/1999.09/fnl_19990923_00_00.grib1',
'grib1/1999/1999.09/fnl_19990923_06_00.grib1',
'grib1/1999/1999.09/fnl_19990923_12_00.grib1',
'grib1/1999/1999.09/fnl_19990923_18_00.grib1',
'grib1/1999/1999.09/fnl_19990924_00_00.grib1',
'grib1/1999/1999.09/fnl_19990924_06_00.grib1',
'grib1/1999/1999.09/fnl_19990924_12_00.grib1',
'grib1/1999/1999.09/fnl_19990924_18_00.grib1',
'grib1/1999/1999.09/fnl_19990925_00_00.grib1',
'grib1/1999/1999.09/fnl_19990925_06_00.grib1',
'grib1/1999/1999.09/fnl_19990925_12_00.grib1',
'grib1/1999/1999.09/fnl_19990925_18_00.grib1',
'grib1/1999/1999.09/fnl_19990926_00_00.grib1',
'grib1/1999/1999.09/fnl_19990926_06_00.grib1',
'grib1/1999/1999.09/fnl_19990926_12_00.grib1',
'grib1/1999/1999.09/fnl_19990926_18_00.grib1',
'grib1/1999/1999.09/fnl_19990927_00_00.grib1',
'grib1/1999/1999.09/fnl_19990927_06_00.grib1',
'grib1/1999/1999.09/fnl_19990927_12_00.grib1',
'grib1/1999/1999.09/fnl_19990927_18_00.grib1',
'grib1/1999/1999.09/fnl_19990928_00_00.grib1',
'grib1/1999/1999.09/fnl_19990928_06_00.grib1',
'grib1/1999/1999.09/fnl_19990928_12_00.grib1',
'grib1/1999/1999.09/fnl_19990928_18_00.grib1',
'grib1/1999/1999.09/fnl_19990929_00_00.grib1',
'grib1/1999/1999.09/fnl_19990929_06_00.grib1',
'grib1/1999/1999.09/fnl_19990929_12_00.grib1',
'grib1/1999/1999.09/fnl_19990929_18_00.grib1',
'grib1/1999/1999.09/fnl_19990930_00_00.grib1',
'grib1/1999/1999.09/fnl_19990930_06_00.grib1',
'grib1/1999/1999.09/fnl_19990930_12_00.grib1',
'grib1/1999/1999.10/fnl_19991001_00_00.grib1',
'grib1/1999/1999.10/fnl_19991001_12_00.grib1',
'grib1/1999/1999.10/fnl_19991002_00_00.grib1',
'grib1/1999/1999.10/fnl_19991002_12_00.grib1',
'grib1/1999/1999.10/fnl_19991003_00_00.grib1',
'grib1/1999/1999.10/fnl_19991003_12_00.grib1',
'grib1/1999/1999.10/fnl_19991004_00_00.grib1',
'grib1/1999/1999.10/fnl_19991004_12_00.grib1',
'grib1/1999/1999.10/fnl_19991005_00_00.grib1',
'grib1/1999/1999.10/fnl_19991005_12_00.grib1',
'grib1/1999/1999.10/fnl_19991006_00_00.grib1',
'grib1/1999/1999.10/fnl_19991006_12_00.grib1',
'grib1/1999/1999.10/fnl_19991007_00_00.grib1',
'grib1/1999/1999.10/fnl_19991007_12_00.grib1',
'grib1/1999/1999.10/fnl_19991008_00_00.grib1',
'grib1/1999/1999.10/fnl_19991008_12_00.grib1',
'grib1/1999/1999.10/fnl_19991009_00_00.grib1',
'grib1/1999/1999.10/fnl_19991009_12_00.grib1',
'grib1/1999/1999.10/fnl_19991010_00_00.grib1',
'grib1/1999/1999.10/fnl_19991010_12_00.grib1',
'grib1/1999/1999.10/fnl_19991011_00_00.grib1',
'grib1/1999/1999.10/fnl_19991011_12_00.grib1',
'grib1/1999/1999.10/fnl_19991012_00_00.grib1',
'grib1/1999/1999.10/fnl_19991012_12_00.grib1',
'grib1/1999/1999.10/fnl_19991013_00_00.grib1',
'grib1/1999/1999.10/fnl_19991013_12_00.grib1',
'grib1/1999/1999.10/fnl_19991014_00_00.grib1',
'grib1/1999/1999.10/fnl_19991014_12_00.grib1',
'grib1/1999/1999.10/fnl_19991015_00_00.grib1',
'grib1/1999/1999.10/fnl_19991015_12_00.grib1',
'grib1/1999/1999.10/fnl_19991016_00_00.grib1',
'grib1/1999/1999.10/fnl_19991016_12_00.grib1',
'grib1/1999/1999.10/fnl_19991017_00_00.grib1',
'grib1/1999/1999.10/fnl_19991017_12_00.grib1',
'grib1/1999/1999.10/fnl_19991018_00_00.grib1',
'grib1/1999/1999.10/fnl_19991018_12_00.grib1',
'grib1/1999/1999.10/fnl_19991019_00_00.grib1',
'grib1/1999/1999.10/fnl_19991019_12_00.grib1',
'grib1/1999/1999.10/fnl_19991020_00_00.grib1',
'grib1/1999/1999.10/fnl_19991020_12_00.grib1',
'grib1/1999/1999.10/fnl_19991021_00_00.grib1',
'grib1/1999/1999.10/fnl_19991021_12_00.grib1',
'grib1/1999/1999.10/fnl_19991022_00_00.grib1',
'grib1/1999/1999.10/fnl_19991022_12_00.grib1',
'grib1/1999/1999.10/fnl_19991023_00_00.grib1',
'grib1/1999/1999.10/fnl_19991023_12_00.grib1',
'grib1/1999/1999.10/fnl_19991024_00_00.grib1',
'grib1/1999/1999.10/fnl_19991024_12_00.grib1',
'grib1/1999/1999.10/fnl_19991025_00_00.grib1',
'grib1/1999/1999.10/fnl_19991025_12_00.grib1',
'grib1/1999/1999.10/fnl_19991026_00_00.grib1',
'grib1/1999/1999.10/fnl_19991026_12_00.grib1',
'grib1/1999/1999.10/fnl_19991027_00_00.grib1',
'grib1/1999/1999.10/fnl_19991027_12_00.grib1',
'grib1/1999/1999.10/fnl_19991028_00_00.grib1',
'grib1/1999/1999.10/fnl_19991028_12_00.grib1',
'grib1/1999/1999.10/fnl_19991029_00_00.grib1',
'grib1/1999/1999.10/fnl_19991029_12_00.grib1',
'grib1/1999/1999.10/fnl_19991030_00_00.grib1',
'grib1/1999/1999.10/fnl_19991030_12_00.grib1',
'grib1/1999/1999.10/fnl_19991031_00_00.grib1',
'grib1/1999/1999.10/fnl_19991031_12_00.grib1',
'grib1/1999/1999.11/fnl_19991101_00_00.grib1',
'grib1/1999/1999.11/fnl_19991101_12_00.grib1',
'grib1/1999/1999.11/fnl_19991102_00_00.grib1',
'grib1/1999/1999.11/fnl_19991102_12_00.grib1',
'grib1/1999/1999.11/fnl_19991103_00_00.grib1',
'grib1/1999/1999.11/fnl_19991103_12_00.grib1',
'grib1/1999/1999.11/fnl_19991104_00_00.grib1',
'grib1/1999/1999.11/fnl_19991104_12_00.grib1',
'grib1/1999/1999.11/fnl_19991105_00_00.grib1',
'grib1/1999/1999.11/fnl_19991105_12_00.grib1',
'grib1/1999/1999.11/fnl_19991106_00_00.grib1',
'grib1/1999/1999.11/fnl_19991106_12_00.grib1',
'grib1/1999/1999.11/fnl_19991107_00_00.grib1',
'grib1/1999/1999.11/fnl_19991107_12_00.grib1',
'grib1/1999/1999.11/fnl_19991108_00_00.grib1',
'grib1/1999/1999.11/fnl_19991108_12_00.grib1',
'grib1/1999/1999.11/fnl_19991109_00_00.grib1',
'grib1/1999/1999.11/fnl_19991109_12_00.grib1',
'grib1/1999/1999.11/fnl_19991110_00_00.grib1',
'grib1/1999/1999.11/fnl_19991110_06_00.grib1',
'grib1/1999/1999.11/fnl_19991110_12_00.grib1',
'grib1/1999/1999.11/fnl_19991111_00_00.grib1',
'grib1/1999/1999.11/fnl_19991111_06_00.grib1',
'grib1/1999/1999.11/fnl_19991111_12_00.grib1',
'grib1/1999/1999.11/fnl_19991112_00_00.grib1',
'grib1/1999/1999.11/fnl_19991112_06_00.grib1',
'grib1/1999/1999.11/fnl_19991112_12_00.grib1',
'grib1/1999/1999.11/fnl_19991113_00_00.grib1',
'grib1/1999/1999.11/fnl_19991113_06_00.grib1',
'grib1/1999/1999.11/fnl_19991113_12_00.grib1',
'grib1/1999/1999.11/fnl_19991114_00_00.grib1',
'grib1/1999/1999.11/fnl_19991114_06_00.grib1',
'grib1/1999/1999.11/fnl_19991114_12_00.grib1',
'grib1/1999/1999.11/fnl_19991115_00_00.grib1',
'grib1/1999/1999.11/fnl_19991115_06_00.grib1',
'grib1/1999/1999.11/fnl_19991115_12_00.grib1',
'grib1/1999/1999.11/fnl_19991115_18_00.grib1',
'grib1/1999/1999.11/fnl_19991116_00_00.grib1',
'grib1/1999/1999.11/fnl_19991116_06_00.grib1',
'grib1/1999/1999.11/fnl_19991116_12_00.grib1',
'grib1/1999/1999.11/fnl_19991116_18_00.grib1',
'grib1/1999/1999.11/fnl_19991117_00_00.grib1',
'grib1/1999/1999.11/fnl_19991117_06_00.grib1',
'grib1/1999/1999.11/fnl_19991117_12_00.grib1',
'grib1/1999/1999.11/fnl_19991117_18_00.grib1',
'grib1/1999/1999.11/fnl_19991118_00_00.grib1',
'grib1/1999/1999.11/fnl_19991118_06_00.grib1',
'grib1/1999/1999.11/fnl_19991118_12_00.grib1',
'grib1/1999/1999.11/fnl_19991118_18_00.grib1',
'grib1/1999/1999.11/fnl_19991119_00_00.grib1',
'grib1/1999/1999.11/fnl_19991119_06_00.grib1',
'grib1/1999/1999.11/fnl_19991119_12_00.grib1',
'grib1/1999/1999.11/fnl_19991119_18_00.grib1',
'grib1/1999/1999.11/fnl_19991120_00_00.grib1',
'grib1/1999/1999.11/fnl_19991120_06_00.grib1',
'grib1/1999/1999.11/fnl_19991120_12_00.grib1',
'grib1/1999/1999.11/fnl_19991120_18_00.grib1',
'grib1/1999/1999.11/fnl_19991121_00_00.grib1',
'grib1/1999/1999.11/fnl_19991121_06_00.grib1',
'grib1/1999/1999.11/fnl_19991121_12_00.grib1',
'grib1/1999/1999.11/fnl_19991121_18_00.grib1',
'grib1/1999/1999.11/fnl_19991122_00_00.grib1',
'grib1/1999/1999.11/fnl_19991122_06_00.grib1',
'grib1/1999/1999.11/fnl_19991122_12_00.grib1',
'grib1/1999/1999.11/fnl_19991122_18_00.grib1',
'grib1/1999/1999.11/fnl_19991123_00_00.grib1',
'grib1/1999/1999.11/fnl_19991123_06_00.grib1',
'grib1/1999/1999.11/fnl_19991123_12_00.grib1',
'grib1/1999/1999.11/fnl_19991123_18_00.grib1',
'grib1/1999/1999.11/fnl_19991124_00_00.grib1',
'grib1/1999/1999.11/fnl_19991124_06_00.grib1',
'grib1/1999/1999.11/fnl_19991124_12_00.grib1',
'grib1/1999/1999.11/fnl_19991124_18_00.grib1',
'grib1/1999/1999.11/fnl_19991125_00_00.grib1',
'grib1/1999/1999.11/fnl_19991125_06_00.grib1',
'grib1/1999/1999.11/fnl_19991125_12_00.grib1',
'grib1/1999/1999.11/fnl_19991125_18_00.grib1',
'grib1/1999/1999.11/fnl_19991126_00_00.grib1',
'grib1/1999/1999.11/fnl_19991126_06_00.grib1',
'grib1/1999/1999.11/fnl_19991126_12_00.grib1',
'grib1/1999/1999.11/fnl_19991126_18_00.grib1',
'grib1/1999/1999.11/fnl_19991127_00_00.grib1',
'grib1/1999/1999.11/fnl_19991127_06_00.grib1',
'grib1/1999/1999.11/fnl_19991127_12_00.grib1',
'grib1/1999/1999.11/fnl_19991127_18_00.grib1',
'grib1/1999/1999.11/fnl_19991128_00_00.grib1',
'grib1/1999/1999.11/fnl_19991128_06_00.grib1',
'grib1/1999/1999.11/fnl_19991128_12_00.grib1',
'grib1/1999/1999.11/fnl_19991128_18_00.grib1',
'grib1/1999/1999.11/fnl_19991129_00_00.grib1',
'grib1/1999/1999.11/fnl_19991129_06_00.grib1',
'grib1/1999/1999.11/fnl_19991129_12_00.grib1',
'grib1/1999/1999.11/fnl_19991129_18_00.grib1',
'grib1/1999/1999.11/fnl_19991130_00_00.grib1',
'grib1/1999/1999.11/fnl_19991130_06_00.grib1',
'grib1/1999/1999.11/fnl_19991130_12_00.grib1',
'grib1/1999/1999.11/fnl_19991130_18_00.grib1',
'grib1/1999/1999.12/fnl_19991201_00_00.grib1',
'grib1/1999/1999.12/fnl_19991201_06_00.grib1',
'grib1/1999/1999.12/fnl_19991201_12_00.grib1',
'grib1/1999/1999.12/fnl_19991201_18_00.grib1',
'grib1/1999/1999.12/fnl_19991202_00_00.grib1',
'grib1/1999/1999.12/fnl_19991202_06_00.grib1',
'grib1/1999/1999.12/fnl_19991202_12_00.grib1',
'grib1/1999/1999.12/fnl_19991202_18_00.grib1',
'grib1/1999/1999.12/fnl_19991203_00_00.grib1',
'grib1/1999/1999.12/fnl_19991203_06_00.grib1',
'grib1/1999/1999.12/fnl_19991203_12_00.grib1',
'grib1/1999/1999.12/fnl_19991203_18_00.grib1',
'grib1/1999/1999.12/fnl_19991204_00_00.grib1',
'grib1/1999/1999.12/fnl_19991204_06_00.grib1',
'grib1/1999/1999.12/fnl_19991204_12_00.grib1',
'grib1/1999/1999.12/fnl_19991204_18_00.grib1',
'grib1/1999/1999.12/fnl_19991205_00_00.grib1',
'grib1/1999/1999.12/fnl_19991205_06_00.grib1',
'grib1/1999/1999.12/fnl_19991205_12_00.grib1',
'grib1/1999/1999.12/fnl_19991205_18_00.grib1',
'grib1/1999/1999.12/fnl_19991206_00_00.grib1',
'grib1/1999/1999.12/fnl_19991206_06_00.grib1',
'grib1/1999/1999.12/fnl_19991206_12_00.grib1',
'grib1/1999/1999.12/fnl_19991206_18_00.grib1',
'grib1/1999/1999.12/fnl_19991207_00_00.grib1',
'grib1/1999/1999.12/fnl_19991207_06_00.grib1',
'grib1/1999/1999.12/fnl_19991207_12_00.grib1',
'grib1/1999/1999.12/fnl_19991208_00_00.grib1',
'grib1/1999/1999.12/fnl_19991208_12_00.grib1',
'grib1/1999/1999.12/fnl_19991209_00_00.grib1',
'grib1/1999/1999.12/fnl_19991209_12_00.grib1',
'grib1/1999/1999.12/fnl_19991209_18_00.grib1',
'grib1/1999/1999.12/fnl_19991210_00_00.grib1',
'grib1/1999/1999.12/fnl_19991210_06_00.grib1',
'grib1/1999/1999.12/fnl_19991210_12_00.grib1',
'grib1/1999/1999.12/fnl_19991210_18_00.grib1',
'grib1/1999/1999.12/fnl_19991211_00_00.grib1',
'grib1/1999/1999.12/fnl_19991211_06_00.grib1',
'grib1/1999/1999.12/fnl_19991211_12_00.grib1',
'grib1/1999/1999.12/fnl_19991211_18_00.grib1',
'grib1/1999/1999.12/fnl_19991212_00_00.grib1',
'grib1/1999/1999.12/fnl_19991212_06_00.grib1',
'grib1/1999/1999.12/fnl_19991212_12_00.grib1',
'grib1/1999/1999.12/fnl_19991212_18_00.grib1',
'grib1/1999/1999.12/fnl_19991213_00_00.grib1',
'grib1/1999/1999.12/fnl_19991213_06_00.grib1',
'grib1/1999/1999.12/fnl_19991213_12_00.grib1',
'grib1/1999/1999.12/fnl_19991213_18_00.grib1',
'grib1/1999/1999.12/fnl_19991214_00_00.grib1',
'grib1/1999/1999.12/fnl_19991214_06_00.grib1',
'grib1/1999/1999.12/fnl_19991214_12_00.grib1',
'grib1/1999/1999.12/fnl_19991214_18_00.grib1',
'grib1/1999/1999.12/fnl_19991215_00_00.grib1',
'grib1/1999/1999.12/fnl_19991215_06_00.grib1',
'grib1/1999/1999.12/fnl_19991215_12_00.grib1',
'grib1/1999/1999.12/fnl_19991215_18_00.grib1',
'grib1/1999/1999.12/fnl_19991216_00_00.grib1',
'grib1/1999/1999.12/fnl_19991216_06_00.grib1',
'grib1/1999/1999.12/fnl_19991216_12_00.grib1',
'grib1/1999/1999.12/fnl_19991216_18_00.grib1',
'grib1/1999/1999.12/fnl_19991217_00_00.grib1',
'grib1/1999/1999.12/fnl_19991217_06_00.grib1',
'grib1/1999/1999.12/fnl_19991217_12_00.grib1',
'grib1/1999/1999.12/fnl_19991217_18_00.grib1',
'grib1/1999/1999.12/fnl_19991218_00_00.grib1',
'grib1/1999/1999.12/fnl_19991218_06_00.grib1',
'grib1/1999/1999.12/fnl_19991218_12_00.grib1',
'grib1/1999/1999.12/fnl_19991218_18_00.grib1',
'grib1/1999/1999.12/fnl_19991219_00_00.grib1',
'grib1/1999/1999.12/fnl_19991219_06_00.grib1',
'grib1/1999/1999.12/fnl_19991219_12_00.grib1',
'grib1/1999/1999.12/fnl_19991219_18_00.grib1',
'grib1/1999/1999.12/fnl_19991220_00_00.grib1',
'grib1/1999/1999.12/fnl_19991220_06_00.grib1',
'grib1/1999/1999.12/fnl_19991220_12_00.grib1',
'grib1/1999/1999.12/fnl_19991220_18_00.grib1',
'grib1/1999/1999.12/fnl_19991221_00_00.grib1',
'grib1/1999/1999.12/fnl_19991221_06_00.grib1',
'grib1/1999/1999.12/fnl_19991221_12_00.grib1',
'grib1/1999/1999.12/fnl_19991221_18_00.grib1',
'grib1/1999/1999.12/fnl_19991222_00_00.grib1',
'grib1/1999/1999.12/fnl_19991222_06_00.grib1',
'grib1/1999/1999.12/fnl_19991222_12_00.grib1',
'grib1/1999/1999.12/fnl_19991222_18_00.grib1',
'grib1/1999/1999.12/fnl_19991223_00_00.grib1',
'grib1/1999/1999.12/fnl_19991223_06_00.grib1',
'grib1/1999/1999.12/fnl_19991223_12_00.grib1',
'grib1/1999/1999.12/fnl_19991223_18_00.grib1',
'grib1/1999/1999.12/fnl_19991224_00_00.grib1',
'grib1/1999/1999.12/fnl_19991224_06_00.grib1',
'grib1/1999/1999.12/fnl_19991224_12_00.grib1',
'grib1/1999/1999.12/fnl_19991224_18_00.grib1',
'grib1/1999/1999.12/fnl_19991225_00_00.grib1',
'grib1/1999/1999.12/fnl_19991225_06_00.grib1',
'grib1/1999/1999.12/fnl_19991225_12_00.grib1',
'grib1/1999/1999.12/fnl_19991225_18_00.grib1',
'grib1/1999/1999.12/fnl_19991226_00_00.grib1',
'grib1/1999/1999.12/fnl_19991226_06_00.grib1',
'grib1/1999/1999.12/fnl_19991226_12_00.grib1',
'grib1/1999/1999.12/fnl_19991226_18_00.grib1',
'grib1/1999/1999.12/fnl_19991227_00_00.grib1',
'grib1/1999/1999.12/fnl_19991227_06_00.grib1',
'grib1/1999/1999.12/fnl_19991227_12_00.grib1',
'grib1/1999/1999.12/fnl_19991227_18_00.grib1',
'grib1/1999/1999.12/fnl_19991228_00_00.grib1',
'grib1/1999/1999.12/fnl_19991228_06_00.grib1',
'grib1/1999/1999.12/fnl_19991228_12_00.grib1',
'grib1/1999/1999.12/fnl_19991228_18_00.grib1',
'grib1/1999/1999.12/fnl_19991229_00_00.grib1',
'grib1/1999/1999.12/fnl_19991229_06_00.grib1',
'grib1/1999/1999.12/fnl_19991229_12_00.grib1',
'grib1/1999/1999.12/fnl_19991229_18_00.grib1',
'grib1/1999/1999.12/fnl_19991230_00_00.grib1',
'grib1/1999/1999.12/fnl_19991230_06_00.grib1',
'grib1/1999/1999.12/fnl_19991230_12_00.grib1',
'grib1/1999/1999.12/fnl_19991230_18_00.grib1',
'grib1/1999/1999.12/fnl_19991231_00_00.grib1',
'grib1/1999/1999.12/fnl_19991231_06_00.grib1',
'grib1/1999/1999.12/fnl_19991231_12_00.grib1',
'grib1/1999/1999.12/fnl_19991231_18_00.grib1']
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
