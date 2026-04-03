# © 2026 Strategos. All rights reserved.
# vistina — stub package. Redirects to vistina-victor.
# See: https://github.com/ShadowStrike-CTF/shadowstrike-suite

try:
    from vistina_victor import *  # noqa: F401, F403
    from vistina_victor import __version__  # noqa: F401
except ImportError:
    raise ImportError(
        "vistina requires vistina-victor. "
        "Install with: pip install vistina-victor"
    )
