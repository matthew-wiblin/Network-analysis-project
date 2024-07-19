import subprocess

def get_ping_connectivity():
    result = subprocess.run(["ping", "-c", "5", "google.com"], capture_output=True, text=True)
    ping_times = []
    packet_loss = 0
    for line in result.stdout.splitlines():
        if "time=" in line:
            parts = line.split()
            for part in parts:
                if "time=" in part:
                    ping_times.append(part.split("=")[1])
        if "packet loss" in line:
            parts = line.split("%")
            packet_loss = parts[0].strip().split()[-1]
    total_ping_time = 0
    for str in ping_times:
        total_ping_time += float(str)
    ave_ping_time = total_ping_time / 5
    print(f"Network connectivity: average ping time = {round(ave_ping_time, 3)}, packet loss = {packet_loss}% (5 pings to google)")
    return

if __name__ == '__main__':
    get_ping_connectivity()
