# Pysilfont commands and scripts

Below is a table listing all the commands installed by Pysilfont followed by descriptions of each command.

All these commands work in consistent ways in terms of certain standard options (eg -h for help) and default names for many files - see details in [Pysilfont Documentation](docs.md).

There are further example scripts supplied with Pysilfont, and some of these are also [documented further down](#example-scripts)

## Table of scripts

| Command | Description |
| ------- | ----------- |
| [CDconvFromXml](#CDconvFromXml) | Convert composite definition file from XML format |
| [CDconvToXml](#CDconvToXml) | Convert composite definition file to XML format |
| [FFchangeGlyphNames](#FFchangeGlyphNames) | Update glyph names in a ttf font based on csv file |
| [FFcopyGlyphs](#FFcopyGlyphs) | Copy glyphs from one font to another, without using ffbuilder |
| [FFremoveAllOverlaps](#FFremoveAllOverlaps) | Remove overlap on all glyphs in a ttf font |
| [FTMLcreateOdt](#FTMLcreateOdt) | Create a LibreOffice Writer file from an FTML test description |
| [GDLchangeNames](#GDLchangeNames) | Change graphite names within GDL based on mappings files |
| [UFOaddAnchors](#UFOaddAnchors) | Read anchor data from XML file and apply to UFO |
| [UFObuildComp](#UFObuildComp) | Add composite glyphs to UFO based on a Composite Definitions file |
| [UFOconvert](#UFOconvert) | Normalize a UFO and optionally converts it between UFO2 and UFO3 versions |
| [UFOcopyMeta](#UFOcopyMeta) | Copy basic metadata from one UFO to another, for fonts in related families |
| [UFOexportAnchors](#UFOexportAnchors) | Export UFO anchor data to a separate XML file |
| [UFOexportPSnames](#UFOexportPSnames) | Export a map of gylph name to PS name to a csv file |
| [UFOexportUnicodes](#UFOexportUnicodes) | Export a map of gylph name to unicode value to a csv file |
| [UFOloadGlyphOrder](#UFOloadGlyphOrder) | Load glyph order data into public.glyphOrder based on a text file |
| [UFOsetAssocFeat](#UFOsetAssocFeat) | Add associate feature info to glif lib based on a csv file |
| [UFOsetAssocUIDs](#UFOsetAssocUIDs) | Add associate UID info to glif lib based on a csv file |
| [UFOsetPSnames](#UFOsetPSnames) | Add public.postscriptname to glif lib based on a csv file |
| [UFOsetUnicodes](#UFOsetUnicodes) | Set unicode values for a glif based on a csv file |
| [UFOsetVersion](#UFOsetVersion) | Change all the version-related info in a UFO's fontinfo.plist |
| [UFOsyncMeta](#UFOsyncMeta) | Copy basic metadata from one member of a font family to other family members |


---
#### CDconvFromXml
Usage: ```CDconvFromXml input output```

_([Standard options](#standard-options) [-h] [-d] [-q] [-p PARAMS] also apply)_

Convert composite definition file from XML format

_This section is WIP!_

- input                 Input file of CD in XML format
- output                Output file of CD in single line format

_[Return to table of scripts](#table-of-scripts)_

---
#### CDconvToXml
Usage: ```CDconvToXml [-p PARAMS] input output log```

_([Standard options](#standard-options) [-h] [-d] [-q] also apply)_

Convert composite definition file from XML format

_This section is WIP!_

  input                 Input file of CD in single line format
  output                Output file of CD in XML format
  log                   Log file

  -p PARAMS, --params PARAMS
                        XML formatting parameters: indentFirst, indentIncr,
                        attOrder
                        
 Defaults    output              _out.xml
    log                 _log.txt

_[Return to table of scripts](#table-of-scripts)_

---
#### FFchangeGlyphNames 
Usage: ```FFchangeGlyphNames [-i INPUT] [--reverse] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Update the glyph names in a ttf font based on csv file.

Example usage:

```
FFchangeGlyphNames -i glyphmap.csv font.ttf
```
will update the glyph names in the font based on mapping file glyphmap.csv

If \-\-reverse  is used, it change names in reverse.

_[Return to table of scripts](#table-of-scripts)_

---
####  FFcopyGlyphs
Usage: ```-i INPUT [-r RANGE] [--rangefile RANGEFILE] [-n NAME] [--namefile NAMEFILE] [-a] [-f] [-s SCALE] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-p PARAMS] also apply)_

_This section is WIP!_

positional arguments:
  ifont                 Input font file
  ofont                 Output font file

optional arguments:

  -i INPUT, --input INPUT
                        Font to get glyphs from
  -r RANGE, --range RANGE
                        StartUnicode..EndUnicode no spaces, e.g. 20..7E
  --rangefile RANGEFILE
                        File with USVs e.g. 20 or a range e.g. 20..7E or both
  -n NAME, --name NAME  Include glyph named name
  --namefile NAMEFILE   File with glyph names
  -a, --anchors         Copy across anchor points
  -f, --force           Overwrite existing glyphs in the font
  -s SCALE, --scale SCALE
                        Scale glyphs by this factor

Default name for ofont is new

_[Return to table of scripts](#table-of-scripts)_

---
#### FFremoveAllOverlaps
Usage: ```FFremoveAllOverlaps ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-p PARAMS] also apply)_

Remove overlap on all glyphs in a ttf font

_[Return to table of scripts](#table-of-scripts)_

---
#### FTMLcreateOdt
Usage: ```FTMLcreateOdt [-f FONT] input [output]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

This creates a LibreOffice writer document based on input test data in [Font Test Markup Language](https://github.com/silnrsi/ftml) format and font information specified with command line parameters.

Example that uses FTML input contained in the file `test-ss.xml` and creates a LibreOffice writer document named `test-ss.odt`. There will be two columns in the output document, one for the installed font `Andika New Basic` and one for the font contained in the file `AndikaNewBasic-Regular.ttf`. (This compares a newly built font with an installed reference.)

```
FTMLcreateOdt -f "Andika New Basic" -f "AndikaNewBasic-Regular.ttf" test-ss.xml test-ss.odt
```

If the font specified with the -f parameter contains a '.' it is assumed to be a file name, otherwise it is assumed to be the name of an installed font. In the former case, the font is embedded in the .odt document, in the latter case the font is expected to be installed on the machine that views the .odt document.

_[Return to table of scripts](#table-of-scripts)_

---
#### GDLchangeNames
Usage: ```GDLchangeNames [-n NAMES] [--names2 [NAMES2]] [--psnames PSNAMES] input [output]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Changes the graphite names within GDL files(s) based on mappings file(s). It can work on an individual file or on all the gdl/gdh files within a folder. It also updates postscript names in postscript() statements

Two mappings files are required (NAMES and PSNAMES).  Optionally a second mapping file, NAMES2 can be supplied.

The mapping files are csv files of the format "```old name, new name```". It logs if any graphite names are in the GDL but not found in the mapping files.

Example usage:

```
GDLchangeNames -n gdlmap.csv --psnames psnames.csv source/graphite
```
will update all the .gdl and.gdh files within the source/graphite folder.

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOaddAnchors
Usage: ```UFOaddAnchors [-i ANCHORINFO]  [-a] [-r {X,S,E,P,W,I,V}] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

_This section is WIP!_

Read anchor data from XML file and apply to UFO

positional arguments:
  ifont                 Input UFO
  ofont                 Output UFO

optional arguments:

  -i ANCHORINFO, --anchorinfo ANCHORINFO
                        XML file with anchor data

  -a, --analysis        Analysis only; no output font generated
  -r {X,S,E,P,W,I,V}, --report {X,S,E,P,W,I,V}
                        Set reporting level for log

_[Return to table of scripts](#table-of-scripts)_

---

####  UFObuildComp
Usage: ```UFObuildComp [-i CDFILE] [-a] [-f] [-r {X,S,E,P,W,I,V}] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

_This section is WIP!_

Read Composite Definitions and add glyphs to a UFO font

positional arguments:
  ifont                 Input UFO
  ofont                 Output UFO

optional arguments:

  -i CDFILE, --cdfile CDFILE
                        Composite Definitions input file

  -a, --analysis        Analysis only; no output font generated
  -f, --force           Force overwrite of glyphs having outlines
  -r {X,S,E,P,W,I,V}, --report {X,S,E,P,W,I,V}
                        Set reporting level for log
                        Set reporting level for log

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOconvert
usage: ```UFOconvert [-v VERSION] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

This converts UFO fonts from one version to another (such as UFO2 to UFO3), but if no version is specified it will simply normalize the font without converting it. _Note that most pysilfont scripts automatically output normalized UFOs, so UFOconvert is normally only needed after fonts have been processed by external font tools._

Example that normalizes the named font:

```
UFOconvert Nokyung-Regular.ufo
```

The normalization follows the [default behaviours](#link-to-be-set), but these can be overriden using [custom parameters](#link-to-be-set)

If you are a macOS user, see _pysilfont/actionsosx/README.txt_ to install an action that will enable you to run UFOconvert without using the command line.

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOcopyMeta
usage: ```UFOcopyMeta [-r] fromfont tofont```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

This copies selected fontlist.plist metadata (eg copyright, openTypeNameVersion, decender) between fonts in different (related) families. 

It is usually run against the master (regular) font in each family then data synced within family afterwards using [UFOsyncMeta](#ufosyncmeta).

Example usage:

```UFOcopyMeta GentiumPlus-Regular.ufo GentiumBookPlus-Bold```

If run with -r or \-\-reportonly it just reports what values would be updated.

Look in UFOcopyMeta.py for a full list of metadata copied.  Note that only fontinfo.plist is updated; the target font is not normalized.

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOexportAnchors
usage: ```UFOexportAnchors [-r {X,S,E,P,W,I,V}]  [-g] [-s] ifont [output]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

This exports anchor data from a UFO font to an XML file. (An "anchor" is also called an "attachment point" which is sometimes abbreviated to "AP".)

Example that exports the anchors contained in the UFO font `CharisSIL-Regular.ufo`, sorts the resulting glyph elements by name (PSName) rather than glyph ID (GID), and writes them to an XML file `CharisSIL-Regular_ap.xml`.

```
UFOexportAnchors -s font-charis/source/CharisSIL-Regular.ufo CharisSIL-Regular_ap.xml
```

If the command line includes

- -g, then the GID attribute will be present in the glyph element.
- -s, then the glyph elements will be sorted by PSName attribute (rather than by GID attribute).
- -u, then the UID attribute will include a "U+" prefix


_[Return to table of scripts](#table-of-scripts)_

---
####  UFOexportPSnames
usage: ```UFOexportPSnames [-o OUTPUT] [--nocomments] ifont```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Export a mapping of glyph name to postscript name to a csv file, format "```glyphname,postscriptname```"

It includes comments at the start saying when it was run etc unless \-\-nocomments is specified

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOexportUnicodes
usage: ```UFOexportUnicodes  [-o OUTPUT] [--nocomments] ifont```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Export a mapping of glyph name to unicode to a csv file, format "```glyphname,unicode```" for glyphs that have a defined unicode. Does not support double-encoded glyphs.

It includes comments at the start saying when it was run etc unless \-\-nocomments is specified

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOloadGlyphOrder
usage: ```UFOloadGlyphOrder [-i INPUT] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Load glyph order data into public.glyphOrder in lib.plist based on a text file with one glyph name per line.

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOsetAssocFeat
usage: ```UFOsetAssocFeat [-i INPUT] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Add associate feature info to  org.sil.assocFeatureValue glif lib based on a csv file, format "```glyphname,featurename[,featurevalue]```"

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOsetAssocUIDs
usage: ```UFOsetAssocUIDs [-i INPUT] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Add associate UID info to org.sil.assocUIDs in glif lib based on a csv file - could be one value for variant UIDs and multiple for ligatures,   format "```glyphname,UID[,UID]```"

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOsetPSnames
usage: ```UFOsetPSnames [-i INPUT] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Add public.postscriptname to glif lib based on a csv file,  format "```glyphname,postscriptname```"

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOsetUnicodes
usage: ```UFOsetUnicodes [-i INPUT] ifont [ofont]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Set the unicodes of glyphs in a font based on a csv file,  format "```glyphname,UID```". Note that this will not currently remove any unicode values that already exist in unlisted glyphs

_[Return to table of scripts](#table-of-scripts)_

---
####  UFOsetVersion
usage: ```UFOsetVersion font [newversion]```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

This updates the various font version fields based on 'newversion' supplied which may be:

- Full openTypeNameVersion string, except for the opening “Version “ text, eg “1.234 beta2”
- +1 to increment to the patch version number - see below
- not supplied, in which case the current values will be validated and existing openTypeNameVersion string displayed

It will update the openTypeNameVersion, versionMajor and versionMinor fields. It works assuming that openTypeNameVersion is of the form:

"Version M.mpp" or "Version M.mpp extrainfo", eg "Version 1.323 Beta2"


Based on [FDBP](#linktobeset), the version number is parsed as M.mpp where M is major, m is minor and pp is patch number.  M matches the versionMajor and mpp the versionMinor fields.

Incrementing will fail if either the openTypeNameVersion is not formatted correctly or the version numbers in there don’t match those in versionMajor and versionMinor.

Examples of usage:

```UFOsetVersion font.ufo "1.423"```

will set:

- openTypeNameVersion to "Version 1.423"
- versionMajor to 1
- versionMinor to 423
 
```UFOsetVersion font.ufo +1```
 
If values were originally as in the first example, openTypeNameVersion will be changed to "Version 1.424" and versionMinor to 424
 
_[Return to table of scripts](#table-of-scripts)_

---
####  UFOsyncMeta
usage: ```UFOsyncMeta [-s] [-m [MASTER]] [-r] [-n] [--normalize] ifont```

_([Standard options](#standard-options) [-h] [-d] [-q] [-l LOG] [-p PARAMS] also apply)_

Verifies and synchronises fontinfo.plist metatdata across a family of fonts.  By default it uses the regular font as the master and updates any other fonts that exist assuming standard name endings of -Regular, -Italic, -Bold and -BoldItalic.  Optionally a single font file can be synced against any other font as master, regardless of file naming.

Example usage for family of fonts:

```
UFOsyncMeta CharisSIL-Regular.ufo
```

This will sync the metadata in CharisSIL-Italic, CharisSIL-Bold and CharisSIL-BoldItalic against values in CharisSIL-Regular.  In addition it will verify certain field in all fonts (including Regular) are valid and follow [FDBP](#linktobeset) best-pactice standards.

Example usages for a single font:

```
UFOsyncMeta -s font-Italic.ufo
UFOsyncMeta -s font-Italic.ufo -m otherfont.ufo
```
The first will sync font-Italic against font-Regular and the second against otherfont.

Look in UFOsyncMeta.py for a full details of metadata actions.  Note that by default only fontinfo.plist is updated so fonts are not normalized.  Use \-\-normalize to additionally normalize all fonts in the family.

_[Return to table of scripts](#table-of-scripts)_

---
#### Standard Options

Will be link to details of these, probably in another document

_[Return to table of scripts](#table-of-scripts)_

#### Link to be set

Will be link to details of these, probably in another document

_[Return to table of scripts](#table-of-scripts)_

---

## Example Scripts

When Pysilfont is downloaded, there are example scripts in pysilfont/examples.  These are a mixture of scripts that are under development, scripts that work but would likely need amending for a specific project's need  and others that are just examples of how things could be done.

Some are documented below; for others just read the scripts!

_This section is WIP!_