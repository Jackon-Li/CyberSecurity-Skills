#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill_query.py — 网络安全技能库检索工具（零依赖，仅需 Python 3.6+）

用法:
    python scripts/skill_query.py 横向移动
    python scripts/skill_query.py kerberos --team red --limit 10
    python scripts/skill_query.py 云安全 --module 22
    python scripts/skill_query.py --list-modules
    python scripts/skill_query.py 取证 --json
"""
import argparse
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(os.path.dirname(HERE), "index.json")

TEAM_CN = {"red": "红队", "blue": "蓝队", "forensic": "取证", "": "-"}


def load_index():
    if not os.path.isfile(INDEX):
        sys.exit("[错误] 找不到 index.json，请确认脚本位于仓库 scripts/ 目录下")
    with io.open(INDEX, encoding="utf-8") as f:
        return json.load(f)


def flatten(idx):
    rows = []
    for m in idx["modules"]:
        for s in m["skills"]:
            r = dict(s)
            r["module_id"] = m["id"]
            r["module"] = m["name"]
            rows.append(r)
    return rows


def score(row, terms):
    """每个词都要命中（AND），得分按命中字段加权。"""
    cn = row.get("name") or ""
    en = (row.get("name_en") or "").lower()
    desc = (row.get("description") or "").lower()
    tags = " ".join(row.get("tags") or []).lower()
    mod = (row.get("module") or "").lower()
    total = 0
    for t in terms:
        w = 0
        if t in cn:
            w = 10
        elif t in en:
            w = 8
        elif t in tags:
            w = 6
        elif t in desc:
            w = 3
        elif t in mod:
            w = 2
        if w == 0:
            return 0
        total += w
    return total


def main():
    ap = argparse.ArgumentParser(add_help=True, description="检索网络安全技能库")
    ap.add_argument("keywords", nargs="*", help="中文或英文关键词，可多个（AND）")
    ap.add_argument("--module", help="限定分类编号，如 02")
    ap.add_argument("--team", choices=["red", "blue", "forensic"], help="限定领域")
    ap.add_argument("--limit", type=int, default=15, help="最多返回条数（默认 15）")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出")
    ap.add_argument("--list-modules", action="store_true", help="列出全部 34 个分类")
    args = ap.parse_args()

    idx = load_index()

    if args.list_modules:
        print("%-4s %-24s %-34s %s" % ("编号", "分类", "英文", "技能数"))
        print("-" * 84)
        for m in idx["modules"]:
            print("%-4s %-24s %-34s %d" % (m["id"], m["name"], m["name_en"], m["count"]))
        print("-" * 84)
        print("合计 %d 个技能 / %d 个分类" % (idx["meta"]["total_skills"], len(idx["modules"])))
        return

    if not args.keywords and not (args.module or args.team):
        ap.print_help()
        return

    terms = [k.lower() for k in args.keywords]
    rows = flatten(idx)

    if args.module:
        rows = [r for r in rows if r["module_id"] == args.module.zfill(2)]
    if args.team:
        rows = [r for r in rows if r["team"] == args.team]

    if terms:
        scored = []
        for r in rows:
            sc = score(r, terms)
            if sc:
                scored.append((sc, r))
        scored.sort(key=lambda x: (-x[0], x[1]["module_id"], x[1]["name"]))
        rows = [r for _, r in scored]

    rows = rows[: args.limit]

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return

    if not rows:
        print("未命中。试试：")
        print("  · 换中文关键词（技能名多为中文），如「横向移动」「内存马」「应急响应」")
        print("  · 用 --list-modules 查看 34 个分类")
        return

    print("命中 %d 条：\n" % len(rows))
    for i, r in enumerate(rows, 1):
        print("%2d. %s  [%s·%s]" % (i, r["name"], r["module_id"], TEAM_CN.get(r["team"], "-")))
        print("    英文: %s" % r["name_en"])
        d = (r.get("description") or "").strip().replace("\n", " ")
        print("    摘要: %s" % (d[:110] + ("…" if len(d) > 110 else "")))
        if r.get("tags"):
            print("    标签: %s" % ", ".join(r["tags"][:6]))
        print("    路径: %s\n" % r["path"])


if __name__ == "__main__":
    main()
