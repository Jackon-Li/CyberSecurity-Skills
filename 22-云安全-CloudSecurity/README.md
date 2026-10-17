# 22-云安全 · CloudSecurity

> 本分类共 **66** 个技能（蓝队 66）。

每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。

| # | 技能 | 英文标识 | 摘要 | 路径 |
|---|---|---|---|---|
| 1 | **AWS CloudTrail异常检测** | `detecting-aws-cloudtrail-anomalies` | Detect unusual API call patterns in AWS CloudTrail logs using boto3, s… | [SKILL.md](skills/AWS CloudTrail异常检测_detecting-aws-cloudtrail-anomalies/SKILL.md) |
| 2 | **AWS Config合规规则** | `implementing-aws-config-rules-for-compliance` | Implements AWS Config managed and custom rules for continuous complian… | [SKILL.md](skills/AWS Config合规规则_implementing-aws-config-rules-for-compliance/SKILL.md) |
| 3 | **AWS IAM权限加固** | `securing-aws-iam-permissions` | Hardens AWS IAM configurations to enforce least-privilege access, cove… | [SKILL.md](skills/AWS IAM权限加固_securing-aws-iam-permissions/SKILL.md) |
| 4 | **AWS IAM权限提升检测** | `detecting-aws-iam-privilege-escalation` | Detect AWS IAM privilege escalation paths using boto3 and Cloudsplaini… | [SKILL.md](skills/AWS IAM权限提升检测_detecting-aws-iam-privilege-escalation/SKILL.md) |
| 5 | **AWS Nitro Enclave安全** | `implementing-aws-nitro-enclave-security` | Build AWS Nitro Enclave confidential computing environments using nitr… | [SKILL.md](skills/AWS Nitro Enclave安全_implementing-aws-nitro-enclave-security/SKILL.md) |
| 6 | **AWS S3存储桶权限审计** | `auditing-aws-s3-bucket-permissions` | Systematically audit AWS S3 bucket permissions to identify publicly ac… | [SKILL.md](skills/AWS S3存储桶权限审计_auditing-aws-s3-bucket-permissions/SKILL.md) |
| 7 | **AWS Security Hub部署** | `implementing-aws-security-hub` | Deploy AWS Security Hub as a centralized CSPM platform, backed by AWS… | [SKILL.md](skills/AWS Security Hub部署_implementing-aws-security-hub/SKILL.md) |
| 8 | **AWS WAF网关防护** | `securing-api-gateway-with-aws-waf` | Secures AWS API Gateway endpoints with AWS WAF by configuring managed… | [SKILL.md](skills/AWS WAF网关防护_securing-api-gateway-with-aws-waf/SKILL.md) |
| 9 | **AWS凭据泄露检测** | `detecting-aws-credential-exposure-with-trufflehog` | Scan source code repositories, CI/CD pipelines, and configuration file… | [SKILL.md](skills/AWS凭据泄露检测_detecting-aws-credential-exposure-with-trufflehog/SKILL.md) |
| 10 | **AWS合规监控中心** | `implementing-aws-security-hub-compliance` | Deploy AWS Security Hub, backed by AWS Config, to aggregate findings f… | [SKILL.md](skills/AWS合规监控中心_implementing-aws-security-hub-compliance/SKILL.md) |
| 11 | **AWS权限提升评估** | `performing-aws-privilege-escalation-assessment` | Performing authorized privilege escalation assessments in AWS environm… | [SKILL.md](skills/AWS权限提升评估_performing-aws-privilege-escalation-assessment/SKILL.md) |
| 12 | **Athena云日志取证** | `performing-cloud-log-forensics-with-athena` | Uses AWS Athena to query CloudTrail, VPC Flow Logs, S3 access logs, an… | [SKILL.md](skills/Athena云日志取证_performing-cloud-log-forensics-with-athena/SKILL.md) |
| 13 | **Azure AD配置审计** | `auditing-azure-active-directory-configuration` | Auditing Microsoft Entra ID (Azure Active Directory) configuration to… | [SKILL.md](skills/Azure AD配置审计_auditing-azure-active-directory-configuration/SKILL.md) |
| 14 | **Azure Defender云防护** | `implementing-azure-defender-for-cloud` | Enable Microsoft Defender for Cloud (CSPM + CWPP) across VMs, containe… | [SKILL.md](skills/Azure Defender云防护_implementing-azure-defender-for-cloud/SKILL.md) |
| 15 | **Azure存储配置错误检测** | `detecting-azure-storage-account-misconfigurations` | Audit Azure Blob and ADLS storage accounts for public access exposure,… | [SKILL.md](skills/Azure存储配置错误检测_detecting-azure-storage-account-misconfigurations/SKILL.md) |
| 16 | **Azure存储配置错误检测** | `detecting-misconfigured-azure-storage` | Audit Azure Storage accounts for public blob containers, missing encry… | [SKILL.md](skills/Azure存储配置错误检测_detecting-misconfigured-azure-storage/SKILL.md) |
| 17 | **Azure服务主体滥用检测** | `detecting-azure-service-principal-abuse` | Detect Azure service principal abuse in Microsoft Entra ID using KQL d… | [SKILL.md](skills/Azure服务主体滥用检测_detecting-azure-service-principal-abuse/SKILL.md) |
| 18 | **Azure横向移动检测** | `detecting-azure-lateral-movement` | Detect lateral movement in Azure AD/Entra ID environments using Micros… | [SKILL.md](skills/Azure横向移动检测_detecting-azure-lateral-movement/SKILL.md) |
| 19 | **CIS基准云安全审计** | `auditing-cloud-with-cis-benchmarks` | Audit AWS, Azure, and GCP environments against the CIS Foundations Ben… | [SKILL.md](skills/CIS基准云安全审计_auditing-cloud-with-cis-benchmarks/SKILL.md) |
| 20 | **Cartography云资产图谱** | `performing-cloud-asset-inventory-with-cartography` | Run Cartography to sync AWS, GCP, or Azure resources into a Neo4j grap… | [SKILL.md](skills/Cartography云资产图谱_performing-cloud-asset-inventory-with-cartography/SKILL.md) |
| 21 | **CloudFox云资产枚举** | `enumerating-cloud-with-cloudfox` | Run CloudFox's read-only Describe/List/Get enumeration (all-checks, ro… | [SKILL.md](skills/CloudFox云资产枚举_enumerating-cloud-with-cloudfox/SKILL.md) |
| 22 | **CloudTrail云取证** | `performing-cloud-forensics-with-aws-cloudtrail` | Investigate AWS account compromise by querying CloudTrail with boto3's… | [SKILL.md](skills/CloudTrail云取证_performing-cloud-forensics-with-aws-cloudtrail/SKILL.md) |
| 23 | **CloudTrail日志分析** | `implementing-cloud-trail-log-analysis` | Implementing AWS CloudTrail log analysis for security monitoring, thre… | [SKILL.md](skills/CloudTrail日志分析_implementing-cloud-trail-log-analysis/SKILL.md) |
| 24 | **Defender云防护部署** | `securing-azure-with-microsoft-defender` | Deploys and configures Microsoft Defender for Cloud as a CNAPP for Azu… | [SKILL.md](skills/Defender云防护部署_securing-azure-with-microsoft-defender/SKILL.md) |
| 25 | **Detective云威胁狩猎** | `performing-cloud-native-threat-hunting-with-aws-detective` | Investigate AWS security incidents using Amazon Detective's behavior g… | [SKILL.md](skills/Detective云威胁狩猎_performing-cloud-native-threat-hunting-with-aws-detective/SKILL.md) |
| 26 | **Falco云原生取证** | `performing-cloud-native-forensics-with-falco` | Uses Falco YAML rules for runtime threat detection in containers and K… | [SKILL.md](skills/Falco云原生取证_performing-cloud-native-forensics-with-falco/SKILL.md) |
| 27 | **Forseti GCP安全评估** | `performing-gcp-security-assessment-with-forseti` | Performing comprehensive security assessments of Google Cloud Platform… | [SKILL.md](skills/Forseti GCP安全评估_performing-gcp-security-assessment-with-forseti/SKILL.md) |
| 28 | **GCP IAM权限审计** | `auditing-gcp-iam-permissions` | Auditing Google Cloud Platform IAM permissions to identify overly perm… | [SKILL.md](skills/GCP IAM权限审计_auditing-gcp-iam-permissions/SKILL.md) |
| 29 | **GCP VPC防火墙规则** | `implementing-gcp-vpc-firewall-rules` | Implements and audits GCP VPC firewall rules using gcloud, covering au… | [SKILL.md](skills/GCP VPC防火墙规则_implementing-gcp-vpc-firewall-rules/SKILL.md) |
| 30 | **GCP二进制授权** | `implementing-gcp-binary-authorization` | Implements GCP Binary Authorization end to end, including creating KMS… | [SKILL.md](skills/GCP二进制授权_implementing-gcp-binary-authorization/SKILL.md) |
| 31 | **GCP存储桶爆破测试** | `performing-gcp-penetration-testing-with-gcpbucketbrute` | Performs authorized GCP security testing using GCPBucketBrute to enume… | [SKILL.md](skills/GCP存储桶爆破测试_performing-gcp-penetration-testing-with-gcpbucketbrute/SKILL.md) |
| 32 | **GCP组织策略约束** | `implementing-gcp-organization-policy-constraints` | Implements GCP Organization Policy constraints via gcloud and Terrafor… | [SKILL.md](skills/GCP组织策略约束_implementing-gcp-organization-policy-constraints/SKILL.md) |
| 33 | **GuardDuty云威胁检测** | `detecting-cloud-threats-with-guardduty` | Deploy and operationalize Amazon GuardDuty, covering protection plans… | [SKILL.md](skills/GuardDuty云威胁检测_detecting-cloud-threats-with-guardduty/SKILL.md) |
| 34 | **GuardDuty告警自动化响应** | `detecting-aws-guardduty-findings-automation` | Build automated AWS GuardDuty finding response pipelines using EventBr… | [SKILL.md](skills/GuardDuty告警自动化响应_detecting-aws-guardduty-findings-automation/SKILL.md) |
| 35 | **K8s集群RBAC审计** | `auditing-kubernetes-cluster-rbac` | Auditing Kubernetes cluster RBAC configurations to identify overly per… | [SKILL.md](skills/K8s集群RBAC审计_auditing-kubernetes-cluster-rbac/SKILL.md) |
| 36 | **Lambda执行角色加固** | `securing-aws-lambda-execution-roles` | Hardens AWS Lambda execution roles by writing least-privilege IAM poli… | [SKILL.md](skills/Lambda执行角色加固_securing-aws-lambda-execution-roles/SKILL.md) |
| 37 | **Macie敏感数据分类** | `implementing-aws-macie-for-data-classification` | Enable and configure Amazon Macie via AWS CLI/Terraform to discover, c… | [SKILL.md](skills/Macie敏感数据分类_implementing-aws-macie-for-data-classification/SKILL.md) |
| 38 | **OAuth令牌窃取检测** | `detecting-oauth-token-theft` | Detect and respond to OAuth token theft and replay in Microsoft Entra… | [SKILL.md](skills/OAuth令牌窃取检测_detecting-oauth-token-theft/SKILL.md) |
| 39 | **OAuth应用授权风险检测** | `detecting-suspicious-oauth-application-consent` | Detect risky OAuth application consent grants in Azure AD / Microsoft… | [SKILL.md](skills/OAuth应用授权风险检测_detecting-suspicious-oauth-application-consent/SKILL.md) |
| 40 | **Office365审计日志分析** | `analyzing-office365-audit-logs-for-compromise` | Parse Office 365 Unified Audit Logs via Microsoft Graph API to detect… | [SKILL.md](skills/Office365审计日志分析_analyzing-office365-audit-logs-for-compromise/SKILL.md) |
| 41 | **Okta云身份管理** | `managing-cloud-identity-with-okta` | Implement Okta as a centralized cloud identity provider: configure SSO… | [SKILL.md](skills/Okta云身份管理_managing-cloud-identity-with-okta/SKILL.md) |
| 42 | **Pacu云渗透测试** | `performing-cloud-penetration-testing-with-pacu` | Run authorized AWS penetration tests with Pacu, the open-source AWS ex… | [SKILL.md](skills/Pacu云渗透测试_performing-cloud-penetration-testing-with-pacu/SKILL.md) |
| 43 | **Pacu框架AWS利用** | `exploiting-aws-with-pacu` | Runs the Pacu AWS exploitation framework end-to-end — session and cred… | [SKILL.md](skills/Pacu框架AWS利用_exploiting-aws-with-pacu/SKILL.md) |
| 44 | **S3存储桶配置修复** | `remediating-s3-bucket-misconfiguration` | Provides step-by-step procedures for remediating Amazon S3 bucket misc… | [SKILL.md](skills/S3存储桶配置修复_remediating-s3-bucket-misconfiguration/SKILL.md) |
| 45 | **S3数据外泄检测** | `detecting-s3-data-exfiltration-attempts` | Detecting data exfiltration attempts from AWS S3 buckets by analyzing… | [SKILL.md](skills/S3数据外泄检测_detecting-s3-data-exfiltration-attempts/SKILL.md) |
| 46 | **ScoutSuite AWS资产枚举** | `performing-aws-account-enumeration-with-scout-suite` | Run the agentless, open-source ScoutSuite tool (via pip install and th… | [SKILL.md](skills/ScoutSuite AWS资产枚举_performing-aws-account-enumeration-with-scout-suite/SKILL.md) |
| 47 | **Sentinel云SIEM建设** | `building-cloud-siem-with-sentinel` | Deploy Microsoft Sentinel as a cloud-native SIEM/SOAR by configuring m… | [SKILL.md](skills/Sentinel云SIEM建设_building-cloud-siem-with-sentinel/SKILL.md) |
| 48 | **Serverless函数加固** | `securing-serverless-functions` | Hardens serverless compute platforms (AWS Lambda, Azure Functions, Goo… | [SKILL.md](skills/Serverless函数加固_securing-serverless-functions/SKILL.md) |
| 49 | **Serverless函数安全审查** | `performing-serverless-function-security-review` | Performing security reviews of serverless functions across AWS Lambda,… | [SKILL.md](skills/Serverless函数安全审查_performing-serverless-function-security-review/SKILL.md) |
| 50 | **Serverless函数注入检测** | `detecting-serverless-function-injection` | Detects and prevents code injection attacks targeting serverless funct… | [SKILL.md](skills/Serverless函数注入检测_detecting-serverless-function-injection/SKILL.md) |
| 51 | **Stratus云攻击模拟** | `emulating-cloud-attacks-with-stratus-red-team` | Install and run Stratus Red Team to detonate granular, MITRE ATT&CK-ma… | [SKILL.md](skills/Stratus云攻击模拟_emulating-cloud-attacks-with-stratus-red-team/SKILL.md) |
| 52 | **Terraform基础设施审计** | `auditing-terraform-infrastructure-for-security` | Auditing Terraform infrastructure-as-code for security misconfiguratio… | [SKILL.md](skills/Terraform基础设施审计_auditing-terraform-infrastructure-for-security/SKILL.md) |
| 53 | **Vault密钥管理** | `implementing-secrets-management-with-vault` | Deploy HashiCorp Vault for centralized secrets management, covering dy… | [SKILL.md](skills/Vault密钥管理_implementing-secrets-management-with-vault/SKILL.md) |
| 54 | **云DLP数据防泄露** | `implementing-cloud-dlp-for-data-protection` | Implement cloud DLP using Amazon Macie, Google Cloud DLP API, Microsof… | [SKILL.md](skills/云DLP数据防泄露_implementing-cloud-dlp-for-data-protection/SKILL.md) |
| 55 | **云WAF规则实施** | `implementing-cloud-waf-rules` | Deploys and tunes Web Application Firewall rules on AWS WAF, Azure WAF… | [SKILL.md](skills/云WAF规则实施_implementing-cloud-waf-rules/SKILL.md) |
| 56 | **云上K8s集群加固** | `securing-kubernetes-on-cloud` | Hardens managed Kubernetes clusters on EKS, AKS, and GKE by implementi… | [SKILL.md](skills/云上K8s集群加固_securing-kubernetes-on-cloud/SKILL.md) |
| 57 | **云凭据失陷检测** | `detecting-compromised-cloud-credentials` | Detect compromised cloud credentials across AWS, Azure, and GCP by ana… | [SKILL.md](skills/云凭据失陷检测_detecting-compromised-cloud-credentials/SKILL.md) |
| 58 | **云存储访问模式分析** | `analyzing-cloud-storage-access-patterns` | Detect abnormal access in AWS S3, GCS, and Azure Blob Storage by analy… | [SKILL.md](skills/云存储访问模式分析_analyzing-cloud-storage-access-patterns/SKILL.md) |
| 59 | **云安全态势管理** | `implementing-cloud-security-posture-management` | Continuously monitor multi-cloud environments (AWS, Azure, GCP) for mi… | [SKILL.md](skills/云安全态势管理_implementing-cloud-security-posture-management/SKILL.md) |
| 60 | **云工作负载防护** | `implementing-cloud-workload-protection` | Implements cloud workload protection using boto3 and google-cloud APIs… | [SKILL.md](skills/云工作负载防护_implementing-cloud-workload-protection/SKILL.md) |
| 61 | **云挖矿活动检测** | `detecting-cryptomining-in-cloud` | This skill teaches security teams how to detect and respond to unautho… | [SKILL.md](skills/云挖矿活动检测_detecting-cryptomining-in-cloud/SKILL.md) |
| 62 | **云环境渗透测试** | `conducting-cloud-penetration-testing` | This skill outlines methodologies for performing authorized penetratio… | [SKILL.md](skills/云环境渗透测试_conducting-cloud-penetration-testing/SKILL.md) |
| 63 | **云环境零信任实施** | `implementing-zero-trust-in-cloud` | Guides zero trust implementation across AWS, Azure, and GCP per NIST S… | [SKILL.md](skills/云环境零信任实施_implementing-zero-trust-in-cloud/SKILL.md) |
| 64 | **容器镜像仓库加固** | `securing-container-registry-images` | Secures container registry images (ECR, ACR, GCR, Docker Hub) by scann… | [SKILL.md](skills/容器镜像仓库加固_securing-container-registry-images/SKILL.md) |
| 65 | **影子IT云使用检测** | `detecting-shadow-it-cloud-usage` | Detect unauthorized SaaS and cloud service usage (shadow IT) by parsin… | [SKILL.md](skills/影子IT云使用检测_detecting-shadow-it-cloud-usage/SKILL.md) |
| 66 | **零信任网络访问实施** | `implementing-zero-trust-network-access` | Configures Zero Trust Network Access (ZTNA) in AWS, Azure, and GCP usi… | [SKILL.md](skills/零信任网络访问实施_implementing-zero-trust-network-access/SKILL.md) |

---

← 返回 [仓库首页](../README.md) · 索引见 [index.json](../index.json)
