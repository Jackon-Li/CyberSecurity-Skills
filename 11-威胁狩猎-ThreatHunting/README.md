# 11 · 威胁狩猎

[← 仓库首页](../README.md) · 分类 **11** · `ThreatHunting` · **58** 个技能 · 领域 **蓝队**

> 每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。
> 技能内容**转载自上游开源项目，非原创**，版权归原作者所有。详见[来源与版权](../README.md#来源与版权)与[使用边界](../SECURITY.md)。

| # | 技能 | 英文标识 | 摘要 | 入口 |
|---|---|---|---|---|
| 1 | **AD DCSync攻击检测** | `detecting-dcsync-attack-in-active-directory` | Detect DCSync attacks (MITRE T1003.006) where adversaries abuse Active… | [SKILL.md](skills/AD%20DCSync攻击检测_detecting-dcsync-attack-in-active-directory/SKILL.md) |
| 2 | **C2信标狩猎** | `hunting-for-command-and-control-beaconing` | Detect C2 beaconing patterns in network traffic using frequency analys… | [SKILL.md](skills/C2信标狩猎_hunting-for-command-and-control-beaconing/SKILL.md) |
| 3 | **Chainsaw事件日志狩猎** | `hunting-evtx-with-chainsaw` | Run Chainsaw against collected Windows EVTX files to hunt with the Sig… | [SKILL.md](skills/Chainsaw事件日志狩猎_hunting-evtx-with-chainsaw/SKILL.md) |
| 4 | **Cobalt Strike信标狩猎** | `hunting-for-cobalt-strike-beacons` | Detect Cobalt Strike beacon command-and-control traffic using default… | [SKILL.md](skills/Cobalt%20Strike信标狩猎_hunting-for-cobalt-strike-beacons/SKILL.md) |
| 5 | **DCOM横向移动狩猎** | `hunting-for-dcom-lateral-movement` | Hunt for DCOM-based lateral movement (MITRE ATT&CK T1021.003) by detec… | [SKILL.md](skills/DCOM横向移动狩猎_hunting-for-dcom-lateral-movement/SKILL.md) |
| 6 | **DCSync攻击狩猎** | `hunting-for-dcsync-attacks` | Detect DCSync attacks (MITRE ATT&CK T1003.006) by analyzing Windows Ev… | [SKILL.md](skills/DCSync攻击狩猎_hunting-for-dcsync-attacks/SKILL.md) |
| 7 | **DLL侧加载攻击检测** | `detecting-dll-sideloading-attacks` | Detect DLL side-loading and search-order hijacking (MITRE T1574) where… | [SKILL.md](skills/DLL侧加载攻击检测_detecting-dll-sideloading-attacks/SKILL.md) |
| 8 | **DNS持久化狩猎** | `hunting-for-dns-based-persistence` | Hunts for DNS-based persistence mechanisms such as DNS hijacking, dang… | [SKILL.md](skills/DNS持久化狩猎_hunting-for-dns-based-persistence/SKILL.md) |
| 9 | **EDR凭据转储检测** | `detecting-t1003-credential-dumping-with-edr` | Detect OS credential dumping (MITRE T1003) targeting LSASS memory, the… | [SKILL.md](skills/EDR凭据转储检测_detecting-t1003-credential-dumping-with-edr/SKILL.md) |
| 10 | **Kerberoasting攻击检测** | `detecting-kerberoasting-attacks` | Detect Kerberoasting attacks by monitoring for anomalous Kerberos TGS… | [SKILL.md](skills/Kerberoasting攻击检测_detecting-kerberoasting-attacks/SKILL.md) |
| 11 | **Kerberos黄金票据检测** | `detecting-golden-ticket-attacks-in-kerberos-logs` | Detect Golden Ticket attacks in Active Directory using Splunk and KQL… | [SKILL.md](skills/Kerberos黄金票据检测_detecting-golden-ticket-attacks-in-kerberos-logs/SKILL.md) |
| 12 | **LOLBins利用狩猎** | `hunting-for-living-off-the-land-binaries` | Proactively hunts for adversary abuse of legitimate, signed system bin… | [SKILL.md](skills/LOLBins利用狩猎_hunting-for-living-off-the-land-binaries/SKILL.md) |
| 13 | **Linux持久化机制分析** | `analyzing-persistence-mechanisms-in-linux` | Scan Linux systems for persistence mechanisms including crontab/system… | [SKILL.md](skills/Linux持久化机制分析_analyzing-persistence-mechanisms-in-linux/SKILL.md) |
| 14 | **Mimikatz执行模式检测** | `detecting-mimikatz-execution-patterns` | Detect Mimikatz credential-dumping activity via command-line pattern m… | [SKILL.md](skills/Mimikatz执行模式检测_detecting-mimikatz-execution-patterns/SKILL.md) |
| 15 | **NTLM中继事件关联检测** | `detecting-ntlm-relay-with-event-correlation` | Detect NTLM relay attacks (T1557.001) by correlating Windows Event 462… | [SKILL.md](skills/NTLM中继事件关联检测_detecting-ntlm-relay-with-event-correlation/SKILL.md) |
| 16 | **NTLM中继攻击狩猎** | `hunting-for-ntlm-relay-attacks` | Detects NTLM relay attacks (MITRE T1557.001) by analyzing Windows Even… | [SKILL.md](skills/NTLM中继攻击狩猎_hunting-for-ntlm-relay-attacks/SKILL.md) |
| 17 | **PowerShell Empire痕迹分析** | `analyzing-powershell-empire-artifacts` | Detect PowerShell Empire post-exploitation framework artifacts in Wind… | [SKILL.md](skills/PowerShell%20Empire痕迹分析_analyzing-powershell-empire-artifacts/SKILL.md) |
| 18 | **Splunk横向移动检测** | `detecting-lateral-movement-with-splunk` | Detect adversary lateral movement across networks using Splunk SPL que… | [SKILL.md](skills/Splunk横向移动检测_detecting-lateral-movement-with-splunk/SKILL.md) |
| 19 | **Sysmon计划任务检测** | `detecting-malicious-scheduled-tasks-with-sysmon` | Detect malicious scheduled task creation and modification using Sysmon… | [SKILL.md](skills/Sysmon计划任务检测_detecting-malicious-scheduled-tasks-with-sysmon/SKILL.md) |
| 20 | **Sysmon进程注入检测** | `detecting-t1055-process-injection-with-sysmon` | Detect process injection techniques (T1055) - including DLL injection,… | [SKILL.md](skills/Sysmon进程注入检测_detecting-t1055-process-injection-with-sysmon/SKILL.md) |
| 21 | **Velociraptor集群狩猎** | `fleet-hunting-with-velociraptor` | Deploy a Velociraptor server and agents, then author VQL (Velociraptor… | [SKILL.md](skills/Velociraptor集群狩猎_fleet-hunting-with-velociraptor/SKILL.md) |
| 22 | **WMI持久化检测** | `detecting-wmi-persistence` | Detect WMI event subscription persistence (MITRE T1546.003) by analyzi… | [SKILL.md](skills/WMI持久化检测_detecting-wmi-persistence/SKILL.md) |
| 23 | **WMI横向移动狩猎** | `hunting-for-lateral-movement-via-wmi` | Detects WMI-based lateral movement (e.g. | [SKILL.md](skills/WMI横向移动狩猎_hunting-for-lateral-movement-via-wmi/SKILL.md) |
| 24 | **WMI订阅持久化狩猎** | `hunting-for-persistence-via-wmi-subscriptions` | Hunts for adversary persistence via WMI event subscriptions (MITRE T15… | [SKILL.md](skills/WMI订阅持久化狩猎_hunting-for-persistence-via-wmi-subscriptions/SKILL.md) |
| 25 | **Webshell活动狩猎** | `hunting-for-webshell-activity` | Runs a hypothesis-driven threat hunt for web shell deployment (T1505.0… | [SKILL.md](skills/Webshell活动狩猎_hunting-for-webshell-activity/SKILL.md) |
| 26 | **Windows持久化机制狩猎** | `hunting-for-persistence-mechanisms-in-windows` | Systematically hunts for adversary persistence mechanisms across Windo… | [SKILL.md](skills/Windows持久化机制狩猎_hunting-for-persistence-mechanisms-in-windows/SKILL.md) |
| 27 | **YARA规则威胁狩猎** | `performing-threat-hunting-with-yara-rules` | Use YARA pattern-matching rules to hunt for malware, suspicious files,… | [SKILL.md](skills/YARA规则威胁狩猎_performing-threat-hunting-with-yara-rules/SKILL.md) |
| 28 | **Zeek DNS隧道狩猎** | `hunting-for-dns-tunneling-with-zeek` | Detects DNS tunneling and covert-channel data exfiltration by analyzin… | [SKILL.md](skills/Zeek%20DNS隧道狩猎_hunting-for-dns-tunneling-with-zeek/SKILL.md) |
| 29 | **云服务滥用狩猎** | `hunting-for-living-off-the-cloud-techniques` | Hunts for adversary abuse of legitimate cloud services (Azure, AWS, GC… | [SKILL.md](skills/云服务滥用狩猎_hunting-for-living-off-the-cloud-techniques/SKILL.md) |
| 30 | **供应链失陷狩猎** | `hunting-for-supply-chain-compromise` | Runs a hypothesis-driven threat hunt for supply-chain compromise (T119… | [SKILL.md](skills/供应链失陷狩猎_hunting-for-supply-chain-compromise/SKILL.md) |
| 31 | **信标频率分析狩猎** | `hunting-for-beaconing-with-frequency-analysis` | Identify command-and-control beaconing patterns in network traffic by… | [SKILL.md](skills/信标频率分析狩猎_hunting-for-beaconing-with-frequency-analysis/SKILL.md) |
| 32 | **内部威胁行为检测** | `detecting-insider-threat-behaviors` | Detect insider threat behavioral indicators including unusual data acc… | [SKILL.md](skills/内部威胁行为检测_detecting-insider-threat-behaviors/SKILL.md) |
| 33 | **勒索网络指标分析** | `analyzing-ransomware-network-indicators` | Identify ransomware-related network indicators, including C2 beaconing… | [SKILL.md](skills/勒索网络指标分析_analyzing-ransomware-network-indicators/SKILL.md) |
| 34 | **卷影副本删除狩猎** | `hunting-for-shadow-copy-deletion` | Runs a hypothesis-driven threat hunt for Volume Shadow Copy deletion (… | [SKILL.md](skills/卷影副本删除狩猎_hunting-for-shadow-copy-deletion/SKILL.md) |
| 35 | **可疑PowerShell执行检测** | `detecting-suspicious-powershell-execution` | Hunt for suspicious PowerShell execution (T1059.001) such as encoded c… | [SKILL.md](skills/可疑PowerShell执行检测_detecting-suspicious-powershell-execution/SKILL.md) |
| 36 | **可疑计划任务狩猎** | `hunting-for-suspicious-scheduled-tasks` | Hunts for adversary persistence and execution via Windows scheduled ta… | [SKILL.md](skills/可疑计划任务狩猎_hunting-for-suspicious-scheduled-tasks/SKILL.md) |
| 37 | **启动文件夹持久化狩猎** | `hunting-for-startup-folder-persistence` | Detects T1547.001 startup folder persistence by monitoring Windows sta… | [SKILL.md](skills/启动文件夹持久化狩猎_hunting-for-startup-folder-persistence/SKILL.md) |
| 38 | **哈希传递攻击检测** | `detecting-pass-the-hash-attacks` | Detect Pass-the-Hash (T1550.002) attacks by analyzing NTLM authenticat… | [SKILL.md](skills/哈希传递攻击检测_detecting-pass-the-hash-attacks/SKILL.md) |
| 39 | **域前置C2流量狩猎** | `hunting-for-domain-fronting-c2-traffic` | Detects domain fronting C2 traffic by analyzing SNI-vs-HTTP-Host-heade… | [SKILL.md](skills/域前置C2流量狩猎_hunting-for-domain-fronting-c2-traffic/SKILL.md) |
| 40 | **外泄前数据暂存狩猎** | `hunting-for-data-staging-before-exfiltration` | Detect data-staging activity (MITRE ATT&CK T1074) by analyzing EDR/Sys… | [SKILL.md](skills/外泄前数据暂存狩猎_hunting-for-data-staging-before-exfiltration/SKILL.md) |
| 41 | **威胁狩猎假设框架** | `building-threat-hunt-hypothesis-framework` | Build a systematic threat-hunt workflow that turns threat intelligence… | [SKILL.md](skills/威胁狩猎假设框架_building-threat-hunt-hypothesis-framework/SKILL.md) |
| 42 | **异常PowerShell狩猎** | `hunting-for-anomalous-powershell-execution` | Hunt for malicious PowerShell activity by analyzing Script Block Loggi… | [SKILL.md](skills/异常PowerShell狩猎_hunting-for-anomalous-powershell-execution/SKILL.md) |
| 43 | **异常服务安装狩猎** | `hunting-for-unusual-service-installations` | Detects suspicious Windows service installations (MITRE ATT&CK T1543.0… | [SKILL.md](skills/异常服务安装狩猎_hunting-for-unusual-service-installations/SKILL.md) |
| 44 | **异常网络连接狩猎** | `hunting-for-unusual-network-connections` | Runs a hypothesis-driven threat hunt for command-and-control activity… | [SKILL.md](skills/异常网络连接狩猎_hunting-for-unusual-network-connections/SKILL.md) |
| 45 | **提权机制滥用检测** | `detecting-t1548-abuse-elevation-control-mechanism` | Detect abuse of elevation control mechanisms (T1548), including Window… | [SKILL.md](skills/提权机制滥用检测_detecting-t1548-abuse-elevation-control-mechanism/SKILL.md) |
| 46 | **数据外泄指标狩猎** | `hunting-for-data-exfiltration-indicators` | Hunt for data exfiltration by analyzing Zeek and Suricata network tele… | [SKILL.md](skills/数据外泄指标狩猎_hunting-for-data-exfiltration-indicators/SKILL.md) |
| 47 | **时间戳篡改规避狩猎** | `hunting-for-defense-evasion-via-timestomping` | Detect NTFS timestamp manipulation (MITRE T1070.006) by comparing $STA… | [SKILL.md](skills/时间戳篡改规避狩猎_hunting-for-defense-evasion-via-timestomping/SKILL.md) |
| 48 | **服务账户滥用检测** | `detecting-service-account-abuse` | Detect abuse of service accounts by hunting for anomalous interactive… | [SKILL.md](skills/服务账户滥用检测_detecting-service-account-abuse/SKILL.md) |
| 49 | **权限提升尝试检测** | `detecting-privilege-escalation-attempts` | Detect privilege escalation attempts across Windows and Linux, includi… | [SKILL.md](skills/权限提升尝试检测_detecting-privilege-escalation-attempts/SKILL.md) |
| 50 | **注册表Run键持久化狩猎** | `hunting-for-registry-run-key-persistence` | Detect MITRE ATT&CK T1547.001 registry Run key persistence by analyzin… | [SKILL.md](skills/注册表Run键持久化狩猎_hunting-for-registry-run-key-persistence/SKILL.md) |
| 51 | **注册表持久化狩猎** | `hunting-for-registry-persistence-mechanisms` | Hunts for registry-based persistence mechanisms (MITRE T1547) in Windo… | [SKILL.md](skills/注册表持久化狩猎_hunting-for-registry-persistence-mechanisms/SKILL.md) |
| 52 | **端点LOLBins执行狩猎** | `hunting-for-lolbins-execution-in-endpoint-logs` | Hunts for LOLBins (Living Off the Land Binaries) abuse, mapped to MITR… | [SKILL.md](skills/端点LOLBins执行狩猎_hunting-for-lolbins-execution-in-endpoint-logs/SKILL.md) |
| 53 | **计划任务持久化狩猎** | `hunting-for-scheduled-task-persistence` | Runs a hypothesis-driven threat hunt for Windows Scheduled Task persis… | [SKILL.md](skills/计划任务持久化狩猎_hunting-for-scheduled-task-persistence/SKILL.md) |
| 54 | **账户操纵T1098狩猎** | `hunting-for-t1098-account-manipulation` | Hunts for MITRE ATT&CK T1098 account manipulation - shadow admin creat… | [SKILL.md](skills/账户操纵T1098狩猎_hunting-for-t1098-account-manipulation/SKILL.md) |
| 55 | **进程注入技术狩猎** | `hunting-for-process-injection-techniques` | Detects process injection techniques (MITRE T1055) — including CreateR… | [SKILL.md](skills/进程注入技术狩猎_hunting-for-process-injection-techniques/SKILL.md) |
| 56 | **进程镂空技术检测** | `detecting-process-hollowing-technique` | Detect process hollowing (MITRE T1055.012) by analyzing memory-mapped… | [SKILL.md](skills/进程镂空技术检测_detecting-process-hollowing-technique/SKILL.md) |
| 57 | **邮件转发规则攻击检测** | `detecting-email-forwarding-rules-attack` | Detect malicious inbox/mail-flow forwarding rules that adversaries cre… | [SKILL.md](skills/邮件转发规则攻击检测_detecting-email-forwarding-rules-attack/SKILL.md) |
| 58 | **鱼叉钓鱼指标狩猎** | `hunting-for-spearphishing-indicators` | Hunt for spearphishing campaign indicators across email logs, endpoint… | [SKILL.md](skills/鱼叉钓鱼指标狩猎_hunting-for-spearphishing-indicators/SKILL.md) |

---

<sub>本页由脚本生成 · 技能内容转载自上游项目，非原创 · [返回首页](../README.md) · [索引](../index.json) · [使用边界](../SECURITY.md)</sub>
