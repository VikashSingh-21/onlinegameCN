import socket
import threading
import random
import json
import time

class HOSTServerNetwork:
    def __init__(self):
        self.SERVER_HOST_IP = '127.0.0.1'
        self.SERVER_HOST_PORT = 0
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.SERVER_HOST_IP, self.SERVER_HOST_PORT))
        self.SERVER_HOST_PORT = self.server_socket.getsockname()[1]

        self.serverIP = "127.0.0.1"
        self.serverPORT = 5555
        self.server_address = (self.serverIP, self.serverPORT)
        
        self.HostAddr = str(self.SERVER_HOST_IP + "," + str(self.SERVER_HOST_PORT))
        self.code = str(random.randint(1000, 9999))
        self.hostmessage = "HOST:" + self.HostAddr + "RNG:" + str(self.code)

        self.data = ""
        self.playerID = None
        self.allAddresses = []
        self.maxPlayers = 4
        self.allPLAYERS = []
        self.pos = ""


        self.player_positions = {
            "PLAYER1": {"x": 300, "y": 250, "last_time": time.time()},
            "PLAYER2": {"x": 300, "y": 200, "last_time": time.time()},
            "PLAYER3": {"x": 250, "y": 200, "last_time": time.time()},
            "PLAYER4": {"x": 300, "y": 200, "last_time": time.time()}
        }
        

        self.server_socket.sendto(self.hostmessage.encode("utf-8"), self.server_address)

        self.receive_thread = threading.Thread(target=self.receiveAsServer)
        self.receive_thread.daemon = True 
        self.receive_thread.start()

        self.fac = "-"
    
    def detect_cheat(self, playerIDrecv, x_pos, y_pos):
        current_time = time.time()
        player_data = self.player_positions[playerIDrecv]

        x_diff = abs(player_data["x"] - x_pos)
        y_diff = abs(player_data["y"] - y_pos)
        time_elapsed = current_time - player_data["last_time"]

        frames_passed = time_elapsed / (1 / 60)
        frames_passed = max(frames_passed, 1)

        mov_per_frame = 3  # pixels
        max_allowed_movement = mov_per_frame * frames_passed
        
        

        tolerance = 0.05  # 5% tolerance
        min_allowed_movement = max_allowed_movement * (1 - tolerance)

        cheatmess = "CHEATER:" + playerIDrecv
        if x_diff > min_allowed_movement:
            print(f"Cheat detected for X: {playerIDrecv}")
            for addresses in self.allAddresses:
                self.server_socket.sendto(cheatmess.encode("utf-8"), addresses)
        if y_diff > min_allowed_movement:
            print(f"Cheat detected for Y: {playerIDrecv}")
            for addresses in self.allAddresses:
                self.server_socket.sendto(cheatmess.encode("utf-8"), addresses)

        player_data["x"] = x_pos
        player_data["y"] = y_pos
        player_data["last_time"] = current_time
    
    def receiveAsServer(self):
        while True:
            data, client_address = self.server_socket.recvfrom(1024)
            d_data = data.decode("utf-8")

            # recipient_index = 1 if client_index == 0 else 0
            # recipient = self.allAddresses[recipient_index]

            if client_address not in self.allAddresses and len(self.allAddresses) < self.maxPlayers:
                self.allAddresses.append(client_address)
                client_index = self.allAddresses.index(client_address)
                # tcp
                playerID = "PLAYER" + str(client_index + 1)
                self.allPLAYERS.append(playerID)
                self.server_socket.sendto(playerID.encode("utf-8"), client_address)
            # print(f"Received data: {d_data}")
            if len(self.allAddresses) == self.maxPlayers:
                for recipient in self.allAddresses:
                    if recipient != client_address:
                        # tcp
                        self.server_socket.sendto(d_data.encode("utf-8"), recipient)
            if "LOBBYCODE" in d_data:
                self.code = d_data.split("LOBBYCODE:")[1]
                pass
            if "CONNECTHOST" in d_data:
                pass
                # print("what a wonderfull day")

            if "READYUP" in d_data:
                numplayers = len(self.allAddresses)
                readyplayers = "READY" + str(numplayers)
                # print("these are bear nessesaties")
                # tcp
                for allplayersunready in self.allAddresses:
                    self.server_socket.sendto(readyplayers.encode("utf-8"), allplayersunready)
            if "X" in d_data:
                playerIDrecv = d_data[0:7]
                x_pos = int(d_data.split("X:")[1].split("Y:")[0].strip())
                y_pos = int(d_data.split("Y:")[1].split()[0].strip())
                self.detect_cheat(playerIDrecv, x_pos, y_pos)
                for recipient in self.allAddresses:
                    if recipient != client_address:
                        self.server_socket.sendto(d_data.encode("utf-8"), recipient)
            if "F:" in d_data:
                for recipient in self.allAddresses:
                    if recipient != client_address:
                        self.server_socket.sendto(d_data.encode("utf-8"), recipient)
            if "WINNER: " in d_data:
                for recipient in self.allAddresses:
                    if recipient != client_address:
                        self.server_socket.sendto(d_data.encode("utf-8"), recipient)
            if "CHEATER:" in d_data:
                for recipient in self.allAddresses:
                    if recipient != client_address:
                        self.server_socket.sendto(d_data.encode("utf-8"), recipient)
            

