#include <pcap.h>
#include <iostream>

void packet_handler(u_char *user_data, const struct pcap_pkthdr *pkthdr, const u_char *packet) {
    std::cout << "Packet received, length: " << pkthdr->len << std::endl;
}

int main() {
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *handle;

    // Open the network device for packet capture
    handle = pcap_open_live("eth0", BUFSIZ, 1, 1000, errbuf);
    if (handle == nullptr) {
        std::cerr << "Failed to open device: " << errbuf << std::endl;
        return 1;
    }

    // Start capturing packets
    if (pcap_loop(handle, 10, packet_handler, nullptr) < 0) {
        std::cerr << "Error during packet capture: " << pcap_geterr(handle) << std::endl;
        return 1;
    }

    // Close the capture handle
    pcap_close(handle);

    return 0;
}
