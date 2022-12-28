from command import getInput
from reno import Reno

def life():
    RENO = Reno()
    while True:
        RENO.initial()
        command = getInput().lower()
        if command == 0:
            continue
        if 'bye' in command or 'no' == command or 'stop' == command:
            RENO.goodbye()
            break
        if 'wikipedia' in command:
            RENO.wikipedia(command)
            continue
        if 'open' in command:
            RENO.openApp(command)
            continue
        if 'time' in command:
            RENO.getTime()
            continue

        RENO.say("I am sorry, I didn't understand.")

if __name__ == "__main__":
    life()