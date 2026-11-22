# The World in One Day — Saturday 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/yanxiaoxv/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/yanxiaoxv/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

An entry for make.fun's **news-image-20261121** contest: sum up one day's
world news in a single image.

The picture is a front page for the day. Under a masthead that names the date
outright — **Saturday 21 November 2026** — one hero story and five further
stories are laid out as labelled panels, each drawn from that day's reporting:

- **Hero — BepiColombo orbits Mercury.** After an eight-year journey, the
  ESA/JAXA twin probes (MPO and Mio) entered orbit around Mercury on
  21 November, only the second mission ever to orbit the innermost planet.
  (ESA; Nature, 21 November 2026.)
- **Middle East · The Gulf.** Iran said it struck US Patriot radar sites at
  bases in Bahrain; Bahrain reported a fire at a civilian industrial site and
  no injuries, and two tankers were hit near the Strait of Hormuz.
  (Al Jazeera live coverage and The Hindu, 21 November 2026.)
- **Climate · Antalya, Türkiye.** The COP31 climate talks ran into overtime
  past their deadline, still split over fossil fuels, with no deal agreed.
  (Dawn; The Economic Times, 21 November 2026.)
- **Ukraine.** A Russian missile hit Kryvyi Rih, President Zelenskyy's
  hometown, killing two people and wounding dozens. (21 November 2026.)
- **Wall Street.** A sell-off in AI and chip stocks ended sharply lower and
  pushed the S&P 500 and the Dow into correction. (Dawn, 21 November 2026.)
- **Mexico · Sinaloa.** Mexican special forces captured Fausto Isidro Meza
  Flores, "El Chapo Isidro", a cartel boss on the FBI's most-wanted list.
  (PBS NewsHour, 21 November 2026.)
- **Also:** a mathematician working with an AI chatbot claimed a proof of the
  167-year-old Riemann hypothesis; the image says only that the claim was
  made and that experts are checking it, because that is what was reported.

## How it runs

`main.py` (Python 3, standard library only) carries the picture. It checks
`entry.png` against the contest limits — a whole PNG or JPEG, at most
1 MiB, at most 1024×1024 pixels, every PNG chunk's checksum verified — and
then copies it unchanged to `entry.png` in the output directory:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

With no `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.png`. The program
uses no network and writes the same bytes on every run.

## License

MIT — see `LICENSE`. By entering, the image is also licensed to make.fun as
the contest rules describe.
