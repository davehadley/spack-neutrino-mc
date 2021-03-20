# from spack import AutotoolsPackage, depends_on, version
import os

from spack.directives import depends_on, patch, variant, version
from spack.package import Package
from spack.util.executable import Executable

# from llnl.util.filesystem import FileFilter


class Genie(Package):  # Genie doesn"t use Autotools
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
        "3.0.6",
        sha256="ab56ea85d0c1d09029254365bfe75a1427effa717389753b9e0c1b6c2eaa5eaf",
        url="https://github.com/GENIE-MC/Generator/archive/R-3_00_06.tar.gz",
    )
    version(
        "3.0.4",
        sha256="53f034618fef9f7f0e17d1c4ed72743e4bba590e824b795177a1a8a8486c861e",
        url="https://github.com/GENIE-MC/Generator/archive/R-3_00_04.tar.gz",
    )
    version(
        "3.0.2",
        sha256="34d6c37017b2387c781aea7bc727a0aac0ef45d6b3f3982cc6f3fc82493f65c3",
        url="https://github.com/GENIE-MC/Generator/archive/R-3_00_02.tar.gz",
    )
    version(
        "3.0.0",
        sha256="3953c7d9f1f832dd32dfbc0b9260be59431206c204aec6ab0aa68c01176f2ae6",
        url="https://github.com/GENIE-MC/Generator/archive/R-3_00_00.tar.gz",
    )
    version(
        "2.12.10",
        sha256="c8762db3dcc490f80f8a61268f5b964d4d35b80134b622e89fe2307a836f2a0b",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_12_10.tar.gz",
    )
    version(
        "2.12.8",
        sha256="7ca169a8d9eda7267d28b76b2f3110552852f8eeae263a03cd5139caacebb4ea",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_12_8.tar.gz",
    )
    version(
        "2.12.6",
        sha256="3b450c609875459798ec98e12cf671cc971cbb13345af6d75bd6278d422f3309",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_12_6.tar.gz",
    )
    version(
        "2.12.4",
        sha256="19a4a1633b0847a9f16a44e0c74b9c224ca3bb93975aecf108603c22e807517b",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_12_4.tar.gz",
    )
    version(
        "2.12.2",
        sha256="cbdc45a739878940dadcaaed575b5cad6b5e7035f29605045b1ca557e6faa6d1",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_12_2.tar.gz",
    )
    version(
        "2.12.0",
        sha256="d2b01c80f38d269cb0296b3f2932798ef3f1d51bd130e81274fbfeeb381fac6b",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_12_0.tar.gz",
    )
    version(
        "2.11.2",
        sha256="0f4c25d8ceb7513553671643c9cdac5aa98c40fc8594a5ecb25c077c6b36166e",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_11_2.tar.gz",
    )
    version(
        "2.11.0",
        sha256="1ebe0eb65d797595413632f1cec1cb2621cb8e8d0384a2843799724a79b1d80c",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_11_0.tar.gz",
    )
    version(
        "2.10.10",
        sha256="1dfaadcf1bbaf6e164b612f410c4399301e63497ad6a4891706b1787ac11a7a1",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_10_10.tar.gz",
    )
    version(
        "2.10.8",
        sha256="4f6f5af2062e7c505b76e70547ac2ae304a9790c3e9b9592818d8aebeebc8398",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_10_8.tar.gz",
    )
    version(
        "2.10.6",
        sha256="d00b4288c886f81459fb2967e539f30315d4385f82d1d3f4330298d313f9a176",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_10_6.tar.gz",
    )
    version(
        "2.10.4",
        sha256="df909bf7e1a789ca01794995687da2af803769f0823273a4a3a31678d6d5b0f1",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_10_4.tar.gz",
    )
    version(
        "2.10.2",
        sha256="6abe4e0cdb5e8f5beddf0ccdbebc94c175a9f72592b1cbbffe01b88ee3972bf9",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_10_2.tar.gz",
    )
    version(
        "2.10.0",
        sha256="17bda900c996b6f4f10a7f6a3be94e56c3b8dcdeb2ef8865ca7f20c5fe725291",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_10_0.tar.gz",
    )
    version(
        "2.9.0",
        sha256="8229beb73f65f5af86a77bf141acfbe4a8b68cba9d797aae083a929906f6f2a2",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_9_0.tar.gz",
    )
    version(
        "2.8.6",
        sha256="310dc8e0d17a65e6b9773e398250703a3a6f94ceafe94f599ae0f7b3fecf7e6c",
        url="https://github.com/GENIE-MC/Generator/archive/R-2_8_6.tar.gz",
    )

    depends_on("root+pythia6")
    depends_on("pythia6")
    depends_on("lhapdf", when="@3:")
    depends_on("lhapdf5", when="@:2")
    depends_on("log4cpp")
    depends_on("libxml2")
    depends_on("gsl")
    depends_on("geant4")

    patch("genie_make_files.patch", level=0, when="@2.12:")

    # Flags for GENIE"s optional but disabled by default features
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

    phases = ["edit", "configure", "build", "install"]

    def configure(self, spec, prefix):
        configure = Executable("./configure")
        args = self.configure_args(spec, prefix)
        configure(*args)

    def configure_args(self, spec, prefix):
        args = [
            "--enable-lhapdf6",
            "--prefix=%s" % prefix,
            "--with-compiler=%s" % os.environ["CC"],
            "--with-libxml2-inc=%s%slibxml2" % (spec["libxml2"].prefix.include, os.sep),
            "--with-libxml2-lib=%s" % spec["libxml2"].prefix.lib,
            "--with-log4cpp-inc=%s" % spec["log4cpp"].prefix.include,
            "--with-log4cpp-lib=%s" % spec["log4cpp"].prefix.lib,
            "--with-pythia6-lib=%s" % spec["pythia6"].prefix.lib,
        ]
        if self.spec.satisfies("@:2"):
            args += [
                "--with-lhapdf-inc=%s" % spec["lhapdf5"].prefix.include,
                "--with-lhapdf-lib=%s" % spec["lhapdf5"].prefix.lib,
            ]
        else:
            args += [
                "--with-lhapdf6-inc=%s" % spec["lhapdf"].prefix.include,
                "--with-lhapdf6-lib=%s" % spec["lhapdf"].prefix.lib,
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

    def edit(self, spec, prefix):
        # makefile = FileFilter("src/make/Make.include")
        # makefile.filter(r"CC = gcc",  "CC = dummygcccommand")
        # makefile.filter(r"CXX = g\+\+", "CXX = dummygxxcommand")
        # makefile.filter(r"LD  = g\+\+", "LD = dummyldcommand")
        pass

    def build(self, spec, prefix):
        # make is injected by build_environment:
        # https://spack.readthedocs.io/en/latest/spack.html#module-spack.build_environment
        # apparently this is considered more readable
        self._make(parallel=spec.satisfies("@3:"))

    def install(self, spec, prefix):
        # GENIE make install support parallel jobs
        self._make("install", parallel=False)
        # GENIE requires these files to be present at runtime, but doesn"t install them
        # so we must install them ourselves
        install_tree("config", os.sep.join((prefix, "config")))  # noqa
        install_tree("data", os.sep.join((prefix, "data")))  # noqa

    def setup_build_environment(self, env):
        env.set("GENIE", self.stage.source_path)
        return super().setup_build_environment(env)

    def setup_run_environment(self, env):
        env.set("GENIE", self.prefix)
        return super().setup_run_environment(env)

    def _make(self, *args, parallel=True):
        # make is injected by build_environment:
        # https://spack.readthedocs.io/en/latest/spack.html#module-spack.build_environment
        # apparently this is considered more readable
        args = list(self._make_args) + list(args)
        make(*args, parallel=parallel)  # noqa

    @property
    def _make_args(self):
        return [
            "CC=c++",
            "CXX=c++",
            "LD=c++",
        ]
