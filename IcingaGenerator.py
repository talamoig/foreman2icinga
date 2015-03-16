class IcingaGenerator:
    hostheader='object Host "%s" {'
    addrline='address = "%s"'
    hostgroup='object HostGroup "%s" {\ndisplay_name = "%s"\n}'
    def define_hostgroup(self,hostgroup):
        return self.hostgroup%(hostgroup,hostgroup)

    def define_host(self, hostname, hostgroups=[], template=None):
        '''
        return an Icinga2-like definition of a host
        If a template name is passed it is included as 'import' in the definition.
        If a hostgroup list is passed, they are considered as hostgroup names
        and the host is declared as part of these hostgroups.
        '''
        hostgroupline=""
        templateline=""
        if len(hostgroups)>0:
            hostgroupline="\n\tgroups = [ %s ]"%", ".join(["\"%s\""%x for x in hostgroups])        
        if template!=None:
            templateline="\n\timport \"%s\""%template
        ret="%s%s%s\n\t%s\n}"%(self.hostheader%hostname,hostgroupline,templateline,self.addrline%hostname)
        return ret
