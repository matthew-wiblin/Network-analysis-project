#include <pcap.h>
#include <iostream>

#include "header.h"

int main() {
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *handle;

    handle = pcap_open_live("enX0", BUFSIZ, 1, 1000, errbuf);
    if (handle == nullptr) {
        std::cerr << "Failed to open device: " << errbuf << std::endl;
        return 1;
    }

    if (pcap_loop(handle, 10, packet_handler, nullptr) < 0) {
        std::cerr << "Error during packet capture: " << pcap_geterr(handle) << std::endl;
        return 1;
    }

    pcap_close(handle);

    return 0;
}
