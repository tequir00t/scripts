#!/bin/bash
ifconfig wlan1 up 10.0.0.1 netmask 255.255.255.0
dhcpd wlan1 &
sleep 5
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
iptables --append FORWARD --in-interface wlan1 -j ACCEPT

iptables -A PREROUTING -t nat -i wlan1 -p tcp --dport 443 -j REDIRECT --to-port 8080
#iptables -A PREROUTING -t nat -i wlan1 -p tcp --dport 80 -j REDIRECT --to-port 8090

sysctl -w net.ipv4.ip_forward=1
hostapd /etc/hostapd/hostapd.conf 
killall dhcpd


