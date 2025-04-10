import socket
import threading
import json
import time

class CLIENTNetwork:
    def __init__(self):
        self.SERVER_HOST = '127.0.0.1'
        self.SERVER_PORT = 5555
        self.server_address = (self.SERVER_HOST, self.SERVER_PORT)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        self.data = ""
        self.playerID = None
        self.pos = ""
        self.running = True

        self.client.sendto("hello".encode("utf-8"), self.server_address)

        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.fac = "-"
        self.readyup = None
        self.numplayers = None
        self.player1x = ""
        self.player2x = ""
        self.player3x = ""
        self.player4x = ""
        self.player1fac = ""
        self.player2fac = ""
        self.player3fac = ""
        self.player4fac = ""
        self.winner = None

        self.ack = ""
        self.cheater = None

    def receive(self):
        while self.running == True:
            data, _ = self.client.recvfrom(1024)
            d_data = data.decode("utf-8")
            
            if "F" in d_data:
                pass
                # print("London Bridge is falling down")
            if "X" in d_data:
                playerIDrecv = d_data[0:7]
                if playerIDrecv == "PLAYER1":
                    self.player1x = d_data
                if playerIDrecv == "PLAYER2":
                    self.player2x = d_data
                if playerIDrecv == "PLAYER3":
                    self.player3x = d_data
                if playerIDrecv == "PLAYER4":
                    self.player4x = d_data
            elif "PLAYER" in d_data:
                # print("+")
                self.playerID = d_data
                # print(self.playerID)
                # print("+")
            if "F:" in d_data:
                playerIDrecv = d_data[0:7]
                if playerIDrecv == "PLAYER1":
                    self.player1fac = d_data
                if playerIDrecv == "PLAYER2":
                    self.player2fac = d_data
                if playerIDrecv == "PLAYER3":
                    self.player3fac = d_data
                if playerIDrecv == "PLAYER4":
                    self.player4fac = d_data
            if "HOSTCONNECT:" in d_data:
                host_info = d_data.split("HOSTCONNECT:('")[1]
                host_ip = host_info.split("', ")[0]
                host_port = host_info.split(', ')[1].split(")")[0]
                # print(host_port)
                # print(host_ip)
                host_port = int(host_port)
                self.server_address = (host_ip,host_port)
                self.client.sendto("CONNECTHOST".encode("utf-8"), self.server_address)
                # print(self.client)
                # print("updated host")
            if "CONNECTHOST" in d_data:
               pass 
            if "READY" in d_data:
                self.readyup = d_data
                self.numplayers = int(d_data.split("READY")[1])
                # print(self.numplayers)
            if "CHEATER" in d_data:
                self.cheater = d_data.split("CHEATER:")[1]
            if "ACK:" in d_data:
                print(d_data)
                self.ack = d_data
            if "WINNER: " in d_data:
                self.winner = d_data
                print(d_data)

    def getPos(self, pos):
        # print("shimishimiyeshimeya")
        self.client.sendto(pos.encode("utf-8"), self.server_address)

    def directionfac(self, fac):
        # print("swalalala")
        self.client.sendto(fac.encode("utf-8"), self.server_address)
    
    def sendmess(self, test):
        self.client.sendto(test.encode("utf-8"), self.server_address)

    def tcp(self,mess,address):
        self.tcpthead = threading.Thread(target=self.tcpconn,args=(mess,address))
        self.tcpthead.start()

    def tcpconn(self,mess,address):
        for i in range(1,5):
            mess = mess + "ACK:" + str(i)
            self.client.sendto(mess.encode("utf-8"), address)
            time.sleep(0.1)
            if self.ack == mess:
                break
            pass



