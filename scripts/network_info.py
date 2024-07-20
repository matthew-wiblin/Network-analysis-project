from lib.get_ping_info import get_ping_info
from lib.check_dns_resolution import check_dns_resolution
from lib.port_scanning import port_scanning
from lib.measure_bandwidth import measure_bandwidth


if __name__ == "__main__":
    get_ping_info()
    check_dns_resolution()
    port_scanning()
    measure_bandwidth()