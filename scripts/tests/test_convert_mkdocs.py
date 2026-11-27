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
    cm.REUSABLE.clear()
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


def test_keys_are_kept_inside_inline_code():
    text = "Type `++ctrl+c++` or ``x ++a++ y`` then ++ctrl+v++"
    assert blocks(text) == "Type `++ctrl+c++` or ``x ++a++ y`` then `Ctrl+V`"


def test_code_annotations_are_removed():
    text = "```python { .annotate }\nprint(x) # (1)\ny = 2  // (2)!\nz = f(1)  # keep (1) here\n```\n\n1. Prints x"
    assert blocks(text) == "```python\nprint(x)\ny = 2\nz = f(1)  # keep (1) here\n```\n\n1. Prints x"
    assert cm.stats["annotations de code retirées (liste sous le bloc à relire)"] == 2


def test_annotation_markers_are_kept_without_annotation_list():
    text = "```python\nhalf = count // (2)\nn = f(x)  # (1)\n```\n\nSome paragraph."
    assert blocks(text) == text
    assert not cm.stats


def test_annotation_list_is_detected_after_blank_lines_and_in_admonition():
    text = "!!! note\n    ```\n    a  # (1)\n    ```\n\n\n    1. Note A"
    assert "a\n" in blocks(text) and "# (1)" not in blocks(text)


def test_report_to_review(capsys):
    cm.report_to_review('a <span style="color:red">b</span><br/>\n```\n<br/>\n```\n<iframe src="x">')
    err = capsys.readouterr().err
    assert "HTML avec style" in err and "balises <br>" in err and "<iframe>/<video>" in err
    cm.report_to_review('<img src="x" style="width:50%">\n<a href="y" style="color:red">z</a>')
    assert cm.stats["à reprendre à la main : HTML avec style"] == 3
    assert cm.stats["à reprendre à la main : balises <br>"] == 1  # the one in the code block is ignored


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


# --- --gitbook-includes -------------------------------------------------------

@pytest.fixture
def shared(docs):
    root = docs.parent / "_shared_content"
    (root / "integration").mkdir(parents=True)
    (root / "integration" / "detection.md").write_text(
        "## Detection\n\n!!! note\n    See [events](/xdr/events.md).\n"
    )
    (root / "integration" / "outer.md").write_text("Outer\n\n{!_shared_content/integration/detection.md!}\n")
    (root / "integration" / "generated").mkdir()
    (root / "integration" / "generated" / "x.md").write_text("generated\n")
    page = docs / "integration" / "categories" / "page.md"
    page.write_text(
        "{!_shared_content/integration/detection.md!}\n\n"
        "{!_shared_content/integration/generated/x.md!}\n\n"
        "{!_shared_content/integration/outer.md!}\n"
    )
    return page


def test_gitbook_includes_write_reusable_content(shared, docs):
    run(docs, "--only", "integration", "--gitbook-includes", "--write")
    assert shared.read_text() == (
        '{% include "../.gitbook/includes/detection.md" %}\n\n'
        "{!_shared_content/integration/generated/x.md!}\n\n"
        '{% include "../.gitbook/includes/outer.md" %}\n'
    )
    includes = docs / "integration" / ".gitbook" / "includes"
    assert (includes / "detection.md").read_text() == (
        '## Detection\n\n{% hint style="info" %}\nSee [events](../../../xdr/events.md).\n{% endhint %}\n'
    )
    # nested inclusion: copied into the reusable content, no reusable content inside another one
    assert "{% include" not in (includes / "outer.md").read_text()
    assert "{% hint" in (includes / "outer.md").read_text()
    assert cm.stats["inclusions -> contenu réutilisable GitBook {% include %}"] == 2
    assert cm.stats["inclusions générées laissées telles quelles (générateurs à adapter)"] == 1


def test_gitbook_includes_dry_run_writes_nothing(shared, docs, capsys):
    run(docs, "--only", "integration", "--gitbook-includes")
    assert "{!" in shared.read_text()
    assert not (docs / "integration" / ".gitbook").exists()
    assert "3 fichier(s) à convertir" in capsys.readouterr().out  # page + 2 reusable contents


def test_gitbook_includes_is_idempotent(shared, docs, capsys):
    run(docs, "--only", "integration", "--gitbook-includes", "--write")
    cm.REUSABLE.clear()
    run(docs, "--only", "integration", "--gitbook-includes", "--write")
    assert "0 fichier(s) convertis" in capsys.readouterr().out


def test_inline_and_gitbook_includes_are_exclusive(docs):
    with pytest.raises(SystemExit):
        run(docs, "--inline-includes", "--gitbook-includes")
