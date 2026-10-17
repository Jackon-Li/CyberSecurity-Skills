# 03-Web应用安全 · WebApplicationSecurity

> 本分类共 **47** 个技能（红队 47）。

每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。

| # | 技能 | 英文标识 | 摘要 | 路径 |
|---|---|---|---|---|
| 1 | **AFL++二进制模糊测试** | `performing-fuzzing-with-aflplusplus` | Performs coverage-guided fuzzing of compiled binaries with AFL++, inst… | [SKILL.md](skills/AFL++二进制模糊测试_performing-fuzzing-with-aflplusplus/SKILL.md) |
| 2 | **CORS配置错误测试** | `testing-cors-misconfiguration` | Identifying and exploiting Cross-Origin Resource Sharing misconfigurat… | [SKILL.md](skills/CORS配置错误测试_testing-cors-misconfiguration/SKILL.md) |
| 3 | **CSP策略绕过测试** | `performing-content-security-policy-bypass` | Analyze Content-Security-Policy headers and bypass them to achieve cro… | [SKILL.md](skills/CSP策略绕过测试_performing-content-security-policy-bypass/SKILL.md) |
| 4 | **CSRF攻击模拟** | `performing-csrf-attack-simulation` | Testing web applications for Cross-Site Request Forgery vulnerabilitie… | [SKILL.md](skills/CSRF攻击模拟_performing-csrf-attack-simulation/SKILL.md) |
| 5 | **DevSecOps自动化安全扫描** | `implementing-devsecops-security-scanning` | Integrates SAST, DAST, and SCA into CI/CD pipelines using Semgrep for… | [SKILL.md](skills/DevSecOps自动化安全扫描_implementing-devsecops-security-scanning/SKILL.md) |
| 6 | **GraphQL安全评估** | `performing-graphql-security-assessment` | Assessing GraphQL API endpoints for introspection leaks, injection att… | [SKILL.md](skills/GraphQL安全评估_performing-graphql-security-assessment/SKILL.md) |
| 7 | **HTTP参数污染攻击** | `performing-http-parameter-pollution-attack` | Executes HTTP Parameter Pollution attacks that inject duplicate reques… | [SKILL.md](skills/HTTP参数污染攻击_performing-http-parameter-pollution-attack/SKILL.md) |
| 8 | **HTTP请求走私利用** | `exploiting-http-request-smuggling` | Detects and exploits HTTP request smuggling caused by Content-Length/T… | [SKILL.md](skills/HTTP请求走私利用_exploiting-http-request-smuggling/SKILL.md) |
| 9 | **Host头注入测试** | `testing-for-host-header-injection` | Test web applications for HTTP Host header injection vulnerabilities t… | [SKILL.md](skills/Host头注入测试_testing-for-host-header-injection/SKILL.md) |
| 10 | **IDOR越权利用** | `exploiting-idor-vulnerabilities` | Identifies and exploits Insecure Direct Object Reference (IDOR) vulner… | [SKILL.md](skills/IDOR越权利用_exploiting-idor-vulnerabilities/SKILL.md) |
| 11 | **JWT令牌安全测试** | `testing-jwt-token-security` | Assessing JSON Web Token implementations for cryptographic weaknesses,… | [SKILL.md](skills/JWT令牌安全测试_testing-jwt-token-security/SKILL.md) |
| 12 | **JWT漏洞测试** | `testing-for-json-web-token-vulnerabilities` | Tests JWT implementations for algorithm confusion, "none" algorithm by… | [SKILL.md](skills/JWT漏洞测试_testing-for-json-web-token-vulnerabilities/SKILL.md) |
| 13 | **JavaScript原型链污染利用** | `exploiting-prototype-pollution-in-javascript` | Detects and exploits JavaScript prototype pollution vulnerabilities in… | [SKILL.md](skills/JavaScript原型链污染利用_exploiting-prototype-pollution-in-javascript/SKILL.md) |
| 14 | **ModSecurity日志审计** | `implementing-web-application-logging-with-modsecurity` | Configure ModSecurity WAF with the OWASP Core Rule Set (CRS) for web a… | [SKILL.md](skills/ModSecurity日志审计_implementing-web-application-logging-with-modsecurity/SKILL.md) |
| 15 | **NoSQL注入漏洞利用** | `exploiting-nosql-injection-vulnerabilities` | Detects and exploits NoSQL injection vulnerabilities in MongoDB, Couch… | [SKILL.md](skills/NoSQL注入漏洞利用_exploiting-nosql-injection-vulnerabilities/SKILL.md) |
| 16 | **OAuth配置错误利用** | `exploiting-oauth-misconfiguration` | Identifying and exploiting OAuth 2.0 and OpenID Connect misconfigurati… | [SKILL.md](skills/OAuth配置错误利用_exploiting-oauth-misconfiguration/SKILL.md) |
| 17 | **OWASP API安全测试** | `testing-api-security-with-owasp-top-10` | Systematically assesses REST, GraphQL, and gRPC API endpoints against… | [SKILL.md](skills/OWASP API安全测试_testing-api-security-with-owasp-top-10/SKILL.md) |
| 18 | **PHP类型混淆利用** | `exploiting-type-juggling-vulnerabilities` | Exploits PHP type juggling vulnerabilities caused by loose (==) compar… | [SKILL.md](skills/PHP类型混淆利用_exploiting-type-juggling-vulnerabilities/SKILL.md) |
| 19 | **RASP应用自保护部署** | `implementing-runtime-application-self-protection` | Deploy Runtime Application Self-Protection (RASP) agents to detect and… | [SKILL.md](skills/RASP应用自保护部署_implementing-runtime-application-self-protection/SKILL.md) |
| 20 | **REST API批量赋值利用** | `exploiting-mass-assignment-in-rest-apis` | Discovers and exploits mass assignment (autobinding) in REST APIs by i… | [SKILL.md](skills/REST API批量赋值利用_exploiting-mass-assignment-in-rest-apis/SKILL.md) |
| 21 | **SSRF服务端请求伪造利用** | `exploiting-server-side-request-forgery` | Identifying and exploiting SSRF vulnerabilities to access internal ser… | [SKILL.md](skills/SSRF服务端请求伪造利用_exploiting-server-side-request-forgery/SKILL.md) |
| 22 | **Subfinder子域名枚举** | `performing-subdomain-enumeration-with-subfinder` | Enumerate subdomains of target domains using ProjectDiscovery's Subfin… | [SKILL.md](skills/Subfinder子域名枚举_performing-subdomain-enumeration-with-subfinder/SKILL.md) |
| 23 | **WAF绕过测试** | `performing-web-application-firewall-bypass` | Bypasses Web Application Firewall protections using encoding tricks, H… | [SKILL.md](skills/WAF绕过测试_performing-web-application-firewall-bypass/SKILL.md) |
| 24 | **WebSocket漏洞利用** | `exploiting-websocket-vulnerabilities` | Testing WebSocket implementations for authentication bypass, cross-sit… | [SKILL.md](skills/WebSocket漏洞利用_exploiting-websocket-vulnerabilities/SKILL.md) |
| 25 | **Web与AI安全测试知识库** | `secknowledge-skill` | \| Web+AI 安全测试知识库。融合 WooYun 88,636 案例 + 先知 L1-L4 方法论 + GAARM 173 风险 + O… | [SKILL.md](skills/Web与AI安全测试知识库_secknowledge-skill/SKILL.md) |
| 26 | **Web缓存投毒攻击** | `performing-web-cache-poisoning-attack` | Exploiting web cache mechanisms to serve malicious content to other us… | [SKILL.md](skills/Web缓存投毒攻击_performing-web-cache-poisoning-attack/SKILL.md) |
| 27 | **Web缓存欺骗攻击** | `performing-web-cache-deception-attack` | Executes web cache deception attacks by exploiting path normalization… | [SKILL.md](skills/Web缓存欺骗攻击_performing-web-cache-deception-attack/SKILL.md) |
| 28 | **XML注入漏洞测试** | `testing-for-xml-injection-vulnerabilities` | Test web applications for XML injection vulnerabilities including XXE,… | [SKILL.md](skills/XML注入漏洞测试_testing-for-xml-injection-vulnerabilities/SKILL.md) |
| 29 | **XSS漏洞测试** | `testing-for-xss-vulnerabilities-with-burpsuite` | Identifying and validating cross-site scripting vulnerabilities using… | [SKILL.md](skills/XSS漏洞测试_testing-for-xss-vulnerabilities-with-burpsuite/SKILL.md) |
| 30 | **XXE注入漏洞测试** | `testing-for-xxe-injection-vulnerabilities` | Discovering and exploiting XML External Entity injection vulnerabiliti… | [SKILL.md](skills/XXE注入漏洞测试_testing-for-xxe-injection-vulnerabilities/SKILL.md) |
| 31 | **sqlmap注入利用** | `exploiting-sql-injection-with-sqlmap` | Detecting and exploiting SQL injection vulnerabilities using sqlmap to… | [SKILL.md](skills/sqlmap注入利用_exploiting-sql-injection-with-sqlmap/SKILL.md) |
| 32 | **不安全反序列化利用** | `exploiting-insecure-deserialization` | Identifying and exploiting insecure deserialization vulnerabilities in… | [SKILL.md](skills/不安全反序列化利用_exploiting-insecure-deserialization/SKILL.md) |
| 33 | **业务逻辑漏洞测试** | `testing-for-business-logic-vulnerabilities` | Manually identifies flaws in application business logic - price manipu… | [SKILL.md](skills/业务逻辑漏洞测试_testing-for-business-logic-vulnerabilities/SKILL.md) |
| 34 | **二次SQL注入利用** | `performing-second-order-sql-injection` | Detect and exploit second-order SQL injection vulnerabilities where ma… | [SKILL.md](skills/二次SQL注入利用_performing-second-order-sql-injection/SKILL.md) |
| 35 | **失效访问控制测试** | `testing-for-broken-access-control` | Systematically tests web applications and APIs for broken access contr… | [SKILL.md](skills/失效访问控制测试_testing-for-broken-access-control/SKILL.md) |
| 36 | **安全响应头审计** | `performing-security-headers-audit` | Auditing HTTP security headers including CSP, HSTS, X-Frame-Options, a… | [SKILL.md](skills/安全响应头审计_performing-security-headers-audit/SKILL.md) |
| 37 | **开放重定向漏洞测试** | `testing-for-open-redirect-vulnerabilities` | Identifies and exploits open redirect vulnerabilities by analyzing URL… | [SKILL.md](skills/开放重定向漏洞测试_testing-for-open-redirect-vulnerabilities/SKILL.md) |
| 38 | **强制浏览绕过认证** | `bypassing-authentication-with-forced-browsing` | Discovering and accessing unprotected pages, APIs, and administrative… | [SKILL.md](skills/强制浏览绕过认证_bypassing-authentication-with-forced-browsing/SKILL.md) |
| 39 | **敏感数据泄露测试** | `testing-for-sensitive-data-exposure` | Identifying sensitive data exposure vulnerabilities including API key… | [SKILL.md](skills/敏感数据泄露测试_testing-for-sensitive-data-exposure/SKILL.md) |
| 40 | **断链劫持利用** | `exploiting-broken-link-hijacking` | Discovers and exploits broken link hijacking by spidering a site (Burp… | [SKILL.md](skills/断链劫持利用_exploiting-broken-link-hijacking/SKILL.md) |
| 41 | **服务端模板注入利用** | `exploiting-template-injection-vulnerabilities` | Detects and exploits Server-Side Template Injection (SSTI) vulnerabili… | [SKILL.md](skills/服务端模板注入利用_exploiting-template-injection-vulnerabilities/SKILL.md) |
| 42 | **点击劫持攻击测试** | `performing-clickjacking-attack-test` | Testing web applications for clickjacking vulnerabilities by assessing… | [SKILL.md](skills/点击劫持攻击测试_performing-clickjacking-attack-test/SKILL.md) |
| 43 | **目录遍历漏洞测试** | `performing-directory-traversal-testing` | Test web applications for path traversal and Local/Remote File Inclusi… | [SKILL.md](skills/目录遍历漏洞测试_performing-directory-traversal-testing/SKILL.md) |
| 44 | **盲SSRF漏洞利用** | `performing-blind-ssrf-exploitation` | Detect and exploit blind Server-Side Request Forgery (SSRF) using out-… | [SKILL.md](skills/盲SSRF漏洞利用_performing-blind-ssrf-exploitation/SKILL.md) |
| 45 | **竞态条件漏洞利用** | `exploiting-race-condition-vulnerabilities` | Detects and exploits race condition (TOCTOU) vulnerabilities in web ap… | [SKILL.md](skills/竞态条件漏洞利用_exploiting-race-condition-vulnerabilities/SKILL.md) |
| 46 | **软件供应链攻击模拟** | `performing-supply-chain-attack-simulation` | Simulates and detects software supply chain attacks: typosquatting det… | [SKILL.md](skills/软件供应链攻击模拟_performing-supply-chain-attack-simulation/SKILL.md) |
| 47 | **邮件头注入测试** | `testing-for-email-header-injection` | Tests web application email functionality (contact forms, password res… | [SKILL.md](skills/邮件头注入测试_testing-for-email-header-injection/SKILL.md) |

---

← 返回 [仓库首页](../README.md) · 索引见 [index.json](../index.json)
