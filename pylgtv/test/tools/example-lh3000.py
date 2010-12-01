import sys
sys.path.append('../../../')
import pylgtv.lh3000 as lg
from time import sleep

def main():
        tv = lg.LG_LH3000()

        print "TV turn on"
        tv.power(on=True)
        sleep(3)

        print "mute on"
        tv.mute(on=True)
        sleep(2)

        print "mute off"
        tv.mute(on=False)
        sleep(2)

        print "TV turn off"
        tv.power(on=False)

if __name__ == "__main__":
        main()
