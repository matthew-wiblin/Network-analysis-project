#include <pcap.h>
#include <iostream>
#include <netinet/ip.h>
#include <arpa/inet.h>

#include "header.h"

void packet_handler(u_char *user_data, const struct pcap_pkthdr *pkthdr, const u_char *packet) {
    // Pointer to the IP header
    const struct ip *iph = (struct ip*)(packet + 14); // Skip Ethernet header (14 bytes)

    // Print basic packet information
    std::cout << "Packet received, length: " << pkthdr->len << std::endl;
    std::cout << "Source IP: " << inet_ntoa(iph->ip_src) << std::endl;
    std::cout << "Destination IP: " << inet_ntoa(iph->ip_dst) << std::endl;

    // Check the protocol
    switch (iph->ip_p) {
        case IPPROTO_TCP: {
            std::cout << "Protocol: TCP" << std::endl; break;
        }
        case IPPROTO_UDP: {
            std::cout << "Protocol: UDP" << std::endl; break;
        }
        case IPPROTO_ICMP: {
            std::cout << "Protocol: ICMP" << std::endl; break;
        }
        default: {
            std::cout << "Protocol: Other" << std::endl; break;
        }
    }

    std::cout << "-----------------------------------" << std::endl;
}
