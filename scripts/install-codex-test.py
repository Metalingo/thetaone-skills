#!/usr/bin/env python3
"""Install local skills under distinct tto-* names without replacing existing skills."""

import argparse
from pathlib import Path
import re
import shutil
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents/skills")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills"
    destination = args.dest.expanduser().resolve()
    skills = sorted(path.parent for path in source.glob("*/SKILL.md"))
    if not skills:
        parser.error("No source skills found")
    names = {path.name: "tto-" + path.name for path in skills}
    for name in names.values():
        target = destination / name
        if target.exists() or target.is_symlink():
            parser.error(f"Already exists; nothing installed: {target}")

    # Transform copies only. Source instructions and existing installations stay intact.
    with tempfile.TemporaryDirectory(prefix="thetaone-codex-test-") as temporary:
        staging = Path(temporary)
        for skill in skills:
            copy = staging / names[skill.name]
            shutil.copytree(skill, copy)
            for document in copy.rglob("*.md"):
                content = document.read_text()
                content = re.sub(
                    r"`(" + "|".join(map(re.escape, names)) + r")`",
                    lambda match: "`" + names[match[1]] + "`",
                    content,
                )
                if document == copy / "SKILL.md":
                    content, count = re.subn(
                        r"(?m)^name: " + re.escape(skill.name) + r"$",
                        "name: " + names[skill.name], content, count=1,
                    )
                    if count != 1:
                        raise ValueError(f"Unexpected frontmatter: {skill}")
                    content += (
                        "\n## Test installation routing\n\n"
                        "For Thetaone workflow handoffs, use the tto-prefixed skills "
                        "from this installation, not same-purpose legacy skills. "
                        "If invocation is unavailable, read the corresponding SKILL.md "
                        "at the paths below. Project rules still apply.\n\n"
                        + "\n".join(
                            f"- `{name}`: `{destination / name / 'SKILL.md'}`"
                            for name in names.values()
                        ) + "\n"
                    )
                document.write_text(content)
        destination.mkdir(parents=True, exist_ok=True)
        installed = []
        try:
            for name in names.values():
                target = destination / name
                # Reserve each directory exclusively, including against concurrent installs.
                target.mkdir()
                installed.append(target)
                shutil.copytree(staging / name, target, dirs_exist_ok=True)
        except Exception:
            for target in installed:
                shutil.rmtree(target)
            raise
    for name in names.values():
        print(f"Installed ${name}: {destination / name}")


if __name__ == "__main__":
    main()
