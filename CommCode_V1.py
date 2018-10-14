import os
import datetime
import socket
from time import sleep
#from Queue import Queue
import threading
#DevicesQueue=Queue()
Devices={}
Window=25


def SetCMD(command, deviceAddress, name):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.settimeout(1)
    error=True
    try:
        sock.connect(deviceAddress)
        sleep(.1)
        data=sock.recv(1024)
        if name==data:
            sock.send(command)
            if 'ACK' in command:
                loop=True
                count=0
                while loop:
                    try:
                        data=sock.recv(1024)
                        if "Check "+command in data:
                            error=False
                            sock.send(name+" Exe")
                        count=10
                    except:
                        pass
                    count=count+1
                    if count>10:
                        loop=False
            if 'Get' in command:
                sleep(1)
                data=sock.recv(1024)
                error=False
        #holdQueue.put((name,error,data))
        hold=data.split(' ')
        string=C_dir+'\Files'+'\\'+name+'.txt'
        f=open(string,'r+')
        data=f.readlines()
        data[0]=hold[1]+','+hold[3]+','+hold[5]+','+hold[7]+','+'0'+'\n'
        f.seek(0)
        for i in range(1,len(data)):
            f.write(data[i])
        f.write(data[0])        
    except socket.error:
        pass
    sock.close()
def PingDevices():
    global Devices
    Look=True
    address=1
    addressString='192.168.1.'
    count=0
    find=3
    while Look:
        string=addressString+str(address)
        try:
            print('Ping: '+string+'\n')
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            sock.settimeout(.2)
            sock.connect((string,2000))
            sleep(.1)
            data=sock.recv(1024)
            Devices[data]=((string,2000))
            count=count+1
            print('Device found: '+data)
            sock.close()
        except socket.error:
            sock.close()
            print(socket.error)
        address=address+1
        if address==10 or count==find:
            Look=False
C_dir=os.getcwd()
try:
    files=os.listdir(C_dir+'\Files')
    print(files)
    for f in files:
        os.remove(C_dir+'\Files\\'+f)
except:
    os.makedirs(C_dir+'\Files')
PingDevices()
for Device in Devices:
    string=C_dir+'\Files'+'\\'+Device+'.txt'
    f=open(string,'w')
    Voltage='NaN'
    Current='NaN'
    Phase='NaN'
    Temp='NaN'
    Occ='NaN'
    data=str(Voltage)+','+str(Current)+','+str(Phase)+','+str(Temp)+','+str(Occ)+'\n'
    for i in range(Window):
        f.write(data)   
    f.close()
e=True
while e:
    threads=[]
    for Device in Devices:
        command="Get Meas"
        deviceAddress=Devices[Device]
        try:
            t=threading.Thread(target=SetCMD,args=(command,Devices[Device],Device,))
            t.setDaemon(True)
            threads.append(t)
            t.start()
        except:
            print('Error: unable to start thread')
    for n in threads:
        n.join()
    # while not DevicesQueue.empty():
        # holdData=DevicesQueue.get()
    sleep(1)
    e=True
##        try:
##            t=threading.Thread(target=sendAgents,args=(command,agentAddress,data,agentQueue,))
##            t.setDaemon(True)
##            threads.append(t)
##            t.start()
##        except:
##            print >>sys.stderr,'Error: unable to start thread'
##    for n in threads:
##        n.join()
##    while not agentQueue.empty():
##        holdData=agentQueue.get()
##        print >>sys.stderr,Agents[holdData[0]]+' '+command+': '+holdData[1]
####while True:
####    command="Get Meas"
##    
