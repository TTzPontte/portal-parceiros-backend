from dataclasses import dataclass
from common.dao_pkg.graphql.base_dao import BaseDAO


@dataclass
class UserInviteDAO(BaseDAO):
    table_name: str = "UserInvite"


@dataclass
class UserDAO(BaseDAO):
    table_name: str = "User"


@dataclass
class MemberDAO(BaseDAO):
    table_name: str = "Member"


@dataclass
class LeadDAO(BaseDAO):
    table_name: str = "Lead"


@dataclass
class OrganizationDAO(BaseDAO):
    table_name: str = "Organization"


@dataclass
class SimulationDAO(BaseDAO):
    table_name: str = "Simulation"


@dataclass
class WhiteLabelDAO(BaseDAO):
    table_name: str = "WhiteLabel"


