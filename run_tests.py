"""Run every exercise's tests, each folder in its own process (every exercise has its own `project` package)."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def test_roots():
    roots = set()
    for test_file in ROOT.glob("0*/**/*test*.py"):
        folder = test_file.parent
        # tests living in a `test/` package next to `project/` must be discovered from the exercise folder
        if (folder / "__init__.py").exists() and (folder.parent / "project").is_dir():
            folder = folder.parent
        roots.add(folder)
    return sorted(roots)


def main():
    failed = []
    for root in test_roots():
        result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-p", "*test*.py"],
                                cwd=root, capture_output=True, text=True)
        summary = result.stderr.strip().splitlines()
        print(f"{'ok  ' if result.returncode == 0 else 'FAIL'} {root.relative_to(ROOT)}: {summary[-3] if len(summary) > 2 else ''}")
        if result.returncode != 0:
            failed.append(root)
            print(result.stderr)
    print(f"\n{len(failed)} failing folder(s)" if failed else "\nAll tests passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
