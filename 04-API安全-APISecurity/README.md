# 04-API安全 · APISecurity

> 本分类共 **28** 个技能（红队 28）。

每个技能为独立目录，内含 `SKILL.md`（入口）、`references/`（补充资料）、`scripts/`（可运行脚本）与 `LICENSE`。

| # | 技能 | 英文标识 | 摘要 | 路径 |
|---|---|---|---|---|
| 1 | **42Crunch平台API安全测试** | `implementing-api-security-testing-with-42crunch` | Implements API security testing on the 42Crunch platform, combining AP… | [SKILL.md](skills/42Crunch平台API安全测试_implementing-api-security-testing-with-42crunch/SKILL.md) |
| 2 | **API功能级越权利用** | `exploiting-broken-function-level-authorization` | Tests APIs for Broken Function Level Authorization (OWASP API5:2023) b… | [SKILL.md](skills/API功能级越权利用_exploiting-broken-function-level-authorization/SKILL.md) |
| 3 | **API安全态势管理** | `implementing-api-security-posture-management` | Implements API Security Posture Management (API-SPM) to continuously d… | [SKILL.md](skills/API安全态势管理_implementing-api-security-posture-management/SKILL.md) |
| 4 | **API密钥安全控制** | `implementing-api-key-security-controls` | Implements secure API key generation with sufficient entropy, server-s… | [SKILL.md](skills/API密钥安全控制_implementing-api-key-security-controls/SKILL.md) |
| 5 | **API对象属性越权检测** | `detecting-broken-object-property-level-authorization` | Detect and test for OWASP API3:2023 Broken Object Property Level Autho… | [SKILL.md](skills/API对象属性越权检测_detecting-broken-object-property-level-authorization/SKILL.md) |
| 6 | **API对象级越权测试** | `testing-api-for-broken-object-level-authorization` | Tests REST and GraphQL APIs for Broken Object Level Authorization (BOL… | [SKILL.md](skills/API对象级越权测试_testing-api-for-broken-object-level-authorization/SKILL.md) |
| 7 | **API批量赋值漏洞测试** | `testing-api-for-mass-assignment-vulnerability` | Tests APIs for mass assignment (auto-binding), OWASP API3:2023, by ide… | [SKILL.md](skills/API批量赋值漏洞测试_testing-api-for-mass-assignment-vulnerability/SKILL.md) |
| 8 | **API枚举攻击检测** | `detecting-api-enumeration-attacks` | Detect API enumeration attacks (BOLA/IDOR, OWASP API1:2023) by writing… | [SKILL.md](skills/API枚举攻击检测_detecting-api-enumeration-attacks/SKILL.md) |
| 9 | **API模式校验安全** | `implementing-api-schema-validation-security` | Implements API schema validation using OpenAPI Specification and JSON… | [SKILL.md](skills/API模式校验安全_implementing-api-schema-validation-security/SKILL.md) |
| 10 | **API注入漏洞利用** | `exploiting-api-injection-vulnerabilities` | Tests API parameters, headers, and request bodies for injection flaws… | [SKILL.md](skills/API注入漏洞利用_exploiting-api-injection-vulnerabilities/SKILL.md) |
| 11 | **API网关安全控制** | `implementing-api-gateway-security-controls` | Configures API gateways such as Kong, AWS API Gateway, Azure APIM, or… | [SKILL.md](skills/API网关安全控制_implementing-api-gateway-security-controls/SKILL.md) |
| 12 | **API认证弱点测试** | `testing-api-authentication-weaknesses` | Tests API authentication mechanisms for weaknesses including broken to… | [SKILL.md](skills/API认证弱点测试_testing-api-authentication-weaknesses/SKILL.md) |
| 13 | **API资产盘点与发现** | `performing-api-inventory-and-discovery` | Performs API inventory and discovery to identify all API endpoints in… | [SKILL.md](skills/API资产盘点与发现_performing-api-inventory-and-discovery/SKILL.md) |
| 14 | **API过度数据暴露利用** | `exploiting-excessive-data-exposure-in-api` | Tests APIs for excessive data exposure (OWASP API3:2023) by intercepti… | [SKILL.md](skills/API过度数据暴露利用_exploiting-excessive-data-exposure-in-api/SKILL.md) |
| 15 | **API限流与节流实施** | `implementing-api-rate-limiting-and-throttling` | Implements API rate limiting and throttling with token bucket, sliding… | [SKILL.md](skills/API限流与节流实施_implementing-api-rate-limiting-and-throttling/SKILL.md) |
| 16 | **API限流滥用检测** | `implementing-api-abuse-detection-with-rate-limiting` | Implements API abuse detection using token bucket, sliding window, and… | [SKILL.md](skills/API限流滥用检测_implementing-api-abuse-detection-with-rate-limiting/SKILL.md) |
| 17 | **API限流绕过测试** | `performing-api-rate-limiting-bypass` | Tests API rate limiting for bypass vulnerabilities using Python (reque… | [SKILL.md](skills/API限流绕过测试_performing-api-rate-limiting-bypass/SKILL.md) |
| 18 | **Apigee网关API威胁防护** | `implementing-api-threat-protection-with-apigee` | Implements API threat protection using Google Apigee reverse-proxy pol… | [SKILL.md](skills/Apigee网关API威胁防护_implementing-api-threat-protection-with-apigee/SKILL.md) |
| 19 | **GraphQL内省攻击** | `performing-graphql-introspection-attack` | Performs GraphQL introspection attacks that extract the full API schem… | [SKILL.md](skills/GraphQL内省攻击_performing-graphql-introspection-attack/SKILL.md) |
| 20 | **GraphQL深度限制攻击** | `performing-graphql-depth-limit-attack` | Execute and test GraphQL depth limit attacks using deeply nested recur… | [SKILL.md](skills/GraphQL深度限制攻击_performing-graphql-depth-limit-attack/SKILL.md) |
| 21 | **JWT空算法攻击** | `performing-jwt-none-algorithm-attack` | Execute and test the JWT none algorithm attack, crafting tokens with t… | [SKILL.md](skills/JWT空算法攻击_performing-jwt-none-algorithm-attack/SKILL.md) |
| 22 | **JWT算法混淆攻击利用** | `exploiting-jwt-algorithm-confusion-attack` | Exploits JWT algorithm confusion where the server's verification libra… | [SKILL.md](skills/JWT算法混淆攻击利用_exploiting-jwt-algorithm-confusion-attack/SKILL.md) |
| 23 | **OAuth2实现缺陷测试** | `testing-oauth2-implementation-flaws` | Tests OAuth 2.0 and OpenID Connect implementations for authorization c… | [SKILL.md](skills/OAuth2实现缺陷测试_testing-oauth2-implementation-flaws/SKILL.md) |
| 24 | **Postman工具API安全测试** | `performing-api-security-testing-with-postman` | Uses Postman to build structured API security test collections coverin… | [SKILL.md](skills/Postman工具API安全测试_performing-api-security-testing-with-postman/SKILL.md) |
| 25 | **RESTler工具API模糊测试** | `performing-api-fuzzing-with-restler` | Uses Microsoft RESTler to perform stateful REST API fuzzing: compiles… | [SKILL.md](skills/RESTler工具API模糊测试_performing-api-fuzzing-with-restler/SKILL.md) |
| 26 | **SOAP服务安全测试** | `performing-soap-web-service-security-testing` | Performs security testing of SOAP web services by analyzing WSDL defin… | [SKILL.md](skills/SOAP服务安全测试_performing-soap-web-service-security-testing/SKILL.md) |
| 27 | **WebSocket API安全测试** | `testing-websocket-api-security` | Tests WebSocket API implementations for missing upgrade-handshake auth… | [SKILL.md](skills/WebSocket API安全测试_testing-websocket-api-security/SKILL.md) |
| 28 | **影子API端点发现** | `detecting-shadow-api-endpoints` | Discover and inventory shadow API endpoints that operate outside docum… | [SKILL.md](skills/影子API端点发现_detecting-shadow-api-endpoints/SKILL.md) |

---

← 返回 [仓库首页](../README.md) · 索引见 [index.json](../index.json)
