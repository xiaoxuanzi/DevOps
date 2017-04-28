import json
import logging
import settings as config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Host

logger = logging.getLogger('Allprocess')

class MachineError( Exception ): pass
class Machine( object ):

    def __init__(self, host):

        if isinstance(host, Host) is False:
            raise MachineError

        self.isVM       = host.isVM
        self.private_ip = host.private_ip
        self.public_ip  = host.public_ip
        self.os_type    = host.os_type
        self.cpu_type   = host.cpu_type
        self.cpu_num    = host.cpu_num
        self.mem        = host.mem
        self.idc        = host.idc
        self.status     = host.status
        self.remark     = host.remark
        self.disks      = self.sum_disk(host.disks)

    def __repr__(self):
        return '<Machine %r>' % self.private_ip

    def sum_disk(self, disks):

        sum   = 0

        try:
            disks = eval(disks)

            for k in disks.keys():
                d = disks[k]

                if d.endswith('GB'):
                    d = d[:-len('GB')]
                    sum += int(float(d))
                else:
                    logger.error('disks is no end with GB, ip: ' + self.private_ip)
                    sum = 'ERROR'
                    return sum

        except Exception as e:
            logger.error("ip: %s, error: %s" % (self.private_ip, e))
            sum = 'ERROR'

        return sum

class Asset(object):

    def __init__(self):

        self.Session = sessionmaker(bind = create_engine(
                                            config.SQLAlCHEMY['ENGINE']))
        self.session = self.Session()

    def host_list(self):

        hosts  = []

        ret = self.session.query(Host).all()
        for h in ret:
            m = Machine(h)
            hosts.append(m)

        return hosts

    def host_update_status(self, private_ip, status):

        # host = self.session.query(Host).filter_by(private_ip=private_ip).get(1)
        # host.status = status
        self.session.query(Host).filter_by(private_ip=private_ip).update({'status' : status})
        self.session.commit()


    def host_query(self, ip):

        host = self.session.query(Host).filter_by(private_ip=ip).one()

        return host

