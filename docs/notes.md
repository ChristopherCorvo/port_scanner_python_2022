
### Common network attacks can be divided into four types:
1. fake message attacks


2. exploitable attacks


3. denial of service attacks


4. information gathering attacks
   * Information collection does not cause harm to the target itself,
   and such attacks are used to provide useful information for further intrusions.


   * Information collection technology is a double-edged sword. On one hand, an
   attacker needs to collect information before an attack to carry out an effective attack.


   * On the other hand, a network administrator can use information collection technology
   to discover system vulnerabilities and repair them in advance [2–4]. Network administrators usually do not hide their identities during scanning. On the contrary, attackers hide their identities.


   * The most common information collection technology is scanning technology [5,6],
   which includes architecture detection and utilization of information services.

### Computer ports:
* Computer Port == In computer networking, a port is a number assigned to uniquely identify
a connection endpoint and to direct data to a specific service


* There are 65,536 ports provided by TCP/IP protocol for an IP address in the computer [7].


* Among them, the range of Well Known Ports is from 0 to 1023


* the range of Registered Ports is from 1024 to 49,151, and the range of dynamic
ports is from 49,152 to 65,535.

### ICMP:
* ICMP (Internet Control Message Protocol):
  * is a network layer protocol used by network devices to diagnose network communication issues


  * mainly used to determine whether or not data is reaching its intended destination in a
  timely manner.


  * The primary purpose of ICMP is for error reporting.
    * When two devices connect over the Internet, the ICMP generates errors to share with the
    sending device in the event that any of the data did not get to its intended destination.
    For example, if a packet of data is too large for a router, the router will drop the
    packet and send an ICMP message back to the original source for the data.


  * The ICMP works with the PING program:
    * ping is a computer network administration software utility used to test the reachability
    of a host on an Internet Protocol (IP) network. It is available for virtually all
    operating systems that have networking capability, including most embedded network
    administration software.
      * Ping operates by means of Internet Control Message Protocol (ICMP) packets.
      Pinging involves sending an ICMP echo request to the target host and waiting for an
      ICMP echo reply. The program reports errors, packet loss, and a statistical summary
      of the results, typically including the minimum, maximum, the mean round-trip times,
      and standard deviation of the mean.

### Port Scanning:
* The intention is to scan a systems port or ports in order to determine which ports
are open and therefore are vulnerable to attack.

### Random Notes:
* IP scanners:
  * scan networks to detect the active devices on them
* Port scanners:
  * Are geared to towards scanning individual devices in a network to discover open ports.
* Think of ports as the windows and doors through which you can enter a house, and the ip
address is the address to the house.
* If you did not specify the IP range which you want to scan, the scanner would use the
default setting, which is the local subnet, so all of the IPs of the local subnet would
be scanned. All the scanner does is send pings to each of the IP addresses in the range
which you are interested in to get details about the IP.
* Some of the information IP scanners would try to find out includes:
  * if an IP address is active
  * the device it is assigned to
  * the device-related information such:
    * as Operating System
    * vendor
    * MAC address
      * description of the device
      * If the scanner has support for scanning ports for each of the IPs/devices:
        * Individual ports to find out the status:
          * open
          * close
          * filtered
### Vocab:
* request packet
*
