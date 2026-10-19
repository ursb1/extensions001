import json

SRC = "index.json"
DST = "index.gh-proxy.json"
PREFIX = "https://gh-proxy.com/"

def rewrite(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "apkUrl" and isinstance(v, str):
                if v.startswith("https://github.com/") and not v.startswith(PREFIX):
                    obj[k] = PREFIX + v
            else:
                rewrite(v)
    elif isinstance(obj, list):
        for item in obj:
            rewrite(item)

with open(SRC, "r", encoding="utf-8") as f:
    data = json.load(f)

rewrite(data)

with open(DST, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("已生成:", DST)