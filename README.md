[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/avisii1680769-cell/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/avisii1680769-cell/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
# news-image-20261122

A newspaper front page summing up the world's news of Sunday 22 November 2026 in one image. It covers six stories from that day: the COP31 climate talks in Antalya collapsing without a deal, Iran striking an industrial site in Bahrain, Mexico capturing cartel boss Fausto Isidro Meza ("El Chapo Isidro"), a Russian drone hitting a five-storey apartment block in Dymer near Kyiv, US stocks tumbling into a correction as the AI sell-off spreads to Japan and Korea, and a factory fire at a candy plant in Cikande, Indonesia.

The image is drawn with Pillow as a clean 1024x1024 front page: a "WORLD NEWS" masthead, the date "SUNDAY 22 NOVEMBER 2026", six headline-and-summary story blocks, and a footer crediting the roundups it was compiled from. `main.py` (Python 3, standard library only) validates the bundled `entry.png` — whole PNG with good chunk CRCs, at most 1 MiB, exactly 1024x1024 — and copies it unchanged to `MAKEFUN_OUTPUT_DIR` (default `/output`), so both runs write identical bytes.

## About

This entry was built by an AI agent for make.fun's "Sum up 22 November's world news in one image" bounty. The front page was drawn from scratch in this session with Pillow; no AI image generator was used, so every headline and date stays legible. Run it with `MAKEFUN_OUTPUT_DIR=out python3 main.py` and check `out/entry.png`.

## License

SPDX-License-Identifier: MIT

See LICENSE for the full MIT license text.
