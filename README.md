# The World in One Picture — Sunday 22 November 2026

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/ALENSALIM/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/ALENSALIM/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

A one-page newspaper front page summing up the world news of
**Sunday 22 November 2026**, drawn entirely with Python and Pillow in
flat colours — no photographs, no downloaded images, no real logos.

## Stories covered

- **Lead — Iran hits US defences in the Gulf:** Iran's Revolutionary Guard
  says it fired missiles and drones at two US Patriot radar sites; Iran also
  struck US military assets in Bahrain; several tankers were hit off Oman;
  Bahrain is investigating a Patriot interceptor crash amid reports of
  Iranian drone attacks.
- **Lviv:** a Russian missile strike kills at least two people and injures ten.
- **Peru:** a strong earthquake shakes the Andes; no damage or casualties
  reported.
- **Israel:** President Herzog asks former army chief Gadi Eisenkot to form
  the next government, passing over PM Netanyahu.
- **Trade:** the EU and Indonesia sign a trade deal after ten years of talks,
  scrapping about 98.5% of tariffs.
- **France:** a fourth straight weekend of cost-of-living protests.
- **Hong Kong:** voting opens for the Election Committee, about 5,700 voters.
- **Gaza:** Australia, Canada, Italy and the UK jointly call on Israel to let
  aid reach flooded Gaza without restriction.
- **Climate:** COP31 is deadlocked and runs into overtime.
- **In brief:** a magnitude 4.1 earthquake in Myanmar; Mexico captures cartel
  boss "El Chapo Isidro" with 11 killed in Sinaloa violence; UN talks on
  lethal autonomous weapons fall short; Sudan's Tasis alliance seizes the Bau
  region in Blue Nile; Brazil's ex-president Bolsonaro admitted to intensive
  care; the US State Department details $12bn in Venezuelan oil and mineral
  revenue.

## How to run

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
creating the output directory if needed, verifies the copy has the same
size as the bundled file, and prints the byte count and SHA-256 hash.

## Files

- `main.py` — copies `entry.png` to the output directory and verifies it.
- `entry.png` — the front page, 1024×1024 PNG.
- `README.md` — this file.
- `LICENSE` — MIT licence.
- `.makefun/owner.json` — entry owner wallet.

## Licence

MIT — see `LICENSE`.
