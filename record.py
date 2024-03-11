import alsaaudio

device = 'dmic_sv'

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, 
    channels=2, rate=32000, format=alsaaudio.PCM_FORMAT_S32_LE, 
    periodsize=640, device=device)
    
while True:
    # Read data from device
    inp.read()

