#!/usr/bin/python
country = {}
for line in open('world.txt'):
    item = line.strip().split('\t')
    country[item[0]] = 'g:'+item[1]
    country[item[1]] = 'g:'+item[1]
    country[item[2]] = 'g:'+item[1]
capital = {}
for line in open('capital.man.txt'):
    item = line.strip().split('\t')
    if item[0] not in country:
        country[item[0]] = 'g:'+item[0]
    for x in item[1:]:
        capital[x] = country[item[0]]+':'+x
for k,v in country.iteritems():
    print '%s\t%s' % (k,v)
    
for k,v in capital.iteritems():
    print '%s\t%s' % (k,v)
