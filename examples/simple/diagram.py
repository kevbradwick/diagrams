from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from pathlib import Path


BASE_DIR = Path(__file__).parent


with Diagram("Web Service", show=False, filename=str(BASE_DIR / "diagram")) as _:
    ELB("lb") >> EC2("web") >> RDS("userdb")  # type: ignore
