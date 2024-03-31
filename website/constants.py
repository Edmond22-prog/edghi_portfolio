from enum import Enum

from website.utils import build_enum_tuple


class EmploymentType(str, Enum):
    """
    Types of employment
    """

    FULL_TIME = "Full-time"
    PART_TIME = "Part-time"
    SELF_EMPLOYED = "Self-employed"
    FREELANCE = "Freelance"
    CONTRACT = "Contract"
    INTERNSHIP = "Internship"
    APPRENTICESHIP = "Apprenticeship"
    SEASONAL = "Seasonal"


class EmploymentLocation(str, Enum):
    """
    Types of employment location
    """

    ON_SITE = "On-site"
    REMOTE = "Remote"
    HYBRID = "Hybrid"


EMPLOYMENT_TYPES = build_enum_tuple(EmploymentType)
EMPLOYMENT_LOCATIONS = build_enum_tuple(EmploymentLocation)
