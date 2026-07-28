"""comcrit: grey-box commutator critic as a measurement instrument.

Public surface (v0.1):
    ModulePartition, BackboneTerms
    stats: spearman, noise_floor, effect_size_precheck, margin_qualify,
           validity_map
    gates: ValidityGate, SynergyGate, NullGate, ResidualSkillGate
    fixture_quadratic: QuadFixture, make_family, closed-form truth
    backbone_jax: JaxBackbone (exact-D default / frozen-D / preview)
    selftest()
"""
from .partition import ModulePartition
from .protocols import BackboneTerms
from . import stats, gates, fixture_quadratic, confusion
from .selftest import selftest

__version__ = "0.1.0"
__all__ = ["ModulePartition", "BackboneTerms", "stats", "gates",
           "fixture_quadratic", "confusion", "selftest", "__version__"]
