import subprocess

def measure_bandwidth():

    result = subprocess.run(["speedtest-cli"], capture_output=True, text=True)
    
    testing_from = "Not available"
    hosted_by = "Not available"
    ping = "Not available"
    download_speed = "Not available"
    upload_speed = "Not available"

    for line in result.stdout.splitlines():
        if "Testing from" in line:
            testing_from = (line.split("from ")[1]).rstrip(".")
        elif "Hosted by" in line:
            hosted_by = line.split("by ")[1].split(":")[0].strip()
            ping = line.split(": ")[1].strip()
        elif "Download:" in line:
            download_speed = line.split(": ")[1].strip()
        elif "Upload:" in line:
            upload_speed = line.split(": ")[1].strip()

    if "Not available" in [testing_from, hosted_by, ping, download_speed, upload_speed]:
        print("Bandwidth test may have failed - Run again or check access to 'speedtest-cli'")
    else:
        print("Bandwidth Test Results:")
        print("-- Command = 'speedtest-cli'")
        print(f"-- Tested from {testing_from}")
        print(f"-- Hosted by '{hosted_by}' with a ping of {ping}")
        print(f"-- Download speed = {download_speed}")
        print(f"-- Upload speed = {upload_speed}\n")

if __name__ == '__main__':
    test_bandwidth()
