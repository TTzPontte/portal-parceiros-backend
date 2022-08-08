from dataclasses import dataclass
from common.dao_pkg.dynamo.base_dao import BaseDAO
import os

API_ID = os.getenv("APP_SYNC_API_ID");
ENV = os.getenv("ENV"); 

def curate(table_name):
    return f"{table_name}-{API_ID}-{ENV}"

@dataclass
class UserInviteDAO(BaseDAO):
    table_name: str = curate("UserInvite")


@dataclass
class UserDAO(BaseDAO):
    table_name: str = curate("User")


@dataclass
class MemberDAO(BaseDAO):
    table_name: str = curate("Member")


@dataclass
class LeadDAO(BaseDAO):
    table_name: str = curate("Lead")


@dataclass
class OrganizationDAO(BaseDAO):
    table_name: str = curate("Organization")


@dataclass
class SimulationDAO(BaseDAO):
    table_name: str = curate("Simulation")


@dataclass
class WhiteLabelDAO(BaseDAO):
    table_name: str = curate("WhiteLabel")

