# from spack import AutotoolsPackage, depends_on, version
import os

from spack.directives import depends_on, patch, version
from spack.package import Package
from spack.util.executable import Executable


class Genie(Package):  # Genie doesn't use Autotools
    """Genie Neutrino MC Generator."""

    homepage = "https://www.genie-mc.org"
    url = "https://github.com/GENIE-MC/Generator/archive/R-3_00_06.tar.gz"
    git = "https://github.com/GENIE-MC/Generator.git"

    tags = ["neutrino", "hep"]

    maintainers = [
        # maintainer of this recipe, not affliated with GENIE collaboration
        "davehadley",
    ]

    version("master", branch="master")
    version(
        "3_00_06",
        sha256="ab56ea85d0c1d09029254365bfe75a1427effa717389753b9e0c1b6c2eaa5eaf",
        preferred=True,
    )

    depends_on("root+pythia6")
    depends_on("pythia6")
    depends_on("lhapdf")
    depends_on("log4cpp")
    depends_on("libxml2")
    depends_on("gsl")
    depends_on("geant4")

    patch("genie_make_files.patch", level=0)

    phases = ["configure", "build", "install"]

    def configure(self, spec, prefix):
        configure = Executable("./configure")
        args = self.configure_args(spec, prefix)
        configure(*args)

    def configure_args(self, spec, prefix):
        args = [
            "--enable-lhapdf6",
            "--prefix=%s" % prefix,
            "--with-compiler=%s" % os.environ["CC"],
            "--with-lhapdf6-inc=%s" % spec["lhapdf"].prefix.include,
            "--with-lhapdf6-lib=%s" % spec["lhapdf"].prefix.lib,
            "--with-libxml2-inc=%s" % spec["libxml2"].prefix.include,
            "--with-libxml2-lib=%s" % spec["libxml2"].prefix.lib,
            "--with-log4cpp-inc=%s" % spec["log4cpp"].prefix.include,
            "--with-log4cpp-lib=%s" % spec["log4cpp"].prefix.lib,
            "--with-pythia6-lib=%s" % spec["pythia6"].prefix.lib,
        ]
        return args

    def build(self, spec, prefix):
        # make is injected by build_environment:
        # https://spack.readthedocs.io/en/latest/spack.html#module-spack.build_environment
        # apparently this is considered more readable
        make()  # noqa

    def install(self, spec, prefix):
        make("install")  # noqa

    def setup_build_environment(self, env):
        env.set("GENIE", self.stage.source_path)
        return super().setup_build_environment(env)

    def setup_run_environment(self, env):
        return super().setup_run_environment(env)
