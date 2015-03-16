import urllib2
import simplejson

class ForemanExtractor:

    api={}
    api['hostgroups']='hostgroups?per_page=1000'
    api['hosts']='hosts?per_page=1000'
    
    hostgroups=None
    hosts=None
    
    def __init__(self,baseurl,token):
        self.baseurl = baseurl
        self.auth_token = token

    def jsondata(self,api):
        req = urllib2.Request("%s/%s"%(self.baseurl,api), None, {'Authorization:Basic':self.auth_token})
        opener = urllib2.build_opener()
        f = opener.open(req)
        return simplejson.load(f)
    
    def getraw(self,what):
        return self.jsondata('api/'+self.api[what])
        
    def hostgroupid2name(self,hostgroup_id,hostgroup_json):
        ''' 
        return the hostgroup name for the given hostgroup id, 
        acording to the hostgroup_json variable 
        '''
        return filter(lambda x:x['hostgroup']['id']==hostgroup_id,hostgroup_json)[0]['hostgroup']['name']            

    def hostgroup_lineage(self,hostgroup_id,hostgroup_json):
        '''
        returns the lineage of the hostgroups with the given hostgroup_id acording to the hostgroup_json variable.
        the return variable is a list, ordered from the oldest to the latest.
        the last one is the hostgroup with the id passed to the method
        '''
        myname=self.hostgroupid2name(hostgroup_id,hostgroup_json)
        parent_id=filter(lambda x:x['hostgroup']['id']==hostgroup_id,hostgroup_json)[0]['hostgroup']['ancestry']
        if parent_id==None:
            return [myname]
        lineage=[]
        for id in parent_id.split('/'):
            lineage.append(self.hostgroupid2name(int(id),hostgroup_json))
        lineage.append(myname)
        return lineage
    
    def all_hostgroups(self):
        hostgroups=self.getraw('hostgroups')
        ids=map(lambda x: x['hostgroup']['id'],hostgroups)
        hg=map(lambda x:(x,self.hostgroup_lineage(x,hostgroups)),ids)
        ret={}
        for i,j in hg:
            ret[i]=j
        return ret

    def host2hostgroup(self):
        hostgroups=self.all_hostgroups()
        rawhosts=self.getraw('hosts')
        hosts={}
        for h in rawhosts:
            hg=[]
            if h['host']['hostgroup_id']!=None:
                hg=hostgroups[int(h['host']['hostgroup_id'])]
            hosts[h['host']['name']]=hg
        return hosts
        
