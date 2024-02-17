from pathlib import Path

from diagrams import Diagram
from diagrams.c4 import (
    Container,
    Database,
    Person,
    Relationship,
    System,
    SystemBoundary,
)

FILENAME = str(Path(__file__).parent / "diagram")


graph_attr = {
    "splines": "spline",
}


with Diagram(
    "3 Tier Architecture", direction="TB", graph_attr=graph_attr, filename=FILENAME
):
    caseworker = Person(name="Caseworker", description="A person that manages cases", shape="person")
    user = Person(
        name="User", description="A person that uses the system", external=True
    )

    with SystemBoundary("Software System"):
        database = Database(
            name="Database",
            description="A database that stores cases",
            technology="PostgreSQL",
        )
        http_api = Container(
            name="HTTP API",
            description="An HTTP API that handles requests",
            technology="Django",
        )
        frontend = Container(
            name="Frontend",
            description="A frontend that displays cases",
            technology="Django",
        )

    
    user >> frontend >> Relationship("uses") >> http_api >> Relationship("uses") >> database
    caseworker >> Relationship("manages") >> frontend
