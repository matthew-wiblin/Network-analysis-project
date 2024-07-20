import socket

def port_scanning():

    successful = []
    connection_refused = []
    unsuccesful = []
    ports = [22, 25, 53, 80, 110, 143, 443, 3306, 5000, 8080]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect(("scanme.nmap.org", port))
            successful.append(port)
            s.close()
        except ConnectionRefusedError:
            connection_refused.append(port)
        except:
            unsuccesful.append(port)
    
    print("TCP Port Connection Attempts:")
    print("-- Command = Socket connection attempts")
    print(f"-- Successful port connections = {successful}")
    print(f"-- Connection refused = {connection_refused}")
    print(f"-- Unsuccessful port connections = {unsuccesful}\n")

if __name__ == "__main__":
    port_scanning()
