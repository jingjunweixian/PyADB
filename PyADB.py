import os, io, re

def getserialNumber():
    ADBrawInput = str(io.StringIO(os.popen(".\\platform-tools\\adb devices").read()).read())
    pattern = re.compile('\\n((?!\\n|\\t).*?)\\t')
    return pattern.findall(ADBrawInput)

def getIMEI(serialNumber):

    IMEIraw = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb -s {} shell "service call iphonesubinfo 1 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"'''.format(DUTadd[i])).read()).read())
    IMEIPattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    return IMEIPattern.findall(IMEIraw)[0]

def getMDN(serialNumber):
	MDNRaw = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 19 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
	rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
	rePattern.findall(dataTemp)

def getIMSI(serialNumber):
	IMSIRaw = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 8 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
	rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
	rePattern.findall(dataTemp)