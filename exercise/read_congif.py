import configparser

data = r'F:\Myself\past\vc_redist.2015.x86和vc_redist.2015.x64\y163yxzcj\163pz.ini'
cf = configparser.ConfigParser()
cf.read(data)
print(cf.sections())
# print(s)