"""
store the current version info of the server.

"""
import re

__version__ = "2.16.6"

# Build up version_info tuple for backwards compatibility
pattern = r"(?P<major>\d+).(?P<minor>\d+).(?P<patch>\d+)(?P<rest>.*)"
match = re.match(pattern, __version__)
assert match is not None  # noqa
parts: list = [int(match[part]) for part in ["major", "minor", "patch"]]
if match["rest"]:
    parts.append(match["rest"])
version_info = tuple(parts)
