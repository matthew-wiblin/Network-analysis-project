from scripts.get_ping_info import get_ping_info
from scripts.check_dns_resolution import check_dns_resolution
from scripts.port_scanning import port_scanning
from scripts.measure_bandwidth import measure_bandwidth

if __name__ == "__main__":
    get_ping_info()
    check_dns_resolution()
    port_scanning()
    measure_bandwidth()
