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
            if len(v) - len(key) > 1:
                if key != "蒙古" or (key == "蒙古" and "内蒙古" not in v):
                    ret.append(key)
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

def ethnicinfo():
    for k, v in ret.items():
        m = matches(v)
        if m: print(k, v, m, long(k, v))

province_suffix = ['省', '市', '自治区', '特别行政区']
city_suffix = ['市', '新区', '地区', '区', '县', '自治州']
county_suffix = ['自治县', '县', '新区', '区', '市']

def names(v, suffix):
    n = [v,]
    m = matches(v)
    a = v
    for i in m: a = a.replace(i, "")
    if a != v: n.append(a)
    for s in suffix:
        if a.endswith(s):
            b = a.rstrip(s)
            if len(b) > 1: n.append(b)
            else: continue
            if b == "内蒙古": n.append("内蒙")
            if s == "自治区":
                n.append(b+"省")
            if s == "自治州":
                n.append(b+"州")
                n.append(b+"市")
            if s == "自治县":
                n.append(b+"县")
            break
    return n

for k, v in ret.items():
    if k[-4:] == '0000':
        n = names(v, province_suffix)
    elif k[-2:] == '00':
        n = names(v, city_suffix)
    else:
        n = names(v, county_suffix)
    print("%s\t%s\t%s" % (k, ','.join(n), ','.join(matches(v))))
