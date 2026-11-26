import pytest
import graphics.micropoly as mod

CASES = [
    ("cluster_cull_double_buffer", (1,)),
    ("triangle_order_stable", (1,)),
    ("material_page_reresolve", (1,)),
    ("projection_versioned_lod", (1,)),
    ("cull_readback_generation", (1,)),
    ("instance_slot_clear", (1,)),
    ("load_cluster_scene", (1,)),
    ("build_clusters", (1,)),
    ("raster_visibility", (1,)),
    ("present_visbuffer", (1,)),
    ("validate_visbuffer", (1,)),
    ("metrics_visbuffer", (1,)),
    ("audit_visbuffer", (1,)),
    ("fallback_visbuffer", (1,)),
    ("determinism_visbuffer", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
