import os, io, re

rePatternA = re.compile('\\n((?!\\n|\\t).*?)\\t')
rePatternB = re.compile('[?!\\n]*(.*.)[\\t]*')

def getserialNumber():
    return rePatternA.findall(str(io.StringIO(os.popen(".\\platform-tools\\adb devices").read()).read()))

def getIMEI(serialNumber):
    return rePatternB.findall(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb -s {} shell "service call iphonesubinfo 1 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"'''.format(DUTadd[i])).read()).read()))

def getMDN(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 19 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read()))

def getIMSI(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 8 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read()))

def getBrand(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.vendor.product.brand''').read()).read()))

def getModel(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.vendor.product.name''').read()).read()))

def getFirmware(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.build.display.id''').read()).read()))

def getAndroidVer(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.build.version.release''').read()).read()))

def getHardwareVer(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.boot.hardware.revision''').read()).read()))

def getMemoryType(serialNumber):
	return rePatternB(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.boot.hardware.ddr''').read()).read()))

def getRadioChipType(serialNumber):
	return rePatternB(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.product.board''').read()).read()))

def getRadioChipVer(serialNumber):
	return rePatternB(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.build.expect.baseband''').read()).read()))

def getCPURev(serialNumber):
	return rePatternB(str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.product.cpu.abi''').read()).read()))

def emergencyCall(serialNumber, callNumber):
	os.system('.\\platform-tools\\adb -s {} shell am start -a android.intent.action.CALL -d tel:{}}'.format(serialNumber, callNumber))
	#change to priveleged call type
	
def makeCall(serialNumber, callNumber):
	os.system('.\\platform-tools\\adb -s {} shell am start -a android.intent.action.CALL -d tel:{}}'.format(serialNumber, callNumber)) 