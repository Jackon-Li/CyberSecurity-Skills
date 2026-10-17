# 15-数字取证 · DigitalForensics

> 本分类共 **41** 个技能（取证 41）。

每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。

| # | 技能 | 英文标识 | 摘要 | 路径 |
|---|---|---|---|---|
| 1 | **Amcache痕迹分析** | `analyzing-windows-amcache-artifacts` | Parses the Windows Amcache.hve registry hive with Eric Zimmerman''s Am… | [SKILL.md](skills/Amcache痕迹分析_analyzing-windows-amcache-artifacts/SKILL.md) |
| 2 | **Autopsy磁盘镜像分析** | `analyzing-disk-image-with-autopsy` | Perform comprehensive forensic analysis of raw (dd), E01, or AFF disk… | [SKILL.md](skills/Autopsy磁盘镜像分析_analyzing-disk-image-with-autopsy/SKILL.md) |
| 3 | **Cellebrite移动设备取证** | `performing-mobile-device-forensics-with-cellebrite` | Acquire and analyze mobile device data using Cellebrite UFED Touch/4PC… | [SKILL.md](skills/Cellebrite移动设备取证_performing-mobile-device-forensics-with-cellebrite/SKILL.md) |
| 4 | **Docker容器取证** | `analyzing-docker-container-forensics` | Investigate compromised Docker containers by analyzing images, layers,… | [SKILL.md](skills/Docker容器取证_analyzing-docker-container-forensics/SKILL.md) |
| 5 | **Foremost文件雕刻** | `performing-file-carving-with-foremost` | Recovers files from disk images and unallocated space using Foremost's… | [SKILL.md](skills/Foremost文件雕刻_performing-file-carving-with-foremost/SKILL.md) |
| 6 | **Hayabusa取证时间线** | `generating-forensic-timelines-with-hayabusa` | Run Hayabusa against collected Windows EVTX files to apply Sigma detec… | [SKILL.md](skills/Hayabusa取证时间线_generating-forensic-timelines-with-hayabusa/SKILL.md) |
| 7 | **Hindsight浏览器取证** | `analyzing-browser-forensics-with-hindsight` | Parse Chromium-based browser databases with Hindsight to extract and c… | [SKILL.md](skills/Hindsight浏览器取证_analyzing-browser-forensics-with-hindsight/SKILL.md) |
| 8 | **KAPE Windows证据提取** | `triaging-windows-with-kape` | Runs KAPE (Kroll Artifact Parser and Extractor) to collect targeted fo… | [SKILL.md](skills/KAPE Windows证据提取_triaging-windows-with-kape/SKILL.md) |
| 9 | **LNK与JumpList取证分析** | `analyzing-lnk-file-and-jump-list-artifacts` | Analyze Windows LNK shortcut files and Jump List artifacts with LECmd,… | [SKILL.md](skills/LNK与JumpList取证分析_analyzing-lnk-file-and-jump-list-artifacts/SKILL.md) |
| 10 | **Linux内核Rootkit分析** | `analyzing-linux-kernel-rootkits` | Detect kernel-level rootkits in Linux memory dumps using Volatility3 l… | [SKILL.md](skills/Linux内核Rootkit分析_analyzing-linux-kernel-rootkits/SKILL.md) |
| 11 | **Linux日志取证调查** | `performing-linux-log-forensics-investigation` | Perform forensic investigation of Linux system logs including syslog,… | [SKILL.md](skills/Linux日志取证调查_performing-linux-log-forensics-investigation/SKILL.md) |
| 12 | **Linux系统痕迹分析** | `analyzing-linux-system-artifacts` | Examine Linux system artifacts (auth logs, cron/systemd persistence, s… | [SKILL.md](skills/Linux系统痕迹分析_analyzing-linux-system-artifacts/SKILL.md) |
| 13 | **MFT删除文件恢复** | `analyzing-mft-for-deleted-file-recovery` | Analyze the NTFS Master File Table ($MFT) with MFTECmd, analyzeMFT, an… | [SKILL.md](skills/MFT删除文件恢复_analyzing-mft-for-deleted-file-recovery/SKILL.md) |
| 14 | **Outlook PST邮件取证** | `analyzing-outlook-pst-for-email-forensics` | Parse Microsoft Outlook PST and OST files using libpff and pst-utils t… | [SKILL.md](skills/Outlook PST邮件取证_analyzing-outlook-pst-for-email-forensics/SKILL.md) |
| 15 | **PhotoRec删除文件恢复** | `recovering-deleted-files-with-photorec` | Recovers deleted files from disk images and storage media using PhotoR… | [SKILL.md](skills/PhotoRec删除文件恢复_recovering-deleted-files-with-photorec/SKILL.md) |
| 16 | **Plaso时间线重建** | `performing-timeline-reconstruction-with-plaso` | Builds comprehensive forensic super-timelines using Plaso (log2timelin… | [SKILL.md](skills/Plaso时间线重建_performing-timeline-reconstruction-with-plaso/SKILL.md) |
| 17 | **Plaso超级时间线构建** | `building-super-timelines-with-plaso` | Generate forensic super-timelines with Plaso's log2timeline.py, pinfo.… | [SKILL.md](skills/Plaso超级时间线构建_building-super-timelines-with-plaso/SKILL.md) |
| 18 | **Prefetch执行历史分析** | `analyzing-prefetch-files-for-execution-history` | Parse Windows Prefetch files (versions 17, 23, 26, 30) with tools like… | [SKILL.md](skills/Prefetch执行历史分析_analyzing-prefetch-files-for-execution-history/SKILL.md) |
| 19 | **Python解析Prefetch** | `analyzing-windows-prefetch-with-python` | Parse Windows Prefetch (.pf) files with the windowsprefetch Python lib… | [SKILL.md](skills/Python解析Prefetch_analyzing-windows-prefetch-with-python/SKILL.md) |
| 20 | **SQLite数据库取证** | `performing-sqlite-database-forensics` | Performs forensic analysis of SQLite databases by examining B-tree pag… | [SKILL.md](skills/SQLite数据库取证_performing-sqlite-database-forensics/SKILL.md) |
| 21 | **Shellbag痕迹分析** | `analyzing-windows-shellbag-artifacts` | Analyze Windows Shellbag (BagMRU) registry artifacts with SBECmd and S… | [SKILL.md](skills/Shellbag痕迹分析_analyzing-windows-shellbag-artifacts/SKILL.md) |
| 22 | **Slack空间文件系统取证** | `analyzing-slack-space-and-file-system-artifacts` | Examine NTFS slack space, MFT entries, the USN Change Journal, and Alt… | [SKILL.md](skills/Slack空间文件系统取证_analyzing-slack-space-and-file-system-artifacts/SKILL.md) |
| 23 | **USB设备连接历史分析** | `analyzing-usb-device-connection-history` | Correlate Windows registry keys (USBSTOR, MountedDevices), Event Logs,… | [SKILL.md](skills/USB设备连接历史分析_analyzing-usb-device-connection-history/SKILL.md) |
| 24 | **Volatility3内存取证** | `performing-memory-forensics-with-volatility3` | Analyze volatile memory (RAM) dumps using the Volatility 3 framework t… | [SKILL.md](skills/Volatility3内存取证_performing-memory-forensics-with-volatility3/SKILL.md) |
| 25 | **Windows LNK痕迹分析** | `analyzing-windows-lnk-files-for-artifacts` | Parse Windows LNK shortcut files to extract target paths, MAC timestam… | [SKILL.md](skills/Windows LNK痕迹分析_analyzing-windows-lnk-files-for-artifacts/SKILL.md) |
| 26 | **Windows事件日志提取** | `extracting-windows-event-logs-artifacts` | Extract, parse, and analyze Windows Event Logs (EVTX) using Chainsaw,… | [SKILL.md](skills/Windows事件日志提取_extracting-windows-event-logs-artifacts/SKILL.md) |
| 27 | **Windows注册表取证** | `analyzing-windows-registry-for-artifacts` | Extract and analyze Windows Registry hives with tools like RegRipper a… | [SKILL.md](skills/Windows注册表取证_analyzing-windows-registry-for-artifacts/SKILL.md) |
| 28 | **Wireshark网络取证** | `performing-network-forensics-with-wireshark` | Capture and analyze network traffic using Wireshark and tshark to reco… | [SKILL.md](skills/Wireshark网络取证_performing-network-forensics-with-wireshark/SKILL.md) |
| 29 | **Zimmerman工具Windows取证** | `performing-windows-artifact-analysis-with-eric-zimmerman-tools` | Performs comprehensive Windows forensic artifact analysis using Eric Z… | [SKILL.md](skills/Zimmerman工具Windows取证_performing-windows-artifact-analysis-with-eric-zimmerman-tools/SKILL.md) |
| 30 | **Zimmerman工具痕迹解析** | `parsing-artifacts-with-eric-zimmerman-tools` | Parse Windows forensic artifacts—$MFT/$J (MFTECmd), Prefetch (PECmd),… | [SKILL.md](skills/Zimmerman工具痕迹解析_parsing-artifacts-with-eric-zimmerman-tools/SKILL.md) |
| 31 | **dd与dcfldd磁盘取证镜像** | `acquiring-disk-image-with-dd-and-dcfldd` | Create forensically sound bit-for-bit disk images with dd or dcfldd on… | [SKILL.md](skills/dd与dcfldd磁盘取证镜像_acquiring-disk-image-with-dd-and-dcfldd/SKILL.md) |
| 32 | **云存储取证获取** | `performing-cloud-storage-forensic-acquisition` | Perform forensic acquisition of cloud storage services including Googl… | [SKILL.md](skills/云存储取证获取_performing-cloud-storage-forensic-acquisition/SKILL.md) |
| 33 | **云环境取证调查** | `performing-cloud-forensics-investigation` | Collect and analyze cloud forensic evidence using AWS CLI, Azure CLI,… | [SKILL.md](skills/云环境取证调查_performing-cloud-forensics-investigation/SKILL.md) |
| 34 | **内存转储凭据提取** | `extracting-credentials-from-memory-dump` | Extracts cached credentials, password hashes, Kerberos tickets, and au… | [SKILL.md](skills/内存转储凭据提取_extracting-credentials-from-memory-dump/SKILL.md) |
| 35 | **勒索攻击痕迹调查** | `investigating-ransomware-attack-artifacts` | Forensically preserve memory and disk, collect ransom notes and encryp… | [SKILL.md](skills/勒索攻击痕迹调查_investigating-ransomware-attack-artifacts/SKILL.md) |
| 36 | **取证日志分析** | `performing-log-analysis-for-forensic-investigation` | Collect, parse, and correlate system, application, and security logs t… | [SKILL.md](skills/取证日志分析_performing-log-analysis-for-forensic-investigation/SKILL.md) |
| 37 | **恶意软件持久化调查** | `performing-malware-persistence-investigation` | Systematically investigate all persistence mechanisms on Windows and L… | [SKILL.md](skills/恶意软件持久化调查_performing-malware-persistence-investigation/SKILL.md) |
| 38 | **浏览器历史痕迹提取** | `extracting-browser-history-artifacts` | Extracts and analyzes browser history, cookies, cache, downloads, and… | [SKILL.md](skills/浏览器历史痕迹提取_extracting-browser-history-artifacts/SKILL.md) |
| 39 | **网络抓包取证分析** | `performing-network-packet-capture-analysis` | Perform forensic analysis of network packet captures (PCAP/PCAPNG) usi… | [SKILL.md](skills/网络抓包取证分析_performing-network-packet-capture-analysis/SKILL.md) |
| 40 | **钓鱼邮件头分析** | `analyzing-email-headers-for-phishing-investigation` | Parse and analyze email headers (Received chain, Return-Path, Message-… | [SKILL.md](skills/钓鱼邮件头分析_analyzing-email-headers-for-phishing-investigation/SKILL.md) |
| 41 | **隐写术检测** | `performing-steganography-detection` | Detects and extracts hidden data embedded in images, audio, and other… | [SKILL.md](skills/隐写术检测_performing-steganography-detection/SKILL.md) |

---

← 返回 [仓库首页](../README.md) · 索引见 [index.json](../index.json)
