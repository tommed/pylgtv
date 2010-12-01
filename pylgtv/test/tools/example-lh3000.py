from time import sleep
import sys

sys.path.append('../../../')
import pylgtv.televisions.lg.lh3000 as tv

def main():
        ctl = tv.LG_LH3000()

        print "TV turn on"
        ctlpower(on=True)
        sleep(3)

        print "mute on"
        ctlmute(on=True)
        sleep(2)

        print "mute off"
        ctlmute(on=False)
        sleep(2)

        print "TV turn off"
        ctlpower(on=False)

if __name__ == "__main__":
        main()
