from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Unicode, SmallInteger
from sqlalchemy.orm import relationship, backref
import settings as config

Base = declarative_base()

class Host(Base):

    __tablename__ = 'asset_hosts'

    id = Column(Integer, primary_key=True)
    isVM       = Column(Unicode)
    private_ip = Column(Unicode)
    public_ip  = Column(Unicode)
    os_type    = Column(Unicode)
    cpu_type   = Column(Unicode)
    cpu_num    = Column(Integer)
    mem        = Column(Unicode)
    disks      = Column(Unicode)
    idc        = Column(Unicode)
    status     = Column(Unicode)
    remark     = Column(Unicode)

    def __repr__(self):
        return '<Host %r>' % self.private_ip

# engine = create_engine('mysql://ManageOS:ManageOS@10.13.89.116:3306/oms?charset=utf8')
engine = create_engine(config.SQLAlCHEMY['ENGINE'])
Base.metadata.create_all(engine)
