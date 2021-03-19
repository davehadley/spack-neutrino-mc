# from spack import AutotoolsPackage, depends_on, version
import os

from spack.directives import depends_on, patch, variant, version
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
        "3.00.06",
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

    # Flags for GENIE's optional but disabled by default features
    variant(
        "vleextension",
        default=False,
        description="Enable GENIE very low energy (1 MeV - 100 MeV) extension",
    )
    variant(
        "validationtools",
        default=False,
        description="GENIE physics model validation tools",
    )
    variant("test", default=False, description="Enable test programs")
    variant(
        "t2k", default=False, description="Enable Enables T2K-specific generation app"
    )
    variant(
        "fnal", default=False, description="Enable Enables T2K-specific generation app"
    )
    variant(
        "atmo",
        default=False,
        description="Enable GENIE Atmospheric neutrino event generation app",
    )
    variant(
        "nucleondecay",
        default=False,
        description="Enable GENIE Nucleon decay event generation app",
    )
    variant(
        "masterclass",
        default=False,
        description="Enable GENIE neutrino masterclass app",
    )

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
            "--with-libxml2-inc=%s%slibxml2" % (spec["libxml2"].prefix.include, os.sep),
            "--with-libxml2-lib=%s" % spec["libxml2"].prefix.lib,
            "--with-log4cpp-inc=%s" % spec["log4cpp"].prefix.include,
            "--with-log4cpp-lib=%s" % spec["log4cpp"].prefix.lib,
            "--with-pythia6-lib=%s" % spec["pythia6"].prefix.lib,
        ]
        if "+vleextension" in self.spec:
            args += ["--enable-vle-extension"]
        if "+validationtools" in self.spec:
            args += ["--enable-validation-tools"]
        if "+test" in self.spec:
            args += ["--enable-test"]
        if "+t2k" in self.spec:
            args += ["--enable-t2k"]
        if "+fnal" in self.spec:
            args += ["--enable-fnal"]
        if "+atmo" in self.spec:
            args += ["--enable-atmo"]
        if "+nucleondecay" in self.spec:
            args += ["--enable-nucleon-decay"]
        if "+masterclass" in self.spec:
            args += ["--enable-masterclass"]
        return args

    def build(self, spec, prefix):
        # make is injected by build_environment:
        # https://spack.readthedocs.io/en/latest/spack.html#module-spack.build_environment
        # apparently this is considered more readable
        make()  # noqa

    def install(self, spec, prefix):
        # GENIE make install support parallel jobs
        make("install", parallel=False)  # noqa
        # GENIE requires these files to be present at runtime, but doesn't install them
        # so we must install them ourselves
        install_tree("config", os.sep.join((prefix, "config")))  # noqa
        install_tree("data", os.sep.join((prefix, "data")))  # noqa

    def makedirs(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def setup_build_environment(self, env):
        env.set("GENIE", self.stage.source_path)
        return super().setup_build_environment(env)

    def setup_run_environment(self, env):
        env.set("GENIE", self.prefix)
        return super().setup_run_environment(env)
