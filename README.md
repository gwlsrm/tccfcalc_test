# tccfcalc_test
Script for testing tccfcalc.dll calculation library from NuclideMasterPlus (LSRM)

## Preparation

Copy `effcalc.exe` -- executable analogue for tccfcalc.dll and `out_cmp.exe` -- utility for compare out-files (built with tccfcalc.dll) to same directory with script. 

Copy `Lib` directory with ensdf-files (can be taken from NuclideMasterPlus distro) to the script directory.

Copy `.\grids\50-3000_10p.enx` to `.\Lib\ENSDF2\290.enx` or run `copy_enx_grid.bat`  from tools directory for Windows or `copy_enx_grid.sh` for Linux.

## How to use

Start script from command line:

```sh
python tccfcalc_test.py
```

Script will output log to console and write out-files to `results` directory

Typical output:

```
calc with: in_files\tccfcalc_hpge_point.in
Calculation: 5539 ms
tccfcalc.out == out_files\tccfcalc_hpge_point.out
```

If output file is different from reference you will see:

```
calc with: in_files\tccfcalc_hpge_point.in
Calculation: 5539 ms
tccfcalc.out != out_files\tccfcalc_hpge_point.out
```

