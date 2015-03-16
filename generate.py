#!/bin/env python
from ForemanExtractor import ForemanExtractor
from IcingaGenerator import IcingaGenerator

import re
import os
import sys
import itertools

configfile='config.py'

if not os.path.isfile(configfile):
    message="Config file %s not found. Exiting\n"%configfile
    sys.stderr.write(message)
    sys.exit(2)

execfile(configfile)

def hostgroup_normalform(hostgroups):
    hg=[]
    if len(hostgroups)==0:
        return hg
    for i in range(1,len(hostgroups)):
        hg.append("/"+"/".join(hostgroups[0:i]))
    return hg

foremanExt=ForemanExtractor(baseurl,auth)
icingaGen=IcingaGenerator()
h2group=foremanExt.host2hostgroup()

re_hostexclude=[]
re_hostinclude=[]
re_templates=[]


for h in hostexclude:
    re_hostexclude.append(re.compile(h))

for h in hostinclude:
    re_hostinclude.append(re.compile(h))

for (h,t) in hosttemplates.items():
    re_templates.append((re.compile(h),t))

for host in h2group.keys():

    inclusion=filter(lambda x: x.match(host),re_hostinclude)
    if len(inclusion)==0:
        continue

    exclusion=filter(lambda x: x.match(host),re_hostexclude)
    if len(exclusion)>0:
        continue

    template=None
    for (m,t) in re_templates:
        if m.match(host):
            template=t
            break

    hostgroups=h2group[host]

    print icingaGen.define_host(host,hostgroup_normalform(hostgroups),template)
    
hostgroups=list(set(itertools.chain(*[hostgroup_normalform(x) for x in h2group.values()])))

for hostgroup in hostgroups:
    print icingaGen.define_hostgroup(hostgroup)

