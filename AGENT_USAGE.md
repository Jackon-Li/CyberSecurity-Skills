# AGENT_USAGE · 给 AI 助手的接入说明

本文件说明如何让 AI 助手（Claude Code、WorkBuddy、Cursor 等）**高效**使用这 820 个技能。

## 核心原则：先检索，再读取

**不要**一次性读取 `index.json`（约 450 KB / 数十万字符），会吃掉大量上下文。正确做法是先跑查询脚本拿到候选，再只读命中技能的 `SKILL.md`。

```bash
python scripts/skill_query.py 域渗透 --limit 8          # 拿候选（输出很短）
python scripts/skill_query.py 域渗透 --json --limit 3   # 需要程序化处理时
```

## 推荐工作流

1. **定位**：用中文关键词或分类编号检索，得到 `name / name_en / path`。
2. **读取**：只读命中的 `SKILL.md`（通常 200–400 行）。
3. **按节执行**：`When to Use` 判断是否适用 → `Prerequisites` 检查前置条件 → `Workflow` 执行步骤 → `Validation Criteria` 自检。
4. **需要细节时**：再读同目录 `references/` 下的文档，或参考 `scripts/` 里的实现。

## 技能元数据字段

| 字段 | 含义 |
|---|---|
| `name` | 中文技能名 |
| `name_en` | 英文标识（slug），对应目录名后缀 |
| `module` | 所属分类（编号 + 中文名） |
| `team` | 领域倾向：`red` 红队 / `blue` 蓝队 / `forensic` 取证 |
| `tags` | 技术标签，用于交叉检索 |
| `path` | `SKILL.md` 的相对路径 |
| `subdomain` | 上游子域分类 |

## 检索建议

- **中文优先**：技能名与描述都有中文，中文关键词召回率高于英文。
- **英文补充**：查具体工具（sqlmap、Volatility、Semgrep）时用英文标识或标签。
- **按领域收窄**：红队任务加 `--team red`，应急取证加 `--team forensic`。

## 注意事项

- **验证小节不完整**：仅约 15% 技能有 `Validation Criteria`，5% 有独立 `## Verification`；其余需自行设计验证。
- **脚本必须审阅**：`scripts/` 为参考实现，可能包含占位符、硬编码路径或需要特定环境；直接在生产环境执行有风险。
- **授权边界**：仅对已授权目标使用；AI 助手应先确认授权范围再给出攻击性操作步骤。
