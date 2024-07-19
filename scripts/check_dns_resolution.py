import subprocess

def check_dns_resolution():
    result = subprocess.run(["nslookup", "google.com"], capture_output=True, text=True)
    response = ""
    if "NXDOMAIN" in result.stdout or "server can't find" in result.stdout:
        response = "Failed to resolve DNS of google.com"
    else:
        response = "Successfully resolved DNS of google.com"
    print("Check DNS resolution:")
    print("-- Command = 'nslookup google.com'")
    print("-- " + response + "\n")
    return

if __name__ == "__main__":
    check_dns_resolution()
