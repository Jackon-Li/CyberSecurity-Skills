# 02 · 红队

[← 仓库首页](../README.md) · 分类 **02** · `RedTeaming` · **35** 个技能 · 领域 **红队**

> 每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。
> 技能内容**转载自上游开源项目，非原创**，版权归原作者所有。详见[来源与版权](../README.md#来源与版权)与[使用边界](../SECURITY.md)。

| # | 技能 | 英文标识 | 摘要 | 入口 |
|---|---|---|---|---|
| 1 | **ADCS ESC1漏洞利用** | `exploiting-active-directory-certificate-services-esc1` | Exploit misconfigured Active Directory Certificate Services (AD CS) ES… | [SKILL.md](skills/ADCS%20ESC1漏洞利用_exploiting-active-directory-certificate-services-esc1/SKILL.md) |
| 2 | **AD林信任攻击** | `performing-active-directory-forest-trust-attack` | Enumerate and audit Active Directory forest trust relationships using… | [SKILL.md](skills/AD林信任攻击_performing-active-directory-forest-trust-attack/SKILL.md) |
| 3 | **BloodHound AD利用** | `exploiting-active-directory-with-bloodhound` | BloodHound is a graph-based Active Directory reconnaissance tool that… | [SKILL.md](skills/BloodHound%20AD利用_exploiting-active-directory-with-bloodhound/SKILL.md) |
| 4 | **BloodHound AD攻击路径分析** | `performing-active-directory-bloodhound-analysis` | Use BloodHound and SharpHound (or AzureHound) to enumerate Active Dire… | [SKILL.md](skills/BloodHound%20AD攻击路径分析_performing-active-directory-bloodhound-analysis/SKILL.md) |
| 5 | **BloodHound内网侦察** | `conducting-internal-reconnaissance-with-bloodhound-ce` | Conduct internal Active Directory reconnaissance using BloodHound Comm… | [SKILL.md](skills/BloodHound内网侦察_conducting-internal-reconnaissance-with-bloodhound-ce/SKILL.md) |
| 6 | **BloodHound攻击路径映射** | `mapping-attack-paths-with-bloodhound-ce` | Collect Active Directory data with SharpHound and Entra ID data with A… | [SKILL.md](skills/BloodHound攻击路径映射_mapping-attack-paths-with-bloodhound-ce/SKILL.md) |
| 7 | **C2重定向器搭建** | `building-c2-redirector-infrastructure` | Build dumb-pipe and traffic-filtering C2 redirectors with nginx (proxy… | [SKILL.md](skills/C2重定向器搭建_building-c2-redirector-infrastructure/SKILL.md) |
| 8 | **Certipy ADCS利用** | `exploiting-adcs-with-certipy` | Use Certipy to enumerate AD CS certificate authorities and templates o… | [SKILL.md](skills/Certipy%20ADCS利用_exploiting-adcs-with-certipy/SKILL.md) |
| 9 | **Covenant红队演练** | `performing-red-team-with-covenant` | Conducts red team operations using the Covenant C2 framework for autho… | [SKILL.md](skills/Covenant红队演练_performing-red-team-with-covenant/SKILL.md) |
| 10 | **DCSync域持久化** | `conducting-domain-persistence-with-dcsync` | Perform DCSync attacks by abusing MS-DRSR replication rights (DS-Repli… | [SKILL.md](skills/DCSync域持久化_conducting-domain-persistence-with-dcsync/SKILL.md) |
| 11 | **DPAPI凭据窃取** | `abusing-dpapi-for-credential-access` | Extract and decrypt Windows DPAPI-protected secrets (Credential Manage… | [SKILL.md](skills/DPAPI凭据窃取_abusing-dpapi-for-credential-access/SKILL.md) |
| 12 | **EvilGinx3初始访问** | `performing-initial-access-with-evilginx3` | Perform authorized initial access using EvilGinx3 adversary-in-the-mid… | [SKILL.md](skills/EvilGinx3初始访问_performing-initial-access-with-evilginx3/SKILL.md) |
| 13 | **Havoc C2设施搭建** | `building-red-team-c2-infrastructure-with-havoc` | Deploy and configure the Havoc C2 framework (teamserver, HTTPS/HTTP/SM… | [SKILL.md](skills/Havoc%20C2设施搭建_building-red-team-c2-infrastructure-with-havoc/SKILL.md) |
| 14 | **Havoc C2运营** | `operating-havoc-c2` | Deploy a Havoc C2 team server with Yaotl malleable profiles, generate… | [SKILL.md](skills/Havoc%20C2运营_operating-havoc-c2/SKILL.md) |
| 15 | **Impacket Kerberoasting** | `exploiting-kerberoasting-with-impacket` | Performs Kerberoasting (MITRE ATT&CK T1558.003) using Impacket's GetUs… | [SKILL.md](skills/Impacket%20Kerberoasting_exploiting-kerberoasting-with-impacket/SKILL.md) |
| 16 | **Kerberoasting攻击执行** | `performing-kerberoasting-attack` | Perform Kerberoasting, a post-exploitation technique that enumerates A… | [SKILL.md](skills/Kerberoasting攻击执行_performing-kerberoasting-attack/SKILL.md) |
| 17 | **LaZagne凭据窃取** | `performing-credential-access-with-lazagne` | Extract stored credentials from compromised endpoints using the LaZagn… | [SKILL.md](skills/LaZagne凭据窃取_performing-credential-access-with-lazagne/SKILL.md) |
| 18 | **Linux权限提升** | `performing-privilege-escalation-on-linux` | Guides manual enumeration and automated tooling to escalate from a low… | [SKILL.md](skills/Linux权限提升_performing-privilege-escalation-on-linux/SKILL.md) |
| 19 | **NTLM中继ADCS利用** | `relaying-ntlm-for-adcs-esc8` | Uses Impacket's ntlmrelayx.py with a coercion tool (PetitPotam, Coerce… | [SKILL.md](skills/NTLM中继ADCS利用_relaying-ntlm-for-adcs-esc8/SKILL.md) |
| 20 | **OSINT情报收集** | `performing-open-source-intelligence-gathering` | Open Source Intelligence (OSINT) gathering is the first active phase o… | [SKILL.md](skills/OSINT情报收集_performing-open-source-intelligence-gathering/SKILL.md) |
| 21 | **Sliver C2设施搭建** | `building-c2-infrastructure-with-sliver-framework` | Deploy and harden a Sliver C2 team server (BishopFox's Go-based advers… | [SKILL.md](skills/Sliver%20C2设施搭建_building-c2-infrastructure-with-sliver-framework/SKILL.md) |
| 22 | **Sliver C2运营** | `operating-sliver-c2` | Stand up a Sliver C2 server and mTLS listeners, generate cross-platfor… | [SKILL.md](skills/Sliver%20C2运营_operating-sliver-c2/SKILL.md) |
| 23 | **Zerologon漏洞利用** | `exploiting-zerologon-vulnerability-cve-2020-1472` | Exploits the Zerologon vulnerability (CVE-2020-1472) in the Netlogon R… | [SKILL.md](skills/Zerologon漏洞利用_exploiting-zerologon-vulnerability-cve-2020-1472/SKILL.md) |
| 24 | **noPac漏洞利用** | `exploiting-nopac-cve-2021-42278-42287` | Exploits the noPac Active Directory privilege-escalation chain (CVE-20… | [SKILL.md](skills/noPac漏洞利用_exploiting-nopac-cve-2021-42278-42287/SKILL.md) |
| 25 | **wmiexec横向移动** | `performing-lateral-movement-with-wmiexec` | Perform lateral movement across Windows networks using WMI-based remot… | [SKILL.md](skills/wmiexec横向移动_performing-lateral-movement-with-wmiexec/SKILL.md) |
| 26 | **全面红队演练** | `conducting-full-scope-red-team-engagement` | Plan and execute a comprehensive, MITRE ATT&CK-aligned red team engage… | [SKILL.md](skills/全面红队演练_conducting-full-scope-red-team-engagement/SKILL.md) |
| 27 | **受限委派滥用利用** | `exploiting-constrained-delegation-abuse` | Exploits Kerberos Constrained Delegation misconfigurations in Active D… | [SKILL.md](skills/受限委派滥用利用_exploiting-constrained-delegation-abuse/SKILL.md) |
| 28 | **定向钓鱼模拟演练** | `conducting-spearphishing-simulation-campaign` | Run a targeted spearphishing simulation for initial access by developi… | [SKILL.md](skills/定向钓鱼模拟演练_conducting-spearphishing-simulation-campaign/SKILL.md) |
| 29 | **影子凭据提权利用** | `abusing-shadow-credentials-for-privesc` | Take over Active Directory accounts by writing attacker-controlled pub… | [SKILL.md](skills/影子凭据提权利用_abusing-shadow-credentials-for-privesc/SKILL.md) |
| 30 | **永恒之蓝漏洞利用** | `exploiting-ms17-010-eternalblue-vulnerability` | Detects and exploits MS17-010 (EternalBlue), a critical remote code ex… | [SKILL.md](skills/永恒之蓝漏洞利用_exploiting-ms17-010-eternalblue-vulnerability/SKILL.md) |
| 31 | **物理入侵评估** | `performing-physical-intrusion-assessment` | Conduct authorized physical penetration testing against facilities, se… | [SKILL.md](skills/物理入侵评估_performing-physical-intrusion-assessment/SKILL.md) |
| 32 | **社工借口电话演练** | `conducting-social-engineering-pretext-call` | Plan and execute authorized vishing (voice phishing) pretext calls to… | [SKILL.md](skills/社工借口电话演练_conducting-social-engineering-pretext-call/SKILL.md) |
| 33 | **票据传递攻击执行** | `conducting-pass-the-ticket-attack` | Perform Pass-the-Ticket (PtT) lateral movement by extracting Kerberos… | [SKILL.md](skills/票据传递攻击执行_conducting-pass-the-ticket-attack/SKILL.md) |
| 34 | **红队演练规划** | `executing-red-team-engagement-planning` | Build the foundational red team engagement plan - scope definition, Ru… | [SKILL.md](skills/红队演练规划_executing-red-team-engagement-planning/SKILL.md) |
| 35 | **认证强制攻击利用** | `coercing-authentication-with-coercer-petitpotam` | Trigger machine account authentication with PetitPotam (MS-EFSR) and C… | [SKILL.md](skills/认证强制攻击利用_coercing-authentication-with-coercer-petitpotam/SKILL.md) |

---

<sub>本页由脚本生成 · 技能内容转载自上游项目，非原创 · [返回首页](../README.md) · [索引](../index.json) · [使用边界](../SECURITY.md)</sub>
