# 19-网络安全 · NetworkSecurity

> 本分类共 **43** 个技能（蓝队 43）。

每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。

| # | 技能 | 英文标识 | 摘要 | 路径 |
|---|---|---|---|---|
| 1 | **802.1X网络接入控制** | `implementing-network-access-control` | Implements 802.1X port-based network access control using RADIUS authe… | [SKILL.md](skills/802.1X网络接入控制_implementing-network-access-control/SKILL.md) |
| 2 | **ARP投毒检测** | `detecting-arp-poisoning-in-network-traffic` | Detect Layer 2 ARP poisoning/spoofing by deploying ARPWatch, Dynamic A… | [SKILL.md](skills/ARP投毒检测_detecting-arp-poisoning-in-network-traffic/SKILL.md) |
| 3 | **ARP欺骗攻击模拟** | `performing-arp-spoofing-attack-simulation` | Simulates ARP spoofing/cache-poisoning attacks in authorized lab or pe… | [SKILL.md](skills/ARP欺骗攻击模拟_performing-arp-spoofing-attack-simulation/SKILL.md) |
| 4 | **Arkime全包捕获分析** | `implementing-network-traffic-analysis-with-arkime` | Queries Arkime (formerly Moloch) full packet capture via its API to se… | [SKILL.md](skills/Arkime全包捕获分析_implementing-network-traffic-analysis-with-arkime/SKILL.md) |
| 5 | **BGP劫持漏洞利用** | `exploiting-bgp-hijacking-vulnerabilities` | Analyzes and simulates BGP hijacking scenarios in authorized lab envir… | [SKILL.md](skills/BGP劫持漏洞利用_exploiting-bgp-hijacking-vulnerabilities/SKILL.md) |
| 6 | **Cisco ISE接入控制** | `implementing-network-access-control-with-cisco-ise` | Deploys Cisco Identity Services Engine (ISE) as a RADIUS policy server… | [SKILL.md](skills/Cisco ISE接入控制_implementing-network-access-control-with-cisco-ise/SKILL.md) |
| 7 | **Cloudflare DDoS防护** | `implementing-ddos-mitigation-with-cloudflare` | Configure Cloudflare DDoS protection with managed rulesets, rate limit… | [SKILL.md](skills/Cloudflare DDoS防护_implementing-ddos-mitigation-with-cloudflare/SKILL.md) |
| 8 | **DNS枚举与区域传送** | `performing-dns-enumeration-and-zone-transfer` | Enumerates DNS records, attempts zone transfers, brute-forces subdomai… | [SKILL.md](skills/DNS枚举与区域传送_performing-dns-enumeration-and-zone-transfer/SKILL.md) |
| 9 | **DNS查询外泄检测** | `detecting-dns-exfiltration-with-dns-query-analysis` | Detect data exfiltration via DNS tunneling (tools like iodine, dnscat2… | [SKILL.md](skills/DNS查询外泄检测_detecting-dns-exfiltration-with-dns-query-analysis/SKILL.md) |
| 10 | **DNS隧道C2检测** | `detecting-command-and-control-over-dns` | Detect command-and-control (C2) traffic tunneled over DNS from tools l… | [SKILL.md](skills/DNS隧道C2检测_detecting-command-and-control-over-dns/SKILL.md) |
| 11 | **IDS网络扫描检测** | `detecting-network-scanning-with-ids-signatures` | Detect network reconnaissance and port scanning using Suricata and Sno… | [SKILL.md](skills/IDS网络扫描检测_detecting-network-scanning-with-ids-signatures/SKILL.md) |
| 12 | **IPv6漏洞利用** | `exploiting-ipv6-vulnerabilities` | Identifies and exploits IPv6-specific vulnerabilities including SLAAC… | [SKILL.md](skills/IPv6漏洞利用_exploiting-ipv6-vulnerabilities/SKILL.md) |
| 13 | **Kismet无线安全评估** | `performing-wireless-security-assessment-with-kismet` | Conduct wireless network security assessments using Kismet to detect r… | [SKILL.md](skills/Kismet无线安全评估_performing-wireless-security-assessment-with-kismet/SKILL.md) |
| 14 | **Metasploit SMB漏洞利用** | `exploiting-smb-vulnerabilities-with-metasploit` | Identifies and exploits SMB protocol vulnerabilities using Metasploit… | [SKILL.md](skills/Metasploit SMB漏洞利用_exploiting-smb-vulnerabilities-with-metasploit/SKILL.md) |
| 15 | **NetFlow流量数据分析** | `analyzing-network-flow-data-with-netflow` | Parse NetFlow v9 and IPFIX records to detect volumetric anomalies, por… | [SKILL.md](skills/NetFlow流量数据分析_analyzing-network-flow-data-with-netflow/SKILL.md) |
| 16 | **Nmap高级扫描** | `scanning-network-with-nmap-advanced` | Performs advanced network recon using Nmap''s Scripting Engine (NSE),… | [SKILL.md](skills/Nmap高级扫描_scanning-network-with-nmap-advanced/SKILL.md) |
| 17 | **Palo Alto下一代防火墙** | `implementing-next-generation-firewall-with-palo-alto` | Configures and deploys Palo Alto Networks next-generation firewalls en… | [SKILL.md](skills/Palo Alto下一代防火墙_implementing-next-generation-firewall-with-palo-alto/SKILL.md) |
| 18 | **RPKI BGP安全实施** | `implementing-bgp-security-with-rpki` | Implement RPKI-based BGP route origin validation by creating Route Ori… | [SKILL.md](skills/RPKI BGP安全实施_implementing-bgp-security-with-rpki/SKILL.md) |
| 19 | **SSL-TLS安全评估** | `performing-ssl-tls-security-assessment` | Assess SSL/TLS server configurations using the sslyze Python scanning… | [SKILL.md](skills/SSL-TLS安全评估_performing-ssl-tls-security-assessment/SKILL.md) |
| 20 | **SSL-TLS检测配置** | `performing-ssl-tls-inspection-configuration` | Configure SSL/TLS break-and-inspect on next-generation firewalls and f… | [SKILL.md](skills/SSL-TLS检测配置_performing-ssl-tls-inspection-configuration/SKILL.md) |
| 21 | **SSL剥离攻击模拟** | `performing-ssl-stripping-attack` | Simulates SSL stripping / HTTPS downgrade attacks using sslstrip, Bett… | [SKILL.md](skills/SSL剥离攻击模拟_performing-ssl-stripping-attack/SKILL.md) |
| 22 | **Scapy网络包分析** | `analyzing-network-packets-with-scapy` | Use Scapy to craft, send, sniff, and dissect TCP/UDP/ICMP/DNS packets,… | [SKILL.md](skills/Scapy网络包分析_analyzing-network-packets-with-scapy/SKILL.md) |
| 23 | **Snort入侵检测配置** | `configuring-snort-ids-for-intrusion-detection` | Installs, configures, and tunes Snort 3 to monitor network traffic for… | [SKILL.md](skills/Snort入侵检测配置_configuring-snort-ids-for-intrusion-detection/SKILL.md) |
| 24 | **Suricata入侵防御** | `implementing-network-intrusion-prevention-with-suricata` | Deploys and configures Suricata as an inline network intrusion prevent… | [SKILL.md](skills/Suricata入侵防御_implementing-network-intrusion-prevention-with-suricata/SKILL.md) |
| 25 | **Suricata流量监控配置** | `configuring-suricata-for-network-monitoring` | Deploys and configures Suricata IDS/IPS with Emerging Threats rulesets… | [SKILL.md](skills/Suricata流量监控配置_configuring-suricata-for-network-monitoring/SKILL.md) |
| 26 | **VLAN网络分段配置** | `configuring-network-segmentation-with-vlans` | Designs and implements VLAN-based (802.1Q) network segmentation on man… | [SKILL.md](skills/VLAN网络分段配置_configuring-network-segmentation-with-vlans/SKILL.md) |
| 27 | **VLAN跳跃攻击模拟** | `performing-vlan-hopping-attack` | Simulates VLAN hopping attacks using switch spoofing and 802.1Q double… | [SKILL.md](skills/VLAN跳跃攻击模拟_performing-vlan-hopping-attack/SKILL.md) |
| 28 | **Wireshark流量分析** | `analyzing-network-traffic-with-wireshark` | Captures and analyzes network packet data using Wireshark and tshark t… | [SKILL.md](skills/Wireshark流量分析_analyzing-network-traffic-with-wireshark/SKILL.md) |
| 29 | **Zeek DNS外泄检测** | `detecting-exfiltration-over-dns-with-zeek` | Detect DNS-based data exfiltration by analyzing Zeek dns.log for high-… | [SKILL.md](skills/Zeek DNS外泄检测_detecting-exfiltration-over-dns-with-zeek/SKILL.md) |
| 30 | **Zeek横向移动检测** | `detecting-lateral-movement-with-zeek` | Detect lateral movement in network traffic using Zeek (formerly Bro) l… | [SKILL.md](skills/Zeek横向移动检测_detecting-lateral-movement-with-zeek/SKILL.md) |
| 31 | **Zeek流量监控部署** | `performing-network-traffic-analysis-with-zeek` | Deploy Zeek (formerly Bro) as a passive network security monitor to ge… | [SKILL.md](skills/Zeek流量监控部署_performing-network-traffic-analysis-with-zeek/SKILL.md) |
| 32 | **Zeek网络异常检测** | `detecting-network-anomalies-with-zeek` | Deploy and configure Zeek (formerly Bro) to passively analyze network… | [SKILL.md](skills/Zeek网络异常检测_detecting-network-anomalies-with-zeek/SKILL.md) |
| 33 | **aircrack WiFi密码破解** | `performing-wifi-password-cracking-with-aircrack` | Captures WPA/WPA2 handshakes and performs offline password cracking us… | [SKILL.md](skills/aircrack WiFi密码破解_performing-wifi-password-cracking-with-aircrack/SKILL.md) |
| 34 | **fail2ban端口扫描检测** | `detecting-port-scanning-with-fail2ban` | Configures Fail2ban with custom filters and actions to detect port sca… | [SKILL.md](skills/fail2ban端口扫描检测_detecting-port-scanning-with-fail2ban/SKILL.md) |
| 35 | **pfSense防火墙配置** | `configuring-pfsense-firewall-rules` | Configures pfSense firewall rules, NAT policies, IPsec/OpenVPN tunnels… | [SKILL.md](skills/pfSense防火墙配置_configuring-pfsense-firewall-rules/SKILL.md) |
| 36 | **tshark流量自动化分析** | `performing-network-traffic-analysis-with-tshark` | Automate network traffic analysis using tshark (Wireshark CLI) and pys… | [SKILL.md](skills/tshark流量自动化分析_performing-network-traffic-analysis-with-tshark/SKILL.md) |
| 37 | **中间人攻击模拟** | `conducting-man-in-the-middle-attack-simulation` | Simulates man-in-the-middle attacks using Ettercap, mitmproxy, and Bet… | [SKILL.md](skills/中间人攻击模拟_conducting-man-in-the-middle-attack-simulation/SKILL.md) |
| 38 | **带宽限制攻击模拟** | `performing-bandwidth-throttling-attack-simulation` | Simulate bandwidth throttling and network degradation attacks using tc… | [SKILL.md](skills/带宽限制攻击模拟_performing-bandwidth-throttling-attack-simulation/SKILL.md) |
| 39 | **数据包注入攻击** | `performing-packet-injection-attack` | Crafts and injects custom network packets using Scapy, hping3, and Nem… | [SKILL.md](skills/数据包注入攻击_performing-packet-injection-attack/SKILL.md) |
| 40 | **网络横向移动检测** | `detecting-lateral-movement-in-network` | Identifies lateral movement techniques in enterprise networks by analy… | [SKILL.md](skills/网络横向移动检测_detecting-lateral-movement-in-network/SKILL.md) |
| 41 | **网络流量基线建设** | `implementing-network-traffic-baselining` | Builds network traffic baselines from NetFlow/IPFIX CSV or JSON export… | [SKILL.md](skills/网络流量基线建设_implementing-network-traffic-baselining/SKILL.md) |
| 42 | **防火墙区域分段** | `implementing-network-segmentation-with-firewall-zones` | Designs and implements network segmentation using firewall security zo… | [SKILL.md](skills/防火墙区域分段_implementing-network-segmentation-with-firewall-zones/SKILL.md) |
| 43 | **零信任浏览器隔离** | `implementing-browser-isolation-for-zero-trust` | Deploys remote browser isolation (RBI) as a core component of a Zero T… | [SKILL.md](skills/零信任浏览器隔离_implementing-browser-isolation-for-zero-trust/SKILL.md) |

---

← 返回 [仓库首页](../README.md) · 索引见 [index.json](../index.json)
