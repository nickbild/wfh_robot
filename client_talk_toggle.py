import os


PAUSEFILE = '.audio.bot.pause'


# Toggle robot/client mute status to switch talk direction.
if os.path.isfile(PAUSEFILE):
    os.system("rm -f {0}".format(PAUSEFILE))
    os.system("ssh pi@192.168.1.177 'touch /home/pi/software/wfh_robot/{0}'".format(PAUSEFILE))
    print("Talk now.")
else:
    os.system("touch {0}".format(PAUSEFILE))
    os.system("ssh pi@192.168.1.177 'rm -f /home/pi/software/wfh_robot/{0}'".format(PAUSEFILE))
    print("You're muted.")
