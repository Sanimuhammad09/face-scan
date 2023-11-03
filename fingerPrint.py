import time
from pyfingerprint.pyfingerprint import PyFingerprint

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if not f.verifyPassword():
        raise ValueError('The given fingerprint sensor password is incorrect!')
except Exception as e:
    print('Error: ' + str(e))

try:
    print('Waiting for finger...')
    while not f.readImage():
        pass

    f.convertImage(0x01)

    # Search for a match in the stored fingerprints
    result = f.searchTemplate()
    position = result[0]

    if position >= 0:
        print('Access granted')
    else:
        print('Access not granted')

    time.sleep(2)

except Exception as e:
    print('Error: ' + str(e))
