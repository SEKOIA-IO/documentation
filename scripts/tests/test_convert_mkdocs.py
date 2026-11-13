"""Tests for scripts/convert_mkdocs.py. Run with: uvx pytest scripts/tests"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import convert_mkdocs as cm


@pytest.fixture(autouse=True)
def reset_state():
    cm.stats.clear()
    cm.ANNOTATED.clear()
    cm.CURRENT[0] = "test.md"


@pytest.fixture
def docs(tmp_path):
    root = tmp_path / "docs"
    (root / "xdr").mkdir(parents=True)
    (root / "xdr" / "events.md").write_text("# Events\n")
    (root / "integration" / "categories").mkdir(parents=True)
    return root


def blocks(text):
    return "\n".join(cm.convert_blocks(text.split("\n")))


# --- Existing behaviour -------------------------------------------------------

def test_admonition_with_title():
    assert blocks('!!! warning "Careful"\n    Body text.') == (
        '{% hint style="warning" %}\n**Careful**\n\nBody text.\n{% endhint %}'
    )


def test_collapsible():
    assert blocks('??? example "Log"\n    line') == (
        "<details>\n<summary>Log</summary>\n\nline\n\n</details>"
    )


def test_tabs_are_grouped():
    out = blocks('=== "Linux"\n    a\n\n=== "Windows"\n    b')
    assert out == (
        '{% tabs %}\n{% tab title="Linux" %}\na\n{% endtab %}\n'
        '{% tab title="Windows" %}\nb\n{% endtab %}\n{% endtabs %}'
    )


def test_nested_admonition_in_tab():
    out = blocks('=== "Tab"\n    !!! note\n        inner')
    assert '{% hint style="info" %}\ninner\n{% endhint %}' in out
    assert out.startswith("{% tabs %}") and out.endswith("{% endtabs %}")


def test_code_blocks_are_untouched():
    text = '```\n!!! note\n=== "x"\n```'
    assert blocks(text) == text


def test_absolute_link_and_attribute(docs):
    page = docs / "integration" / "categories" / "page.md"
    out = cm.convert_inline("[E](/xdr/events.md#a) [Go](https://x.io){ .md-button }", page, docs)
    assert out == "[E](../../xdr/events.md#a) [Go](https://x.io)"


def test_conversion_is_idempotent():
    once = blocks('!!! tip\n    a\n\n=== "T"\n    b')
    assert blocks(once) == once


# --- Additions for docs/integration -------------------------------------------

@pytest.mark.parametrize("kind,style", [
    ("warn", "warning"), ("disclaimer", "warning"), ("information", "info"), ("prerequisites", "info"),
])
def test_extra_admonition_types(kind, style):
    assert blocks(f"!!! {kind}\n    x").startswith(f'{{% hint style="{style}" %}}')
    assert not any("inconnu" in k for k in cm.stats)


def test_keys():
    assert blocks("Press ++ctrl+alt+del++ or ++f5++.") == "Press `Ctrl+Alt+Del` or `F5`."


def test_keys_inside_admonition_but_not_in_code():
    assert "`Ctrl+C`" in blocks("!!! tip\n    Use ++ctrl+c++")
    assert blocks("```\nx = ++a++\n```") == "```\nx = ++a++\n```"


def test_code_annotations_are_removed():
    text = "```python { .annotate }\nprint(x) # (1)\ny = 2  // (2)!\nz = f(1)  # keep (1) here\n```\n\n1. Prints x"
    assert blocks(text) == "```python\nprint(x)\ny = 2\nz = f(1)  # keep (1) here\n```\n\n1. Prints x"
    assert cm.stats["annotations de code retirées (liste sous le bloc à relire)"] == 2


def test_report_to_review(capsys):
    cm.report_to_review('a <span style="color:red">b</span><br/>\n```\n<br/>\n```\n<iframe src="x">')
    err = capsys.readouterr().err
    assert "HTML avec style" in err and "balises <br>" in err and "<iframe>/<video>" in err
    assert cm.stats["à reprendre à la main : balises <br>"] == 1  # the one in the code block is ignored


# --- main() -------------------------------------------------------------------

def run(docs, *args):
    cm.main([str(docs), "--repo-root", str(docs.parent), *args])


def test_crlf_is_preserved(docs):
    page = docs / "integration" / "crlf.md"
    page.write_bytes(b"!!! note\r\n    text\r\n")
    run(docs, "--only", "integration", "--write")
    assert page.read_bytes() == b'{% hint style="info" %}\r\ntext\r\n{% endhint %}\r\n'


def test_crlf_file_without_syntax_is_not_rewritten(docs):
    page = docs / "integration" / "plain.md"
    page.write_bytes(b"# Title\r\n\r\nText\r\n")
    run(docs, "--only", "integration", "--write")
    assert page.read_bytes() == b"# Title\r\n\r\nText\r\n"


def test_only_and_exclude_accept_files_and_folders(docs):
    lib = docs / "integration" / "action_library"
    lib.mkdir()
    (lib / "gen.md").write_text("!!! note\n    generated\n")
    index = docs / "integration" / "index.md"
    index.write_text("!!! note\n    index\n")
    other = docs / "integration" / "categories" / "other.md"
    other.write_text("!!! note\n    other\n")

    run(docs, "--only", "integration/index.md", "--write")
    assert "{% hint" in index.read_text()
    assert "!!!" in other.read_text()

    run(docs, "--only", "integration", "--exclude", "integration/action_library", "--write")
    assert "{% hint" in other.read_text()
    assert "!!!" in (lib / "gen.md").read_text()


def test_includes_are_kept_without_inline_option(docs):
    page = docs / "integration" / "inc.md"
    page.write_text("{!_shared_content/x.md!}\n")
    run(docs, "--only", "integration", "--write")
    assert page.read_text() == "{!_shared_content/x.md!}\n"
