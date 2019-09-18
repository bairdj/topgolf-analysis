These scripts allow you to download your Topgolf data and automatically generate a dashboard to see your statistics at a game and ball level.

## Requirements
### To download data
* Python 3
* requests library

### To create dashboard
* R
* Pandoc
* CRAN packages
  * ggplot2
  * readr
  * dplyr
  * flexdashboard

## Running
Firstly run download.py with your Topgolf username and password. This will download your data to output.csv. You can use this file for your own analysis, or keep going to automatically generate analysis.

`python download.py USERNAME PASSWORD`

Then run the R script

`Rscript build_notebook.R`

This will create a file analysis.html where you can view your statistics

## Disclaimer
This has no affiliation with Topgolf. [See Topgolf Terms](https://topgolf.com/uk/company/terms-and-conditions/)

