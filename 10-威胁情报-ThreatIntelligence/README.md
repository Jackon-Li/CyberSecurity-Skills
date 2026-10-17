# 10 · 威胁情报

[← 仓库首页](../README.md) · 分类 **10** · `ThreatIntelligence` · **52** 个技能 · 领域 **蓝队**

> 每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。
> 技能内容**转载自上游开源项目，非原创**，版权归原作者所有。详见[来源与版权](../README.md#来源与版权)与[使用边界](../SECURITY.md)。

| # | 技能 | 英文标识 | 摘要 | 入口 |
|---|---|---|---|---|
| 1 | **AI驱动OSINT关联** | `performing-ai-driven-osint-correlation` | Use AI/LLM-based reasoning with Sherlock, theHarvester, and SpiderFoot… | [SKILL.md](skills/AI驱动OSINT关联_performing-ai-driven-osint-correlation/SKILL.md) |
| 2 | **APT主动威胁狩猎** | `hunting-advanced-persistent-threats` | Proactively hunts for Advanced Persistent Threat (APT) activity within… | [SKILL.md](skills/APT主动威胁狩猎_hunting-advanced-persistent-threats/SKILL.md) |
| 3 | **APT组织ATT&CK分析** | `analyzing-apt-group-with-mitre-navigator` | Query ATT&CK data with attackcti, mitreattack-python, and stix2, then… | [SKILL.md](skills/APT组织ATT&CK分析_analyzing-apt-group-with-mitre-navigator/SKILL.md) |
| 4 | **APT组织TTP可视化** | `analyzing-threat-actor-ttps-with-mitre-navigator` | Map advanced persistent threat (APT) group TTPs to the MITRE ATT&CK fr… | [SKILL.md](skills/APT组织TTP可视化_analyzing-threat-actor-ttps-with-mitre-navigator/SKILL.md) |
| 5 | **ATT&CK技术映射** | `mapping-mitre-attack-techniques` | Maps observed adversary behaviors, security alerts, and detection rule… | [SKILL.md](skills/ATT&CK技术映射_mapping-mitre-attack-techniques/SKILL.md) |
| 6 | **Atomic Red Team威胁模拟** | `performing-threat-emulation-with-atomic-red-team` | Executes Atomic Red Team tests for MITRE ATT&CK technique validation u… | [SKILL.md](skills/Atomic%20Red%20Team威胁模拟_performing-threat-emulation-with-atomic-red-team/SKILL.md) |
| 7 | **CTI报告攻击模式库** | `building-attack-pattern-library-from-cti-reports` | Parse cyber threat intelligence reports (Mandiant, CrowdStrike, Talos,… | [SKILL.md](skills/CTI报告攻击模式库_building-attack-pattern-library-from-cti-reports/SKILL.md) |
| 8 | **IOC去活性化共享管道** | `building-ioc-defanging-and-sharing-pipeline` | Build an automated pipeline that ingests raw IOCs (URLs, IPs, domains,… | [SKILL.md](skills/IOC去活性化共享管道_building-ioc-defanging-and-sharing-pipeline/SKILL.md) |
| 9 | **IOC自动化富化** | `automating-ioc-enrichment` | Automates the enrichment of raw indicators of compromise with multi-so… | [SKILL.md](skills/IOC自动化富化_automating-ioc-enrichment/SKILL.md) |
| 10 | **MISP威胁态势分析** | `analyzing-threat-landscape-with-misp` | Query a MISP (Malware Information Sharing Platform) instance via PyMIS… | [SKILL.md](skills/MISP威胁态势分析_analyzing-threat-landscape-with-misp/SKILL.md) |
| 11 | **MISP威胁情报收集** | `collecting-threat-intelligence-with-misp` | Deploy MISP, configure threat feeds (MISP community, freetext, TAXII,… | [SKILL.md](skills/MISP威胁情报收集_collecting-threat-intelligence-with-misp/SKILL.md) |
| 12 | **MISP威胁源聚合** | `building-threat-feed-aggregation-with-misp` | Deploy MISP via Docker and configure feeds from sources like abuse.ch,… | [SKILL.md](skills/MISP威胁源聚合_building-threat-feed-aggregation-with-misp/SKILL.md) |
| 13 | **MISP威胁源运营** | `operationalizing-misp-threat-feeds` | Stand up MISP, enable and cache curated threat feeds (CIRCL, abuse.ch,… | [SKILL.md](skills/MISP威胁源运营_operationalizing-misp-threat-feeds/SKILL.md) |
| 14 | **MISP情报共享** | `performing-threat-intelligence-sharing-with-misp` | Uses PyMISP (the official MISP REST API library) to create events with… | [SKILL.md](skills/MISP情报共享_performing-threat-intelligence-sharing-with-misp/SKILL.md) |
| 15 | **Malpedia恶意家族分析** | `analyzing-malware-family-relationships-with-malpedia` | Query the Malpedia API to look up malware family aliases and naming (p… | [SKILL.md](skills/Malpedia恶意家族分析_analyzing-malware-family-relationships-with-malpedia/SKILL.md) |
| 16 | **OSINT威胁画像构建** | `building-threat-actor-profile-from-osint` | Build threat actor profiles by collecting OSINT from vendor reports, p… | [SKILL.md](skills/OSINT威胁画像构建_building-threat-actor-profile-from-osint/SKILL.md) |
| 17 | **OpenCTI IOC富化管道** | `building-ioc-enrichment-pipeline-with-opencti` | Build an automated IOC enrichment pipeline on OpenCTI (STIX 2.1 native… | [SKILL.md](skills/OpenCTI%20IOC富化管道_building-ioc-enrichment-pipeline-with-opencti/SKILL.md) |
| 18 | **OpenCTI威胁建模** | `modeling-threats-with-opencti` | Deploy OpenCTI (Filigran) via Docker Compose and use the pycti Python… | [SKILL.md](skills/OpenCTI威胁建模_modeling-threats-with-opencti/SKILL.md) |
| 19 | **OpenTAXII服务部署** | `implementing-taxii-server-with-opentaxii` | Deploy and configure a TAXII 2.1 server (Medallion) with Docker, publi… | [SKILL.md](skills/OpenTAXII服务部署_implementing-taxii-server-with-opentaxii/SKILL.md) |
| 20 | **STIX-TAXII源处理** | `processing-stix-taxii-feeds` | Processes STIX 2.1 threat intelligence bundles delivered via TAXII 2.1… | [SKILL.md](skills/STIX-TAXII源处理_processing-stix-taxii-feeds/SKILL.md) |
| 21 | **STIX-TAXII源集成** | `implementing-stix-taxii-feed-integration` | Implements a STIX 2.1/TAXII 2.1 threat-intelligence feed consumer and… | [SKILL.md](skills/STIX-TAXII源集成_implementing-stix-taxii-feed-integration/SKILL.md) |
| 22 | **STIX2情报共享实施** | `implementing-security-information-sharing-with-stix2` | Create, validate, and share STIX 2.1 threat intelligence objects (indi… | [SKILL.md](skills/STIX2情报共享实施_implementing-security-information-sharing-with-stix2/SKILL.md) |
| 23 | **Shodan IP信誉分析** | `performing-ip-reputation-analysis-with-shodan` | Analyze IP address reputation using the Shodan API to identify open po… | [SKILL.md](skills/Shodan%20IP信誉分析_performing-ip-reputation-analysis-with-shodan/SKILL.md) |
| 24 | **SpiderFoot OSINT收集** | `performing-osint-with-spiderfoot` | Automate OSINT collection with the SpiderFoot REST API and CLI (sf.py/… | [SKILL.md](skills/SpiderFoot%20OSINT收集_performing-osint-with-spiderfoot/SKILL.md) |
| 25 | **VirusTotal哈希富化** | `performing-malware-hash-enrichment-with-virustotal` | Enrich malware file hashes (MD5, SHA-1, SHA-256) using the VirusTotal… | [SKILL.md](skills/VirusTotal哈希富化_performing-malware-hash-enrichment-with-virustotal/SKILL.md) |
| 26 | **dnstwist仿冒域名分析** | `analyzing-typosquatting-domains-with-dnstwist` | Generate domain permutations with dnstwist and check DNS resolution to… | [SKILL.md](skills/dnstwist仿冒域名分析_analyzing-typosquatting-domains-with-dnstwist/SKILL.md) |
| 27 | **勒索数据泄露站点情报** | `analyzing-ransomware-leak-site-intelligence` | Safely monitor ransomware group Tor-hosted data leak sites (DLS) to co… | [SKILL.md](skills/勒索数据泄露站点情报_analyzing-ransomware-leak-site-intelligence/SKILL.md) |
| 28 | **品牌仿冒监控** | `performing-brand-monitoring-for-impersonation` | Monitor for brand impersonation attacks across domains, social media,… | [SKILL.md](skills/品牌仿冒监控_performing-brand-monitoring-for-impersonation/SKILL.md) |
| 29 | **失陷指标IOC分析** | `analyzing-indicators-of-compromise` | Analyzes indicators of compromise (IOCs) including IP addresses, domai… | [SKILL.md](skills/失陷指标IOC分析_analyzing-indicators-of-compromise/SKILL.md) |
| 30 | **失陷指标生命周期管理** | `performing-indicator-lifecycle-management` | Tracks IOCs through discovery, enrichment/validation (VirusTotal, Shod… | [SKILL.md](skills/失陷指标生命周期管理_performing-indicator-lifecycle-management/SKILL.md) |
| 31 | **威胁基础设施追踪** | `tracking-threat-actor-infrastructure` | Discovers and maps adversary-controlled infrastructure (C2 servers, ph… | [SKILL.md](skills/威胁基础设施追踪_tracking-threat-actor-infrastructure/SKILL.md) |
| 32 | **威胁情报平台建设** | `building-threat-intelligence-platform` | Design and deploy a Threat Intelligence Platform (TIP) by integrating… | [SKILL.md](skills/威胁情报平台建设_building-threat-intelligence-platform/SKILL.md) |
| 33 | **威胁情报平台评估** | `evaluating-threat-intelligence-platforms` | Evaluates and selects Threat Intelligence Platform (TIP) products base… | [SKILL.md](skills/威胁情报平台评估_evaluating-threat-intelligence-platforms/SKILL.md) |
| 34 | **威胁情报报告生成** | `generating-threat-intelligence-reports` | Generates structured cyber threat intelligence reports at strategic, o… | [SKILL.md](skills/威胁情报报告生成_generating-threat-intelligence-reports/SKILL.md) |
| 35 | **威胁情报源分析** | `analyzing-threat-intelligence-feeds` | Analyzes structured and unstructured threat intelligence feeds to extr… | [SKILL.md](skills/威胁情报源分析_analyzing-threat-intelligence-feeds/SKILL.md) |
| 36 | **威胁情报生命周期管理** | `implementing-threat-intelligence-lifecycle-management` | Build out a full CTI program around the six-phase threat intelligence… | [SKILL.md](skills/威胁情报生命周期管理_implementing-threat-intelligence-lifecycle-management/SKILL.md) |
| 37 | **威胁活动关联分析** | `correlating-threat-campaigns` | Correlates disparate security incidents, IOCs, and adversary behaviors… | [SKILL.md](skills/威胁活动关联分析_correlating-threat-campaigns/SKILL.md) |
| 38 | **威胁行为者TTP映射** | `analyzing-threat-actor-ttps-with-mitre-attack` | Systematically map threat actor behavior and observed IOCs to the MITR… | [SKILL.md](skills/威胁行为者TTP映射_analyzing-threat-actor-ttps-with-mitre-attack/SKILL.md) |
| 39 | **威胁行为者画像** | `profiling-threat-actor-groups` | Develops comprehensive threat actor profiles for APT groups, criminal… | [SKILL.md](skills/威胁行为者画像_profiling-threat-actor-groups/SKILL.md) |
| 40 | **开源情报OSINT收集** | `collecting-open-source-intelligence` | Collects and synthesizes open-source intelligence (OSINT) about threat… | [SKILL.md](skills/开源情报OSINT收集_collecting-open-source-intelligence/SKILL.md) |
| 41 | **恶意软件IOC提取** | `performing-malware-ioc-extraction` | Malware IOC extraction is the process of analyzing malicious software… | [SKILL.md](skills/恶意软件IOC提取_performing-malware-ioc-extraction/SKILL.md) |
| 42 | **情报生命周期管理** | `managing-intelligence-lifecycle` | Manages the end-to-end cyber threat intelligence lifecycle from planni… | [SKILL.md](skills/情报生命周期管理_managing-intelligence-lifecycle/SKILL.md) |
| 43 | **攻击活动归因分析** | `analyzing-campaign-attribution-evidence` | Systematically evaluate cyber-campaign evidence to attribute an operat… | [SKILL.md](skills/攻击活动归因分析_analyzing-campaign-attribution-evidence/SKILL.md) |
| 44 | **敌手基础设施追踪** | `building-adversary-infrastructure-tracking-system` | Build an automated adversary infrastructure tracking system in Python… | [SKILL.md](skills/敌手基础设施追踪_building-adversary-infrastructure-tracking-system/SKILL.md) |
| 45 | **暗网威胁监控** | `performing-dark-web-monitoring-for-threats` | Dark web monitoring involves systematically scanning Tor hidden servic… | [SKILL.md](skills/暗网威胁监控_performing-dark-web-monitoring-for-threats/SKILL.md) |
| 46 | **暗网情报监控** | `monitoring-darkweb-sources` | Monitors dark web forums, marketplaces, paste sites, and ransomware le… | [SKILL.md](skills/暗网情报监控_monitoring-darkweb-sources/SKILL.md) |
| 47 | **粘贴站点凭据监控** | `performing-paste-site-monitoring-for-credentials` | Monitor paste sites like Pastebin and GitHub Gists for leaked credenti… | [SKILL.md](skills/粘贴站点凭据监控_performing-paste-site-monitoring-for-credentials/SKILL.md) |
| 48 | **网络杀伤链分析** | `analyzing-cyber-kill-chain` | Analyzes intrusion activity against the Lockheed Martin Cyber Kill Cha… | [SKILL.md](skills/网络杀伤链分析_analyzing-cyber-kill-chain/SKILL.md) |
| 49 | **行业威胁态势评估** | `performing-threat-landscape-assessment-for-sector` | Conducts a sector-specific threat landscape assessment (financial, hea… | [SKILL.md](skills/行业威胁态势评估_performing-threat-landscape-assessment-for-sector/SKILL.md) |
| 50 | **证书透明日志审计** | `auditing-tls-certificate-transparency-logs` | Monitors Certificate Transparency (CT) logs to detect unauthorized cer… | [SKILL.md](skills/证书透明日志审计_auditing-tls-certificate-transparency-logs/SKILL.md) |
| 51 | **证书透明日志钓鱼监测** | `analyzing-certificate-transparency-for-phishing` | Monitor Certificate Transparency logs using crt.sh and Certstream to d… | [SKILL.md](skills/证书透明日志钓鱼监测_analyzing-certificate-transparency-for-phishing/SKILL.md) |
| 52 | **钻石模型入侵分析** | `implementing-diamond-model-analysis` | The Diamond Model of Intrusion Analysis provides a structured framewor… | [SKILL.md](skills/钻石模型入侵分析_implementing-diamond-model-analysis/SKILL.md) |

---

<sub>本页由脚本生成 · 技能内容转载自上游项目，非原创 · [返回首页](../README.md) · [索引](../index.json) · [使用边界](../SECURITY.md)</sub>
