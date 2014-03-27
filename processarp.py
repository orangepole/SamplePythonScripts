#!/usr/bin/python

#Author: Suraj Patil
#Version: 1.0
#Date: 27th March 2014

#Reads a pcap file into python using scapy and produces a csv file as output in the following format: Timestamp, source MAC address, source IP address, Destination MAC address, Destination IP address

from scapy.all import *

pcap_path = raw_input('Path of pcap file: ') # enter the path where you stored the pcap file
file_path = raw_input('Enter target file name')  #enter the path where you want to create a csv file

try:
  file = open(file_path+'.csv','w')  #tries to opens the file in read mode
  pkts = rdpcap(pcap_path)  #inbuilt function of scapy to read pcap files
  for i in range(len(pkts)):
    if ARP in pkts[i]:  #checks if the packet is an ARP packet or not
     file.write ('%d,%s,%s,%s,%s,%d,%s\n'%( a[i].time, a[i].hwsrc, a[i].psrc, a[i].hwdst, a[i].pdst, a[i].hwtype, a[i].op))
     print 'file write complete'
     #Timestamp, source MAC address, source IP address, Destination MAC address, Destination IP address
  file.close()
except:
  print 'some error occured'
