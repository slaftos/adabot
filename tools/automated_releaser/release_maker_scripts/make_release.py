# SPDX-FileCopyrightText: 2023 Tim Cocks
#
# SPDX-License-Identifier: MIT

"""
make a new release using the gh cli
"""
import subprocess
from get_release_info import get_release_info

RELEASE_TITLE = "Fix RTD Theme Issue"


def make_release():
    """
    Make the release
    """
    # pylint: disable=line-too-long
    release_info = get_release_info()
    result = subprocess.getoutput(
        f"gh release create {release_info['new_tag']} -F release_notes.md -t '{release_info['new_tag']} - {RELEASE_TITLE}'"
    )

    print(result)
