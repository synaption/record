import time
import alsaaudio
import traceback

if __name__ == '__main__':

    device = 'dmic_sv'

    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, 
        channels=2, rate=32000, format=alsaaudio.PCM_FORMAT_S32_LE, 
        periodsize=640, device=device)


    while True:
        try:
            # Read data from device
            l, data = inp.read()
            time.sleep(.001)
            
                
        except Exception as e:  # Catch the exception and print the traceback
            traceback.print_exc()
            
