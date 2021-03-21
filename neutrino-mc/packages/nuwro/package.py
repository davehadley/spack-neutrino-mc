import os

from spack.build_systems.makefile import MakefilePackage
from spack.directives import depends_on, patch, version


class Nuwro(MakefilePackage):
    """NuWro is a Monte Carlo neutrino event generator."""

    homepage = "https://nuwro.github.io/user-guide/"
    url = "https://github.com/NuWro/nuwro/archive/refs/tags/nuwro_19.02.2.tar.gz"
    git = "https://github.com/NuWro/nuwro"

    maintainers = [
        # maintainer of this recipe, not affliated with the NuWro collaboration
        "davehadley"
    ]

    version(
        "19.02.2",
        sha256="e6edf0cd3d9ae22261193ec9ee56f6a0bee5fbeae684f92361f091bb7f1fb055",
    )
    version(
        "19.02.1",
        sha256="66ec5ce8be747e821edf2e784fe579226c73301a886b0805410d929b61a90371",
    )
    version(
        "19.02",
        sha256="6b5dd5419fc43c3df9fc3c976180fffe24e48478502acdb86b4af8cc0f55e94f",
    )
    version(
        "18.02.1",
        sha256="4d3324207e1ff7192905b80dc0d422028ac06f1681c84430d8c33f6626a09c67",
    )
    version(
        "18.02",
        sha256="f98f5073ed3b1d21604ffd3ec1e2ca907a15aacd69c8e813526e3d2fd40b2ebc",
    )
    version(
        "17.09",
        sha256="350fa6043fa39253afad30bbcb655bde7d85b641843344aa978faca32535456d",
    )
    version(
        "17.01.1",
        sha256="5071d9d1495b780060215729bf7c52e1db0f26a213a1c25b5f7c99d43af97f65",
    )
    version(
        "17.01",
        sha256="bbbf73bc3c7436fb2fd28c7df538b4e20ad3f2f90a6c1c72f739f14a2ab8cf64",
    )

    depends_on("root+pythia6")

    # nuwro does not actually require cmake, but root does.
    # Spack's concretizer fails with "unsatisfiable constraint" if we don't add this.
    depends_on("cmake@3:")

    # Missing include directive in nuwro2rootracker.cc causes compilation failure with
    # some versions of ROOT
    patch("nuwro2rootracker_missing_include.patch", level=0)

    @property
    def build_targets(self):
        return [
            "CC=c++",
            "CXX=c++",
            "LD=c++",
            "FC=fc",
            "VERSION=%s" % self.spec.version,
        ]

    def install(self, spec, prefix):
        # nuwro has no install stage,
        # so we must install its binaries ourselves
        # install_tree function is injected into scope by spack build_environment.py
        install_tree("bin", prefix.bin)  # noqa
        install_tree("data", os.sep.join((prefix, "data")))  # noqa

    def setup_run_environment(self, env):
        # nuwro uses this environment variable to find the data directory
        env.set("NUWRO", self.prefix)
        return super(Nuwro, self).setup_run_environment(env)
