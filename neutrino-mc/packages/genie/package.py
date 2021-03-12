# from spack import AutotoolsPackage, depends_on, version
from spack.build_systems.autotools import AutotoolsPackage
from spack.directives import depends_on, version


class Genie(AutotoolsPackage):
    """Genie Generator."""

    homepage = "https://www.genie-mc.org"
    url = "https://github.com/GENIE-MC/Generator/archive/R-3_00_06.tar.gz"

    amaintainers = [
        "davehadley",
    ]

    version(
        "3_00_06",
        sha256="ab56ea85d0c1d09029254365bfe75a1427effa717389753b9e0c1b6c2eaa5eaf",
    )

    depends_on("root")
    depends_on("pythia6")
    depends_on("lhapdf")
    depends_on("log4cpp")
    depends_on("libxml2")
    depends_on("gsl")
    depends_on("geant4")

    def configure_args(self):
        args = []
        return args
