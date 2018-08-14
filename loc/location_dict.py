import glob
import json
files = glob.glob("data/*.json")
files.sort()
ret = {}
for f in files:
    items = json.loads(open(f).read())
    for k, v in items.items(): ret[k] = v
out = "loc_cn.json"
#open(out, "w").write(json.dumps(ret, ensure_ascii=False, indent=2))
print("write %d locations to %s" % (len(ret), out))

ethnic = open("../ethnicgroups/dict.txt").read().split()
ethnic_abbr = [x[:-1] for x in ethnic if len(x) >= 3]
ethnicset = set(ethnic + ethnic_abbr)
import pygtrie as trie
t = trie.CharTrie()
for w in ethnicset: t[w] = w

def matches(v):
    n = len(v)
    i = 0
    ret = []
    while i < n:
        key, _ = t.longest_prefix(v[i:])
        if key is not None:
            if len(v) - len(key) > 1: ret.append(key)
            i += len(key)
        else:
            i += 1
    return ret

def long(k ,v):
    if k[-4:] == "0000":
        return v
    elif k[-2:] == "00":
        return "%s:%s" % (ret[k[:2]+"0000"], v)
    else:
        if k[:4]+"00" in ret:
            return "%s:%s:%s" % (ret[k[:2]+"0000"], ret[k[:4]+"00"], v)
        else:
            return "%s:%s" % (ret[k[:2]+"0000"], v)

for k, v in ret.items():
    m = matches(v)
    if m:
        print(k, v, m, long(k, v))

