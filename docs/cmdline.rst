Command Line Usage
##################

Compare files for similarity and generate an HTML report of results.

Basic Usage
===========
Test files for similarity in one directory:
  ``copydetect -t DIRECTORY``

Test files for similarity in one directory against files in another directory:
  ``copydetect -t DIRECTORY -r DIRECTORY``

Test files in multiple directories for similarity:
  ``copydetect -t DIRECTORY1 DIRECTORY2 DIRECTORY3``

Specify which file types to test for similarity:
  ``copydetect -t DIRECTORY -e py java c``

Exclude boilerplate lines from test for similarity.
  ``copydetect -t DIRECTORY -b BOILERPLATE``

Options
=======

  -t, --test-dirs DIRS         Directories to search for files to check (test_directories)
  -r, --ref-dirs DIRS          Reference directories to compare against (reference_directories)
                               (defaults to test directories when not specified)
  -b, --boilerplate-dirs DIRS  Directories with code to exclude from matches (boilerplate_directories)
  -e, --extensions EXTS        File extensions to check (extensions) (default: all files)
  -n, --noise-thresh N         Min matching characters to flag for similarity (noise_threshold). Note that tokenization and filtering replaces variable names with ``V``, function names with ``F``, object names with ``O``, and strings with S`` so the threshold should be lower than you would expect from the original code. (default: 25)
  -g, --guarantee-thresh N     Min characters for guaranteed detection (guarantee_threshold). The smallest sequence of matching characters between two files for which the system is guaranteed to detect a match. This must be greater than or equal to the noise threshold. If computation time is not an issue, you can set guarantee_threshold = noise_threshold. (default: 30)
  -d, --display-thresh N       Similarity % cutoff for inclusion in report (display_threshold) (default: 0.33)
  -o, --force-language LANG    Force specific language tokenization (force_language)
  -s, --same-name              Only compare files with identical names (same_name_only)
  -l, --ignore-leaf            Skip comparing files in same leaf directory (ignore_leaf)
  -f, --disable-filter         Disable code tokenization and filtering before generating file fingerprints(disable_filtering)
  -a, --disable-autoopen       Don't automatically open the report in browser (disable_autoopen)
  -T, --truncate               Truncate non-highlighted regions in output (truncate). Sections not within 10 lines of highlighted code will be replaced with “…”
  -O, --out-file PATH          Path to save report (out_file) (default: report.html)
  -c, --config FILE            Load options from JSON config file
      --encoding ENC           File encoding (encoding) (default: UTF-8, use DETECT for to detect encoding automatically)
      --css FILES              Custom CSS files for report styling (css)
  -h, --help                   Show this help message and exit
  -v, --version                Show program version and exit
  

Configuration File
==================
You can use a JSON file to set options instead of using command line flags (JSON keys are shown in parentheses in the Options section):

To specify a configuration file:

  ``copydetect -c config.json``

See sample config: https://github.com/blingenf/copydetect/blob/master/docs/_static/sample.json

For more information, visit: https://copydetect.readthedocs.io
