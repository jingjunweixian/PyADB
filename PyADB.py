import os, io, re

rePatternA = re.compile('\\n((?!\\n|\\t).*?)\\t')
rePatternB = re.compile('[?!\\n]*(.*.)[\\t]*')

def getserialNumber():
    return rePatternA.findall(str(io.StringIO(os.popen(".\\platform-tools\\adb devices").read()).read()))
    #returns Serial of all connected devices as a list

def getIMEI(serialNumber):
    return rePatternB.findall(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell "service call iphonesubinfo 1 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"'''.format(DUTadd[i])).read()).read()))

def getMDN(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell "service call iphonesubinfo 19 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"'''.format(serialNumber)).read()).read()))

def getIMSI(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell "service call iphonesubinfo 8 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"'''.format(serialNumber)).read()).read()))

def getBrand(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell getprop ro.vendor.product.brand'''.format(serialNumber)).read()).read()))

def getModel(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell getprop ro.vendor.product.name'''.format(serialNumber)).read()).read()))

def getFirmware(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell getprop ro.build.display.id'''.format(serialNumber)).read()).read()))

def getAndroidVer(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell getprop ro.build.version.release'''.format(serialNumber)).read()).read()))

def getHardwareVer(serialNumber):
	return rePatternB.findall(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell getprop ro.boot.hardware.revision'''.format(serialNumber)).read()).read()))

def getMemoryType(serialNumber):
	return rePatternB(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell getprop ro.boot.hardware.ddr'''.format(serialNumber)).read()).read()))

def getRadioChipType(serialNumber):
	return rePatternB(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell getprop ro.product.board'''.format(serialNumber)).read()).read()))

def getRadioChipVer(serialNumber):
	return rePatternB(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell getprop ro.build.expect.baseband'''.format(serialNumber)).read()).read()))

def getCPURev(serialNumber):
	return rePatternB(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell getprop ro.product.cpu.abi'''.format(serialNumber)).read()).read()))

def emergencyCall(serialNumber, callNumber):
	os.popen(r'''\\platform-tools\\adb -s {} shell am start -a android.intent.action.CALL_PRIVILEGED -d tel:{}'''.format(serialNumber, callNumber))
	#change to priveleged call type

def makeCall(serialNumber, callNumber):
	os.popen(r'''.\\platform-tools\\adb -s {} shell am start -a android.intent.action.CALL -d tel:{}'''.format(serialNumber, callNumber))

def endCall(serialNumber):
	os.popen(r'''.\\platform-tools\\adb -s {} shell input keyevent KEYCODE_ENDCALL''')

def getCallStatus(serialNumber):
	DevStatus = str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} shell "dumpsys telephony.registry | grep 'mCallState' " '''.format(serialNumber)).read()).read())
    return DevStatus[-3]
    '''Status 0 is waiting
       Status 1 is ringing
       Status 2 is active call'''

def push(serialNumber ,source, destination):
	rePatternB(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} push ,{} , {}'''.format(serialNumber, source, destination)).read()).read()))

def pull(serialNumber, source, destination):
	rePatternB(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} pull ,{} , {}'''.format(serialNumber, source, destination)).read()).read()))

def install(serialNumber,APK):
	rePatternB(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} install {}'''.format(serialNumber, APK)).read()).read()))

def uninstall(serialNumber,APK):
	rePatternB(str(io.StringIO(os.popen(r'''.\\platform-tools\\adb -s {} uninstall {}'''.format(serialNumber, APK)).read()).read()))
