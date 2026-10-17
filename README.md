# 网络安全技能库 · CyberSecurity Skills

> 820 个面向 AI 助手的安全技能，按 34 个分类组织。
> 每个技能 = 一份可执行的作业流程 + 参考资料 + 可运行脚本。

本仓库是一套**给 AI 编程助手（Claude Code / WorkBuddy / Cursor 等）直接加载的技能库**，也可以脱离 AI 当作网络安全知识库与代码样例库使用。技能覆盖从渗透测试、红队行动，到威胁狩猎、应急响应、数字取证，再到云原生、零信任、合规治理的完整链条。

| 指标 | 数值 |
|---|---|
| 技能总数 | **820** |
| 分类模块 | **34** |
| 红队向 / 蓝队向 / 取证向 | 166 / 547 / 107 |
| 附带 Python 脚本 | 1,091 个 / 约 24.4 万行 |
| 参考资料文档 | 2,106 个 Markdown |
| 仓库体积 | 约 46 MB |
| 许可 | Apache-2.0 |

---

## 这是什么

每个技能是一个独立目录，结构统一：

```
01-渗透测试-PenetrationTesting/
└── skills/
    └── AD攻击模拟_executing-active-directory-attack-simulation/
        ├── SKILL.md          # 入口：何时使用 / 前置条件 / 工作流 / 验证标准
        ├── references/       # 深入资料（.md）
        ├── scripts/          # 可运行脚本（.py，部分是完整工具）
        ├── assets/           # 图例、配置样例等（部分技能有）
        └── LICENSE           # Apache-2.0
```

`SKILL.md` 采用统一小节：`When to Use`、`Prerequisites`、`Workflow`、`Key Concepts`、`Tools & Systems`、`Validation Criteria`，并在 frontmatter 中标注 `mitre_attack`、`nist_csf`、`tags` 等映射字段。

---

## 快速开始

### 1. 直接浏览

从下方[分类导航](#分类导航)进入任意分类，分类页有该分类全部技能的表格与直达链接。

### 2. 用脚本检索（推荐）

```bash
# 按中文关键词检索（技能名 / 英文标识 / 标签 / 描述）
python scripts/skill_query.py 横向移动

# 限定分类，只看红队向
python scripts/skill_query.py kerberos --module 02 --team red

# 输出 JSON，供程序消费
python scripts/skill_query.py 云安全 --json
```

### 3. 交给 AI 助手使用

把仓库根目录挂到 AI 助手的技能目录下，或直接把 `index.json` 与 `AGENT_USAGE.md` 提供给它。具体做法见 [AGENT_USAGE.md](AGENT_USAGE.md)。

---

## 分类导航

| # | 分类 | 技能数 | 红/蓝/取证 | 说明 |
|---|---|---|---|---|
| 01 | [渗透测试](01-渗透测试-PenetrationTesting/README.md) | 24 | 24/0/0 | 授权范围内的漏洞发现与利用验证 |
| 02 | [红队](02-红队-RedTeaming/README.md) | 35 | 35/0/0 | 模拟攻击者全流程行动与对抗 |
| 03 | [Web应用安全](03-Web应用安全-WebApplicationSecurity/README.md) | 47 | 47/0/0 | OWASP 类漏洞的发现、利用与修复 |
| 04 | [API安全](04-API安全-APISecurity/README.md) | 28 | 28/0/0 | REST/GraphQL/gRPC 接口攻击面 |
| 05 | [移动安全](05-移动安全-MobileSecurity/README.md) | 13 | 13/0/0 | Android/iOS 应用逆向与攻击面 |
| 06 | [无线安全](06-无线安全-WirelessSecurity/README.md) | 2 | 2/0/0 | Wi-Fi/BLE 等无线协议攻击 |
| 07 | [区块链安全](07-区块链安全-BlockchainSecurity/README.md) | 2 | 2/0/0 | 智能合约审计与链上攻击 |
| 08 | [欺骗技术](08-欺骗技术-DeceptionTechnology/README.md) | 6 | 0/6/0 | 蜜罐、蜜标与诱捕 |
| 09 | [漏洞管理](09-漏洞管理-VulnerabilityManagement/README.md) | 25 | 0/25/0 | 资产测绘、优先级排序与修复闭环 |
| 10 | [威胁情报](10-威胁情报-ThreatIntelligence/README.md) | 52 | 0/52/0 | 情报采集、研判与运营化 |
| 11 | [威胁狩猎](11-威胁狩猎-ThreatHunting/README.md) | 58 | 0/58/0 | 假设驱动的主动搜寻 |
| 12 | [威胁检测](12-威胁检测-ThreatDetection/README.md) | 7 | 0/7/0 | 检测规则与信号工程 |
| 13 | [安全运营中心](13-安全运营中心-SOCOperations/README.md) | 63 | 0/63/0 | SOC 流程、告警分级与响应 |
| 14 | [应急响应](14-应急响应-IncidentResponse/README.md) | 26 | 0/0/26 | 事件处置流程与遏制 |
| 15 | [数字取证](15-数字取证-DigitalForensics/README.md) | 41 | 0/0/41 | 主机/网络/云取证与证据链 |
| 16 | [恶意软件分析](16-恶意软件分析-MalwareAnalysis/README.md) | 39 | 0/0/39 | 样本静态与动态分析 |
| 17 | [勒索软件防御](17-勒索软件防御-RansomwareDefense/README.md) | 13 | 0/13/0 | 预防、检测与恢复 |
| 18 | [端点安全](18-端点安全-EndpointSecurity/README.md) | 17 | 0/17/0 | EDR、加固与主机防护 |
| 19 | [网络安全](19-网络安全-NetworkSecurity/README.md) | 43 | 0/43/0 | 网络分段、流量分析与边界防护 |
| 20 | [身份与访问管理](20-身份与访问管理-IdentityAccessManagement/README.md) | 40 | 0/40/0 | 认证、授权与特权管理 |
| 21 | [零信任架构](21-零信任架构-ZeroTrustArchitecture/README.md) | 18 | 0/18/0 | 持续验证与最小权限落地 |
| 22 | [云安全](22-云安全-CloudSecurity/README.md) | 66 | 0/66/0 | AWS/Azure/GCP 配置与攻击面 |
| 23 | [容器安全](23-容器安全-ContainerSecurity/README.md) | 33 | 0/33/0 | K8s/镜像/运行时安全 |
| 24 | [OT与ICS安全](24-OT与ICS安全-OTICSSecurity/README.md) | 29 | 0/29/0 | 工控协议与关键基础设施 |
| 25 | [硬件与固件安全](25-硬件与固件安全-HardwareFirmwareSecurity/README.md) | 6 | 0/6/0 | 固件提取、侧信道与硬件攻击 |
| 26 | [供应链安全](26-供应链安全-SupplyChainSecurity/README.md) | 8 | 0/8/0 | 依赖、构建与投毒防护 |
| 27 | [DevSecOps](27-DevSecOps-DevSecOps/README.md) | 18 | 0/18/0 | 流水线内嵌安全门禁 |
| 28 | [密码学](28-密码学-Cryptography/README.md) | 16 | 0/16/0 | 协议、密钥管理与后量子迁移 |
| 29 | [数据保护](29-数据保护-DataProtection/README.md) | 1 | 0/0/1 | 数据分级、脱敏与防泄漏 |
| 30 | [隐私合规](30-隐私合规-PrivacyCompliance/README.md) | 2 | 0/2/0 | GDPR/个保法工程化落地 |
| 31 | [合规与治理](31-合规与治理-ComplianceGovernance/README.md) | 11 | 0/11/0 | 等保、审计与风险治理 |
| 32 | [网络钓鱼防御](32-网络钓鱼防御-PhishingDefense/README.md) | 16 | 0/16/0 | 邮件防护与安全意识 |
| 33 | [AI安全](33-AI安全-AISecurity/README.md) | 14 | 14/0/0 | 提示注入、模型与 Agent 攻击面 |
| 34 | [紫队](34-紫队-PurpleTeam/README.md) | 1 | 1/0/0 | 红蓝协同与检测验证 |

> 目录名格式：`编号-中文名-英文名`，编号顺序按「攻击面 → 检测响应 → 平台工程 → 治理」排列。

---

## 机器可读索引

| 文件 | 用途 |
|---|---|
| [`index.json`](index.json) | 全量索引：34 个模块、820 个技能，含中文名/英文标识/标签/领域/路径 |
| [`index.schema.json`](index.schema.json) | 索引的 JSON Schema，可用于校验与生成 |
| [`scripts/skill_query.py`](scripts/skill_query.py) | 零依赖查询脚本，支持关键词/分类/领域过滤 |
| [`AGENT_USAGE.md`](AGENT_USAGE.md) | 给 AI 助手的接入说明 |

---

## 质量与边界（实测）

为保证「拿来即用」，以下是实测数据而非宣称：

| 项目 | 覆盖情况 |
|---|---|
| `Prerequisites` 小节 | 100% |
| `When to Use` 小节 | 99.6% |
| `Workflow` 小节 | 74% |
| `Validation Criteria` 小节 | 15% |
| 独立 `## Verification` 小节 | 5% |

因此：**不是每个技能都有逐条验证步骤**，约 80% 的技能以「工作流 + 注意事项」为主，验证需要结合 `Validation Criteria`（若有）与目标环境实际判断。脚本为参考实现，**上线前必须审阅**。

---

## 来源与许可

- 上游项目：[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- 上游作者：mahipal；许可：**Apache-2.0**
- 本仓库仅做**目录重排与索引化**（编号分类、统一索引、查询脚本），技能内容保持原样，未修改原文、脚本与许可声明；每个技能目录下的 `LICENSE` 均予保留。
- 按 Apache-2.0 要求：保留版权与许可声明，修改处已在本文档说明。详见 [NOTICE.md](NOTICE.md)。

---

## 授权使用声明（重要）

本仓库内容面向**合法授权的安全测试与研究**：

- 仅可用于你拥有、或已获得**书面授权**的目标系统；
- 适用于渗透测试授权项目、CTF 竞赛、漏洞赏金计划（在范围内）、内部安全建设与教学；
- **禁止**用于未授权的入侵、数据窃取、破坏或任何违反所在地法律的行为；
- 部分技能涉及免杀、凭证窃取、横向移动等敏感技术，**仅限红队演练与检测能力验证场景**。

使用者自行承担全部法律责任。作者与仓库维护者不对任何滥用行为负责。
