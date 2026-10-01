# Anvil rulebook

Cited design rules extracted from the reference library. Each row id (`TAG-nnn`) names its source
book in `../bibliography.json` (`rule_prefixes`) and carries the page/section it came from.
Use them to choose values and limits, cite them in `design/rules.tsv` `source` and in
`audit/decisions.tsv`, and prefer the mechanized versions in `scripts/anvil_rules.py`.
Rules are engineering extracts for design work; the licensed originals and current
datasheets/standards govern. Extraction noise (OCR, missing figures) is logged per file in section 8.

Search, do not read whole files: `grep -n "| pdn |" rulebook/*.md`, `grep -n "BROOKS-10" ...`.

| File | Tag | Source | Rules | Coverage |
|---|---|---|---|---|
| [AOE-art-of-electronics-part1.md](AOE-art-of-electronics-part1.md) | AOE | `horowitz2015` | 377 | read in full |
| [AOE-art-of-electronics-part2.md](AOE-art-of-electronics-part2.md) | AOE | `horowitz2015` | 867 | read in full |
| [AOE-art-of-electronics-part3.md](AOE-art-of-electronics-part3.md) | AOE | `horowitz2015` | 424 | read in full |
| [AOE-art-of-electronics-part4.md](AOE-art-of-electronics-part4.md) | AOE | `horowitz2015` | 301 | read in full |
| [ARCH-pcb-emi-control.md](ARCH-pcb-emi-control.md) | ARCH | `archambeault2002` | 119 | read in full |
| [BALANIS-antenna-theory-part1.md](BALANIS-antenna-theory-part1.md) | BALANIS | `balanis2016` | 259 | read in full |
| [BALANIS-antenna-theory-part2.md](BALANIS-antenna-theory-part2.md) | BALANIS | `balanis2016` | 363 | read in full |
| [BOGATIN-si-pi-part1.md](BOGATIN-si-pi-part1.md) | BOGATIN | `bogatin2018` | 235 | read in full |
| [BOGATIN-si-pi-part2.md](BOGATIN-si-pi-part2.md) | BOGATIN | `bogatin2018` | 212 | read in full |
| [BOWICK-rf-circuit-design.md](BOWICK-rf-circuit-design.md) | BOWICK | `bowick2008` | 269 | read in full |
| [BROOKS-via-trace-currents.md](BROOKS-via-trace-currents.md) | BROOKS | `brooks2021` | 143 | read in full |
| [COHEN-prototype-to-product.md](COHEN-prototype-to-product.md) | COHEN | `cohen2015` | 268 | read in full |
| [COOMBS-printed-circuits-handbook-part1.md](COOMBS-printed-circuits-handbook-part1.md) | COOMBS | `coombs2016` | 218 | read in full |
| [COOMBS-printed-circuits-handbook-part2.md](COOMBS-printed-circuits-handbook-part2.md) | COOMBS | `coombs2016` | 464 | read in full |
| [COOMBS-printed-circuits-handbook-part3.md](COOMBS-printed-circuits-handbook-part3.md) | COOMBS | `coombs2016` | 349 | read in full |
| [COOMBS-printed-circuits-handbook-part4.md](COOMBS-printed-circuits-handbook-part4.md) | COOMBS | `coombs2016` | 323 | read in full |
| [ERICKSON-power-electronics-part1.md](ERICKSON-power-electronics-part1.md) | ERICKSON | `erickson2020` | 199 | read in full |
| [ERICKSON-power-electronics-part2.md](ERICKSON-power-electronics-part2.md) | ERICKSON | `erickson2020` | 200 | read in full |
| [HALL00-high-speed-digital-system-design.md](HALL00-high-speed-digital-system-design.md) | HALL00 | `hall2000` | 210 | read in full |
| [HALLHECK-advanced-si-part1.md](HALLHECK-advanced-si-part1.md) | HALLHECK | `hallheck2009` | 115 | read in full |
| [HALLHECK-advanced-si-part2.md](HALLHECK-advanced-si-part2.md) | HALLHECK | `hallheck2009` | 151 | read in full |
| [HWFW-stringham-hardware-firmware-interface.md](HWFW-stringham-hardware-firmware-interface.md) | HWFW | `stringham2009` | 322 | read in full |
| [IPC-standards-and-library-guides.md](IPC-standards-and-library-guides.md) | IPC | `ipc2221c` | 210 | read in full |
| [JOHNSON03-signal-propagation-part1.md](JOHNSON03-signal-propagation-part1.md) | JOHNSON03 | `johnson2003` | 323 | read in full |
| [JOHNSON03-signal-propagation-part2.md](JOHNSON03-signal-propagation-part2.md) | JOHNSON03 | `johnson2003` | 338 | read in full |
| [JOHNSON93-high-speed-digital-design.md](JOHNSON93-high-speed-digital-design.md) | JOHNSON93 | `johnson1993` | 560 | read in full |
| [KICAD-dalmaris-kicad6.md](KICAD-dalmaris-kicad6.md) | KICAD | `dalmaris2022` | 123 | read in full |
| [MITZ-complete-pcb-design.md](MITZ-complete-pcb-design.md) | MITZ | `mitzner2019` | 270 | read in full |
| [PAUL-intro-emc-part1.md](PAUL-intro-emc-part1.md) | PAUL | `paul2022` | 188 | read in full |
| [PAUL-intro-emc-part2.md](PAUL-intro-emc-part2.md) | PAUL | `paul2022` | 204 | read in full |
| [POZAR-microwave-engineering-part1.md](POZAR-microwave-engineering-part1.md) | POZAR | `pozar2012` | 249 | read in full |
| [POZAR-microwave-engineering-part2.md](POZAR-microwave-engineering-part2.md) | POZAR | `pozar2012` | 282 | read in full |
| [PRESSMAN-switching-power-supply-part1.md](PRESSMAN-switching-power-supply-part1.md) | PRESSMAN | `pressman2009` | 322 | read in full |
| [PRESSMAN-switching-power-supply-part2.md](PRESSMAN-switching-power-supply-part2.md) | PRESSMAN | `pressman2009` | 271 | read in full |
| [RITCHEY-right-the-first-time-v2.md](RITCHEY-right-the-first-time-v2.md) | RITCHEY | `ritchey2007` | 342 | read in full |
| [SCHERZ-practical-electronics-part1.md](SCHERZ-practical-electronics-part1.md) | SCHERZ | `scherz2016` | 309 | read in full |
| [SCHERZ-practical-electronics-part2.md](SCHERZ-practical-electronics-part2.md) | SCHERZ | `scherz2016` | 289 | read in full |
| [WHITE-making-embedded-systems.md](WHITE-making-embedded-systems.md) | WHITE | `white2024` | 225 | read in full |
| [WILLIAMS-emc-product-designers-part1.md](WILLIAMS-emc-product-designers-part1.md) | WILLIAMS | `williams2016` | 298 | read in full |
| [WILLIAMS-emc-product-designers-part2.md](WILLIAMS-emc-product-designers-part2.md) | WILLIAMS | `williams2016` | 339 | read in full |
| [WILSON-circuit-designers-companion.md](WILSON-circuit-designers-companion.md) | WILSON | `wilson2011` | 421 | read in full |

Mined in full (index pages and exercises excepted; each file's section 8 lists OCR/figure losses and
suspected misprints found while cross-checking worked examples).
