# Vistina — Forensic legal review platform.
# © 2026 Strategos Pty Ltd. All rights reserved.
# Aut Viam Inveniam Aut Faciam

try:
    from vistina_victor import *  # noqa: F401, F403
    from vistina_victor import __version__  # noqa: F401
except ImportError:
    raise ImportError(
        "vistina requires vistina-victor. "
        "Install with: pip install vistina-victor"
    )
