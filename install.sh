#!/usr/bin/env bash

source setup.sh && spack repo add neutrino-mc

# add E4S build cache
spack mirror add E4S https://cache.e4s.io \
&& wget https://oaciss.uoregon.edu/e4s/e4s.pub \
&& spack gpg trust e4s.pub \
&& rm e4s.pub
