#ifndef HEADER_H
#define HEADER_H

#include <pcap.h>

void packet_handler(u_char *user_data, const struct pcap_pkthdr *pkthdr, const u_char *packet);

#endif
