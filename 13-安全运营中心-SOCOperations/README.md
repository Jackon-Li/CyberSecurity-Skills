# 13-安全运营中心 · SOCOperations

> 本分类共 **63** 个技能（蓝队 63）。

每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。

| # | 技能 | 英文标识 | 摘要 | 路径 |
|---|---|---|---|---|
| 1 | **API网关访问日志分析** | `analyzing-api-gateway-access-logs` | Parses API Gateway access logs (AWS API Gateway, Kong, Nginx) to detec… | [SKILL.md](skills/API网关访问日志分析_analyzing-api-gateway-access-logs/SKILL.md) |
| 2 | **APT关联规则编写** | `implementing-siem-correlation-rules-for-apt` | Write multi-event correlation rules in Splunk SPL and Sigma format tha… | [SKILL.md](skills/APT关联规则编写_implementing-siem-correlation-rules-for-apt/SKILL.md) |
| 3 | **ATT&CK威胁建模** | `implementing-threat-modeling-with-mitre-attack` | Implements threat modeling using the MITRE ATT&CK framework to map adv… | [SKILL.md](skills/ATT&CK威胁建模_implementing-threat-modeling-with-mitre-attack/SKILL.md) |
| 4 | **ATT&CK覆盖映射** | `implementing-mitre-attack-coverage-mapping` | Implement MITRE ATT&CK coverage mapping to identify detection gaps, pr… | [SKILL.md](skills/ATT&CK覆盖映射_implementing-mitre-attack-coverage-mapping/SKILL.md) |
| 5 | **Azure活动日志分析** | `analyzing-azure-activity-logs-for-threats` | Queries Azure Monitor activity logs and sign-in logs via azure-monitor… | [SKILL.md](skills/Azure活动日志分析_analyzing-azure-activity-logs-for-threats/SKILL.md) |
| 6 | **CI-CD供应链攻击检测** | `detecting-supply-chain-attacks-in-ci-cd` | Scans GitHub Actions workflows and CI/CD pipeline configurations for s… | [SKILL.md](skills/CI-CD供应链攻击检测_detecting-supply-chain-attacks-in-ci-cd/SKILL.md) |
| 7 | **DLP内部数据外泄检测** | `detecting-insider-data-exfiltration-via-dlp` | Detects insider data exfiltration by analyzing DLP policy violations,… | [SKILL.md](skills/DLP内部数据外泄检测_detecting-insider-data-exfiltration-via-dlp/SKILL.md) |
| 8 | **DNS日志外泄分析** | `analyzing-dns-logs-for-exfiltration` | Analyzes DNS query logs to detect data exfiltration via DNS tunneling,… | [SKILL.md](skills/DNS日志外泄分析_analyzing-dns-logs-for-exfiltration/SKILL.md) |
| 9 | **DNS隧道检测** | `performing-dns-tunneling-detection` | Detects DNS tunneling by computing Shannon entropy of DNS query names,… | [SKILL.md](skills/DNS隧道检测_performing-dns-tunneling-detection/SKILL.md) |
| 10 | **Datadog安全监控** | `implementing-security-monitoring-with-datadog` | Implements security monitoring using Datadog Cloud SIEM, Cloud Securit… | [SKILL.md](skills/Datadog安全监控_implementing-security-monitoring-with-datadog/SKILL.md) |
| 11 | **Elastic告警分流** | `performing-alert-triage-with-elastic-siem` | Perform systematic alert triage in Elastic Security SIEM—classifying,… | [SKILL.md](skills/Elastic告警分流_performing-alert-triage-with-elastic-siem/SKILL.md) |
| 12 | **Elastic威胁狩猎** | `performing-threat-hunting-with-elastic-siem` | Performs proactive threat hunting in Elastic Security SIEM using KQL/E… | [SKILL.md](skills/Elastic威胁狩猎_performing-threat-hunting-with-elastic-siem/SKILL.md) |
| 13 | **Entra攻击工具检测** | `detecting-entra-offensive-tools-in-graph-logs` | Hunt AADGraphActivityLogs and MicrosoftGraphActivityLogs in Microsoft… | [SKILL.md](skills/Entra攻击工具检测_detecting-entra-offensive-tools-in-graph-logs/SKILL.md) |
| 14 | **Fluentd日志转发实施** | `implementing-log-forwarding-with-fluentd` | Configures Fluent Bit as an endpoint log forwarder and Fluentd as the… | [SKILL.md](skills/Fluentd日志转发实施_implementing-log-forwarding-with-fluentd/SKILL.md) |
| 15 | **GoPhish钓鱼演练** | `performing-red-team-phishing-with-gophish` | Automates GoPhish phishing simulation campaigns using the Python gophi… | [SKILL.md](skills/GoPhish钓鱼演练_performing-red-team-phishing-with-gophish/SKILL.md) |
| 16 | **IOC富化自动化** | `performing-ioc-enrichment-automation` | Automates Indicator of Compromise (IOC) enrichment by orchestrating lo… | [SKILL.md](skills/IOC富化自动化_performing-ioc-enrichment-automation/SKILL.md) |
| 17 | **LiME与Volatility内存取证** | `analyzing-memory-forensics-with-lime-and-volatility` | Performs Linux memory acquisition using LiME (Linux Memory Extractor)… | [SKILL.md](skills/LiME与Volatility内存取证_analyzing-memory-forensics-with-lime-and-volatility/SKILL.md) |
| 18 | **PowerShell脚本块日志分析** | `analyzing-powershell-script-block-logging` | Parse Windows PowerShell Script Block Logs (Event ID 4104) from EVTX f… | [SKILL.md](skills/PowerShell脚本块日志分析_analyzing-powershell-script-block-logging/SKILL.md) |
| 19 | **QRadar安全事件关联** | `correlating-security-events-in-qradar` | Correlates security events in IBM QRadar SIEM using AQL (Ariel Query L… | [SKILL.md](skills/QRadar安全事件关联_correlating-security-events-in-qradar/SKILL.md) |
| 20 | **Rekall内存取证分析** | `extracting-memory-artifacts-with-rekall` | Uses Rekall memory forensics framework to analyze memory dumps for pro… | [SKILL.md](skills/Rekall内存取证分析_extracting-memory-artifacts-with-rekall/SKILL.md) |
| 21 | **SIEM日志源接入** | `performing-log-source-onboarding-in-siem` | Perform structured log source onboarding into SIEM platforms (Splunk,… | [SKILL.md](skills/SIEM日志源接入_performing-log-source-onboarding-in-siem/SKILL.md) |
| 22 | **SIEM检测用例实施** | `implementing-siem-use-cases-for-detection` | Implements SIEM detection use cases by designing correlation rules, th… | [SKILL.md](skills/SIEM检测用例实施_implementing-siem-use-cases-for-detection/SKILL.md) |
| 23 | **SIEM用例调优** | `implementing-siem-use-case-tuning` | Tune SIEM detection rules in Splunk and Elastic to reduce false positi… | [SKILL.md](skills/SIEM用例调优_implementing-siem-use-case-tuning/SKILL.md) |
| 24 | **SIEM误报削减** | `performing-false-positive-reduction-in-siem` | Reduces SIEM false positives through systematic rule tuning, threshold… | [SKILL.md](skills/SIEM误报削减_performing-false-positive-reduction-in-siem/SKILL.md) |
| 25 | **SOAR钓鱼响应预案** | `implementing-soar-playbook-for-phishing` | Automates phishing incident response by calling the Splunk SOAR (Phant… | [SKILL.md](skills/SOAR钓鱼响应预案_implementing-soar-playbook-for-phishing/SKILL.md) |
| 26 | **SOC升级矩阵建设** | `building-soc-escalation-matrix` | Build a structured SOC escalation matrix defining severity tiers, resp… | [SKILL.md](skills/SOC升级矩阵建设_building-soc-escalation-matrix/SKILL.md) |
| 27 | **SOC指标与KPI追踪** | `building-soc-metrics-and-kpi-tracking` | Builds SOC performance metrics and KPI tracking dashboards measuring M… | [SKILL.md](skills/SOC指标与KPI追踪_building-soc-metrics-and-kpi-tracking/SKILL.md) |
| 28 | **SOC桌面演练** | `performing-soc-tabletop-exercise` | Performs tabletop exercises for SOC teams simulating security incident… | [SKILL.md](skills/SOC桌面演练_performing-soc-tabletop-exercise/SKILL.md) |
| 29 | **SSRF漏洞利用** | `performing-ssrf-vulnerability-exploitation` | Tests web application URL parameters for Server-Side Request Forgery b… | [SKILL.md](skills/SSRF漏洞利用_performing-ssrf-vulnerability-exploitation/SKILL.md) |
| 30 | **SaaS令牌滥用狩猎** | `hunting-saas-sso-token-abuse` | Hunts for stolen-session and OAuth/PRT token replay (T1550.001) by cor… | [SKILL.md](skills/SaaS令牌滥用狩猎_hunting-saas-sso-token-abuse/SKILL.md) |
| 31 | **Sigma检测规则编写** | `building-detection-rules-with-sigma` | Builds vendor-agnostic detection rules using the Sigma rule format for… | [SKILL.md](skills/Sigma检测规则编写_building-detection-rules-with-sigma/SKILL.md) |
| 32 | **Splunk SOAR自动化** | `implementing-soar-automation-with-phantom` | Implements Security Orchestration, Automation, and Response (SOAR) wor… | [SKILL.md](skills/Splunk SOAR自动化_implementing-soar-automation-with-phantom/SKILL.md) |
| 33 | **Splunk事件日志分析** | `analyzing-windows-event-logs-in-splunk` | Analyzes Windows Security, System, and Sysmon event logs in Splunk to… | [SKILL.md](skills/Splunk事件日志分析_analyzing-windows-event-logs-in-splunk/SKILL.md) |
| 34 | **Splunk告警分流** | `triaging-security-alerts-in-splunk` | Triages security alerts in Splunk Enterprise Security by classifying s… | [SKILL.md](skills/Splunk告警分流_triaging-security-alerts-in-splunk/SKILL.md) |
| 35 | **Splunk威胁情报富化** | `building-threat-intelligence-enrichment-in-splunk` | Build automated IOC enrichment pipelines in Splunk Enterprise Security… | [SKILL.md](skills/Splunk威胁情报富化_building-threat-intelligence-enrichment-in-splunk/SKILL.md) |
| 36 | **Splunk检测规则编写** | `building-detection-rule-with-splunk-spl` | Build effective detection rules using Splunk Search Processing Languag… | [SKILL.md](skills/Splunk检测规则编写_building-detection-rule-with-splunk-spl/SKILL.md) |
| 37 | **TLS证书透明日志分析** | `analyzing-tls-certificate-transparency-logs` | Queries Certificate Transparency logs via crt.sh and pycrtsh to detect… | [SKILL.md](skills/TLS证书透明日志分析_analyzing-tls-certificate-transparency-logs/SKILL.md) |
| 38 | **WAF日志SQL注入检测** | `detecting-sql-injection-via-waf-logs` | Analyze WAF (ModSecurity/AWS WAF/Cloudflare) logs to detect SQL inject… | [SKILL.md](skills/WAF日志SQL注入检测_detecting-sql-injection-via-waf-logs/SKILL.md) |
| 39 | **Wazuh端点检测部署** | `implementing-endpoint-detection-with-wazuh` | Deploys and configures Wazuh SIEM/XDR for endpoint detection, covering… | [SKILL.md](skills/Wazuh端点检测部署_implementing-endpoint-detection-with-wazuh/SKILL.md) |
| 40 | **Web服务器入侵日志分析** | `analyzing-web-server-logs-for-intrusion` | Parse Apache and Nginx access logs to detect SQL injection attempts, l… | [SKILL.md](skills/Web服务器入侵日志分析_analyzing-web-server-logs-for-intrusion/SKILL.md) |
| 41 | **XSOAR自动化预案** | `implementing-soar-playbook-with-palo-alto-xsoar` | Build automated incident response playbooks in Cortex XSOAR (Demisto)… | [SKILL.md](skills/XSOAR自动化预案_implementing-soar-playbook-with-palo-alto-xsoar/SKILL.md) |
| 42 | **Zeek信标模式检测** | `detecting-beaconing-patterns-with-zeek` | Performs statistical analysis of Zeek conn.log connection intervals to… | [SKILL.md](skills/Zeek信标模式检测_detecting-beaconing-patterns-with-zeek/SKILL.md) |
| 43 | **eBPF安全监控实施** | `implementing-ebpf-security-monitoring` | Implements eBPF-based security monitoring using Cilium Tetragon for re… | [SKILL.md](skills/eBPF安全监控实施_implementing-ebpf-security-monitoring/SKILL.md) |
| 44 | **mTLS零信任服务** | `implementing-mtls-for-zero-trust-services` | Configures mutual TLS (mTLS) authentication between microservices usin… | [SKILL.md](skills/mTLS零信任服务_implementing-mtls-for-zero-trust-services/SKILL.md) |
| 45 | **rsyslog日志集中化** | `implementing-syslog-centralization-with-rsyslog` | Configure rsyslog for centralized log collection with TLS encryption,… | [SKILL.md](skills/rsyslog日志集中化_implementing-syslog-centralization-with-rsyslog/SKILL.md) |
| 46 | **事件工单系统实施** | `implementing-ticketing-system-for-incidents` | Implements an integrated incident ticketing system connecting SIEM ale… | [SKILL.md](skills/事件工单系统实施_implementing-ticketing-system-for-incidents/SKILL.md) |
| 47 | **内部威胁指标调查** | `investigating-insider-threat-indicators` | Investigates insider threat indicators including data exfiltration att… | [SKILL.md](skills/内部威胁指标调查_investigating-insider-threat-indicators/SKILL.md) |
| 48 | **勒索软件SOC预案** | `building-soc-playbook-for-ransomware` | Builds a structured SOC incident response playbook for ransomware atta… | [SKILL.md](skills/勒索软件SOC预案_building-soc-playbook-for-ransomware/SKILL.md) |
| 49 | **区块链日志完整性** | `implementing-log-integrity-with-blockchain` | Builds an append-only log integrity chain using SHA-256 hash chaining,… | [SKILL.md](skills/区块链日志完整性_implementing-log-integrity-with-blockchain/SKILL.md) |
| 50 | **告警疲劳缓解** | `implementing-alert-fatigue-reduction` | Implements strategies to reduce SOC alert fatigue by tuning detection… | [SKILL.md](skills/告警疲劳缓解_implementing-alert-fatigue-reduction/SKILL.md) |
| 51 | **威胁情报源集成** | `building-threat-intelligence-feed-integration` | Builds automated threat intelligence feed integration pipelines connec… | [SKILL.md](skills/威胁情报源集成_building-threat-intelligence-feed-integration/SKILL.md) |
| 52 | **安全混沌工程实施** | `implementing-security-chaos-engineering` | Implements security chaos engineering experiments that deliberately di… | [SKILL.md](skills/安全混沌工程实施_implementing-security-chaos-engineering/SKILL.md) |
| 53 | **应急响应仪表盘建设** | `building-incident-response-dashboard` | Builds real-time incident response dashboards in Splunk, Elastic, or G… | [SKILL.md](skills/应急响应仪表盘建设_building-incident-response-dashboard/SKILL.md) |
| 54 | **恶意样本自动提交管道** | `building-automated-malware-submission-pipeline` | Builds an automated malware submission and analysis pipeline that coll… | [SKILL.md](skills/恶意样本自动提交管道_building-automated-malware-submission-pipeline/SKILL.md) |
| 55 | **撞库攻击狩猎** | `hunting-credential-stuffing-attacks` | Detects credential stuffing attacks by analyzing authentication logs f… | [SKILL.md](skills/撞库攻击狩猎_hunting-credential-stuffing-attacks/SKILL.md) |
| 56 | **横向移动检测** | `performing-lateral-movement-detection` | Detects lateral movement techniques including Pass-the-Hash, PsExec, W… | [SKILL.md](skills/横向移动检测_performing-lateral-movement-detection/SKILL.md) |
| 57 | **欺骗技术部署** | `performing-deception-technology-deployment` | Deploys deception technology including honeypots, honeytokens, and dec… | [SKILL.md](skills/欺骗技术部署_performing-deception-technology-deployment/SKILL.md) |
| 58 | **漏洞扫描工作流建设** | `building-vulnerability-scanning-workflow` | Builds a structured vulnerability scanning workflow using tools like N… | [SKILL.md](skills/漏洞扫描工作流建设_building-vulnerability-scanning-workflow/SKILL.md) |
| 59 | **用户行为分析UEBA** | `performing-user-behavior-analytics` | Performs User and Entity Behavior Analytics (UEBA) to detect anomalous… | [SKILL.md](skills/用户行为分析UEBA_performing-user-behavior-analytics/SKILL.md) |
| 60 | **紫队演练实施** | `performing-purple-team-exercise` | Performs purple team exercises by coordinating red team adversary emul… | [SKILL.md](skills/紫队演练实施_performing-purple-team-exercise/SKILL.md) |
| 61 | **蜜标令牌失陷检测** | `implementing-honeytokens-for-breach-detection` | Deploys canary tokens and honeytokens (fake AWS credentials, DNS canar… | [SKILL.md](skills/蜜标令牌失陷检测_implementing-honeytokens-for-breach-detection/SKILL.md) |
| 62 | **金丝雀令牌网络入侵检测** | `implementing-canary-tokens-for-network-intrusion` | Deploys DNS, HTTP, and AWS API key canary tokens across network infras… | [SKILL.md](skills/金丝雀令牌网络入侵检测_implementing-canary-tokens-for-network-intrusion/SKILL.md) |
| 63 | **钓鱼邮件事件调查** | `investigating-phishing-email-incident` | Investigates phishing email incidents from initial user report through… | [SKILL.md](skills/钓鱼邮件事件调查_investigating-phishing-email-incident/SKILL.md) |

---

← 返回 [仓库首页](../README.md) · 索引见 [index.json](../index.json)
