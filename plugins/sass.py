import glob
import logging
import os
from pathlib import Path
from mkdocs import plugins
import sass

STYLE_DIR = (Path(__file__).parent.parent / "style").absolute()
OUT_DIR = (Path(__file__).parent.parent / "docs" / "stylesheets").absolute()


class CompileSCSSPlugin(plugins.BasePlugin):
    def on_pre_build(self, config):
        os.makedirs(OUT_DIR, exist_ok=True)
        for f in glob.glob(f"{STYLE_DIR}/*.scss"):
            outf = f.replace(".scss", ".css").replace(
                str(STYLE_DIR),
                str(OUT_DIR),
            )
            logging.info(f"Compile SCSS {f} to {outf}")
            with open(f) as fd:
                css = sass.compile(string=fd.read(), output_style="compressed")

            # Skip writing if no change is detected
            if os.path.isfile(outf):
                with open(outf) as fd:
                    if css.strip() == fd.read().strip():
                        continue

            with open(outf, "w") as fd:
                fd.write(css)
