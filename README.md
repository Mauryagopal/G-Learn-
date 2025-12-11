# G-Learn
A lightweight machine learning library implemented from scratch.

## 📂 Project Structure
```
├── README.md
├── examples
├── glearn
│   ├── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   └── utils.py
│   ├── models
│   │   ├── __init__.py
│   │   └── linear_regression.py
│   └── preprocessing
│       ├── __init__.py
│       └── standard_scaler.py
├── setup_glearn.py
├── tests
└── venv
    ├── Include
    ├── Lib
    │   └── site-packages
    │       ├── PIL
    │       │   ├── AvifImagePlugin.py
    │       │   ├── BdfFontFile.py
    │       │   ├── BlpImagePlugin.py
    │       │   ├── BmpImagePlugin.py
    │       │   ├── BufrStubImagePlugin.py
    │       │   ├── ContainerIO.py
    │       │   ├── CurImagePlugin.py
    │       │   ├── DcxImagePlugin.py
    │       │   ├── DdsImagePlugin.py
    │       │   ├── EpsImagePlugin.py
    │       │   ├── ExifTags.py
    │       │   ├── FitsImagePlugin.py
    │       │   ├── FliImagePlugin.py
    │       │   ├── FontFile.py
    │       │   ├── FpxImagePlugin.py
    │       │   ├── FtexImagePlugin.py
    │       │   ├── GbrImagePlugin.py
    │       │   ├── GdImageFile.py
    │       │   ├── GifImagePlugin.py
    │       │   ├── GimpGradientFile.py
    │       │   ├── GimpPaletteFile.py
    │       │   ├── GribStubImagePlugin.py
    │       │   ├── Hdf5StubImagePlugin.py
    │       │   ├── IcnsImagePlugin.py
    │       │   ├── IcoImagePlugin.py
    │       │   ├── ImImagePlugin.py
    │       │   ├── Image.py
    │       │   ├── ImageChops.py
    │       │   ├── ImageCms.py
    │       │   ├── ImageColor.py
    │       │   ├── ImageDraw.py
    │       │   ├── ImageDraw2.py
    │       │   ├── ImageEnhance.py
    │       │   ├── ImageFile.py
    │       │   ├── ImageFilter.py
    │       │   ├── ImageFont.py
    │       │   ├── ImageGrab.py
    │       │   ├── ImageMath.py
    │       │   ├── ImageMode.py
    │       │   ├── ImageMorph.py
    │       │   ├── ImageOps.py
    │       │   ├── ImagePalette.py
    │       │   ├── ImagePath.py
    │       │   ├── ImageQt.py
    │       │   ├── ImageSequence.py
    │       │   ├── ImageShow.py
    │       │   ├── ImageStat.py
    │       │   ├── ImageText.py
    │       │   ├── ImageTk.py
    │       │   ├── ImageTransform.py
    │       │   ├── ImageWin.py
    │       │   ├── ImtImagePlugin.py
    │       │   ├── IptcImagePlugin.py
    │       │   ├── Jpeg2KImagePlugin.py
    │       │   ├── JpegImagePlugin.py
    │       │   ├── JpegPresets.py
    │       │   ├── McIdasImagePlugin.py
    │       │   ├── MicImagePlugin.py
    │       │   ├── MpegImagePlugin.py
    │       │   ├── MpoImagePlugin.py
    │       │   ├── MspImagePlugin.py
    │       │   ├── PSDraw.py
    │       │   ├── PaletteFile.py
    │       │   ├── PalmImagePlugin.py
    │       │   ├── PcdImagePlugin.py
    │       │   ├── PcfFontFile.py
    │       │   ├── PcxImagePlugin.py
    │       │   ├── PdfImagePlugin.py
    │       │   ├── PdfParser.py
    │       │   ├── PixarImagePlugin.py
    │       │   ├── PngImagePlugin.py
    │       │   ├── PpmImagePlugin.py
    │       │   ├── PsdImagePlugin.py
    │       │   ├── QoiImagePlugin.py
    │       │   ├── SgiImagePlugin.py
    │       │   ├── SpiderImagePlugin.py
    │       │   ├── SunImagePlugin.py
    │       │   ├── TarIO.py
    │       │   ├── TgaImagePlugin.py
    │       │   ├── TiffImagePlugin.py
    │       │   ├── TiffTags.py
    │       │   ├── WalImageFile.py
    │       │   ├── WebPImagePlugin.py
    │       │   ├── WmfImagePlugin.py
    │       │   ├── XVThumbImagePlugin.py
    │       │   ├── XbmImagePlugin.py
    │       │   ├── XpmImagePlugin.py
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__
    │       │   │   ├── AvifImagePlugin.cpython-312.pyc
    │       │   │   ├── BdfFontFile.cpython-312.pyc
    │       │   │   ├── BlpImagePlugin.cpython-312.pyc
    │       │   │   ├── BmpImagePlugin.cpython-312.pyc
    │       │   │   ├── BufrStubImagePlugin.cpython-312.pyc
    │       │   │   ├── ContainerIO.cpython-312.pyc
    │       │   │   ├── CurImagePlugin.cpython-312.pyc
    │       │   │   ├── DcxImagePlugin.cpython-312.pyc
    │       │   │   ├── DdsImagePlugin.cpython-312.pyc
    │       │   │   ├── EpsImagePlugin.cpython-312.pyc
    │       │   │   ├── ExifTags.cpython-312.pyc
    │       │   │   ├── FitsImagePlugin.cpython-312.pyc
    │       │   │   ├── FliImagePlugin.cpython-312.pyc
    │       │   │   ├── FontFile.cpython-312.pyc
    │       │   │   ├── FpxImagePlugin.cpython-312.pyc
    │       │   │   ├── FtexImagePlugin.cpython-312.pyc
    │       │   │   ├── GbrImagePlugin.cpython-312.pyc
    │       │   │   ├── GdImageFile.cpython-312.pyc
    │       │   │   ├── GifImagePlugin.cpython-312.pyc
    │       │   │   ├── GimpGradientFile.cpython-312.pyc
    │       │   │   ├── GimpPaletteFile.cpython-312.pyc
    │       │   │   ├── GribStubImagePlugin.cpython-312.pyc
    │       │   │   ├── Hdf5StubImagePlugin.cpython-312.pyc
    │       │   │   ├── IcnsImagePlugin.cpython-312.pyc
    │       │   │   ├── IcoImagePlugin.cpython-312.pyc
    │       │   │   ├── ImImagePlugin.cpython-312.pyc
    │       │   │   ├── Image.cpython-312.pyc
    │       │   │   ├── ImageChops.cpython-312.pyc
    │       │   │   ├── ImageCms.cpython-312.pyc
    │       │   │   ├── ImageColor.cpython-312.pyc
    │       │   │   ├── ImageDraw.cpython-312.pyc
    │       │   │   ├── ImageDraw2.cpython-312.pyc
    │       │   │   ├── ImageEnhance.cpython-312.pyc
    │       │   │   ├── ImageFile.cpython-312.pyc
    │       │   │   ├── ImageFilter.cpython-312.pyc
    │       │   │   ├── ImageFont.cpython-312.pyc
    │       │   │   ├── ImageGrab.cpython-312.pyc
    │       │   │   ├── ImageMath.cpython-312.pyc
    │       │   │   ├── ImageMode.cpython-312.pyc
    │       │   │   ├── ImageMorph.cpython-312.pyc
    │       │   │   ├── ImageOps.cpython-312.pyc
    │       │   │   ├── ImagePalette.cpython-312.pyc
    │       │   │   ├── ImagePath.cpython-312.pyc
    │       │   │   ├── ImageQt.cpython-312.pyc
    │       │   │   ├── ImageSequence.cpython-312.pyc
    │       │   │   ├── ImageShow.cpython-312.pyc
    │       │   │   ├── ImageStat.cpython-312.pyc
    │       │   │   ├── ImageText.cpython-312.pyc
    │       │   │   ├── ImageTk.cpython-312.pyc
    │       │   │   ├── ImageTransform.cpython-312.pyc
    │       │   │   ├── ImageWin.cpython-312.pyc
    │       │   │   ├── ImtImagePlugin.cpython-312.pyc
    │       │   │   ├── IptcImagePlugin.cpython-312.pyc
    │       │   │   ├── Jpeg2KImagePlugin.cpython-312.pyc
    │       │   │   ├── JpegImagePlugin.cpython-312.pyc
    │       │   │   ├── JpegPresets.cpython-312.pyc
    │       │   │   ├── McIdasImagePlugin.cpython-312.pyc
    │       │   │   ├── MicImagePlugin.cpython-312.pyc
    │       │   │   ├── MpegImagePlugin.cpython-312.pyc
    │       │   │   ├── MpoImagePlugin.cpython-312.pyc
    │       │   │   ├── MspImagePlugin.cpython-312.pyc
    │       │   │   ├── PSDraw.cpython-312.pyc
    │       │   │   ├── PaletteFile.cpython-312.pyc
    │       │   │   ├── PalmImagePlugin.cpython-312.pyc
    │       │   │   ├── PcdImagePlugin.cpython-312.pyc
    │       │   │   ├── PcfFontFile.cpython-312.pyc
    │       │   │   ├── PcxImagePlugin.cpython-312.pyc
    │       │   │   ├── PdfImagePlugin.cpython-312.pyc
    │       │   │   ├── PdfParser.cpython-312.pyc
    │       │   │   ├── PixarImagePlugin.cpython-312.pyc
    │       │   │   ├── PngImagePlugin.cpython-312.pyc
    │       │   │   ├── PpmImagePlugin.cpython-312.pyc
    │       │   │   ├── PsdImagePlugin.cpython-312.pyc
    │       │   │   ├── QoiImagePlugin.cpython-312.pyc
    │       │   │   ├── SgiImagePlugin.cpython-312.pyc
    │       │   │   ├── SpiderImagePlugin.cpython-312.pyc
    │       │   │   ├── SunImagePlugin.cpython-312.pyc
    │       │   │   ├── TarIO.cpython-312.pyc
    │       │   │   ├── TgaImagePlugin.cpython-312.pyc
    │       │   │   ├── TiffImagePlugin.cpython-312.pyc
    │       │   │   ├── TiffTags.cpython-312.pyc
    │       │   │   ├── WalImageFile.cpython-312.pyc
    │       │   │   ├── WebPImagePlugin.cpython-312.pyc
    │       │   │   ├── WmfImagePlugin.cpython-312.pyc
    │       │   │   ├── XVThumbImagePlugin.cpython-312.pyc
    │       │   │   ├── XbmImagePlugin.cpython-312.pyc
    │       │   │   ├── XpmImagePlugin.cpython-312.pyc
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── __main__.cpython-312.pyc
    │       │   │   ├── _binary.cpython-312.pyc
    │       │   │   ├── _deprecate.cpython-312.pyc
    │       │   │   ├── _tkinter_finder.cpython-312.pyc
    │       │   │   ├── _typing.cpython-312.pyc
    │       │   │   ├── _util.cpython-312.pyc
    │       │   │   ├── _version.cpython-312.pyc
    │       │   │   ├── features.cpython-312.pyc
    │       │   │   └── report.cpython-312.pyc
    │       │   ├── _avif.cp312-win_amd64.pyd
    │       │   ├── _avif.pyi
    │       │   ├── _binary.py
    │       │   ├── _deprecate.py
    │       │   ├── _imaging.cp312-win_amd64.pyd
    │       │   ├── _imaging.pyi
    │       │   ├── _imagingcms.cp312-win_amd64.pyd
    │       │   ├── _imagingcms.pyi
    │       │   ├── _imagingft.cp312-win_amd64.pyd
    │       │   ├── _imagingft.pyi
    │       │   ├── _imagingmath.cp312-win_amd64.pyd
    │       │   ├── _imagingmath.pyi
    │       │   ├── _imagingmorph.cp312-win_amd64.pyd
    │       │   ├── _imagingmorph.pyi
    │       │   ├── _imagingtk.cp312-win_amd64.pyd
    │       │   ├── _imagingtk.pyi
    │       │   ├── _tkinter_finder.py
    │       │   ├── _typing.py
    │       │   ├── _util.py
    │       │   ├── _version.py
    │       │   ├── _webp.cp312-win_amd64.pyd
    │       │   ├── _webp.pyi
    │       │   ├── features.py
    │       │   ├── py.typed
    │       │   └── report.py
    │       ├── __pycache__
    │       │   ├── py.cpython-312.pyc
    │       │   ├── pylab.cpython-312.pyc
    │       │   └── six.cpython-312.pyc
    │       ├── _pytest
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── _argcomplete.cpython-312.pyc
    │       │   │   ├── _version.cpython-312.pyc
    │       │   │   ├── cacheprovider.cpython-312.pyc
    │       │   │   ├── capture.cpython-312.pyc
    │       │   │   ├── compat.cpython-312.pyc
    │       │   │   ├── debugging.cpython-312.pyc
    │       │   │   ├── deprecated.cpython-312.pyc
    │       │   │   ├── doctest.cpython-312.pyc
    │       │   │   ├── faulthandler.cpython-312.pyc
    │       │   │   ├── fixtures.cpython-312.pyc
    │       │   │   ├── freeze_support.cpython-312.pyc
    │       │   │   ├── helpconfig.cpython-312.pyc
    │       │   │   ├── hookspec.cpython-312.pyc
    │       │   │   ├── junitxml.cpython-312.pyc
    │       │   │   ├── legacypath.cpython-312.pyc
    │       │   │   ├── logging.cpython-312.pyc
    │       │   │   ├── main.cpython-312.pyc
    │       │   │   ├── monkeypatch.cpython-312.pyc
    │       │   │   ├── nodes.cpython-312.pyc
    │       │   │   ├── outcomes.cpython-312.pyc
    │       │   │   ├── pastebin.cpython-312.pyc
    │       │   │   ├── pathlib.cpython-312.pyc
    │       │   │   ├── pytester.cpython-312.pyc
    │       │   │   ├── pytester_assertions.cpython-312.pyc
    │       │   │   ├── python.cpython-312.pyc
    │       │   │   ├── python_api.cpython-312.pyc
    │       │   │   ├── raises.cpython-312.pyc
    │       │   │   ├── recwarn.cpython-312.pyc
    │       │   │   ├── reports.cpython-312.pyc
    │       │   │   ├── runner.cpython-312.pyc
    │       │   │   ├── scope.cpython-312.pyc
    │       │   │   ├── setuponly.cpython-312.pyc
    │       │   │   ├── setupplan.cpython-312.pyc
    │       │   │   ├── skipping.cpython-312.pyc
    │       │   │   ├── stash.cpython-312.pyc
    │       │   │   ├── stepwise.cpython-312.pyc
    │       │   │   ├── subtests.cpython-312.pyc
    │       │   │   ├── terminal.cpython-312.pyc
    │       │   │   ├── terminalprogress.cpython-312.pyc
    │       │   │   ├── threadexception.cpython-312.pyc
    │       │   │   ├── timing.cpython-312.pyc
    │       │   │   ├── tmpdir.cpython-312.pyc
    │       │   │   ├── tracemalloc.cpython-312.pyc
    │       │   │   ├── unittest.cpython-312.pyc
    │       │   │   ├── unraisableexception.cpython-312.pyc
    │       │   │   ├── warning_types.cpython-312.pyc
    │       │   │   └── warnings.cpython-312.pyc
    │       │   ├── _argcomplete.py
    │       │   ├── _code
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── code.cpython-312.pyc
    │       │   │   │   └── source.cpython-312.pyc
    │       │   │   ├── code.py
    │       │   │   └── source.py
    │       │   ├── _io
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── pprint.cpython-312.pyc
    │       │   │   │   ├── saferepr.cpython-312.pyc
    │       │   │   │   ├── terminalwriter.cpython-312.pyc
    │       │   │   │   └── wcwidth.cpython-312.pyc
    │       │   │   ├── pprint.py
    │       │   │   ├── saferepr.py
    │       │   │   ├── terminalwriter.py
    │       │   │   └── wcwidth.py
    │       │   ├── _py
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── error.cpython-312.pyc
    │       │   │   │   └── path.cpython-312.pyc
    │       │   │   ├── error.py
    │       │   │   └── path.py
    │       │   ├── _version.py
    │       │   ├── assertion
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── rewrite.cpython-312.pyc
    │       │   │   │   ├── truncate.cpython-312.pyc
    │       │   │   │   └── util.cpython-312.pyc
    │       │   │   ├── rewrite.py
    │       │   │   ├── truncate.py
    │       │   │   └── util.py
    │       │   ├── cacheprovider.py
    │       │   ├── capture.py
    │       │   ├── compat.py
    │       │   ├── config
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── argparsing.cpython-312.pyc
    │       │   │   │   ├── compat.cpython-312.pyc
    │       │   │   │   ├── exceptions.cpython-312.pyc
    │       │   │   │   └── findpaths.cpython-312.pyc
    │       │   │   ├── argparsing.py
    │       │   │   ├── compat.py
    │       │   │   ├── exceptions.py
    │       │   │   └── findpaths.py
    │       │   ├── debugging.py
    │       │   ├── deprecated.py
    │       │   ├── doctest.py
    │       │   ├── faulthandler.py
    │       │   ├── fixtures.py
    │       │   ├── freeze_support.py
    │       │   ├── helpconfig.py
    │       │   ├── hookspec.py
    │       │   ├── junitxml.py
    │       │   ├── legacypath.py
    │       │   ├── logging.py
    │       │   ├── main.py
    │       │   ├── mark
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── expression.cpython-312.pyc
    │       │   │   │   └── structures.cpython-312.pyc
    │       │   │   ├── expression.py
    │       │   │   └── structures.py
    │       │   ├── monkeypatch.py
    │       │   ├── nodes.py
    │       │   ├── outcomes.py
    │       │   ├── pastebin.py
    │       │   ├── pathlib.py
    │       │   ├── py.typed
    │       │   ├── pytester.py
    │       │   ├── pytester_assertions.py
    │       │   ├── python.py
    │       │   ├── python_api.py
    │       │   ├── raises.py
    │       │   ├── recwarn.py
    │       │   ├── reports.py
    │       │   ├── runner.py
    │       │   ├── scope.py
    │       │   ├── setuponly.py
    │       │   ├── setupplan.py
    │       │   ├── skipping.py
    │       │   ├── stash.py
    │       │   ├── stepwise.py
    │       │   ├── subtests.py
    │       │   ├── terminal.py
    │       │   ├── terminalprogress.py
    │       │   ├── threadexception.py
    │       │   ├── timing.py
    │       │   ├── tmpdir.py
    │       │   ├── tracemalloc.py
    │       │   ├── unittest.py
    │       │   ├── unraisableexception.py
    │       │   ├── warning_types.py
    │       │   └── warnings.py
    │       ├── colorama
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── ansi.cpython-312.pyc
    │       │   │   ├── ansitowin32.cpython-312.pyc
    │       │   │   ├── initialise.cpython-312.pyc
    │       │   │   ├── win32.cpython-312.pyc
    │       │   │   └── winterm.cpython-312.pyc
    │       │   ├── ansi.py
    │       │   ├── ansitowin32.py
    │       │   ├── initialise.py
    │       │   ├── tests
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── ansi_test.cpython-312.pyc
    │       │   │   │   ├── ansitowin32_test.cpython-312.pyc
    │       │   │   │   ├── initialise_test.cpython-312.pyc
    │       │   │   │   ├── isatty_test.cpython-312.pyc
    │       │   │   │   ├── utils.cpython-312.pyc
    │       │   │   │   └── winterm_test.cpython-312.pyc
    │       │   │   ├── ansi_test.py
    │       │   │   ├── ansitowin32_test.py
    │       │   │   ├── initialise_test.py
    │       │   │   ├── isatty_test.py
    │       │   │   ├── utils.py
    │       │   │   └── winterm_test.py
    │       │   ├── win32.py
    │       │   └── winterm.py
    │       ├── colorama-0.4.6.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   └── licenses
    │       │       └── LICENSE.txt
    │       ├── contourpy
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── _version.cpython-312.pyc
    │       │   │   ├── array.cpython-312.pyc
    │       │   │   ├── chunk.cpython-312.pyc
    │       │   │   ├── convert.cpython-312.pyc
    │       │   │   ├── dechunk.cpython-312.pyc
    │       │   │   ├── enum_util.cpython-312.pyc
    │       │   │   ├── typecheck.cpython-312.pyc
    │       │   │   └── types.cpython-312.pyc
    │       │   ├── _contourpy.cp312-win_amd64.lib
    │       │   ├── _contourpy.cp312-win_amd64.pyd
    │       │   ├── _contourpy.pyi
    │       │   ├── _version.py
    │       │   ├── array.py
    │       │   ├── chunk.py
    │       │   ├── convert.py
    │       │   ├── dechunk.py
    │       │   ├── enum_util.py
    │       │   ├── py.typed
    │       │   ├── typecheck.py
    │       │   ├── types.py
    │       │   └── util
    │       │       ├── __init__.py
    │       │       ├── __pycache__
    │       │       │   ├── __init__.cpython-312.pyc
    │       │       │   ├── _build_config.cpython-312.pyc
    │       │       │   ├── bokeh_renderer.cpython-312.pyc
    │       │       │   ├── bokeh_util.cpython-312.pyc
    │       │       │   ├── data.cpython-312.pyc
    │       │       │   ├── mpl_renderer.cpython-312.pyc
    │       │       │   ├── mpl_util.cpython-312.pyc
    │       │       │   └── renderer.cpython-312.pyc
    │       │       ├── _build_config.py
    │       │       ├── bokeh_renderer.py
    │       │       ├── bokeh_util.py
    │       │       ├── data.py
    │       │       ├── mpl_renderer.py
    │       │       ├── mpl_util.py
    │       │       └── renderer.py
    │       ├── contourpy-1.3.3.dist-info
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   └── WHEEL
    │       ├── cycler
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   └── __init__.cpython-312.pyc
    │       │   └── py.typed
    │       ├── cycler-0.12.1.dist-info
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       ├── dateutil
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── _common.cpython-312.pyc
    │       │   │   ├── _version.cpython-312.pyc
    │       │   │   ├── easter.cpython-312.pyc
    │       │   │   ├── relativedelta.cpython-312.pyc
    │       │   │   ├── rrule.cpython-312.pyc
    │       │   │   ├── tzwin.cpython-312.pyc
    │       │   │   └── utils.cpython-312.pyc
    │       │   ├── _common.py
    │       │   ├── _version.py
    │       │   ├── easter.py
    │       │   ├── parser
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _parser.cpython-312.pyc
    │       │   │   │   └── isoparser.cpython-312.pyc
    │       │   │   ├── _parser.py
    │       │   │   └── isoparser.py
    │       │   ├── relativedelta.py
    │       │   ├── rrule.py
    │       │   ├── tz
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _common.cpython-312.pyc
    │       │   │   │   ├── _factories.cpython-312.pyc
    │       │   │   │   ├── tz.cpython-312.pyc
    │       │   │   │   └── win.cpython-312.pyc
    │       │   │   ├── _common.py
    │       │   │   ├── _factories.py
    │       │   │   ├── tz.py
    │       │   │   └── win.py
    │       │   ├── tzwin.py
    │       │   ├── utils.py
    │       │   └── zoneinfo
    │       │       ├── __init__.py
    │       │       ├── __pycache__
    │       │       │   ├── __init__.cpython-312.pyc
    │       │       │   └── rebuild.cpython-312.pyc
    │       │       ├── dateutil-zoneinfo.tar.gz
    │       │       └── rebuild.py
    │       ├── fontTools
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── __main__.cpython-312.pyc
    │       │   │   ├── afmLib.cpython-312.pyc
    │       │   │   ├── agl.cpython-312.pyc
    │       │   │   ├── annotations.cpython-312.pyc
    │       │   │   ├── fontBuilder.cpython-312.pyc
    │       │   │   ├── help.cpython-312.pyc
    │       │   │   ├── tfmLib.cpython-312.pyc
    │       │   │   ├── ttx.cpython-312.pyc
    │       │   │   └── unicode.cpython-312.pyc
    │       │   ├── afmLib.py
    │       │   ├── agl.py
    │       │   ├── annotations.py
    │       │   ├── cffLib
    │       │   │   ├── CFF2ToCFF.py
    │       │   │   ├── CFFToCFF2.py
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── CFF2ToCFF.cpython-312.pyc
    │       │   │   │   ├── CFFToCFF2.cpython-312.pyc
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── specializer.cpython-312.pyc
    │       │   │   │   ├── transforms.cpython-312.pyc
    │       │   │   │   └── width.cpython-312.pyc
    │       │   │   ├── specializer.py
    │       │   │   ├── transforms.py
    │       │   │   └── width.py
    │       │   ├── colorLib
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── builder.cpython-312.pyc
    │       │   │   │   ├── errors.cpython-312.pyc
    │       │   │   │   ├── geometry.cpython-312.pyc
    │       │   │   │   ├── table_builder.cpython-312.pyc
    │       │   │   │   └── unbuilder.cpython-312.pyc
    │       │   │   ├── builder.py
    │       │   │   ├── errors.py
    │       │   │   ├── geometry.py
    │       │   │   ├── table_builder.py
    │       │   │   └── unbuilder.py
    │       │   ├── config
    │       │   │   ├── __init__.py
    │       │   │   └── __pycache__
    │       │   │       └── __init__.cpython-312.pyc
    │       │   ├── cu2qu
    │       │   │   ├── __init__.py
    │       │   │   ├── __main__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   ├── benchmark.cpython-312.pyc
    │       │   │   │   ├── cli.cpython-312.pyc
    │       │   │   │   ├── cu2qu.cpython-312.pyc
    │       │   │   │   ├── errors.cpython-312.pyc
    │       │   │   │   └── ufo.cpython-312.pyc
    │       │   │   ├── benchmark.py
    │       │   │   ├── cli.py
    │       │   │   ├── cu2qu.c
    │       │   │   ├── cu2qu.cp312-win_amd64.pyd
    │       │   │   ├── cu2qu.py
    │       │   │   ├── errors.py
    │       │   │   └── ufo.py
    │       │   ├── designspaceLib
    │       │   │   ├── __init__.py
    │       │   │   ├── __main__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   ├── split.cpython-312.pyc
    │       │   │   │   ├── statNames.cpython-312.pyc
    │       │   │   │   └── types.cpython-312.pyc
    │       │   │   ├── split.py
    │       │   │   ├── statNames.py
    │       │   │   └── types.py
    │       │   ├── encodings
    │       │   │   ├── MacRoman.py
    │       │   │   ├── StandardEncoding.py
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── MacRoman.cpython-312.pyc
    │       │   │   │   ├── StandardEncoding.cpython-312.pyc
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── codecs.cpython-312.pyc
    │       │   │   └── codecs.py
    │       │   ├── feaLib
    │       │   │   ├── __init__.py
    │       │   │   ├── __main__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   ├── ast.cpython-312.pyc
    │       │   │   │   ├── builder.cpython-312.pyc
    │       │   │   │   ├── error.cpython-312.pyc
    │       │   │   │   ├── lexer.cpython-312.pyc
    │       │   │   │   ├── location.cpython-312.pyc
    │       │   │   │   ├── lookupDebugInfo.cpython-312.pyc
    │       │   │   │   ├── parser.cpython-312.pyc
    │       │   │   │   └── variableScalar.cpython-312.pyc
    │       │   │   ├── ast.py
    │       │   │   ├── builder.py
    │       │   │   ├── error.py
    │       │   │   ├── lexer.c
    │       │   │   ├── lexer.cp312-win_amd64.pyd
    │       │   │   ├── lexer.py
    │       │   │   ├── location.py
    │       │   │   ├── lookupDebugInfo.py
    │       │   │   ├── parser.py
    │       │   │   └── variableScalar.py
    │       │   ├── fontBuilder.py
    │       │   ├── help.py
    │       │   ├── merge
    │       │   │   ├── __init__.py
    │       │   │   ├── __main__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   ├── base.cpython-312.pyc
    │       │   │   │   ├── cmap.cpython-312.pyc
    │       │   │   │   ├── layout.cpython-312.pyc
    │       │   │   │   ├── options.cpython-312.pyc
    │       │   │   │   ├── tables.cpython-312.pyc
    │       │   │   │   ├── unicode.cpython-312.pyc
    │       │   │   │   └── util.cpython-312.pyc
    │       │   │   ├── base.py
    │       │   │   ├── cmap.py
    │       │   │   ├── layout.py
    │       │   │   ├── options.py
    │       │   │   ├── tables.py
    │       │   │   ├── unicode.py
    │       │   │   └── util.py
    │       │   ├── misc
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── arrayTools.cpython-312.pyc
    │       │   │   │   ├── bezierTools.cpython-312.pyc
    │       │   │   │   ├── classifyTools.cpython-312.pyc
    │       │   │   │   ├── cliTools.cpython-312.pyc
    │       │   │   │   ├── configTools.cpython-312.pyc
    │       │   │   │   ├── cython.cpython-312.pyc
    │       │   │   │   ├── dictTools.cpython-312.pyc
    │       │   │   │   ├── eexec.cpython-312.pyc
    │       │   │   │   ├── encodingTools.cpython-312.pyc
    │       │   │   │   ├── enumTools.cpython-312.pyc
    │       │   │   │   ├── etree.cpython-312.pyc
    │       │   │   │   ├── filenames.cpython-312.pyc
    │       │   │   │   ├── fixedTools.cpython-312.pyc
    │       │   │   │   ├── intTools.cpython-312.pyc
    │       │   │   │   ├── iterTools.cpython-312.pyc
    │       │   │   │   ├── lazyTools.cpython-312.pyc
    │       │   │   │   ├── loggingTools.cpython-312.pyc
    │       │   │   │   ├── macCreatorType.cpython-312.pyc
    │       │   │   │   ├── macRes.cpython-312.pyc
    │       │   │   │   ├── psCharStrings.cpython-312.pyc
    │       │   │   │   ├── psLib.cpython-312.pyc
    │       │   │   │   ├── psOperators.cpython-312.pyc
    │       │   │   │   ├── py23.cpython-312.pyc
    │       │   │   │   ├── roundTools.cpython-312.pyc
    │       │   │   │   ├── sstruct.cpython-312.pyc
    │       │   │   │   ├── symfont.cpython-312.pyc
    │       │   │   │   ├── testTools.cpython-312.pyc
    │       │   │   │   ├── textTools.cpython-312.pyc
    │       │   │   │   ├── timeTools.cpython-312.pyc
    │       │   │   │   ├── transform.cpython-312.pyc
    │       │   │   │   ├── treeTools.cpython-312.pyc
    │       │   │   │   ├── vector.cpython-312.pyc
    │       │   │   │   ├── visitor.cpython-312.pyc
    │       │   │   │   ├── xmlReader.cpython-312.pyc
    │       │   │   │   └── xmlWriter.cpython-312.pyc
    │       │   │   ├── arrayTools.py
    │       │   │   ├── bezierTools.c
    │       │   │   ├── bezierTools.cp312-win_amd64.pyd
    │       │   │   ├── bezierTools.py
    │       │   │   ├── classifyTools.py
    │       │   │   ├── cliTools.py
    │       │   │   ├── configTools.py
    │       │   │   ├── cython.py
    │       │   │   ├── dictTools.py
    │       │   │   ├── eexec.py
    │       │   │   ├── encodingTools.py
    │       │   │   ├── enumTools.py
    │       │   │   ├── etree.py
    │       │   │   ├── filenames.py
    │       │   │   ├── filesystem
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _base.cpython-312.pyc
    │       │   │   │   │   ├── _copy.cpython-312.pyc
    │       │   │   │   │   ├── _errors.cpython-312.pyc
    │       │   │   │   │   ├── _info.cpython-312.pyc
    │       │   │   │   │   ├── _osfs.cpython-312.pyc
    │       │   │   │   │   ├── _path.cpython-312.pyc
    │       │   │   │   │   ├── _subfs.cpython-312.pyc
    │       │   │   │   │   ├── _tempfs.cpython-312.pyc
    │       │   │   │   │   ├── _tools.cpython-312.pyc
    │       │   │   │   │   ├── _walk.cpython-312.pyc
    │       │   │   │   │   └── _zipfs.cpython-312.pyc
    │       │   │   │   ├── _base.py
    │       │   │   │   ├── _copy.py
    │       │   │   │   ├── _errors.py
    │       │   │   │   ├── _info.py
    │       │   │   │   ├── _osfs.py
    │       │   │   │   ├── _path.py
    │       │   │   │   ├── _subfs.py
    │       │   │   │   ├── _tempfs.py
    │       │   │   │   ├── _tools.py
    │       │   │   │   ├── _walk.py
    │       │   │   │   └── _zipfs.py
    │       │   │   ├── fixedTools.py
    │       │   │   ├── intTools.py
    │       │   │   ├── iterTools.py
    │       │   │   ├── lazyTools.py
    │       │   │   ├── loggingTools.py
    │       │   │   ├── macCreatorType.py
    │       │   │   ├── macRes.py
    │       │   │   ├── plistlib
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   └── __init__.cpython-312.pyc
    │       │   │   │   └── py.typed
    │       │   │   ├── psCharStrings.py
    │       │   │   ├── psLib.py
    │       │   │   ├── psOperators.py
    │       │   │   ├── py23.py
    │       │   │   ├── roundTools.py
    │       │   │   ├── sstruct.py
    │       │   │   ├── symfont.py
    │       │   │   ├── testTools.py
    │       │   │   ├── textTools.py
    │       │   │   ├── timeTools.py
    │       │   │   ├── transform.py
    │       │   │   ├── treeTools.py
    │       │   │   ├── vector.py
    │       │   │   ├── visitor.py
    │       │   │   ├── xmlReader.py
    │       │   │   └── xmlWriter.py
    │       │   ├── mtiLib
    │       │   │   ├── __init__.py
    │       │   │   ├── __main__.py
    │       │   │   └── __pycache__
    │       │   │       ├── __init__.cpython-312.pyc
    │       │   │       └── __main__.cpython-312.pyc
    │       │   ├── otlLib
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── builder.cpython-312.pyc
    │       │   │   │   ├── error.cpython-312.pyc
    │       │   │   │   └── maxContextCalc.cpython-312.pyc
    │       │   │   ├── builder.py
    │       │   │   ├── error.py
    │       │   │   ├── maxContextCalc.py
    │       │   │   └── optimize
    │       │   │       ├── __init__.py
    │       │   │       ├── __main__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── __main__.cpython-312.pyc
    │       │   │       │   └── gpos.cpython-312.pyc
    │       │   │       └── gpos.py
    │       │   ├── pens
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── areaPen.cpython-312.pyc
    │       │   │   │   ├── basePen.cpython-312.pyc
    │       │   │   │   ├── boundsPen.cpython-312.pyc
    │       │   │   │   ├── cairoPen.cpython-312.pyc
    │       │   │   │   ├── cocoaPen.cpython-312.pyc
    │       │   │   │   ├── cu2quPen.cpython-312.pyc
    │       │   │   │   ├── explicitClosingLinePen.cpython-312.pyc
    │       │   │   │   ├── filterPen.cpython-312.pyc
    │       │   │   │   ├── freetypePen.cpython-312.pyc
    │       │   │   │   ├── hashPointPen.cpython-312.pyc
    │       │   │   │   ├── momentsPen.cpython-312.pyc
    │       │   │   │   ├── perimeterPen.cpython-312.pyc
    │       │   │   │   ├── pointInsidePen.cpython-312.pyc
    │       │   │   │   ├── pointPen.cpython-312.pyc
    │       │   │   │   ├── qtPen.cpython-312.pyc
    │       │   │   │   ├── qu2cuPen.cpython-312.pyc
    │       │   │   │   ├── quartzPen.cpython-312.pyc
    │       │   │   │   ├── recordingPen.cpython-312.pyc
    │       │   │   │   ├── reportLabPen.cpython-312.pyc
    │       │   │   │   ├── reverseContourPen.cpython-312.pyc
    │       │   │   │   ├── roundingPen.cpython-312.pyc
    │       │   │   │   ├── statisticsPen.cpython-312.pyc
    │       │   │   │   ├── svgPathPen.cpython-312.pyc
    │       │   │   │   ├── t2CharStringPen.cpython-312.pyc
    │       │   │   │   ├── teePen.cpython-312.pyc
    │       │   │   │   ├── transformPen.cpython-312.pyc
    │       │   │   │   ├── ttGlyphPen.cpython-312.pyc
    │       │   │   │   └── wxPen.cpython-312.pyc
    │       │   │   ├── areaPen.py
    │       │   │   ├── basePen.py
    │       │   │   ├── boundsPen.py
    │       │   │   ├── cairoPen.py
    │       │   │   ├── cocoaPen.py
    │       │   │   ├── cu2quPen.py
    │       │   │   ├── explicitClosingLinePen.py
    │       │   │   ├── filterPen.py
    │       │   │   ├── freetypePen.py
    │       │   │   ├── hashPointPen.py
    │       │   │   ├── momentsPen.c
    │       │   │   ├── momentsPen.cp312-win_amd64.pyd
    │       │   │   ├── momentsPen.py
    │       │   │   ├── perimeterPen.py
    │       │   │   ├── pointInsidePen.py
    │       │   │   ├── pointPen.py
    │       │   │   ├── qtPen.py
    │       │   │   ├── qu2cuPen.py
    │       │   │   ├── quartzPen.py
    │       │   │   ├── recordingPen.py
    │       │   │   ├── reportLabPen.py
    │       │   │   ├── reverseContourPen.py
    │       │   │   ├── roundingPen.py
    │       │   │   ├── statisticsPen.py
    │       │   │   ├── svgPathPen.py
    │       │   │   ├── t2CharStringPen.py
    │       │   │   ├── teePen.py
    │       │   │   ├── transformPen.py
    │       │   │   ├── ttGlyphPen.py
    │       │   │   └── wxPen.py
    │       │   ├── qu2cu
    │       │   │   ├── __init__.py
    │       │   │   ├── __main__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   ├── benchmark.cpython-312.pyc
    │       │   │   │   ├── cli.cpython-312.pyc
    │       │   │   │   └── qu2cu.cpython-312.pyc
    │       │   │   ├── benchmark.py
    │       │   │   ├── cli.py
    │       │   │   ├── qu2cu.c
    │       │   │   ├── qu2cu.cp312-win_amd64.pyd
    │       │   │   └── qu2cu.py
    │       │   ├── subset
    │       │   │   ├── __init__.py
    │       │   │   ├── __main__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   ├── cff.cpython-312.pyc
    │       │   │   │   ├── svg.cpython-312.pyc
    │       │   │   │   └── util.cpython-312.pyc
    │       │   │   ├── cff.py
    │       │   │   ├── svg.py
    │       │   │   └── util.py
    │       │   ├── svgLib
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   └── __init__.cpython-312.pyc
    │       │   │   └── path
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── arc.cpython-312.pyc
    │       │   │       │   ├── parser.cpython-312.pyc
    │       │   │       │   └── shapes.cpython-312.pyc
    │       │   │       ├── arc.py
    │       │   │       ├── parser.py
    │       │   │       └── shapes.py
    │       │   ├── t1Lib
    │       │   │   ├── __init__.py
    │       │   │   └── __pycache__
    │       │   │       └── __init__.cpython-312.pyc
    │       │   ├── tfmLib.py
    │       │   ├── ttLib
    │       │   │   ├── __init__.py
    │       │   │   ├── __main__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   ├── macUtils.cpython-312.pyc
    │       │   │   │   ├── removeOverlaps.cpython-312.pyc
    │       │   │   │   ├── reorderGlyphs.cpython-312.pyc
    │       │   │   │   ├── scaleUpem.cpython-312.pyc
    │       │   │   │   ├── sfnt.cpython-312.pyc
    │       │   │   │   ├── standardGlyphOrder.cpython-312.pyc
    │       │   │   │   ├── ttCollection.cpython-312.pyc
    │       │   │   │   ├── ttFont.cpython-312.pyc
    │       │   │   │   ├── ttGlyphSet.cpython-312.pyc
    │       │   │   │   ├── ttVisitor.cpython-312.pyc
    │       │   │   │   └── woff2.cpython-312.pyc
    │       │   │   ├── macUtils.py
    │       │   │   ├── removeOverlaps.py
    │       │   │   ├── reorderGlyphs.py
    │       │   │   ├── scaleUpem.py
    │       │   │   ├── sfnt.py
    │       │   │   ├── standardGlyphOrder.py
    │       │   │   ├── tables
    │       │   │   │   ├── B_A_S_E_.py
    │       │   │   │   ├── BitmapGlyphMetrics.py
    │       │   │   │   ├── C_B_D_T_.py
    │       │   │   │   ├── C_B_L_C_.py
    │       │   │   │   ├── C_F_F_.py
    │       │   │   │   ├── C_F_F__2.py
    │       │   │   │   ├── C_O_L_R_.py
    │       │   │   │   ├── C_P_A_L_.py
    │       │   │   │   ├── D_S_I_G_.py
    │       │   │   │   ├── D__e_b_g.py
    │       │   │   │   ├── DefaultTable.py
    │       │   │   │   ├── E_B_D_T_.py
    │       │   │   │   ├── E_B_L_C_.py
    │       │   │   │   ├── F_F_T_M_.py
    │       │   │   │   ├── F__e_a_t.py
    │       │   │   │   ├── G_D_E_F_.py
    │       │   │   │   ├── G_M_A_P_.py
    │       │   │   │   ├── G_P_K_G_.py
    │       │   │   │   ├── G_P_O_S_.py
    │       │   │   │   ├── G_S_U_B_.py
    │       │   │   │   ├── G_V_A_R_.py
    │       │   │   │   ├── G__l_a_t.py
    │       │   │   │   ├── G__l_o_c.py
    │       │   │   │   ├── H_V_A_R_.py
    │       │   │   │   ├── J_S_T_F_.py
    │       │   │   │   ├── L_T_S_H_.py
    │       │   │   │   ├── M_A_T_H_.py
    │       │   │   │   ├── M_E_T_A_.py
    │       │   │   │   ├── M_V_A_R_.py
    │       │   │   │   ├── O_S_2f_2.py
    │       │   │   │   ├── S_I_N_G_.py
    │       │   │   │   ├── S_T_A_T_.py
    │       │   │   │   ├── S_V_G_.py
    │       │   │   │   ├── S__i_l_f.py
    │       │   │   │   ├── S__i_l_l.py
    │       │   │   │   ├── T_S_I_B_.py
    │       │   │   │   ├── T_S_I_C_.py
    │       │   │   │   ├── T_S_I_D_.py
    │       │   │   │   ├── T_S_I_J_.py
    │       │   │   │   ├── T_S_I_P_.py
    │       │   │   │   ├── T_S_I_S_.py
    │       │   │   │   ├── T_S_I_V_.py
    │       │   │   │   ├── T_S_I__0.py
    │       │   │   │   ├── T_S_I__1.py
    │       │   │   │   ├── T_S_I__2.py
    │       │   │   │   ├── T_S_I__3.py
    │       │   │   │   ├── T_S_I__5.py
    │       │   │   │   ├── T_T_F_A_.py
    │       │   │   │   ├── TupleVariation.py
    │       │   │   │   ├── V_A_R_C_.py
    │       │   │   │   ├── V_D_M_X_.py
    │       │   │   │   ├── V_O_R_G_.py
    │       │   │   │   ├── V_V_A_R_.py
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── B_A_S_E_.cpython-312.pyc
    │       │   │   │   │   ├── BitmapGlyphMetrics.cpython-312.pyc
    │       │   │   │   │   ├── C_B_D_T_.cpython-312.pyc
    │       │   │   │   │   ├── C_B_L_C_.cpython-312.pyc
    │       │   │   │   │   ├── C_F_F_.cpython-312.pyc
    │       │   │   │   │   ├── C_F_F__2.cpython-312.pyc
    │       │   │   │   │   ├── C_O_L_R_.cpython-312.pyc
    │       │   │   │   │   ├── C_P_A_L_.cpython-312.pyc
    │       │   │   │   │   ├── D_S_I_G_.cpython-312.pyc
    │       │   │   │   │   ├── D__e_b_g.cpython-312.pyc
    │       │   │   │   │   ├── DefaultTable.cpython-312.pyc
    │       │   │   │   │   ├── E_B_D_T_.cpython-312.pyc
    │       │   │   │   │   ├── E_B_L_C_.cpython-312.pyc
    │       │   │   │   │   ├── F_F_T_M_.cpython-312.pyc
    │       │   │   │   │   ├── F__e_a_t.cpython-312.pyc
    │       │   │   │   │   ├── G_D_E_F_.cpython-312.pyc
    │       │   │   │   │   ├── G_M_A_P_.cpython-312.pyc
    │       │   │   │   │   ├── G_P_K_G_.cpython-312.pyc
    │       │   │   │   │   ├── G_P_O_S_.cpython-312.pyc
    │       │   │   │   │   ├── G_S_U_B_.cpython-312.pyc
    │       │   │   │   │   ├── G_V_A_R_.cpython-312.pyc
    │       │   │   │   │   ├── G__l_a_t.cpython-312.pyc
    │       │   │   │   │   ├── G__l_o_c.cpython-312.pyc
    │       │   │   │   │   ├── H_V_A_R_.cpython-312.pyc
    │       │   │   │   │   ├── J_S_T_F_.cpython-312.pyc
    │       │   │   │   │   ├── L_T_S_H_.cpython-312.pyc
    │       │   │   │   │   ├── M_A_T_H_.cpython-312.pyc
    │       │   │   │   │   ├── M_E_T_A_.cpython-312.pyc
    │       │   │   │   │   ├── M_V_A_R_.cpython-312.pyc
    │       │   │   │   │   ├── O_S_2f_2.cpython-312.pyc
    │       │   │   │   │   ├── S_I_N_G_.cpython-312.pyc
    │       │   │   │   │   ├── S_T_A_T_.cpython-312.pyc
    │       │   │   │   │   ├── S_V_G_.cpython-312.pyc
    │       │   │   │   │   ├── S__i_l_f.cpython-312.pyc
    │       │   │   │   │   ├── S__i_l_l.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I_B_.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I_C_.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I_D_.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I_J_.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I_P_.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I_S_.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I_V_.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I__0.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I__1.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I__2.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I__3.cpython-312.pyc
    │       │   │   │   │   ├── T_S_I__5.cpython-312.pyc
    │       │   │   │   │   ├── T_T_F_A_.cpython-312.pyc
    │       │   │   │   │   ├── TupleVariation.cpython-312.pyc
    │       │   │   │   │   ├── V_A_R_C_.cpython-312.pyc
    │       │   │   │   │   ├── V_D_M_X_.cpython-312.pyc
    │       │   │   │   │   ├── V_O_R_G_.cpython-312.pyc
    │       │   │   │   │   ├── V_V_A_R_.cpython-312.pyc
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _a_n_k_r.cpython-312.pyc
    │       │   │   │   │   ├── _a_v_a_r.cpython-312.pyc
    │       │   │   │   │   ├── _b_s_l_n.cpython-312.pyc
    │       │   │   │   │   ├── _c_i_d_g.cpython-312.pyc
    │       │   │   │   │   ├── _c_m_a_p.cpython-312.pyc
    │       │   │   │   │   ├── _c_v_a_r.cpython-312.pyc
    │       │   │   │   │   ├── _c_v_t.cpython-312.pyc
    │       │   │   │   │   ├── _f_e_a_t.cpython-312.pyc
    │       │   │   │   │   ├── _f_p_g_m.cpython-312.pyc
    │       │   │   │   │   ├── _f_v_a_r.cpython-312.pyc
    │       │   │   │   │   ├── _g_a_s_p.cpython-312.pyc
    │       │   │   │   │   ├── _g_c_i_d.cpython-312.pyc
    │       │   │   │   │   ├── _g_l_y_f.cpython-312.pyc
    │       │   │   │   │   ├── _g_v_a_r.cpython-312.pyc
    │       │   │   │   │   ├── _h_d_m_x.cpython-312.pyc
    │       │   │   │   │   ├── _h_e_a_d.cpython-312.pyc
    │       │   │   │   │   ├── _h_h_e_a.cpython-312.pyc
    │       │   │   │   │   ├── _h_m_t_x.cpython-312.pyc
    │       │   │   │   │   ├── _k_e_r_n.cpython-312.pyc
    │       │   │   │   │   ├── _l_c_a_r.cpython-312.pyc
    │       │   │   │   │   ├── _l_o_c_a.cpython-312.pyc
    │       │   │   │   │   ├── _l_t_a_g.cpython-312.pyc
    │       │   │   │   │   ├── _m_a_x_p.cpython-312.pyc
    │       │   │   │   │   ├── _m_e_t_a.cpython-312.pyc
    │       │   │   │   │   ├── _m_o_r_t.cpython-312.pyc
    │       │   │   │   │   ├── _m_o_r_x.cpython-312.pyc
    │       │   │   │   │   ├── _n_a_m_e.cpython-312.pyc
    │       │   │   │   │   ├── _o_p_b_d.cpython-312.pyc
    │       │   │   │   │   ├── _p_o_s_t.cpython-312.pyc
    │       │   │   │   │   ├── _p_r_e_p.cpython-312.pyc
    │       │   │   │   │   ├── _p_r_o_p.cpython-312.pyc
    │       │   │   │   │   ├── _s_b_i_x.cpython-312.pyc
    │       │   │   │   │   ├── _t_r_a_k.cpython-312.pyc
    │       │   │   │   │   ├── _v_h_e_a.cpython-312.pyc
    │       │   │   │   │   ├── _v_m_t_x.cpython-312.pyc
    │       │   │   │   │   ├── asciiTable.cpython-312.pyc
    │       │   │   │   │   ├── grUtils.cpython-312.pyc
    │       │   │   │   │   ├── otBase.cpython-312.pyc
    │       │   │   │   │   ├── otConverters.cpython-312.pyc
    │       │   │   │   │   ├── otData.cpython-312.pyc
    │       │   │   │   │   ├── otTables.cpython-312.pyc
    │       │   │   │   │   ├── otTraverse.cpython-312.pyc
    │       │   │   │   │   ├── sbixGlyph.cpython-312.pyc
    │       │   │   │   │   ├── sbixStrike.cpython-312.pyc
    │       │   │   │   │   └── ttProgram.cpython-312.pyc
    │       │   │   │   ├── _a_n_k_r.py
    │       │   │   │   ├── _a_v_a_r.py
    │       │   │   │   ├── _b_s_l_n.py
    │       │   │   │   ├── _c_i_d_g.py
    │       │   │   │   ├── _c_m_a_p.py
    │       │   │   │   ├── _c_v_a_r.py
    │       │   │   │   ├── _c_v_t.py
    │       │   │   │   ├── _f_e_a_t.py
    │       │   │   │   ├── _f_p_g_m.py
    │       │   │   │   ├── _f_v_a_r.py
    │       │   │   │   ├── _g_a_s_p.py
    │       │   │   │   ├── _g_c_i_d.py
    │       │   │   │   ├── _g_l_y_f.py
    │       │   │   │   ├── _g_v_a_r.py
    │       │   │   │   ├── _h_d_m_x.py
    │       │   │   │   ├── _h_e_a_d.py
    │       │   │   │   ├── _h_h_e_a.py
    │       │   │   │   ├── _h_m_t_x.py
    │       │   │   │   ├── _k_e_r_n.py
    │       │   │   │   ├── _l_c_a_r.py
    │       │   │   │   ├── _l_o_c_a.py
    │       │   │   │   ├── _l_t_a_g.py
    │       │   │   │   ├── _m_a_x_p.py
    │       │   │   │   ├── _m_e_t_a.py
    │       │   │   │   ├── _m_o_r_t.py
    │       │   │   │   ├── _m_o_r_x.py
    │       │   │   │   ├── _n_a_m_e.py
    │       │   │   │   ├── _o_p_b_d.py
    │       │   │   │   ├── _p_o_s_t.py
    │       │   │   │   ├── _p_r_e_p.py
    │       │   │   │   ├── _p_r_o_p.py
    │       │   │   │   ├── _s_b_i_x.py
    │       │   │   │   ├── _t_r_a_k.py
    │       │   │   │   ├── _v_h_e_a.py
    │       │   │   │   ├── _v_m_t_x.py
    │       │   │   │   ├── asciiTable.py
    │       │   │   │   ├── grUtils.py
    │       │   │   │   ├── otBase.py
    │       │   │   │   ├── otConverters.py
    │       │   │   │   ├── otData.py
    │       │   │   │   ├── otTables.py
    │       │   │   │   ├── otTraverse.py
    │       │   │   │   ├── sbixGlyph.py
    │       │   │   │   ├── sbixStrike.py
    │       │   │   │   ├── table_API_readme.txt
    │       │   │   │   └── ttProgram.py
    │       │   │   ├── ttCollection.py
    │       │   │   ├── ttFont.py
    │       │   │   ├── ttGlyphSet.py
    │       │   │   ├── ttVisitor.py
    │       │   │   └── woff2.py
    │       │   ├── ttx.py
    │       │   ├── ufoLib
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── converters.cpython-312.pyc
    │       │   │   │   ├── errors.cpython-312.pyc
    │       │   │   │   ├── etree.cpython-312.pyc
    │       │   │   │   ├── filenames.cpython-312.pyc
    │       │   │   │   ├── glifLib.cpython-312.pyc
    │       │   │   │   ├── kerning.cpython-312.pyc
    │       │   │   │   ├── plistlib.cpython-312.pyc
    │       │   │   │   ├── pointPen.cpython-312.pyc
    │       │   │   │   ├── utils.cpython-312.pyc
    │       │   │   │   └── validators.cpython-312.pyc
    │       │   │   ├── converters.py
    │       │   │   ├── errors.py
    │       │   │   ├── etree.py
    │       │   │   ├── filenames.py
    │       │   │   ├── glifLib.py
    │       │   │   ├── kerning.py
    │       │   │   ├── plistlib.py
    │       │   │   ├── pointPen.py
    │       │   │   ├── utils.py
    │       │   │   └── validators.py
    │       │   ├── unicode.py
    │       │   ├── unicodedata
    │       │   │   ├── Blocks.py
    │       │   │   ├── Mirrored.py
    │       │   │   ├── OTTags.py
    │       │   │   ├── ScriptExtensions.py
    │       │   │   ├── Scripts.py
    │       │   │   ├── __init__.py
    │       │   │   └── __pycache__
    │       │   │       ├── Blocks.cpython-312.pyc
    │       │   │       ├── Mirrored.cpython-312.pyc
    │       │   │       ├── OTTags.cpython-312.pyc
    │       │   │       ├── ScriptExtensions.cpython-312.pyc
    │       │   │       ├── Scripts.cpython-312.pyc
    │       │   │       └── __init__.cpython-312.pyc
    │       │   ├── varLib
    │       │   │   ├── __init__.py
    │       │   │   ├── __main__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   ├── avarPlanner.cpython-312.pyc
    │       │   │   │   ├── builder.cpython-312.pyc
    │       │   │   │   ├── cff.cpython-312.pyc
    │       │   │   │   ├── errors.cpython-312.pyc
    │       │   │   │   ├── featureVars.cpython-312.pyc
    │       │   │   │   ├── hvar.cpython-312.pyc
    │       │   │   │   ├── interpolatable.cpython-312.pyc
    │       │   │   │   ├── interpolatableHelpers.cpython-312.pyc
    │       │   │   │   ├── interpolatablePlot.cpython-312.pyc
    │       │   │   │   ├── interpolatableTestContourOrder.cpython-312.pyc
    │       │   │   │   ├── interpolatableTestStartingPoint.cpython-312.pyc
    │       │   │   │   ├── interpolate_layout.cpython-312.pyc
    │       │   │   │   ├── iup.cpython-312.pyc
    │       │   │   │   ├── merger.cpython-312.pyc
    │       │   │   │   ├── models.cpython-312.pyc
    │       │   │   │   ├── multiVarStore.cpython-312.pyc
    │       │   │   │   ├── mutator.cpython-312.pyc
    │       │   │   │   ├── mvar.cpython-312.pyc
    │       │   │   │   ├── plot.cpython-312.pyc
    │       │   │   │   ├── stat.cpython-312.pyc
    │       │   │   │   └── varStore.cpython-312.pyc
    │       │   │   ├── avar
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   │   ├── build.cpython-312.pyc
    │       │   │   │   │   ├── map.cpython-312.pyc
    │       │   │   │   │   ├── plan.cpython-312.pyc
    │       │   │   │   │   └── unbuild.cpython-312.pyc
    │       │   │   │   ├── build.py
    │       │   │   │   ├── map.py
    │       │   │   │   ├── plan.py
    │       │   │   │   └── unbuild.py
    │       │   │   ├── avarPlanner.py
    │       │   │   ├── builder.py
    │       │   │   ├── cff.py
    │       │   │   ├── errors.py
    │       │   │   ├── featureVars.py
    │       │   │   ├── hvar.py
    │       │   │   ├── instancer
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   │   ├── featureVars.cpython-312.pyc
    │       │   │   │   │   ├── names.cpython-312.pyc
    │       │   │   │   │   └── solver.cpython-312.pyc
    │       │   │   │   ├── featureVars.py
    │       │   │   │   ├── names.py
    │       │   │   │   └── solver.py
    │       │   │   ├── interpolatable.py
    │       │   │   ├── interpolatableHelpers.py
    │       │   │   ├── interpolatablePlot.py
    │       │   │   ├── interpolatableTestContourOrder.py
    │       │   │   ├── interpolatableTestStartingPoint.py
    │       │   │   ├── interpolate_layout.py
    │       │   │   ├── iup.c
    │       │   │   ├── iup.cp312-win_amd64.pyd
    │       │   │   ├── iup.py
    │       │   │   ├── merger.py
    │       │   │   ├── models.py
    │       │   │   ├── multiVarStore.py
    │       │   │   ├── mutator.py
    │       │   │   ├── mvar.py
    │       │   │   ├── plot.py
    │       │   │   ├── stat.py
    │       │   │   └── varStore.py
    │       │   └── voltLib
    │       │       ├── __init__.py
    │       │       ├── __main__.py
    │       │       ├── __pycache__
    │       │       │   ├── __init__.cpython-312.pyc
    │       │       │   ├── __main__.cpython-312.pyc
    │       │       │   ├── ast.cpython-312.pyc
    │       │       │   ├── error.cpython-312.pyc
    │       │       │   ├── lexer.cpython-312.pyc
    │       │       │   ├── parser.cpython-312.pyc
    │       │       │   └── voltToFea.cpython-312.pyc
    │       │       ├── ast.py
    │       │       ├── error.py
    │       │       ├── lexer.py
    │       │       ├── parser.py
    │       │       └── voltToFea.py
    │       ├── fonttools-4.61.0.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   ├── licenses
    │       │   │   ├── LICENSE
    │       │   │   └── LICENSE.external
    │       │   └── top_level.txt
    │       ├── iniconfig
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── _parse.cpython-312.pyc
    │       │   │   ├── _version.cpython-312.pyc
    │       │   │   └── exceptions.cpython-312.pyc
    │       │   ├── _parse.py
    │       │   ├── _version.py
    │       │   ├── exceptions.py
    │       │   └── py.typed
    │       ├── iniconfig-2.3.0.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   ├── licenses
    │       │   │   └── LICENSE
    │       │   └── top_level.txt
    │       ├── kiwisolver
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   └── exceptions.cpython-312.pyc
    │       │   ├── _cext.cp312-win_amd64.pyd
    │       │   ├── _cext.pyi
    │       │   ├── exceptions.py
    │       │   └── py.typed
    │       ├── kiwisolver-1.4.9.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   ├── licenses
    │       │   │   └── LICENSE
    │       │   └── top_level.txt
    │       ├── matplotlib
    │       │   ├── __init__.py
    │       │   ├── __init__.pyi
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── _afm.cpython-312.pyc
    │       │   │   ├── _animation_data.cpython-312.pyc
    │       │   │   ├── _blocking_input.cpython-312.pyc
    │       │   │   ├── _cm.cpython-312.pyc
    │       │   │   ├── _cm_bivar.cpython-312.pyc
    │       │   │   ├── _cm_listed.cpython-312.pyc
    │       │   │   ├── _cm_multivar.cpython-312.pyc
    │       │   │   ├── _color_data.cpython-312.pyc
    │       │   │   ├── _constrained_layout.cpython-312.pyc
    │       │   │   ├── _docstring.cpython-312.pyc
    │       │   │   ├── _enums.cpython-312.pyc
    │       │   │   ├── _fontconfig_pattern.cpython-312.pyc
    │       │   │   ├── _internal_utils.cpython-312.pyc
    │       │   │   ├── _layoutgrid.cpython-312.pyc
    │       │   │   ├── _mathtext.cpython-312.pyc
    │       │   │   ├── _mathtext_data.cpython-312.pyc
    │       │   │   ├── _pylab_helpers.cpython-312.pyc
    │       │   │   ├── _text_helpers.cpython-312.pyc
    │       │   │   ├── _tight_bbox.cpython-312.pyc
    │       │   │   ├── _tight_layout.cpython-312.pyc
    │       │   │   ├── _type1font.cpython-312.pyc
    │       │   │   ├── _version.cpython-312.pyc
    │       │   │   ├── animation.cpython-312.pyc
    │       │   │   ├── artist.cpython-312.pyc
    │       │   │   ├── axis.cpython-312.pyc
    │       │   │   ├── backend_bases.cpython-312.pyc
    │       │   │   ├── backend_managers.cpython-312.pyc
    │       │   │   ├── backend_tools.cpython-312.pyc
    │       │   │   ├── bezier.cpython-312.pyc
    │       │   │   ├── category.cpython-312.pyc
    │       │   │   ├── cbook.cpython-312.pyc
    │       │   │   ├── cm.cpython-312.pyc
    │       │   │   ├── collections.cpython-312.pyc
    │       │   │   ├── colorbar.cpython-312.pyc
    │       │   │   ├── colorizer.cpython-312.pyc
    │       │   │   ├── colors.cpython-312.pyc
    │       │   │   ├── container.cpython-312.pyc
    │       │   │   ├── contour.cpython-312.pyc
    │       │   │   ├── dates.cpython-312.pyc
    │       │   │   ├── dviread.cpython-312.pyc
    │       │   │   ├── figure.cpython-312.pyc
    │       │   │   ├── font_manager.cpython-312.pyc
    │       │   │   ├── gridspec.cpython-312.pyc
    │       │   │   ├── hatch.cpython-312.pyc
    │       │   │   ├── image.cpython-312.pyc
    │       │   │   ├── inset.cpython-312.pyc
    │       │   │   ├── layout_engine.cpython-312.pyc
    │       │   │   ├── legend.cpython-312.pyc
    │       │   │   ├── legend_handler.cpython-312.pyc
    │       │   │   ├── lines.cpython-312.pyc
    │       │   │   ├── markers.cpython-312.pyc
    │       │   │   ├── mathtext.cpython-312.pyc
    │       │   │   ├── mlab.cpython-312.pyc
    │       │   │   ├── offsetbox.cpython-312.pyc
    │       │   │   ├── patches.cpython-312.pyc
    │       │   │   ├── path.cpython-312.pyc
    │       │   │   ├── patheffects.cpython-312.pyc
    │       │   │   ├── pylab.cpython-312.pyc
    │       │   │   ├── pyplot.cpython-312.pyc
    │       │   │   ├── quiver.cpython-312.pyc
    │       │   │   ├── rcsetup.cpython-312.pyc
    │       │   │   ├── sankey.cpython-312.pyc
    │       │   │   ├── scale.cpython-312.pyc
    │       │   │   ├── spines.cpython-312.pyc
    │       │   │   ├── stackplot.cpython-312.pyc
    │       │   │   ├── streamplot.cpython-312.pyc
    │       │   │   ├── table.cpython-312.pyc
    │       │   │   ├── texmanager.cpython-312.pyc
    │       │   │   ├── text.cpython-312.pyc
    │       │   │   ├── textpath.cpython-312.pyc
    │       │   │   ├── ticker.cpython-312.pyc
    │       │   │   ├── transforms.cpython-312.pyc
    │       │   │   ├── typing.cpython-312.pyc
    │       │   │   ├── units.cpython-312.pyc
    │       │   │   └── widgets.cpython-312.pyc
    │       │   ├── _afm.py
    │       │   ├── _animation_data.py
    │       │   ├── _api
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── deprecation.cpython-312.pyc
    │       │   │   ├── deprecation.py
    │       │   │   └── deprecation.pyi
    │       │   ├── _blocking_input.py
    │       │   ├── _c_internal_utils.cp312-win_amd64.pyd
    │       │   ├── _c_internal_utils.pyi
    │       │   ├── _cm.py
    │       │   ├── _cm_bivar.py
    │       │   ├── _cm_listed.py
    │       │   ├── _cm_multivar.py
    │       │   ├── _color_data.py
    │       │   ├── _color_data.pyi
    │       │   ├── _constrained_layout.py
    │       │   ├── _docstring.py
    │       │   ├── _docstring.pyi
    │       │   ├── _enums.py
    │       │   ├── _enums.pyi
    │       │   ├── _fontconfig_pattern.py
    │       │   ├── _image.cp312-win_amd64.pyd
    │       │   ├── _image.pyi
    │       │   ├── _internal_utils.py
    │       │   ├── _layoutgrid.py
    │       │   ├── _mathtext.py
    │       │   ├── _mathtext_data.py
    │       │   ├── _path.cp312-win_amd64.pyd
    │       │   ├── _path.pyi
    │       │   ├── _pylab_helpers.py
    │       │   ├── _pylab_helpers.pyi
    │       │   ├── _qhull.cp312-win_amd64.pyd
    │       │   ├── _qhull.pyi
    │       │   ├── _text_helpers.py
    │       │   ├── _tight_bbox.py
    │       │   ├── _tight_layout.py
    │       │   ├── _tri.cp312-win_amd64.pyd
    │       │   ├── _tri.pyi
    │       │   ├── _type1font.py
    │       │   ├── _version.py
    │       │   ├── animation.py
    │       │   ├── animation.pyi
    │       │   ├── artist.py
    │       │   ├── artist.pyi
    │       │   ├── axes
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _axes.cpython-312.pyc
    │       │   │   │   ├── _base.cpython-312.pyc
    │       │   │   │   └── _secondary_axes.cpython-312.pyc
    │       │   │   ├── _axes.py
    │       │   │   ├── _axes.pyi
    │       │   │   ├── _base.py
    │       │   │   ├── _base.pyi
    │       │   │   ├── _secondary_axes.py
    │       │   │   └── _secondary_axes.pyi
    │       │   ├── axis.py
    │       │   ├── axis.pyi
    │       │   ├── backend_bases.py
    │       │   ├── backend_bases.pyi
    │       │   ├── backend_managers.py
    │       │   ├── backend_managers.pyi
    │       │   ├── backend_tools.py
    │       │   ├── backend_tools.pyi
    │       │   ├── backends
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _backend_gtk.cpython-312.pyc
    │       │   │   │   ├── _backend_pdf_ps.cpython-312.pyc
    │       │   │   │   ├── _backend_tk.cpython-312.pyc
    │       │   │   │   ├── backend_agg.cpython-312.pyc
    │       │   │   │   ├── backend_cairo.cpython-312.pyc
    │       │   │   │   ├── backend_gtk3.cpython-312.pyc
    │       │   │   │   ├── backend_gtk3agg.cpython-312.pyc
    │       │   │   │   ├── backend_gtk3cairo.cpython-312.pyc
    │       │   │   │   ├── backend_gtk4.cpython-312.pyc
    │       │   │   │   ├── backend_gtk4agg.cpython-312.pyc
    │       │   │   │   ├── backend_gtk4cairo.cpython-312.pyc
    │       │   │   │   ├── backend_macosx.cpython-312.pyc
    │       │   │   │   ├── backend_mixed.cpython-312.pyc
    │       │   │   │   ├── backend_nbagg.cpython-312.pyc
    │       │   │   │   ├── backend_pdf.cpython-312.pyc
    │       │   │   │   ├── backend_pgf.cpython-312.pyc
    │       │   │   │   ├── backend_ps.cpython-312.pyc
    │       │   │   │   ├── backend_qt.cpython-312.pyc
    │       │   │   │   ├── backend_qt5.cpython-312.pyc
    │       │   │   │   ├── backend_qt5agg.cpython-312.pyc
    │       │   │   │   ├── backend_qt5cairo.cpython-312.pyc
    │       │   │   │   ├── backend_qtagg.cpython-312.pyc
    │       │   │   │   ├── backend_qtcairo.cpython-312.pyc
    │       │   │   │   ├── backend_svg.cpython-312.pyc
    │       │   │   │   ├── backend_template.cpython-312.pyc
    │       │   │   │   ├── backend_tkagg.cpython-312.pyc
    │       │   │   │   ├── backend_tkcairo.cpython-312.pyc
    │       │   │   │   ├── backend_webagg.cpython-312.pyc
    │       │   │   │   ├── backend_webagg_core.cpython-312.pyc
    │       │   │   │   ├── backend_wx.cpython-312.pyc
    │       │   │   │   ├── backend_wxagg.cpython-312.pyc
    │       │   │   │   ├── backend_wxcairo.cpython-312.pyc
    │       │   │   │   ├── qt_compat.cpython-312.pyc
    │       │   │   │   └── registry.cpython-312.pyc
    │       │   │   ├── _backend_agg.cp312-win_amd64.pyd
    │       │   │   ├── _backend_agg.pyi
    │       │   │   ├── _backend_gtk.py
    │       │   │   ├── _backend_pdf_ps.py
    │       │   │   ├── _backend_tk.py
    │       │   │   ├── _macosx.pyi
    │       │   │   ├── _tkagg.cp312-win_amd64.pyd
    │       │   │   ├── _tkagg.pyi
    │       │   │   ├── backend_agg.py
    │       │   │   ├── backend_cairo.py
    │       │   │   ├── backend_gtk3.py
    │       │   │   ├── backend_gtk3agg.py
    │       │   │   ├── backend_gtk3cairo.py
    │       │   │   ├── backend_gtk4.py
    │       │   │   ├── backend_gtk4agg.py
    │       │   │   ├── backend_gtk4cairo.py
    │       │   │   ├── backend_macosx.py
    │       │   │   ├── backend_mixed.py
    │       │   │   ├── backend_nbagg.py
    │       │   │   ├── backend_pdf.py
    │       │   │   ├── backend_pgf.py
    │       │   │   ├── backend_ps.py
    │       │   │   ├── backend_qt.py
    │       │   │   ├── backend_qt5.py
    │       │   │   ├── backend_qt5agg.py
    │       │   │   ├── backend_qt5cairo.py
    │       │   │   ├── backend_qtagg.py
    │       │   │   ├── backend_qtcairo.py
    │       │   │   ├── backend_svg.py
    │       │   │   ├── backend_template.py
    │       │   │   ├── backend_tkagg.py
    │       │   │   ├── backend_tkcairo.py
    │       │   │   ├── backend_webagg.py
    │       │   │   ├── backend_webagg_core.py
    │       │   │   ├── backend_wx.py
    │       │   │   ├── backend_wxagg.py
    │       │   │   ├── backend_wxcairo.py
    │       │   │   ├── qt_compat.py
    │       │   │   ├── qt_editor
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _formlayout.cpython-312.pyc
    │       │   │   │   │   └── figureoptions.cpython-312.pyc
    │       │   │   │   ├── _formlayout.py
    │       │   │   │   └── figureoptions.py
    │       │   │   ├── registry.py
    │       │   │   └── web_backend
    │       │   │       ├── all_figures.html
    │       │   │       ├── css
    │       │   │       │   ├── boilerplate.css
    │       │   │       │   ├── fbm.css
    │       │   │       │   ├── mpl.css
    │       │   │       │   └── page.css
    │       │   │       ├── ipython_inline_figure.html
    │       │   │       ├── js
    │       │   │       │   ├── mpl.js
    │       │   │       │   ├── mpl_tornado.js
    │       │   │       │   └── nbagg_mpl.js
    │       │   │       └── single_figure.html
    │       │   ├── bezier.py
    │       │   ├── bezier.pyi
    │       │   ├── category.py
    │       │   ├── cbook.py
    │       │   ├── cbook.pyi
    │       │   ├── cm.py
    │       │   ├── cm.pyi
    │       │   ├── collections.py
    │       │   ├── collections.pyi
    │       │   ├── colorbar.py
    │       │   ├── colorbar.pyi
    │       │   ├── colorizer.py
    │       │   ├── colorizer.pyi
    │       │   ├── colors.py
    │       │   ├── colors.pyi
    │       │   ├── container.py
    │       │   ├── container.pyi
    │       │   ├── contour.py
    │       │   ├── contour.pyi
    │       │   ├── dates.py
    │       │   ├── dviread.py
    │       │   ├── dviread.pyi
    │       │   ├── figure.py
    │       │   ├── figure.pyi
    │       │   ├── font_manager.py
    │       │   ├── font_manager.pyi
    │       │   ├── ft2font.cp312-win_amd64.pyd
    │       │   ├── ft2font.pyi
    │       │   ├── gridspec.py
    │       │   ├── gridspec.pyi
    │       │   ├── hatch.py
    │       │   ├── hatch.pyi
    │       │   ├── image.py
    │       │   ├── image.pyi
    │       │   ├── inset.py
    │       │   ├── inset.pyi
    │       │   ├── layout_engine.py
    │       │   ├── layout_engine.pyi
    │       │   ├── legend.py
    │       │   ├── legend.pyi
    │       │   ├── legend_handler.py
    │       │   ├── legend_handler.pyi
    │       │   ├── lines.py
    │       │   ├── lines.pyi
    │       │   ├── markers.py
    │       │   ├── markers.pyi
    │       │   ├── mathtext.py
    │       │   ├── mathtext.pyi
    │       │   ├── mlab.py
    │       │   ├── mlab.pyi
    │       │   ├── mpl-data
    │       │   │   ├── fonts
    │       │   │   │   ├── afm
    │       │   │   │   │   ├── cmex10.afm
    │       │   │   │   │   ├── cmmi10.afm
    │       │   │   │   │   ├── cmr10.afm
    │       │   │   │   │   ├── cmsy10.afm
    │       │   │   │   │   ├── cmtt10.afm
    │       │   │   │   │   ├── pagd8a.afm
    │       │   │   │   │   ├── pagdo8a.afm
    │       │   │   │   │   ├── pagk8a.afm
    │       │   │   │   │   ├── pagko8a.afm
    │       │   │   │   │   ├── pbkd8a.afm
    │       │   │   │   │   ├── pbkdi8a.afm
    │       │   │   │   │   ├── pbkl8a.afm
    │       │   │   │   │   ├── pbkli8a.afm
    │       │   │   │   │   ├── pcrb8a.afm
    │       │   │   │   │   ├── pcrbo8a.afm
    │       │   │   │   │   ├── pcrr8a.afm
    │       │   │   │   │   ├── pcrro8a.afm
    │       │   │   │   │   ├── phvb8a.afm
    │       │   │   │   │   ├── phvb8an.afm
    │       │   │   │   │   ├── phvbo8a.afm
    │       │   │   │   │   ├── phvbo8an.afm
    │       │   │   │   │   ├── phvl8a.afm
    │       │   │   │   │   ├── phvlo8a.afm
    │       │   │   │   │   ├── phvr8a.afm
    │       │   │   │   │   ├── phvr8an.afm
    │       │   │   │   │   ├── phvro8a.afm
    │       │   │   │   │   ├── phvro8an.afm
    │       │   │   │   │   ├── pncb8a.afm
    │       │   │   │   │   ├── pncbi8a.afm
    │       │   │   │   │   ├── pncr8a.afm
    │       │   │   │   │   ├── pncri8a.afm
    │       │   │   │   │   ├── pplb8a.afm
    │       │   │   │   │   ├── pplbi8a.afm
    │       │   │   │   │   ├── pplr8a.afm
    │       │   │   │   │   ├── pplri8a.afm
    │       │   │   │   │   ├── psyr.afm
    │       │   │   │   │   ├── ptmb8a.afm
    │       │   │   │   │   ├── ptmbi8a.afm
    │       │   │   │   │   ├── ptmr8a.afm
    │       │   │   │   │   ├── ptmri8a.afm
    │       │   │   │   │   ├── putb8a.afm
    │       │   │   │   │   ├── putbi8a.afm
    │       │   │   │   │   ├── putr8a.afm
    │       │   │   │   │   ├── putri8a.afm
    │       │   │   │   │   ├── pzcmi8a.afm
    │       │   │   │   │   └── pzdr.afm
    │       │   │   │   ├── pdfcorefonts
    │       │   │   │   │   ├── Courier-Bold.afm
    │       │   │   │   │   ├── Courier-BoldOblique.afm
    │       │   │   │   │   ├── Courier-Oblique.afm
    │       │   │   │   │   ├── Courier.afm
    │       │   │   │   │   ├── Helvetica-Bold.afm
    │       │   │   │   │   ├── Helvetica-BoldOblique.afm
    │       │   │   │   │   ├── Helvetica-Oblique.afm
    │       │   │   │   │   ├── Helvetica.afm
    │       │   │   │   │   ├── Symbol.afm
    │       │   │   │   │   ├── Times-Bold.afm
    │       │   │   │   │   ├── Times-BoldItalic.afm
    │       │   │   │   │   ├── Times-Italic.afm
    │       │   │   │   │   ├── Times-Roman.afm
    │       │   │   │   │   ├── ZapfDingbats.afm
    │       │   │   │   │   └── readme.txt
    │       │   │   │   └── ttf
    │       │   │   │       ├── DejaVuSans-Bold.ttf
    │       │   │   │       ├── DejaVuSans-BoldOblique.ttf
    │       │   │   │       ├── DejaVuSans-Oblique.ttf
    │       │   │   │       ├── DejaVuSans.ttf
    │       │   │   │       ├── DejaVuSansDisplay.ttf
    │       │   │   │       ├── DejaVuSansMono-Bold.ttf
    │       │   │   │       ├── DejaVuSansMono-BoldOblique.ttf
    │       │   │   │       ├── DejaVuSansMono-Oblique.ttf
    │       │   │   │       ├── DejaVuSansMono.ttf
    │       │   │   │       ├── DejaVuSerif-Bold.ttf
    │       │   │   │       ├── DejaVuSerif-BoldItalic.ttf
    │       │   │   │       ├── DejaVuSerif-Italic.ttf
    │       │   │   │       ├── DejaVuSerif.ttf
    │       │   │   │       ├── DejaVuSerifDisplay.ttf
    │       │   │   │       ├── LICENSE_DEJAVU
    │       │   │   │       ├── LICENSE_STIX
    │       │   │   │       ├── STIXGeneral.ttf
    │       │   │   │       ├── STIXGeneralBol.ttf
    │       │   │   │       ├── STIXGeneralBolIta.ttf
    │       │   │   │       ├── STIXGeneralItalic.ttf
    │       │   │   │       ├── STIXNonUni.ttf
    │       │   │   │       ├── STIXNonUniBol.ttf
    │       │   │   │       ├── STIXNonUniBolIta.ttf
    │       │   │   │       ├── STIXNonUniIta.ttf
    │       │   │   │       ├── STIXSizFiveSymReg.ttf
    │       │   │   │       ├── STIXSizFourSymBol.ttf
    │       │   │   │       ├── STIXSizFourSymReg.ttf
    │       │   │   │       ├── STIXSizOneSymBol.ttf
    │       │   │   │       ├── STIXSizOneSymReg.ttf
    │       │   │   │       ├── STIXSizThreeSymBol.ttf
    │       │   │   │       ├── STIXSizThreeSymReg.ttf
    │       │   │   │       ├── STIXSizTwoSymBol.ttf
    │       │   │   │       ├── STIXSizTwoSymReg.ttf
    │       │   │   │       ├── cmb10.ttf
    │       │   │   │       ├── cmex10.ttf
    │       │   │   │       ├── cmmi10.ttf
    │       │   │   │       ├── cmr10.ttf
    │       │   │   │       ├── cmss10.ttf
    │       │   │   │       ├── cmsy10.ttf
    │       │   │   │       └── cmtt10.ttf
    │       │   │   ├── images
    │       │   │   │   ├── back-symbolic.svg
    │       │   │   │   ├── back.pdf
    │       │   │   │   ├── back.png
    │       │   │   │   ├── back.svg
    │       │   │   │   ├── back_large.png
    │       │   │   │   ├── filesave-symbolic.svg
    │       │   │   │   ├── filesave.pdf
    │       │   │   │   ├── filesave.png
    │       │   │   │   ├── filesave.svg
    │       │   │   │   ├── filesave_large.png
    │       │   │   │   ├── forward-symbolic.svg
    │       │   │   │   ├── forward.pdf
    │       │   │   │   ├── forward.png
    │       │   │   │   ├── forward.svg
    │       │   │   │   ├── forward_large.png
    │       │   │   │   ├── hand.pdf
    │       │   │   │   ├── hand.png
    │       │   │   │   ├── hand.svg
    │       │   │   │   ├── help-symbolic.svg
    │       │   │   │   ├── help.pdf
    │       │   │   │   ├── help.png
    │       │   │   │   ├── help.svg
    │       │   │   │   ├── help_large.png
    │       │   │   │   ├── home-symbolic.svg
    │       │   │   │   ├── home.pdf
    │       │   │   │   ├── home.png
    │       │   │   │   ├── home.svg
    │       │   │   │   ├── home_large.png
    │       │   │   │   ├── matplotlib.pdf
    │       │   │   │   ├── matplotlib.png
    │       │   │   │   ├── matplotlib.svg
    │       │   │   │   ├── matplotlib_large.png
    │       │   │   │   ├── move-symbolic.svg
    │       │   │   │   ├── move.pdf
    │       │   │   │   ├── move.png
    │       │   │   │   ├── move.svg
    │       │   │   │   ├── move_large.png
    │       │   │   │   ├── qt4_editor_options.pdf
    │       │   │   │   ├── qt4_editor_options.png
    │       │   │   │   ├── qt4_editor_options.svg
    │       │   │   │   ├── qt4_editor_options_large.png
    │       │   │   │   ├── subplots-symbolic.svg
    │       │   │   │   ├── subplots.pdf
    │       │   │   │   ├── subplots.png
    │       │   │   │   ├── subplots.svg
    │       │   │   │   ├── subplots_large.png
    │       │   │   │   ├── zoom_to_rect-symbolic.svg
    │       │   │   │   ├── zoom_to_rect.pdf
    │       │   │   │   ├── zoom_to_rect.png
    │       │   │   │   ├── zoom_to_rect.svg
    │       │   │   │   └── zoom_to_rect_large.png
    │       │   │   ├── kpsewhich.lua
    │       │   │   ├── matplotlibrc
    │       │   │   ├── plot_directive
    │       │   │   │   └── plot_directive.css
    │       │   │   ├── sample_data
    │       │   │   │   ├── Minduka_Present_Blue_Pack.png
    │       │   │   │   ├── README.txt
    │       │   │   │   ├── Stocks.csv
    │       │   │   │   ├── axes_grid
    │       │   │   │   │   └── bivariate_normal.npy
    │       │   │   │   ├── data_x_x2_x3.csv
    │       │   │   │   ├── eeg.dat
    │       │   │   │   ├── embedding_in_wx3.xrc
    │       │   │   │   ├── goog.npz
    │       │   │   │   ├── grace_hopper.jpg
    │       │   │   │   ├── jacksboro_fault_dem.npz
    │       │   │   │   ├── logo2.png
    │       │   │   │   ├── membrane.dat
    │       │   │   │   ├── msft.csv
    │       │   │   │   ├── s1045.ima.gz
    │       │   │   │   └── topobathy.npz
    │       │   │   └── stylelib
    │       │   │       ├── Solarize_Light2.mplstyle
    │       │   │       ├── _classic_test_patch.mplstyle
    │       │   │       ├── _mpl-gallery-nogrid.mplstyle
    │       │   │       ├── _mpl-gallery.mplstyle
    │       │   │       ├── bmh.mplstyle
    │       │   │       ├── classic.mplstyle
    │       │   │       ├── dark_background.mplstyle
    │       │   │       ├── fast.mplstyle
    │       │   │       ├── fivethirtyeight.mplstyle
    │       │   │       ├── ggplot.mplstyle
    │       │   │       ├── grayscale.mplstyle
    │       │   │       ├── petroff10.mplstyle
    │       │   │       ├── seaborn-v0_8-bright.mplstyle
    │       │   │       ├── seaborn-v0_8-colorblind.mplstyle
    │       │   │       ├── seaborn-v0_8-dark-palette.mplstyle
    │       │   │       ├── seaborn-v0_8-dark.mplstyle
    │       │   │       ├── seaborn-v0_8-darkgrid.mplstyle
    │       │   │       ├── seaborn-v0_8-deep.mplstyle
    │       │   │       ├── seaborn-v0_8-muted.mplstyle
    │       │   │       ├── seaborn-v0_8-notebook.mplstyle
    │       │   │       ├── seaborn-v0_8-paper.mplstyle
    │       │   │       ├── seaborn-v0_8-pastel.mplstyle
    │       │   │       ├── seaborn-v0_8-poster.mplstyle
    │       │   │       ├── seaborn-v0_8-talk.mplstyle
    │       │   │       ├── seaborn-v0_8-ticks.mplstyle
    │       │   │       ├── seaborn-v0_8-white.mplstyle
    │       │   │       ├── seaborn-v0_8-whitegrid.mplstyle
    │       │   │       ├── seaborn-v0_8.mplstyle
    │       │   │       └── tableau-colorblind10.mplstyle
    │       │   ├── offsetbox.py
    │       │   ├── offsetbox.pyi
    │       │   ├── patches.py
    │       │   ├── patches.pyi
    │       │   ├── path.py
    │       │   ├── path.pyi
    │       │   ├── patheffects.py
    │       │   ├── patheffects.pyi
    │       │   ├── projections
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── geo.cpython-312.pyc
    │       │   │   │   └── polar.cpython-312.pyc
    │       │   │   ├── geo.py
    │       │   │   ├── geo.pyi
    │       │   │   ├── polar.py
    │       │   │   └── polar.pyi
    │       │   ├── py.typed
    │       │   ├── pylab.py
    │       │   ├── pyplot.py
    │       │   ├── quiver.py
    │       │   ├── quiver.pyi
    │       │   ├── rcsetup.py
    │       │   ├── rcsetup.pyi
    │       │   ├── sankey.py
    │       │   ├── sankey.pyi
    │       │   ├── scale.py
    │       │   ├── scale.pyi
    │       │   ├── sphinxext
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── figmpl_directive.cpython-312.pyc
    │       │   │   │   ├── mathmpl.cpython-312.pyc
    │       │   │   │   ├── plot_directive.cpython-312.pyc
    │       │   │   │   └── roles.cpython-312.pyc
    │       │   │   ├── figmpl_directive.py
    │       │   │   ├── mathmpl.py
    │       │   │   ├── plot_directive.py
    │       │   │   └── roles.py
    │       │   ├── spines.py
    │       │   ├── spines.pyi
    │       │   ├── stackplot.py
    │       │   ├── stackplot.pyi
    │       │   ├── streamplot.py
    │       │   ├── streamplot.pyi
    │       │   ├── style
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── core.cpython-312.pyc
    │       │   │   ├── core.py
    │       │   │   └── core.pyi
    │       │   ├── table.py
    │       │   ├── table.pyi
    │       │   ├── testing
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _markers.cpython-312.pyc
    │       │   │   │   ├── compare.cpython-312.pyc
    │       │   │   │   ├── conftest.cpython-312.pyc
    │       │   │   │   ├── decorators.cpython-312.pyc
    │       │   │   │   ├── exceptions.cpython-312.pyc
    │       │   │   │   └── widgets.cpython-312.pyc
    │       │   │   ├── _markers.py
    │       │   │   ├── compare.py
    │       │   │   ├── compare.pyi
    │       │   │   ├── conftest.py
    │       │   │   ├── conftest.pyi
    │       │   │   ├── decorators.py
    │       │   │   ├── decorators.pyi
    │       │   │   ├── exceptions.py
    │       │   │   ├── jpl_units
    │       │   │   │   ├── Duration.py
    │       │   │   │   ├── Epoch.py
    │       │   │   │   ├── EpochConverter.py
    │       │   │   │   ├── StrConverter.py
    │       │   │   │   ├── UnitDbl.py
    │       │   │   │   ├── UnitDblConverter.py
    │       │   │   │   ├── UnitDblFormatter.py
    │       │   │   │   ├── __init__.py
    │       │   │   │   └── __pycache__
    │       │   │   │       ├── Duration.cpython-312.pyc
    │       │   │   │       ├── Epoch.cpython-312.pyc
    │       │   │   │       ├── EpochConverter.cpython-312.pyc
    │       │   │   │       ├── StrConverter.cpython-312.pyc
    │       │   │   │       ├── UnitDbl.cpython-312.pyc
    │       │   │   │       ├── UnitDblConverter.cpython-312.pyc
    │       │   │   │       ├── UnitDblFormatter.cpython-312.pyc
    │       │   │   │       └── __init__.cpython-312.pyc
    │       │   │   ├── widgets.py
    │       │   │   └── widgets.pyi
    │       │   ├── tests
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── conftest.cpython-312.pyc
    │       │   │   │   ├── test_afm.cpython-312.pyc
    │       │   │   │   ├── test_agg.cpython-312.pyc
    │       │   │   │   ├── test_agg_filter.cpython-312.pyc
    │       │   │   │   ├── test_animation.cpython-312.pyc
    │       │   │   │   ├── test_api.cpython-312.pyc
    │       │   │   │   ├── test_arrow_patches.cpython-312.pyc
    │       │   │   │   ├── test_artist.cpython-312.pyc
    │       │   │   │   ├── test_axes.cpython-312.pyc
    │       │   │   │   ├── test_axis.cpython-312.pyc
    │       │   │   │   ├── test_backend_bases.cpython-312.pyc
    │       │   │   │   ├── test_backend_cairo.cpython-312.pyc
    │       │   │   │   ├── test_backend_gtk3.cpython-312.pyc
    │       │   │   │   ├── test_backend_inline.cpython-312.pyc
    │       │   │   │   ├── test_backend_macosx.cpython-312.pyc
    │       │   │   │   ├── test_backend_nbagg.cpython-312.pyc
    │       │   │   │   ├── test_backend_pdf.cpython-312.pyc
    │       │   │   │   ├── test_backend_pgf.cpython-312.pyc
    │       │   │   │   ├── test_backend_ps.cpython-312.pyc
    │       │   │   │   ├── test_backend_qt.cpython-312.pyc
    │       │   │   │   ├── test_backend_registry.cpython-312.pyc
    │       │   │   │   ├── test_backend_svg.cpython-312.pyc
    │       │   │   │   ├── test_backend_template.cpython-312.pyc
    │       │   │   │   ├── test_backend_tk.cpython-312.pyc
    │       │   │   │   ├── test_backend_tools.cpython-312.pyc
    │       │   │   │   ├── test_backend_webagg.cpython-312.pyc
    │       │   │   │   ├── test_backends_interactive.cpython-312.pyc
    │       │   │   │   ├── test_basic.cpython-312.pyc
    │       │   │   │   ├── test_bbox_tight.cpython-312.pyc
    │       │   │   │   ├── test_bezier.cpython-312.pyc
    │       │   │   │   ├── test_category.cpython-312.pyc
    │       │   │   │   ├── test_cbook.cpython-312.pyc
    │       │   │   │   ├── test_collections.cpython-312.pyc
    │       │   │   │   ├── test_colorbar.cpython-312.pyc
    │       │   │   │   ├── test_colors.cpython-312.pyc
    │       │   │   │   ├── test_compare_images.cpython-312.pyc
    │       │   │   │   ├── test_constrainedlayout.cpython-312.pyc
    │       │   │   │   ├── test_container.cpython-312.pyc
    │       │   │   │   ├── test_contour.cpython-312.pyc
    │       │   │   │   ├── test_cycles.cpython-312.pyc
    │       │   │   │   ├── test_dates.cpython-312.pyc
    │       │   │   │   ├── test_datetime.cpython-312.pyc
    │       │   │   │   ├── test_determinism.cpython-312.pyc
    │       │   │   │   ├── test_doc.cpython-312.pyc
    │       │   │   │   ├── test_dviread.cpython-312.pyc
    │       │   │   │   ├── test_figure.cpython-312.pyc
    │       │   │   │   ├── test_font_manager.cpython-312.pyc
    │       │   │   │   ├── test_fontconfig_pattern.cpython-312.pyc
    │       │   │   │   ├── test_ft2font.cpython-312.pyc
    │       │   │   │   ├── test_getattr.cpython-312.pyc
    │       │   │   │   ├── test_gridspec.cpython-312.pyc
    │       │   │   │   ├── test_image.cpython-312.pyc
    │       │   │   │   ├── test_legend.cpython-312.pyc
    │       │   │   │   ├── test_lines.cpython-312.pyc
    │       │   │   │   ├── test_marker.cpython-312.pyc
    │       │   │   │   ├── test_mathtext.cpython-312.pyc
    │       │   │   │   ├── test_matplotlib.cpython-312.pyc
    │       │   │   │   ├── test_mlab.cpython-312.pyc
    │       │   │   │   ├── test_multivariate_colormaps.cpython-312.pyc
    │       │   │   │   ├── test_offsetbox.cpython-312.pyc
    │       │   │   │   ├── test_patches.cpython-312.pyc
    │       │   │   │   ├── test_path.cpython-312.pyc
    │       │   │   │   ├── test_patheffects.cpython-312.pyc
    │       │   │   │   ├── test_pickle.cpython-312.pyc
    │       │   │   │   ├── test_png.cpython-312.pyc
    │       │   │   │   ├── test_polar.cpython-312.pyc
    │       │   │   │   ├── test_preprocess_data.cpython-312.pyc
    │       │   │   │   ├── test_pyplot.cpython-312.pyc
    │       │   │   │   ├── test_quiver.cpython-312.pyc
    │       │   │   │   ├── test_rcparams.cpython-312.pyc
    │       │   │   │   ├── test_sankey.cpython-312.pyc
    │       │   │   │   ├── test_scale.cpython-312.pyc
    │       │   │   │   ├── test_simplification.cpython-312.pyc
    │       │   │   │   ├── test_skew.cpython-312.pyc
    │       │   │   │   ├── test_sphinxext.cpython-312.pyc
    │       │   │   │   ├── test_spines.cpython-312.pyc
    │       │   │   │   ├── test_streamplot.cpython-312.pyc
    │       │   │   │   ├── test_style.cpython-312.pyc
    │       │   │   │   ├── test_subplots.cpython-312.pyc
    │       │   │   │   ├── test_table.cpython-312.pyc
    │       │   │   │   ├── test_testing.cpython-312.pyc
    │       │   │   │   ├── test_texmanager.cpython-312.pyc
    │       │   │   │   ├── test_text.cpython-312.pyc
    │       │   │   │   ├── test_textpath.cpython-312.pyc
    │       │   │   │   ├── test_ticker.cpython-312.pyc
    │       │   │   │   ├── test_tightlayout.cpython-312.pyc
    │       │   │   │   ├── test_transforms.cpython-312.pyc
    │       │   │   │   ├── test_triangulation.cpython-312.pyc
    │       │   │   │   ├── test_type1font.cpython-312.pyc
    │       │   │   │   ├── test_units.cpython-312.pyc
    │       │   │   │   ├── test_usetex.cpython-312.pyc
    │       │   │   │   └── test_widgets.cpython-312.pyc
    │       │   │   ├── conftest.py
    │       │   │   ├── test_afm.py
    │       │   │   ├── test_agg.py
    │       │   │   ├── test_agg_filter.py
    │       │   │   ├── test_animation.py
    │       │   │   ├── test_api.py
    │       │   │   ├── test_arrow_patches.py
    │       │   │   ├── test_artist.py
    │       │   │   ├── test_axes.py
    │       │   │   ├── test_axis.py
    │       │   │   ├── test_backend_bases.py
    │       │   │   ├── test_backend_cairo.py
    │       │   │   ├── test_backend_gtk3.py
    │       │   │   ├── test_backend_inline.py
    │       │   │   ├── test_backend_macosx.py
    │       │   │   ├── test_backend_nbagg.py
    │       │   │   ├── test_backend_pdf.py
    │       │   │   ├── test_backend_pgf.py
    │       │   │   ├── test_backend_ps.py
    │       │   │   ├── test_backend_qt.py
    │       │   │   ├── test_backend_registry.py
    │       │   │   ├── test_backend_svg.py
    │       │   │   ├── test_backend_template.py
    │       │   │   ├── test_backend_tk.py
    │       │   │   ├── test_backend_tools.py
    │       │   │   ├── test_backend_webagg.py
    │       │   │   ├── test_backends_interactive.py
    │       │   │   ├── test_basic.py
    │       │   │   ├── test_bbox_tight.py
    │       │   │   ├── test_bezier.py
    │       │   │   ├── test_category.py
    │       │   │   ├── test_cbook.py
    │       │   │   ├── test_collections.py
    │       │   │   ├── test_colorbar.py
    │       │   │   ├── test_colors.py
    │       │   │   ├── test_compare_images.py
    │       │   │   ├── test_constrainedlayout.py
    │       │   │   ├── test_container.py
    │       │   │   ├── test_contour.py
    │       │   │   ├── test_cycles.py
    │       │   │   ├── test_dates.py
    │       │   │   ├── test_datetime.py
    │       │   │   ├── test_determinism.py
    │       │   │   ├── test_doc.py
    │       │   │   ├── test_dviread.py
    │       │   │   ├── test_figure.py
    │       │   │   ├── test_font_manager.py
    │       │   │   ├── test_fontconfig_pattern.py
    │       │   │   ├── test_ft2font.py
    │       │   │   ├── test_getattr.py
    │       │   │   ├── test_gridspec.py
    │       │   │   ├── test_image.py
    │       │   │   ├── test_legend.py
    │       │   │   ├── test_lines.py
    │       │   │   ├── test_marker.py
    │       │   │   ├── test_mathtext.py
    │       │   │   ├── test_matplotlib.py
    │       │   │   ├── test_mlab.py
    │       │   │   ├── test_multivariate_colormaps.py
    │       │   │   ├── test_offsetbox.py
    │       │   │   ├── test_patches.py
    │       │   │   ├── test_path.py
    │       │   │   ├── test_patheffects.py
    │       │   │   ├── test_pickle.py
    │       │   │   ├── test_png.py
    │       │   │   ├── test_polar.py
    │       │   │   ├── test_preprocess_data.py
    │       │   │   ├── test_pyplot.py
    │       │   │   ├── test_quiver.py
    │       │   │   ├── test_rcparams.py
    │       │   │   ├── test_sankey.py
    │       │   │   ├── test_scale.py
    │       │   │   ├── test_simplification.py
    │       │   │   ├── test_skew.py
    │       │   │   ├── test_sphinxext.py
    │       │   │   ├── test_spines.py
    │       │   │   ├── test_streamplot.py
    │       │   │   ├── test_style.py
    │       │   │   ├── test_subplots.py
    │       │   │   ├── test_table.py
    │       │   │   ├── test_testing.py
    │       │   │   ├── test_texmanager.py
    │       │   │   ├── test_text.py
    │       │   │   ├── test_textpath.py
    │       │   │   ├── test_ticker.py
    │       │   │   ├── test_tightlayout.py
    │       │   │   ├── test_transforms.py
    │       │   │   ├── test_triangulation.py
    │       │   │   ├── test_type1font.py
    │       │   │   ├── test_units.py
    │       │   │   ├── test_usetex.py
    │       │   │   └── test_widgets.py
    │       │   ├── texmanager.py
    │       │   ├── texmanager.pyi
    │       │   ├── text.py
    │       │   ├── text.pyi
    │       │   ├── textpath.py
    │       │   ├── textpath.pyi
    │       │   ├── ticker.py
    │       │   ├── ticker.pyi
    │       │   ├── transforms.py
    │       │   ├── transforms.pyi
    │       │   ├── tri
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _triangulation.cpython-312.pyc
    │       │   │   │   ├── _tricontour.cpython-312.pyc
    │       │   │   │   ├── _trifinder.cpython-312.pyc
    │       │   │   │   ├── _triinterpolate.cpython-312.pyc
    │       │   │   │   ├── _tripcolor.cpython-312.pyc
    │       │   │   │   ├── _triplot.cpython-312.pyc
    │       │   │   │   ├── _trirefine.cpython-312.pyc
    │       │   │   │   └── _tritools.cpython-312.pyc
    │       │   │   ├── _triangulation.py
    │       │   │   ├── _triangulation.pyi
    │       │   │   ├── _tricontour.py
    │       │   │   ├── _tricontour.pyi
    │       │   │   ├── _trifinder.py
    │       │   │   ├── _trifinder.pyi
    │       │   │   ├── _triinterpolate.py
    │       │   │   ├── _triinterpolate.pyi
    │       │   │   ├── _tripcolor.py
    │       │   │   ├── _tripcolor.pyi
    │       │   │   ├── _triplot.py
    │       │   │   ├── _triplot.pyi
    │       │   │   ├── _trirefine.py
    │       │   │   ├── _trirefine.pyi
    │       │   │   ├── _tritools.py
    │       │   │   └── _tritools.pyi
    │       │   ├── typing.py
    │       │   ├── units.py
    │       │   ├── widgets.py
    │       │   └── widgets.pyi
    │       ├── matplotlib-3.10.8.dist-info
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   └── WHEEL
    │       ├── mpl_toolkits
    │       │   ├── axes_grid1
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── anchored_artists.cpython-312.pyc
    │       │   │   │   ├── axes_divider.cpython-312.pyc
    │       │   │   │   ├── axes_grid.cpython-312.pyc
    │       │   │   │   ├── axes_rgb.cpython-312.pyc
    │       │   │   │   ├── axes_size.cpython-312.pyc
    │       │   │   │   ├── inset_locator.cpython-312.pyc
    │       │   │   │   ├── mpl_axes.cpython-312.pyc
    │       │   │   │   └── parasite_axes.cpython-312.pyc
    │       │   │   ├── anchored_artists.py
    │       │   │   ├── axes_divider.py
    │       │   │   ├── axes_grid.py
    │       │   │   ├── axes_rgb.py
    │       │   │   ├── axes_size.py
    │       │   │   ├── inset_locator.py
    │       │   │   ├── mpl_axes.py
    │       │   │   ├── parasite_axes.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── conftest.cpython-312.pyc
    │       │   │       │   └── test_axes_grid1.cpython-312.pyc
    │       │   │       ├── conftest.py
    │       │   │       └── test_axes_grid1.py
    │       │   ├── axisartist
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── angle_helper.cpython-312.pyc
    │       │   │   │   ├── axes_divider.cpython-312.pyc
    │       │   │   │   ├── axis_artist.cpython-312.pyc
    │       │   │   │   ├── axisline_style.cpython-312.pyc
    │       │   │   │   ├── axislines.cpython-312.pyc
    │       │   │   │   ├── floating_axes.cpython-312.pyc
    │       │   │   │   ├── grid_finder.cpython-312.pyc
    │       │   │   │   ├── grid_helper_curvelinear.cpython-312.pyc
    │       │   │   │   └── parasite_axes.cpython-312.pyc
    │       │   │   ├── angle_helper.py
    │       │   │   ├── axes_divider.py
    │       │   │   ├── axis_artist.py
    │       │   │   ├── axisline_style.py
    │       │   │   ├── axislines.py
    │       │   │   ├── floating_axes.py
    │       │   │   ├── grid_finder.py
    │       │   │   ├── grid_helper_curvelinear.py
    │       │   │   ├── parasite_axes.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── conftest.cpython-312.pyc
    │       │   │       │   ├── test_angle_helper.cpython-312.pyc
    │       │   │       │   ├── test_axis_artist.cpython-312.pyc
    │       │   │       │   ├── test_axislines.cpython-312.pyc
    │       │   │       │   ├── test_floating_axes.cpython-312.pyc
    │       │   │       │   ├── test_grid_finder.cpython-312.pyc
    │       │   │       │   └── test_grid_helper_curvelinear.cpython-312.pyc
    │       │   │       ├── conftest.py
    │       │   │       ├── test_angle_helper.py
    │       │   │       ├── test_axis_artist.py
    │       │   │       ├── test_axislines.py
    │       │   │       ├── test_floating_axes.py
    │       │   │       ├── test_grid_finder.py
    │       │   │       └── test_grid_helper_curvelinear.py
    │       │   └── mplot3d
    │       │       ├── __init__.py
    │       │       ├── __pycache__
    │       │       │   ├── __init__.cpython-312.pyc
    │       │       │   ├── art3d.cpython-312.pyc
    │       │       │   ├── axes3d.cpython-312.pyc
    │       │       │   ├── axis3d.cpython-312.pyc
    │       │       │   └── proj3d.cpython-312.pyc
    │       │       ├── art3d.py
    │       │       ├── axes3d.py
    │       │       ├── axis3d.py
    │       │       ├── proj3d.py
    │       │       └── tests
    │       │           ├── __init__.py
    │       │           ├── __pycache__
    │       │           │   ├── __init__.cpython-312.pyc
    │       │           │   ├── conftest.cpython-312.pyc
    │       │           │   ├── test_art3d.cpython-312.pyc
    │       │           │   ├── test_axes3d.cpython-312.pyc
    │       │           │   └── test_legend3d.cpython-312.pyc
    │       │           ├── conftest.py
    │       │           ├── test_art3d.py
    │       │           ├── test_axes3d.py
    │       │           └── test_legend3d.py
    │       ├── numpy
    │       │   ├── __config__.py
    │       │   ├── __config__.pyi
    │       │   ├── __init__.cython-30.pxd
    │       │   ├── __init__.pxd
    │       │   ├── __init__.py
    │       │   ├── __init__.pyi
    │       │   ├── __pycache__
    │       │   │   ├── __config__.cpython-312.pyc
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── _array_api_info.cpython-312.pyc
    │       │   │   ├── _configtool.cpython-312.pyc
    │       │   │   ├── _distributor_init.cpython-312.pyc
    │       │   │   ├── _expired_attrs_2_0.cpython-312.pyc
    │       │   │   ├── _globals.cpython-312.pyc
    │       │   │   ├── _pytesttester.cpython-312.pyc
    │       │   │   ├── conftest.cpython-312.pyc
    │       │   │   ├── dtypes.cpython-312.pyc
    │       │   │   ├── exceptions.cpython-312.pyc
    │       │   │   ├── matlib.cpython-312.pyc
    │       │   │   └── version.cpython-312.pyc
    │       │   ├── _array_api_info.py
    │       │   ├── _array_api_info.pyi
    │       │   ├── _configtool.py
    │       │   ├── _configtool.pyi
    │       │   ├── _core
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _add_newdocs.cpython-312.pyc
    │       │   │   │   ├── _add_newdocs_scalars.cpython-312.pyc
    │       │   │   │   ├── _asarray.cpython-312.pyc
    │       │   │   │   ├── _dtype.cpython-312.pyc
    │       │   │   │   ├── _dtype_ctypes.cpython-312.pyc
    │       │   │   │   ├── _exceptions.cpython-312.pyc
    │       │   │   │   ├── _internal.cpython-312.pyc
    │       │   │   │   ├── _machar.cpython-312.pyc
    │       │   │   │   ├── _methods.cpython-312.pyc
    │       │   │   │   ├── _string_helpers.cpython-312.pyc
    │       │   │   │   ├── _type_aliases.cpython-312.pyc
    │       │   │   │   ├── _ufunc_config.cpython-312.pyc
    │       │   │   │   ├── arrayprint.cpython-312.pyc
    │       │   │   │   ├── cversions.cpython-312.pyc
    │       │   │   │   ├── defchararray.cpython-312.pyc
    │       │   │   │   ├── einsumfunc.cpython-312.pyc
    │       │   │   │   ├── fromnumeric.cpython-312.pyc
    │       │   │   │   ├── function_base.cpython-312.pyc
    │       │   │   │   ├── getlimits.cpython-312.pyc
    │       │   │   │   ├── memmap.cpython-312.pyc
    │       │   │   │   ├── multiarray.cpython-312.pyc
    │       │   │   │   ├── numeric.cpython-312.pyc
    │       │   │   │   ├── numerictypes.cpython-312.pyc
    │       │   │   │   ├── overrides.cpython-312.pyc
    │       │   │   │   ├── printoptions.cpython-312.pyc
    │       │   │   │   ├── records.cpython-312.pyc
    │       │   │   │   ├── shape_base.cpython-312.pyc
    │       │   │   │   ├── strings.cpython-312.pyc
    │       │   │   │   └── umath.cpython-312.pyc
    │       │   │   ├── _add_newdocs.py
    │       │   │   ├── _add_newdocs.pyi
    │       │   │   ├── _add_newdocs_scalars.py
    │       │   │   ├── _add_newdocs_scalars.pyi
    │       │   │   ├── _asarray.py
    │       │   │   ├── _asarray.pyi
    │       │   │   ├── _dtype.py
    │       │   │   ├── _dtype.pyi
    │       │   │   ├── _dtype_ctypes.py
    │       │   │   ├── _dtype_ctypes.pyi
    │       │   │   ├── _exceptions.py
    │       │   │   ├── _exceptions.pyi
    │       │   │   ├── _internal.py
    │       │   │   ├── _internal.pyi
    │       │   │   ├── _machar.py
    │       │   │   ├── _machar.pyi
    │       │   │   ├── _methods.py
    │       │   │   ├── _methods.pyi
    │       │   │   ├── _multiarray_tests.cp312-win_amd64.lib
    │       │   │   ├── _multiarray_tests.cp312-win_amd64.pyd
    │       │   │   ├── _multiarray_umath.cp312-win_amd64.lib
    │       │   │   ├── _multiarray_umath.cp312-win_amd64.pyd
    │       │   │   ├── _operand_flag_tests.cp312-win_amd64.lib
    │       │   │   ├── _operand_flag_tests.cp312-win_amd64.pyd
    │       │   │   ├── _rational_tests.cp312-win_amd64.lib
    │       │   │   ├── _rational_tests.cp312-win_amd64.pyd
    │       │   │   ├── _simd.cp312-win_amd64.lib
    │       │   │   ├── _simd.cp312-win_amd64.pyd
    │       │   │   ├── _simd.pyi
    │       │   │   ├── _string_helpers.py
    │       │   │   ├── _string_helpers.pyi
    │       │   │   ├── _struct_ufunc_tests.cp312-win_amd64.lib
    │       │   │   ├── _struct_ufunc_tests.cp312-win_amd64.pyd
    │       │   │   ├── _type_aliases.py
    │       │   │   ├── _type_aliases.pyi
    │       │   │   ├── _ufunc_config.py
    │       │   │   ├── _ufunc_config.pyi
    │       │   │   ├── _umath_tests.cp312-win_amd64.lib
    │       │   │   ├── _umath_tests.cp312-win_amd64.pyd
    │       │   │   ├── arrayprint.py
    │       │   │   ├── arrayprint.pyi
    │       │   │   ├── cversions.py
    │       │   │   ├── defchararray.py
    │       │   │   ├── defchararray.pyi
    │       │   │   ├── einsumfunc.py
    │       │   │   ├── einsumfunc.pyi
    │       │   │   ├── fromnumeric.py
    │       │   │   ├── fromnumeric.pyi
    │       │   │   ├── function_base.py
    │       │   │   ├── function_base.pyi
    │       │   │   ├── getlimits.py
    │       │   │   ├── getlimits.pyi
    │       │   │   ├── include
    │       │   │   │   └── numpy
    │       │   │   │       ├── __multiarray_api.c
    │       │   │   │       ├── __multiarray_api.h
    │       │   │   │       ├── __ufunc_api.c
    │       │   │   │       ├── __ufunc_api.h
    │       │   │   │       ├── _neighborhood_iterator_imp.h
    │       │   │   │       ├── _numpyconfig.h
    │       │   │   │       ├── _public_dtype_api_table.h
    │       │   │   │       ├── arrayobject.h
    │       │   │   │       ├── arrayscalars.h
    │       │   │   │       ├── dtype_api.h
    │       │   │   │       ├── halffloat.h
    │       │   │   │       ├── ndarrayobject.h
    │       │   │   │       ├── ndarraytypes.h
    │       │   │   │       ├── npy_2_compat.h
    │       │   │   │       ├── npy_2_complexcompat.h
    │       │   │   │       ├── npy_3kcompat.h
    │       │   │   │       ├── npy_common.h
    │       │   │   │       ├── npy_cpu.h
    │       │   │   │       ├── npy_endian.h
    │       │   │   │       ├── npy_math.h
    │       │   │   │       ├── npy_no_deprecated_api.h
    │       │   │   │       ├── npy_os.h
    │       │   │   │       ├── numpyconfig.h
    │       │   │   │       ├── random
    │       │   │   │       │   ├── LICENSE.txt
    │       │   │   │       │   ├── bitgen.h
    │       │   │   │       │   ├── distributions.h
    │       │   │   │       │   └── libdivide.h
    │       │   │   │       ├── ufuncobject.h
    │       │   │   │       └── utils.h
    │       │   │   ├── lib
    │       │   │   │   ├── npy-pkg-config
    │       │   │   │   │   ├── mlib.ini
    │       │   │   │   │   └── npymath.ini
    │       │   │   │   ├── npymath.lib
    │       │   │   │   └── pkgconfig
    │       │   │   │       └── numpy.pc
    │       │   │   ├── memmap.py
    │       │   │   ├── memmap.pyi
    │       │   │   ├── multiarray.py
    │       │   │   ├── multiarray.pyi
    │       │   │   ├── numeric.py
    │       │   │   ├── numeric.pyi
    │       │   │   ├── numerictypes.py
    │       │   │   ├── numerictypes.pyi
    │       │   │   ├── overrides.py
    │       │   │   ├── overrides.pyi
    │       │   │   ├── printoptions.py
    │       │   │   ├── printoptions.pyi
    │       │   │   ├── records.py
    │       │   │   ├── records.pyi
    │       │   │   ├── shape_base.py
    │       │   │   ├── shape_base.pyi
    │       │   │   ├── strings.py
    │       │   │   ├── strings.pyi
    │       │   │   ├── tests
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── _locales.cpython-312.pyc
    │       │   │   │   │   ├── _natype.cpython-312.pyc
    │       │   │   │   │   ├── test__exceptions.cpython-312.pyc
    │       │   │   │   │   ├── test_abc.cpython-312.pyc
    │       │   │   │   │   ├── test_api.cpython-312.pyc
    │       │   │   │   │   ├── test_argparse.cpython-312.pyc
    │       │   │   │   │   ├── test_array_api_info.cpython-312.pyc
    │       │   │   │   │   ├── test_array_coercion.cpython-312.pyc
    │       │   │   │   │   ├── test_array_interface.cpython-312.pyc
    │       │   │   │   │   ├── test_arraymethod.cpython-312.pyc
    │       │   │   │   │   ├── test_arrayobject.cpython-312.pyc
    │       │   │   │   │   ├── test_arrayprint.cpython-312.pyc
    │       │   │   │   │   ├── test_casting_floatingpoint_errors.cpython-312.pyc
    │       │   │   │   │   ├── test_casting_unittests.cpython-312.pyc
    │       │   │   │   │   ├── test_conversion_utils.cpython-312.pyc
    │       │   │   │   │   ├── test_cpu_dispatcher.cpython-312.pyc
    │       │   │   │   │   ├── test_cpu_features.cpython-312.pyc
    │       │   │   │   │   ├── test_custom_dtypes.cpython-312.pyc
    │       │   │   │   │   ├── test_cython.cpython-312.pyc
    │       │   │   │   │   ├── test_datetime.cpython-312.pyc
    │       │   │   │   │   ├── test_defchararray.cpython-312.pyc
    │       │   │   │   │   ├── test_deprecations.cpython-312.pyc
    │       │   │   │   │   ├── test_dlpack.cpython-312.pyc
    │       │   │   │   │   ├── test_dtype.cpython-312.pyc
    │       │   │   │   │   ├── test_einsum.cpython-312.pyc
    │       │   │   │   │   ├── test_errstate.cpython-312.pyc
    │       │   │   │   │   ├── test_extint128.cpython-312.pyc
    │       │   │   │   │   ├── test_function_base.cpython-312.pyc
    │       │   │   │   │   ├── test_getlimits.cpython-312.pyc
    │       │   │   │   │   ├── test_half.cpython-312.pyc
    │       │   │   │   │   ├── test_hashtable.cpython-312.pyc
    │       │   │   │   │   ├── test_indexerrors.cpython-312.pyc
    │       │   │   │   │   ├── test_indexing.cpython-312.pyc
    │       │   │   │   │   ├── test_item_selection.cpython-312.pyc
    │       │   │   │   │   ├── test_limited_api.cpython-312.pyc
    │       │   │   │   │   ├── test_longdouble.cpython-312.pyc
    │       │   │   │   │   ├── test_machar.cpython-312.pyc
    │       │   │   │   │   ├── test_mem_overlap.cpython-312.pyc
    │       │   │   │   │   ├── test_mem_policy.cpython-312.pyc
    │       │   │   │   │   ├── test_memmap.cpython-312.pyc
    │       │   │   │   │   ├── test_multiarray.cpython-312.pyc
    │       │   │   │   │   ├── test_multithreading.cpython-312.pyc
    │       │   │   │   │   ├── test_nditer.cpython-312.pyc
    │       │   │   │   │   ├── test_nep50_promotions.cpython-312.pyc
    │       │   │   │   │   ├── test_numeric.cpython-312.pyc
    │       │   │   │   │   ├── test_numerictypes.cpython-312.pyc
    │       │   │   │   │   ├── test_overrides.cpython-312.pyc
    │       │   │   │   │   ├── test_print.cpython-312.pyc
    │       │   │   │   │   ├── test_protocols.cpython-312.pyc
    │       │   │   │   │   ├── test_records.cpython-312.pyc
    │       │   │   │   │   ├── test_regression.cpython-312.pyc
    │       │   │   │   │   ├── test_scalar_ctors.cpython-312.pyc
    │       │   │   │   │   ├── test_scalar_methods.cpython-312.pyc
    │       │   │   │   │   ├── test_scalarbuffer.cpython-312.pyc
    │       │   │   │   │   ├── test_scalarinherit.cpython-312.pyc
    │       │   │   │   │   ├── test_scalarmath.cpython-312.pyc
    │       │   │   │   │   ├── test_scalarprint.cpython-312.pyc
    │       │   │   │   │   ├── test_shape_base.cpython-312.pyc
    │       │   │   │   │   ├── test_simd.cpython-312.pyc
    │       │   │   │   │   ├── test_simd_module.cpython-312.pyc
    │       │   │   │   │   ├── test_stringdtype.cpython-312.pyc
    │       │   │   │   │   ├── test_strings.cpython-312.pyc
    │       │   │   │   │   ├── test_ufunc.cpython-312.pyc
    │       │   │   │   │   ├── test_umath.cpython-312.pyc
    │       │   │   │   │   ├── test_umath_accuracy.cpython-312.pyc
    │       │   │   │   │   ├── test_umath_complex.cpython-312.pyc
    │       │   │   │   │   └── test_unicode.cpython-312.pyc
    │       │   │   │   ├── _locales.py
    │       │   │   │   ├── _natype.py
    │       │   │   │   ├── data
    │       │   │   │   │   ├── astype_copy.pkl
    │       │   │   │   │   ├── generate_umath_validation_data.cpp
    │       │   │   │   │   ├── recarray_from_file.fits
    │       │   │   │   │   ├── umath-validation-set-README.txt
    │       │   │   │   │   ├── umath-validation-set-arccos.csv
    │       │   │   │   │   ├── umath-validation-set-arccosh.csv
    │       │   │   │   │   ├── umath-validation-set-arcsin.csv
    │       │   │   │   │   ├── umath-validation-set-arcsinh.csv
    │       │   │   │   │   ├── umath-validation-set-arctan.csv
    │       │   │   │   │   ├── umath-validation-set-arctanh.csv
    │       │   │   │   │   ├── umath-validation-set-cbrt.csv
    │       │   │   │   │   ├── umath-validation-set-cos.csv
    │       │   │   │   │   ├── umath-validation-set-cosh.csv
    │       │   │   │   │   ├── umath-validation-set-exp.csv
    │       │   │   │   │   ├── umath-validation-set-exp2.csv
    │       │   │   │   │   ├── umath-validation-set-expm1.csv
    │       │   │   │   │   ├── umath-validation-set-log.csv
    │       │   │   │   │   ├── umath-validation-set-log10.csv
    │       │   │   │   │   ├── umath-validation-set-log1p.csv
    │       │   │   │   │   ├── umath-validation-set-log2.csv
    │       │   │   │   │   ├── umath-validation-set-sin.csv
    │       │   │   │   │   ├── umath-validation-set-sinh.csv
    │       │   │   │   │   ├── umath-validation-set-tan.csv
    │       │   │   │   │   └── umath-validation-set-tanh.csv
    │       │   │   │   ├── examples
    │       │   │   │   │   ├── cython
    │       │   │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   │   └── setup.cpython-312.pyc
    │       │   │   │   │   │   ├── checks.pyx
    │       │   │   │   │   │   ├── meson.build
    │       │   │   │   │   │   └── setup.py
    │       │   │   │   │   └── limited_api
    │       │   │   │   │       ├── __pycache__
    │       │   │   │   │       │   └── setup.cpython-312.pyc
    │       │   │   │   │       ├── limited_api1.c
    │       │   │   │   │       ├── limited_api2.pyx
    │       │   │   │   │       ├── limited_api_latest.c
    │       │   │   │   │       ├── meson.build
    │       │   │   │   │       └── setup.py
    │       │   │   │   ├── test__exceptions.py
    │       │   │   │   ├── test_abc.py
    │       │   │   │   ├── test_api.py
    │       │   │   │   ├── test_argparse.py
    │       │   │   │   ├── test_array_api_info.py
    │       │   │   │   ├── test_array_coercion.py
    │       │   │   │   ├── test_array_interface.py
    │       │   │   │   ├── test_arraymethod.py
    │       │   │   │   ├── test_arrayobject.py
    │       │   │   │   ├── test_arrayprint.py
    │       │   │   │   ├── test_casting_floatingpoint_errors.py
    │       │   │   │   ├── test_casting_unittests.py
    │       │   │   │   ├── test_conversion_utils.py
    │       │   │   │   ├── test_cpu_dispatcher.py
    │       │   │   │   ├── test_cpu_features.py
    │       │   │   │   ├── test_custom_dtypes.py
    │       │   │   │   ├── test_cython.py
    │       │   │   │   ├── test_datetime.py
    │       │   │   │   ├── test_defchararray.py
    │       │   │   │   ├── test_deprecations.py
    │       │   │   │   ├── test_dlpack.py
    │       │   │   │   ├── test_dtype.py
    │       │   │   │   ├── test_einsum.py
    │       │   │   │   ├── test_errstate.py
    │       │   │   │   ├── test_extint128.py
    │       │   │   │   ├── test_function_base.py
    │       │   │   │   ├── test_getlimits.py
    │       │   │   │   ├── test_half.py
    │       │   │   │   ├── test_hashtable.py
    │       │   │   │   ├── test_indexerrors.py
    │       │   │   │   ├── test_indexing.py
    │       │   │   │   ├── test_item_selection.py
    │       │   │   │   ├── test_limited_api.py
    │       │   │   │   ├── test_longdouble.py
    │       │   │   │   ├── test_machar.py
    │       │   │   │   ├── test_mem_overlap.py
    │       │   │   │   ├── test_mem_policy.py
    │       │   │   │   ├── test_memmap.py
    │       │   │   │   ├── test_multiarray.py
    │       │   │   │   ├── test_multithreading.py
    │       │   │   │   ├── test_nditer.py
    │       │   │   │   ├── test_nep50_promotions.py
    │       │   │   │   ├── test_numeric.py
    │       │   │   │   ├── test_numerictypes.py
    │       │   │   │   ├── test_overrides.py
    │       │   │   │   ├── test_print.py
    │       │   │   │   ├── test_protocols.py
    │       │   │   │   ├── test_records.py
    │       │   │   │   ├── test_regression.py
    │       │   │   │   ├── test_scalar_ctors.py
    │       │   │   │   ├── test_scalar_methods.py
    │       │   │   │   ├── test_scalarbuffer.py
    │       │   │   │   ├── test_scalarinherit.py
    │       │   │   │   ├── test_scalarmath.py
    │       │   │   │   ├── test_scalarprint.py
    │       │   │   │   ├── test_shape_base.py
    │       │   │   │   ├── test_simd.py
    │       │   │   │   ├── test_simd_module.py
    │       │   │   │   ├── test_stringdtype.py
    │       │   │   │   ├── test_strings.py
    │       │   │   │   ├── test_ufunc.py
    │       │   │   │   ├── test_umath.py
    │       │   │   │   ├── test_umath_accuracy.py
    │       │   │   │   ├── test_umath_complex.py
    │       │   │   │   └── test_unicode.py
    │       │   │   ├── umath.py
    │       │   │   └── umath.pyi
    │       │   ├── _distributor_init.py
    │       │   ├── _distributor_init.pyi
    │       │   ├── _expired_attrs_2_0.py
    │       │   ├── _expired_attrs_2_0.pyi
    │       │   ├── _globals.py
    │       │   ├── _globals.pyi
    │       │   ├── _pyinstaller
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── hook-numpy.cpython-312.pyc
    │       │   │   ├── hook-numpy.py
    │       │   │   ├── hook-numpy.pyi
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── pyinstaller-smoke.cpython-312.pyc
    │       │   │       │   └── test_pyinstaller.cpython-312.pyc
    │       │   │       ├── pyinstaller-smoke.py
    │       │   │       └── test_pyinstaller.py
    │       │   ├── _pytesttester.py
    │       │   ├── _pytesttester.pyi
    │       │   ├── _typing
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _add_docstring.cpython-312.pyc
    │       │   │   │   ├── _array_like.cpython-312.pyc
    │       │   │   │   ├── _char_codes.cpython-312.pyc
    │       │   │   │   ├── _dtype_like.cpython-312.pyc
    │       │   │   │   ├── _extended_precision.cpython-312.pyc
    │       │   │   │   ├── _nbit.cpython-312.pyc
    │       │   │   │   ├── _nbit_base.cpython-312.pyc
    │       │   │   │   ├── _nested_sequence.cpython-312.pyc
    │       │   │   │   ├── _scalars.cpython-312.pyc
    │       │   │   │   ├── _shape.cpython-312.pyc
    │       │   │   │   └── _ufunc.cpython-312.pyc
    │       │   │   ├── _add_docstring.py
    │       │   │   ├── _array_like.py
    │       │   │   ├── _char_codes.py
    │       │   │   ├── _dtype_like.py
    │       │   │   ├── _extended_precision.py
    │       │   │   ├── _nbit.py
    │       │   │   ├── _nbit_base.py
    │       │   │   ├── _nbit_base.pyi
    │       │   │   ├── _nested_sequence.py
    │       │   │   ├── _scalars.py
    │       │   │   ├── _shape.py
    │       │   │   ├── _ufunc.py
    │       │   │   └── _ufunc.pyi
    │       │   ├── _utils
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _convertions.cpython-312.pyc
    │       │   │   │   ├── _inspect.cpython-312.pyc
    │       │   │   │   └── _pep440.cpython-312.pyc
    │       │   │   ├── _convertions.py
    │       │   │   ├── _convertions.pyi
    │       │   │   ├── _inspect.py
    │       │   │   ├── _inspect.pyi
    │       │   │   ├── _pep440.py
    │       │   │   └── _pep440.pyi
    │       │   ├── char
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   └── __pycache__
    │       │   │       └── __init__.cpython-312.pyc
    │       │   ├── conftest.py
    │       │   ├── core
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _dtype.cpython-312.pyc
    │       │   │   │   ├── _dtype_ctypes.cpython-312.pyc
    │       │   │   │   ├── _internal.cpython-312.pyc
    │       │   │   │   ├── _multiarray_umath.cpython-312.pyc
    │       │   │   │   ├── _utils.cpython-312.pyc
    │       │   │   │   ├── arrayprint.cpython-312.pyc
    │       │   │   │   ├── defchararray.cpython-312.pyc
    │       │   │   │   ├── einsumfunc.cpython-312.pyc
    │       │   │   │   ├── fromnumeric.cpython-312.pyc
    │       │   │   │   ├── function_base.cpython-312.pyc
    │       │   │   │   ├── getlimits.cpython-312.pyc
    │       │   │   │   ├── multiarray.cpython-312.pyc
    │       │   │   │   ├── numeric.cpython-312.pyc
    │       │   │   │   ├── numerictypes.cpython-312.pyc
    │       │   │   │   ├── overrides.cpython-312.pyc
    │       │   │   │   ├── records.cpython-312.pyc
    │       │   │   │   ├── shape_base.cpython-312.pyc
    │       │   │   │   └── umath.cpython-312.pyc
    │       │   │   ├── _dtype.py
    │       │   │   ├── _dtype.pyi
    │       │   │   ├── _dtype_ctypes.py
    │       │   │   ├── _dtype_ctypes.pyi
    │       │   │   ├── _internal.py
    │       │   │   ├── _multiarray_umath.py
    │       │   │   ├── _utils.py
    │       │   │   ├── arrayprint.py
    │       │   │   ├── defchararray.py
    │       │   │   ├── einsumfunc.py
    │       │   │   ├── fromnumeric.py
    │       │   │   ├── function_base.py
    │       │   │   ├── getlimits.py
    │       │   │   ├── multiarray.py
    │       │   │   ├── numeric.py
    │       │   │   ├── numerictypes.py
    │       │   │   ├── overrides.py
    │       │   │   ├── overrides.pyi
    │       │   │   ├── records.py
    │       │   │   ├── shape_base.py
    │       │   │   └── umath.py
    │       │   ├── ctypeslib
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── _ctypeslib.cpython-312.pyc
    │       │   │   ├── _ctypeslib.py
    │       │   │   └── _ctypeslib.pyi
    │       │   ├── doc
    │       │   │   ├── __pycache__
    │       │   │   │   └── ufuncs.cpython-312.pyc
    │       │   │   └── ufuncs.py
    │       │   ├── dtypes.py
    │       │   ├── dtypes.pyi
    │       │   ├── exceptions.py
    │       │   ├── exceptions.pyi
    │       │   ├── f2py
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __main__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   ├── __version__.cpython-312.pyc
    │       │   │   │   ├── _isocbind.cpython-312.pyc
    │       │   │   │   ├── _src_pyf.cpython-312.pyc
    │       │   │   │   ├── auxfuncs.cpython-312.pyc
    │       │   │   │   ├── capi_maps.cpython-312.pyc
    │       │   │   │   ├── cb_rules.cpython-312.pyc
    │       │   │   │   ├── cfuncs.cpython-312.pyc
    │       │   │   │   ├── common_rules.cpython-312.pyc
    │       │   │   │   ├── crackfortran.cpython-312.pyc
    │       │   │   │   ├── diagnose.cpython-312.pyc
    │       │   │   │   ├── f2py2e.cpython-312.pyc
    │       │   │   │   ├── f90mod_rules.cpython-312.pyc
    │       │   │   │   ├── func2subr.cpython-312.pyc
    │       │   │   │   ├── rules.cpython-312.pyc
    │       │   │   │   ├── symbolic.cpython-312.pyc
    │       │   │   │   └── use_rules.cpython-312.pyc
    │       │   │   ├── __version__.py
    │       │   │   ├── __version__.pyi
    │       │   │   ├── _backends
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __init__.pyi
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _backend.cpython-312.pyc
    │       │   │   │   │   ├── _distutils.cpython-312.pyc
    │       │   │   │   │   └── _meson.cpython-312.pyc
    │       │   │   │   ├── _backend.py
    │       │   │   │   ├── _backend.pyi
    │       │   │   │   ├── _distutils.py
    │       │   │   │   ├── _distutils.pyi
    │       │   │   │   ├── _meson.py
    │       │   │   │   ├── _meson.pyi
    │       │   │   │   └── meson.build.template
    │       │   │   ├── _isocbind.py
    │       │   │   ├── _isocbind.pyi
    │       │   │   ├── _src_pyf.py
    │       │   │   ├── _src_pyf.pyi
    │       │   │   ├── auxfuncs.py
    │       │   │   ├── auxfuncs.pyi
    │       │   │   ├── capi_maps.py
    │       │   │   ├── capi_maps.pyi
    │       │   │   ├── cb_rules.py
    │       │   │   ├── cb_rules.pyi
    │       │   │   ├── cfuncs.py
    │       │   │   ├── cfuncs.pyi
    │       │   │   ├── common_rules.py
    │       │   │   ├── common_rules.pyi
    │       │   │   ├── crackfortran.py
    │       │   │   ├── crackfortran.pyi
    │       │   │   ├── diagnose.py
    │       │   │   ├── diagnose.pyi
    │       │   │   ├── f2py2e.py
    │       │   │   ├── f2py2e.pyi
    │       │   │   ├── f90mod_rules.py
    │       │   │   ├── f90mod_rules.pyi
    │       │   │   ├── func2subr.py
    │       │   │   ├── func2subr.pyi
    │       │   │   ├── rules.py
    │       │   │   ├── rules.pyi
    │       │   │   ├── setup.cfg
    │       │   │   ├── src
    │       │   │   │   ├── fortranobject.c
    │       │   │   │   └── fortranobject.h
    │       │   │   ├── symbolic.py
    │       │   │   ├── symbolic.pyi
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── test_abstract_interface.cpython-312.pyc
    │       │   │   │   │   ├── test_array_from_pyobj.cpython-312.pyc
    │       │   │   │   │   ├── test_assumed_shape.cpython-312.pyc
    │       │   │   │   │   ├── test_block_docstring.cpython-312.pyc
    │       │   │   │   │   ├── test_callback.cpython-312.pyc
    │       │   │   │   │   ├── test_character.cpython-312.pyc
    │       │   │   │   │   ├── test_common.cpython-312.pyc
    │       │   │   │   │   ├── test_crackfortran.cpython-312.pyc
    │       │   │   │   │   ├── test_data.cpython-312.pyc
    │       │   │   │   │   ├── test_docs.cpython-312.pyc
    │       │   │   │   │   ├── test_f2cmap.cpython-312.pyc
    │       │   │   │   │   ├── test_f2py2e.cpython-312.pyc
    │       │   │   │   │   ├── test_isoc.cpython-312.pyc
    │       │   │   │   │   ├── test_kind.cpython-312.pyc
    │       │   │   │   │   ├── test_mixed.cpython-312.pyc
    │       │   │   │   │   ├── test_modules.cpython-312.pyc
    │       │   │   │   │   ├── test_parameter.cpython-312.pyc
    │       │   │   │   │   ├── test_pyf_src.cpython-312.pyc
    │       │   │   │   │   ├── test_quoted_character.cpython-312.pyc
    │       │   │   │   │   ├── test_regression.cpython-312.pyc
    │       │   │   │   │   ├── test_return_character.cpython-312.pyc
    │       │   │   │   │   ├── test_return_complex.cpython-312.pyc
    │       │   │   │   │   ├── test_return_integer.cpython-312.pyc
    │       │   │   │   │   ├── test_return_logical.cpython-312.pyc
    │       │   │   │   │   ├── test_return_real.cpython-312.pyc
    │       │   │   │   │   ├── test_routines.cpython-312.pyc
    │       │   │   │   │   ├── test_semicolon_split.cpython-312.pyc
    │       │   │   │   │   ├── test_size.cpython-312.pyc
    │       │   │   │   │   ├── test_string.cpython-312.pyc
    │       │   │   │   │   ├── test_symbolic.cpython-312.pyc
    │       │   │   │   │   ├── test_value_attrspec.cpython-312.pyc
    │       │   │   │   │   └── util.cpython-312.pyc
    │       │   │   │   ├── src
    │       │   │   │   │   ├── abstract_interface
    │       │   │   │   │   │   ├── foo.f90
    │       │   │   │   │   │   └── gh18403_mod.f90
    │       │   │   │   │   ├── array_from_pyobj
    │       │   │   │   │   │   └── wrapmodule.c
    │       │   │   │   │   ├── assumed_shape
    │       │   │   │   │   │   ├── .f2py_f2cmap
    │       │   │   │   │   │   ├── foo_free.f90
    │       │   │   │   │   │   ├── foo_mod.f90
    │       │   │   │   │   │   ├── foo_use.f90
    │       │   │   │   │   │   └── precision.f90
    │       │   │   │   │   ├── block_docstring
    │       │   │   │   │   │   └── foo.f
    │       │   │   │   │   ├── callback
    │       │   │   │   │   │   ├── foo.f
    │       │   │   │   │   │   ├── gh17797.f90
    │       │   │   │   │   │   ├── gh18335.f90
    │       │   │   │   │   │   ├── gh25211.f
    │       │   │   │   │   │   ├── gh25211.pyf
    │       │   │   │   │   │   └── gh26681.f90
    │       │   │   │   │   ├── cli
    │       │   │   │   │   │   ├── gh_22819.pyf
    │       │   │   │   │   │   ├── hi77.f
    │       │   │   │   │   │   └── hiworld.f90
    │       │   │   │   │   ├── common
    │       │   │   │   │   │   ├── block.f
    │       │   │   │   │   │   └── gh19161.f90
    │       │   │   │   │   ├── crackfortran
    │       │   │   │   │   │   ├── accesstype.f90
    │       │   │   │   │   │   ├── common_with_division.f
    │       │   │   │   │   │   ├── data_common.f
    │       │   │   │   │   │   ├── data_multiplier.f
    │       │   │   │   │   │   ├── data_stmts.f90
    │       │   │   │   │   │   ├── data_with_comments.f
    │       │   │   │   │   │   ├── foo_deps.f90
    │       │   │   │   │   │   ├── gh15035.f
    │       │   │   │   │   │   ├── gh17859.f
    │       │   │   │   │   │   ├── gh22648.pyf
    │       │   │   │   │   │   ├── gh23533.f
    │       │   │   │   │   │   ├── gh23598.f90
    │       │   │   │   │   │   ├── gh23598Warn.f90
    │       │   │   │   │   │   ├── gh23879.f90
    │       │   │   │   │   │   ├── gh27697.f90
    │       │   │   │   │   │   ├── gh2848.f90
    │       │   │   │   │   │   ├── operators.f90
    │       │   │   │   │   │   ├── privatemod.f90
    │       │   │   │   │   │   ├── publicmod.f90
    │       │   │   │   │   │   ├── pubprivmod.f90
    │       │   │   │   │   │   └── unicode_comment.f90
    │       │   │   │   │   ├── f2cmap
    │       │   │   │   │   │   ├── .f2py_f2cmap
    │       │   │   │   │   │   └── isoFortranEnvMap.f90
    │       │   │   │   │   ├── isocintrin
    │       │   │   │   │   │   └── isoCtests.f90
    │       │   │   │   │   ├── kind
    │       │   │   │   │   │   └── foo.f90
    │       │   │   │   │   ├── mixed
    │       │   │   │   │   │   ├── foo.f
    │       │   │   │   │   │   ├── foo_fixed.f90
    │       │   │   │   │   │   └── foo_free.f90
    │       │   │   │   │   ├── modules
    │       │   │   │   │   │   ├── gh25337
    │       │   │   │   │   │   │   ├── data.f90
    │       │   │   │   │   │   │   └── use_data.f90
    │       │   │   │   │   │   ├── gh26920
    │       │   │   │   │   │   │   ├── two_mods_with_no_public_entities.f90
    │       │   │   │   │   │   │   └── two_mods_with_one_public_routine.f90
    │       │   │   │   │   │   ├── module_data_docstring.f90
    │       │   │   │   │   │   └── use_modules.f90
    │       │   │   │   │   ├── negative_bounds
    │       │   │   │   │   │   └── issue_20853.f90
    │       │   │   │   │   ├── parameter
    │       │   │   │   │   │   ├── constant_array.f90
    │       │   │   │   │   │   ├── constant_both.f90
    │       │   │   │   │   │   ├── constant_compound.f90
    │       │   │   │   │   │   ├── constant_integer.f90
    │       │   │   │   │   │   ├── constant_non_compound.f90
    │       │   │   │   │   │   └── constant_real.f90
    │       │   │   │   │   ├── quoted_character
    │       │   │   │   │   │   └── foo.f
    │       │   │   │   │   ├── regression
    │       │   │   │   │   │   ├── AB.inc
    │       │   │   │   │   │   ├── assignOnlyModule.f90
    │       │   │   │   │   │   ├── datonly.f90
    │       │   │   │   │   │   ├── f77comments.f
    │       │   │   │   │   │   ├── f77fixedform.f95
    │       │   │   │   │   │   ├── f90continuation.f90
    │       │   │   │   │   │   ├── incfile.f90
    │       │   │   │   │   │   ├── inout.f90
    │       │   │   │   │   │   ├── lower_f2py_fortran.f90
    │       │   │   │   │   │   └── mod_derived_types.f90
    │       │   │   │   │   ├── return_character
    │       │   │   │   │   │   ├── foo77.f
    │       │   │   │   │   │   └── foo90.f90
    │       │   │   │   │   ├── return_complex
    │       │   │   │   │   │   ├── foo77.f
    │       │   │   │   │   │   └── foo90.f90
    │       │   │   │   │   ├── return_integer
    │       │   │   │   │   │   ├── foo77.f
    │       │   │   │   │   │   └── foo90.f90
    │       │   │   │   │   ├── return_logical
    │       │   │   │   │   │   ├── foo77.f
    │       │   │   │   │   │   └── foo90.f90
    │       │   │   │   │   ├── return_real
    │       │   │   │   │   │   ├── foo77.f
    │       │   │   │   │   │   └── foo90.f90
    │       │   │   │   │   ├── routines
    │       │   │   │   │   │   ├── funcfortranname.f
    │       │   │   │   │   │   ├── funcfortranname.pyf
    │       │   │   │   │   │   ├── subrout.f
    │       │   │   │   │   │   └── subrout.pyf
    │       │   │   │   │   ├── size
    │       │   │   │   │   │   └── foo.f90
    │       │   │   │   │   ├── string
    │       │   │   │   │   │   ├── char.f90
    │       │   │   │   │   │   ├── fixed_string.f90
    │       │   │   │   │   │   ├── gh24008.f
    │       │   │   │   │   │   ├── gh24662.f90
    │       │   │   │   │   │   ├── gh25286.f90
    │       │   │   │   │   │   ├── gh25286.pyf
    │       │   │   │   │   │   ├── gh25286_bc.pyf
    │       │   │   │   │   │   ├── scalar_string.f90
    │       │   │   │   │   │   └── string.f
    │       │   │   │   │   └── value_attrspec
    │       │   │   │   │       └── gh21665.f90
    │       │   │   │   ├── test_abstract_interface.py
    │       │   │   │   ├── test_array_from_pyobj.py
    │       │   │   │   ├── test_assumed_shape.py
    │       │   │   │   ├── test_block_docstring.py
    │       │   │   │   ├── test_callback.py
    │       │   │   │   ├── test_character.py
    │       │   │   │   ├── test_common.py
    │       │   │   │   ├── test_crackfortran.py
    │       │   │   │   ├── test_data.py
    │       │   │   │   ├── test_docs.py
    │       │   │   │   ├── test_f2cmap.py
    │       │   │   │   ├── test_f2py2e.py
    │       │   │   │   ├── test_isoc.py
    │       │   │   │   ├── test_kind.py
    │       │   │   │   ├── test_mixed.py
    │       │   │   │   ├── test_modules.py
    │       │   │   │   ├── test_parameter.py
    │       │   │   │   ├── test_pyf_src.py
    │       │   │   │   ├── test_quoted_character.py
    │       │   │   │   ├── test_regression.py
    │       │   │   │   ├── test_return_character.py
    │       │   │   │   ├── test_return_complex.py
    │       │   │   │   ├── test_return_integer.py
    │       │   │   │   ├── test_return_logical.py
    │       │   │   │   ├── test_return_real.py
    │       │   │   │   ├── test_routines.py
    │       │   │   │   ├── test_semicolon_split.py
    │       │   │   │   ├── test_size.py
    │       │   │   │   ├── test_string.py
    │       │   │   │   ├── test_symbolic.py
    │       │   │   │   ├── test_value_attrspec.py
    │       │   │   │   └── util.py
    │       │   │   ├── use_rules.py
    │       │   │   └── use_rules.pyi
    │       │   ├── fft
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _helper.cpython-312.pyc
    │       │   │   │   ├── _pocketfft.cpython-312.pyc
    │       │   │   │   └── helper.cpython-312.pyc
    │       │   │   ├── _helper.py
    │       │   │   ├── _helper.pyi
    │       │   │   ├── _pocketfft.py
    │       │   │   ├── _pocketfft.pyi
    │       │   │   ├── _pocketfft_umath.cp312-win_amd64.lib
    │       │   │   ├── _pocketfft_umath.cp312-win_amd64.pyd
    │       │   │   ├── helper.py
    │       │   │   ├── helper.pyi
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_helper.cpython-312.pyc
    │       │   │       │   └── test_pocketfft.cpython-312.pyc
    │       │   │       ├── test_helper.py
    │       │   │       └── test_pocketfft.py
    │       │   ├── lib
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _array_utils_impl.cpython-312.pyc
    │       │   │   │   ├── _arraypad_impl.cpython-312.pyc
    │       │   │   │   ├── _arraysetops_impl.cpython-312.pyc
    │       │   │   │   ├── _arrayterator_impl.cpython-312.pyc
    │       │   │   │   ├── _datasource.cpython-312.pyc
    │       │   │   │   ├── _format_impl.cpython-312.pyc
    │       │   │   │   ├── _function_base_impl.cpython-312.pyc
    │       │   │   │   ├── _histograms_impl.cpython-312.pyc
    │       │   │   │   ├── _index_tricks_impl.cpython-312.pyc
    │       │   │   │   ├── _iotools.cpython-312.pyc
    │       │   │   │   ├── _nanfunctions_impl.cpython-312.pyc
    │       │   │   │   ├── _npyio_impl.cpython-312.pyc
    │       │   │   │   ├── _polynomial_impl.cpython-312.pyc
    │       │   │   │   ├── _scimath_impl.cpython-312.pyc
    │       │   │   │   ├── _shape_base_impl.cpython-312.pyc
    │       │   │   │   ├── _stride_tricks_impl.cpython-312.pyc
    │       │   │   │   ├── _twodim_base_impl.cpython-312.pyc
    │       │   │   │   ├── _type_check_impl.cpython-312.pyc
    │       │   │   │   ├── _ufunclike_impl.cpython-312.pyc
    │       │   │   │   ├── _user_array_impl.cpython-312.pyc
    │       │   │   │   ├── _utils_impl.cpython-312.pyc
    │       │   │   │   ├── _version.cpython-312.pyc
    │       │   │   │   ├── array_utils.cpython-312.pyc
    │       │   │   │   ├── format.cpython-312.pyc
    │       │   │   │   ├── introspect.cpython-312.pyc
    │       │   │   │   ├── mixins.cpython-312.pyc
    │       │   │   │   ├── npyio.cpython-312.pyc
    │       │   │   │   ├── recfunctions.cpython-312.pyc
    │       │   │   │   ├── scimath.cpython-312.pyc
    │       │   │   │   ├── stride_tricks.cpython-312.pyc
    │       │   │   │   └── user_array.cpython-312.pyc
    │       │   │   ├── _array_utils_impl.py
    │       │   │   ├── _array_utils_impl.pyi
    │       │   │   ├── _arraypad_impl.py
    │       │   │   ├── _arraypad_impl.pyi
    │       │   │   ├── _arraysetops_impl.py
    │       │   │   ├── _arraysetops_impl.pyi
    │       │   │   ├── _arrayterator_impl.py
    │       │   │   ├── _arrayterator_impl.pyi
    │       │   │   ├── _datasource.py
    │       │   │   ├── _datasource.pyi
    │       │   │   ├── _format_impl.py
    │       │   │   ├── _format_impl.pyi
    │       │   │   ├── _function_base_impl.py
    │       │   │   ├── _function_base_impl.pyi
    │       │   │   ├── _histograms_impl.py
    │       │   │   ├── _histograms_impl.pyi
    │       │   │   ├── _index_tricks_impl.py
    │       │   │   ├── _index_tricks_impl.pyi
    │       │   │   ├── _iotools.py
    │       │   │   ├── _iotools.pyi
    │       │   │   ├── _nanfunctions_impl.py
    │       │   │   ├── _nanfunctions_impl.pyi
    │       │   │   ├── _npyio_impl.py
    │       │   │   ├── _npyio_impl.pyi
    │       │   │   ├── _polynomial_impl.py
    │       │   │   ├── _polynomial_impl.pyi
    │       │   │   ├── _scimath_impl.py
    │       │   │   ├── _scimath_impl.pyi
    │       │   │   ├── _shape_base_impl.py
    │       │   │   ├── _shape_base_impl.pyi
    │       │   │   ├── _stride_tricks_impl.py
    │       │   │   ├── _stride_tricks_impl.pyi
    │       │   │   ├── _twodim_base_impl.py
    │       │   │   ├── _twodim_base_impl.pyi
    │       │   │   ├── _type_check_impl.py
    │       │   │   ├── _type_check_impl.pyi
    │       │   │   ├── _ufunclike_impl.py
    │       │   │   ├── _ufunclike_impl.pyi
    │       │   │   ├── _user_array_impl.py
    │       │   │   ├── _user_array_impl.pyi
    │       │   │   ├── _utils_impl.py
    │       │   │   ├── _utils_impl.pyi
    │       │   │   ├── _version.py
    │       │   │   ├── _version.pyi
    │       │   │   ├── array_utils.py
    │       │   │   ├── array_utils.pyi
    │       │   │   ├── format.py
    │       │   │   ├── format.pyi
    │       │   │   ├── introspect.py
    │       │   │   ├── introspect.pyi
    │       │   │   ├── mixins.py
    │       │   │   ├── mixins.pyi
    │       │   │   ├── npyio.py
    │       │   │   ├── npyio.pyi
    │       │   │   ├── recfunctions.py
    │       │   │   ├── recfunctions.pyi
    │       │   │   ├── scimath.py
    │       │   │   ├── scimath.pyi
    │       │   │   ├── stride_tricks.py
    │       │   │   ├── stride_tricks.pyi
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── test__datasource.cpython-312.pyc
    │       │   │   │   │   ├── test__iotools.cpython-312.pyc
    │       │   │   │   │   ├── test__version.cpython-312.pyc
    │       │   │   │   │   ├── test_array_utils.cpython-312.pyc
    │       │   │   │   │   ├── test_arraypad.cpython-312.pyc
    │       │   │   │   │   ├── test_arraysetops.cpython-312.pyc
    │       │   │   │   │   ├── test_arrayterator.cpython-312.pyc
    │       │   │   │   │   ├── test_format.cpython-312.pyc
    │       │   │   │   │   ├── test_function_base.cpython-312.pyc
    │       │   │   │   │   ├── test_histograms.cpython-312.pyc
    │       │   │   │   │   ├── test_index_tricks.cpython-312.pyc
    │       │   │   │   │   ├── test_io.cpython-312.pyc
    │       │   │   │   │   ├── test_loadtxt.cpython-312.pyc
    │       │   │   │   │   ├── test_mixins.cpython-312.pyc
    │       │   │   │   │   ├── test_nanfunctions.cpython-312.pyc
    │       │   │   │   │   ├── test_packbits.cpython-312.pyc
    │       │   │   │   │   ├── test_polynomial.cpython-312.pyc
    │       │   │   │   │   ├── test_recfunctions.cpython-312.pyc
    │       │   │   │   │   ├── test_regression.cpython-312.pyc
    │       │   │   │   │   ├── test_shape_base.cpython-312.pyc
    │       │   │   │   │   ├── test_stride_tricks.cpython-312.pyc
    │       │   │   │   │   ├── test_twodim_base.cpython-312.pyc
    │       │   │   │   │   ├── test_type_check.cpython-312.pyc
    │       │   │   │   │   ├── test_ufunclike.cpython-312.pyc
    │       │   │   │   │   └── test_utils.cpython-312.pyc
    │       │   │   │   ├── data
    │       │   │   │   │   ├── py2-np0-objarr.npy
    │       │   │   │   │   ├── py2-objarr.npy
    │       │   │   │   │   ├── py2-objarr.npz
    │       │   │   │   │   ├── py3-objarr.npy
    │       │   │   │   │   ├── py3-objarr.npz
    │       │   │   │   │   ├── python3.npy
    │       │   │   │   │   └── win64python2.npy
    │       │   │   │   ├── test__datasource.py
    │       │   │   │   ├── test__iotools.py
    │       │   │   │   ├── test__version.py
    │       │   │   │   ├── test_array_utils.py
    │       │   │   │   ├── test_arraypad.py
    │       │   │   │   ├── test_arraysetops.py
    │       │   │   │   ├── test_arrayterator.py
    │       │   │   │   ├── test_format.py
    │       │   │   │   ├── test_function_base.py
    │       │   │   │   ├── test_histograms.py
    │       │   │   │   ├── test_index_tricks.py
    │       │   │   │   ├── test_io.py
    │       │   │   │   ├── test_loadtxt.py
    │       │   │   │   ├── test_mixins.py
    │       │   │   │   ├── test_nanfunctions.py
    │       │   │   │   ├── test_packbits.py
    │       │   │   │   ├── test_polynomial.py
    │       │   │   │   ├── test_recfunctions.py
    │       │   │   │   ├── test_regression.py
    │       │   │   │   ├── test_shape_base.py
    │       │   │   │   ├── test_stride_tricks.py
    │       │   │   │   ├── test_twodim_base.py
    │       │   │   │   ├── test_type_check.py
    │       │   │   │   ├── test_ufunclike.py
    │       │   │   │   └── test_utils.py
    │       │   │   ├── user_array.py
    │       │   │   └── user_array.pyi
    │       │   ├── linalg
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _linalg.cpython-312.pyc
    │       │   │   │   └── linalg.cpython-312.pyc
    │       │   │   ├── _linalg.py
    │       │   │   ├── _linalg.pyi
    │       │   │   ├── _umath_linalg.cp312-win_amd64.lib
    │       │   │   ├── _umath_linalg.cp312-win_amd64.pyd
    │       │   │   ├── _umath_linalg.pyi
    │       │   │   ├── lapack_lite.cp312-win_amd64.lib
    │       │   │   ├── lapack_lite.cp312-win_amd64.pyd
    │       │   │   ├── lapack_lite.pyi
    │       │   │   ├── linalg.py
    │       │   │   ├── linalg.pyi
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_deprecations.cpython-312.pyc
    │       │   │       │   ├── test_linalg.cpython-312.pyc
    │       │   │       │   └── test_regression.cpython-312.pyc
    │       │   │       ├── test_deprecations.py
    │       │   │       ├── test_linalg.py
    │       │   │       └── test_regression.py
    │       │   ├── ma
    │       │   │   ├── API_CHANGES.txt
    │       │   │   ├── LICENSE
    │       │   │   ├── README.rst
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── core.cpython-312.pyc
    │       │   │   │   ├── extras.cpython-312.pyc
    │       │   │   │   ├── mrecords.cpython-312.pyc
    │       │   │   │   └── testutils.cpython-312.pyc
    │       │   │   ├── core.py
    │       │   │   ├── core.pyi
    │       │   │   ├── extras.py
    │       │   │   ├── extras.pyi
    │       │   │   ├── mrecords.py
    │       │   │   ├── mrecords.pyi
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── test_arrayobject.cpython-312.pyc
    │       │   │   │   │   ├── test_core.cpython-312.pyc
    │       │   │   │   │   ├── test_deprecations.cpython-312.pyc
    │       │   │   │   │   ├── test_extras.cpython-312.pyc
    │       │   │   │   │   ├── test_mrecords.cpython-312.pyc
    │       │   │   │   │   ├── test_old_ma.cpython-312.pyc
    │       │   │   │   │   ├── test_regression.cpython-312.pyc
    │       │   │   │   │   └── test_subclassing.cpython-312.pyc
    │       │   │   │   ├── test_arrayobject.py
    │       │   │   │   ├── test_core.py
    │       │   │   │   ├── test_deprecations.py
    │       │   │   │   ├── test_extras.py
    │       │   │   │   ├── test_mrecords.py
    │       │   │   │   ├── test_old_ma.py
    │       │   │   │   ├── test_regression.py
    │       │   │   │   └── test_subclassing.py
    │       │   │   └── testutils.py
    │       │   ├── matlib.py
    │       │   ├── matlib.pyi
    │       │   ├── matrixlib
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── defmatrix.cpython-312.pyc
    │       │   │   ├── defmatrix.py
    │       │   │   ├── defmatrix.pyi
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_defmatrix.cpython-312.pyc
    │       │   │       │   ├── test_interaction.cpython-312.pyc
    │       │   │       │   ├── test_masked_matrix.cpython-312.pyc
    │       │   │       │   ├── test_matrix_linalg.cpython-312.pyc
    │       │   │       │   ├── test_multiarray.cpython-312.pyc
    │       │   │       │   ├── test_numeric.cpython-312.pyc
    │       │   │       │   └── test_regression.cpython-312.pyc
    │       │   │       ├── test_defmatrix.py
    │       │   │       ├── test_interaction.py
    │       │   │       ├── test_masked_matrix.py
    │       │   │       ├── test_matrix_linalg.py
    │       │   │       ├── test_multiarray.py
    │       │   │       ├── test_numeric.py
    │       │   │       └── test_regression.py
    │       │   ├── polynomial
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _polybase.cpython-312.pyc
    │       │   │   │   ├── chebyshev.cpython-312.pyc
    │       │   │   │   ├── hermite.cpython-312.pyc
    │       │   │   │   ├── hermite_e.cpython-312.pyc
    │       │   │   │   ├── laguerre.cpython-312.pyc
    │       │   │   │   ├── legendre.cpython-312.pyc
    │       │   │   │   ├── polynomial.cpython-312.pyc
    │       │   │   │   └── polyutils.cpython-312.pyc
    │       │   │   ├── _polybase.py
    │       │   │   ├── _polybase.pyi
    │       │   │   ├── _polytypes.pyi
    │       │   │   ├── chebyshev.py
    │       │   │   ├── chebyshev.pyi
    │       │   │   ├── hermite.py
    │       │   │   ├── hermite.pyi
    │       │   │   ├── hermite_e.py
    │       │   │   ├── hermite_e.pyi
    │       │   │   ├── laguerre.py
    │       │   │   ├── laguerre.pyi
    │       │   │   ├── legendre.py
    │       │   │   ├── legendre.pyi
    │       │   │   ├── polynomial.py
    │       │   │   ├── polynomial.pyi
    │       │   │   ├── polyutils.py
    │       │   │   ├── polyutils.pyi
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_chebyshev.cpython-312.pyc
    │       │   │       │   ├── test_classes.cpython-312.pyc
    │       │   │       │   ├── test_hermite.cpython-312.pyc
    │       │   │       │   ├── test_hermite_e.cpython-312.pyc
    │       │   │       │   ├── test_laguerre.cpython-312.pyc
    │       │   │       │   ├── test_legendre.cpython-312.pyc
    │       │   │       │   ├── test_polynomial.cpython-312.pyc
    │       │   │       │   ├── test_polyutils.cpython-312.pyc
    │       │   │       │   ├── test_printing.cpython-312.pyc
    │       │   │       │   └── test_symbol.cpython-312.pyc
    │       │   │       ├── test_chebyshev.py
    │       │   │       ├── test_classes.py
    │       │   │       ├── test_hermite.py
    │       │   │       ├── test_hermite_e.py
    │       │   │       ├── test_laguerre.py
    │       │   │       ├── test_legendre.py
    │       │   │       ├── test_polynomial.py
    │       │   │       ├── test_polyutils.py
    │       │   │       ├── test_printing.py
    │       │   │       └── test_symbol.py
    │       │   ├── py.typed
    │       │   ├── random
    │       │   │   ├── LICENSE.md
    │       │   │   ├── __init__.pxd
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── _pickle.cpython-312.pyc
    │       │   │   ├── _bounded_integers.cp312-win_amd64.lib
    │       │   │   ├── _bounded_integers.cp312-win_amd64.pyd
    │       │   │   ├── _bounded_integers.pxd
    │       │   │   ├── _bounded_integers.pyi
    │       │   │   ├── _common.cp312-win_amd64.lib
    │       │   │   ├── _common.cp312-win_amd64.pyd
    │       │   │   ├── _common.pxd
    │       │   │   ├── _common.pyi
    │       │   │   ├── _examples
    │       │   │   │   ├── cffi
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── extending.cpython-312.pyc
    │       │   │   │   │   │   └── parse.cpython-312.pyc
    │       │   │   │   │   ├── extending.py
    │       │   │   │   │   └── parse.py
    │       │   │   │   ├── cython
    │       │   │   │   │   ├── extending.pyx
    │       │   │   │   │   ├── extending_distributions.pyx
    │       │   │   │   │   └── meson.build
    │       │   │   │   └── numba
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── extending.cpython-312.pyc
    │       │   │   │       │   └── extending_distributions.cpython-312.pyc
    │       │   │   │       ├── extending.py
    │       │   │   │       └── extending_distributions.py
    │       │   │   ├── _generator.cp312-win_amd64.lib
    │       │   │   ├── _generator.cp312-win_amd64.pyd
    │       │   │   ├── _generator.pyi
    │       │   │   ├── _mt19937.cp312-win_amd64.lib
    │       │   │   ├── _mt19937.cp312-win_amd64.pyd
    │       │   │   ├── _mt19937.pyi
    │       │   │   ├── _pcg64.cp312-win_amd64.lib
    │       │   │   ├── _pcg64.cp312-win_amd64.pyd
    │       │   │   ├── _pcg64.pyi
    │       │   │   ├── _philox.cp312-win_amd64.lib
    │       │   │   ├── _philox.cp312-win_amd64.pyd
    │       │   │   ├── _philox.pyi
    │       │   │   ├── _pickle.py
    │       │   │   ├── _pickle.pyi
    │       │   │   ├── _sfc64.cp312-win_amd64.lib
    │       │   │   ├── _sfc64.cp312-win_amd64.pyd
    │       │   │   ├── _sfc64.pyi
    │       │   │   ├── bit_generator.cp312-win_amd64.lib
    │       │   │   ├── bit_generator.cp312-win_amd64.pyd
    │       │   │   ├── bit_generator.pxd
    │       │   │   ├── bit_generator.pyi
    │       │   │   ├── c_distributions.pxd
    │       │   │   ├── lib
    │       │   │   │   └── npyrandom.lib
    │       │   │   ├── mtrand.cp312-win_amd64.lib
    │       │   │   ├── mtrand.cp312-win_amd64.pyd
    │       │   │   ├── mtrand.pyi
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_direct.cpython-312.pyc
    │       │   │       │   ├── test_extending.cpython-312.pyc
    │       │   │       │   ├── test_generator_mt19937.cpython-312.pyc
    │       │   │       │   ├── test_generator_mt19937_regressions.cpython-312.pyc
    │       │   │       │   ├── test_random.cpython-312.pyc
    │       │   │       │   ├── test_randomstate.cpython-312.pyc
    │       │   │       │   ├── test_randomstate_regression.cpython-312.pyc
    │       │   │       │   ├── test_regression.cpython-312.pyc
    │       │   │       │   ├── test_seed_sequence.cpython-312.pyc
    │       │   │       │   └── test_smoke.cpython-312.pyc
    │       │   │       ├── data
    │       │   │       │   ├── __init__.py
    │       │   │       │   ├── __pycache__
    │       │   │       │   │   └── __init__.cpython-312.pyc
    │       │   │       │   ├── generator_pcg64_np121.pkl.gz
    │       │   │       │   ├── generator_pcg64_np126.pkl.gz
    │       │   │       │   ├── mt19937-testset-1.csv
    │       │   │       │   ├── mt19937-testset-2.csv
    │       │   │       │   ├── pcg64-testset-1.csv
    │       │   │       │   ├── pcg64-testset-2.csv
    │       │   │       │   ├── pcg64dxsm-testset-1.csv
    │       │   │       │   ├── pcg64dxsm-testset-2.csv
    │       │   │       │   ├── philox-testset-1.csv
    │       │   │       │   ├── philox-testset-2.csv
    │       │   │       │   ├── sfc64-testset-1.csv
    │       │   │       │   ├── sfc64-testset-2.csv
    │       │   │       │   └── sfc64_np126.pkl.gz
    │       │   │       ├── test_direct.py
    │       │   │       ├── test_extending.py
    │       │   │       ├── test_generator_mt19937.py
    │       │   │       ├── test_generator_mt19937_regressions.py
    │       │   │       ├── test_random.py
    │       │   │       ├── test_randomstate.py
    │       │   │       ├── test_randomstate_regression.py
    │       │   │       ├── test_regression.py
    │       │   │       ├── test_seed_sequence.py
    │       │   │       └── test_smoke.py
    │       │   ├── rec
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   └── __pycache__
    │       │   │       └── __init__.cpython-312.pyc
    │       │   ├── strings
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   └── __pycache__
    │       │   │       └── __init__.cpython-312.pyc
    │       │   ├── testing
    │       │   │   ├── __init__.py
    │       │   │   ├── __init__.pyi
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── overrides.cpython-312.pyc
    │       │   │   │   └── print_coercion_tables.cpython-312.pyc
    │       │   │   ├── _private
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __init__.pyi
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── extbuild.cpython-312.pyc
    │       │   │   │   │   └── utils.cpython-312.pyc
    │       │   │   │   ├── extbuild.py
    │       │   │   │   ├── extbuild.pyi
    │       │   │   │   ├── utils.py
    │       │   │   │   └── utils.pyi
    │       │   │   ├── overrides.py
    │       │   │   ├── overrides.pyi
    │       │   │   ├── print_coercion_tables.py
    │       │   │   ├── print_coercion_tables.pyi
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   └── test_utils.cpython-312.pyc
    │       │   │       └── test_utils.py
    │       │   ├── tests
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── test__all__.cpython-312.pyc
    │       │   │   │   ├── test_configtool.cpython-312.pyc
    │       │   │   │   ├── test_ctypeslib.cpython-312.pyc
    │       │   │   │   ├── test_lazyloading.cpython-312.pyc
    │       │   │   │   ├── test_matlib.cpython-312.pyc
    │       │   │   │   ├── test_numpy_config.cpython-312.pyc
    │       │   │   │   ├── test_numpy_version.cpython-312.pyc
    │       │   │   │   ├── test_public_api.cpython-312.pyc
    │       │   │   │   ├── test_reloading.cpython-312.pyc
    │       │   │   │   ├── test_scripts.cpython-312.pyc
    │       │   │   │   └── test_warnings.cpython-312.pyc
    │       │   │   ├── test__all__.py
    │       │   │   ├── test_configtool.py
    │       │   │   ├── test_ctypeslib.py
    │       │   │   ├── test_lazyloading.py
    │       │   │   ├── test_matlib.py
    │       │   │   ├── test_numpy_config.py
    │       │   │   ├── test_numpy_version.py
    │       │   │   ├── test_public_api.py
    │       │   │   ├── test_reloading.py
    │       │   │   ├── test_scripts.py
    │       │   │   └── test_warnings.py
    │       │   ├── typing
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── mypy_plugin.cpython-312.pyc
    │       │   │   ├── mypy_plugin.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_isfile.cpython-312.pyc
    │       │   │       │   ├── test_runtime.cpython-312.pyc
    │       │   │       │   └── test_typing.cpython-312.pyc
    │       │   │       ├── data
    │       │   │       │   ├── fail
    │       │   │       │   │   ├── arithmetic.pyi
    │       │   │       │   │   ├── array_constructors.pyi
    │       │   │       │   │   ├── array_like.pyi
    │       │   │       │   │   ├── array_pad.pyi
    │       │   │       │   │   ├── arrayprint.pyi
    │       │   │       │   │   ├── arrayterator.pyi
    │       │   │       │   │   ├── bitwise_ops.pyi
    │       │   │       │   │   ├── char.pyi
    │       │   │       │   │   ├── chararray.pyi
    │       │   │       │   │   ├── comparisons.pyi
    │       │   │       │   │   ├── constants.pyi
    │       │   │       │   │   ├── datasource.pyi
    │       │   │       │   │   ├── dtype.pyi
    │       │   │       │   │   ├── einsumfunc.pyi
    │       │   │       │   │   ├── flatiter.pyi
    │       │   │       │   │   ├── fromnumeric.pyi
    │       │   │       │   │   ├── histograms.pyi
    │       │   │       │   │   ├── index_tricks.pyi
    │       │   │       │   │   ├── lib_function_base.pyi
    │       │   │       │   │   ├── lib_polynomial.pyi
    │       │   │       │   │   ├── lib_utils.pyi
    │       │   │       │   │   ├── lib_version.pyi
    │       │   │       │   │   ├── linalg.pyi
    │       │   │       │   │   ├── ma.pyi
    │       │   │       │   │   ├── memmap.pyi
    │       │   │       │   │   ├── modules.pyi
    │       │   │       │   │   ├── multiarray.pyi
    │       │   │       │   │   ├── ndarray.pyi
    │       │   │       │   │   ├── ndarray_misc.pyi
    │       │   │       │   │   ├── nditer.pyi
    │       │   │       │   │   ├── nested_sequence.pyi
    │       │   │       │   │   ├── npyio.pyi
    │       │   │       │   │   ├── numerictypes.pyi
    │       │   │       │   │   ├── random.pyi
    │       │   │       │   │   ├── rec.pyi
    │       │   │       │   │   ├── scalars.pyi
    │       │   │       │   │   ├── shape.pyi
    │       │   │       │   │   ├── shape_base.pyi
    │       │   │       │   │   ├── stride_tricks.pyi
    │       │   │       │   │   ├── strings.pyi
    │       │   │       │   │   ├── testing.pyi
    │       │   │       │   │   ├── twodim_base.pyi
    │       │   │       │   │   ├── type_check.pyi
    │       │   │       │   │   ├── ufunc_config.pyi
    │       │   │       │   │   ├── ufunclike.pyi
    │       │   │       │   │   ├── ufuncs.pyi
    │       │   │       │   │   └── warnings_and_errors.pyi
    │       │   │       │   ├── misc
    │       │   │       │   │   └── extended_precision.pyi
    │       │   │       │   ├── mypy.ini
    │       │   │       │   ├── pass
    │       │   │       │   │   ├── __pycache__
    │       │   │       │   │   │   ├── arithmetic.cpython-312.pyc
    │       │   │       │   │   │   ├── array_constructors.cpython-312.pyc
    │       │   │       │   │   │   ├── array_like.cpython-312.pyc
    │       │   │       │   │   │   ├── arrayprint.cpython-312.pyc
    │       │   │       │   │   │   ├── arrayterator.cpython-312.pyc
    │       │   │       │   │   │   ├── bitwise_ops.cpython-312.pyc
    │       │   │       │   │   │   ├── comparisons.cpython-312.pyc
    │       │   │       │   │   │   ├── dtype.cpython-312.pyc
    │       │   │       │   │   │   ├── einsumfunc.cpython-312.pyc
    │       │   │       │   │   │   ├── flatiter.cpython-312.pyc
    │       │   │       │   │   │   ├── fromnumeric.cpython-312.pyc
    │       │   │       │   │   │   ├── index_tricks.cpython-312.pyc
    │       │   │       │   │   │   ├── lib_user_array.cpython-312.pyc
    │       │   │       │   │   │   ├── lib_utils.cpython-312.pyc
    │       │   │       │   │   │   ├── lib_version.cpython-312.pyc
    │       │   │       │   │   │   ├── literal.cpython-312.pyc
    │       │   │       │   │   │   ├── ma.cpython-312.pyc
    │       │   │       │   │   │   ├── mod.cpython-312.pyc
    │       │   │       │   │   │   ├── modules.cpython-312.pyc
    │       │   │       │   │   │   ├── multiarray.cpython-312.pyc
    │       │   │       │   │   │   ├── ndarray_conversion.cpython-312.pyc
    │       │   │       │   │   │   ├── ndarray_misc.cpython-312.pyc
    │       │   │       │   │   │   ├── ndarray_shape_manipulation.cpython-312.pyc
    │       │   │       │   │   │   ├── nditer.cpython-312.pyc
    │       │   │       │   │   │   ├── numeric.cpython-312.pyc
    │       │   │       │   │   │   ├── numerictypes.cpython-312.pyc
    │       │   │       │   │   │   ├── random.cpython-312.pyc
    │       │   │       │   │   │   ├── recfunctions.cpython-312.pyc
    │       │   │       │   │   │   ├── scalars.cpython-312.pyc
    │       │   │       │   │   │   ├── shape.cpython-312.pyc
    │       │   │       │   │   │   ├── simple.cpython-312.pyc
    │       │   │       │   │   │   ├── simple_py3.cpython-312.pyc
    │       │   │       │   │   │   ├── ufunc_config.cpython-312.pyc
    │       │   │       │   │   │   ├── ufunclike.cpython-312.pyc
    │       │   │       │   │   │   ├── ufuncs.cpython-312.pyc
    │       │   │       │   │   │   └── warnings_and_errors.cpython-312.pyc
    │       │   │       │   │   ├── arithmetic.py
    │       │   │       │   │   ├── array_constructors.py
    │       │   │       │   │   ├── array_like.py
    │       │   │       │   │   ├── arrayprint.py
    │       │   │       │   │   ├── arrayterator.py
    │       │   │       │   │   ├── bitwise_ops.py
    │       │   │       │   │   ├── comparisons.py
    │       │   │       │   │   ├── dtype.py
    │       │   │       │   │   ├── einsumfunc.py
    │       │   │       │   │   ├── flatiter.py
    │       │   │       │   │   ├── fromnumeric.py
    │       │   │       │   │   ├── index_tricks.py
    │       │   │       │   │   ├── lib_user_array.py
    │       │   │       │   │   ├── lib_utils.py
    │       │   │       │   │   ├── lib_version.py
    │       │   │       │   │   ├── literal.py
    │       │   │       │   │   ├── ma.py
    │       │   │       │   │   ├── mod.py
    │       │   │       │   │   ├── modules.py
    │       │   │       │   │   ├── multiarray.py
    │       │   │       │   │   ├── ndarray_conversion.py
    │       │   │       │   │   ├── ndarray_misc.py
    │       │   │       │   │   ├── ndarray_shape_manipulation.py
    │       │   │       │   │   ├── nditer.py
    │       │   │       │   │   ├── numeric.py
    │       │   │       │   │   ├── numerictypes.py
    │       │   │       │   │   ├── random.py
    │       │   │       │   │   ├── recfunctions.py
    │       │   │       │   │   ├── scalars.py
    │       │   │       │   │   ├── shape.py
    │       │   │       │   │   ├── simple.py
    │       │   │       │   │   ├── simple_py3.py
    │       │   │       │   │   ├── ufunc_config.py
    │       │   │       │   │   ├── ufunclike.py
    │       │   │       │   │   ├── ufuncs.py
    │       │   │       │   │   └── warnings_and_errors.py
    │       │   │       │   └── reveal
    │       │   │       │       ├── arithmetic.pyi
    │       │   │       │       ├── array_api_info.pyi
    │       │   │       │       ├── array_constructors.pyi
    │       │   │       │       ├── arraypad.pyi
    │       │   │       │       ├── arrayprint.pyi
    │       │   │       │       ├── arraysetops.pyi
    │       │   │       │       ├── arrayterator.pyi
    │       │   │       │       ├── bitwise_ops.pyi
    │       │   │       │       ├── char.pyi
    │       │   │       │       ├── chararray.pyi
    │       │   │       │       ├── comparisons.pyi
    │       │   │       │       ├── constants.pyi
    │       │   │       │       ├── ctypeslib.pyi
    │       │   │       │       ├── datasource.pyi
    │       │   │       │       ├── dtype.pyi
    │       │   │       │       ├── einsumfunc.pyi
    │       │   │       │       ├── emath.pyi
    │       │   │       │       ├── fft.pyi
    │       │   │       │       ├── flatiter.pyi
    │       │   │       │       ├── fromnumeric.pyi
    │       │   │       │       ├── getlimits.pyi
    │       │   │       │       ├── histograms.pyi
    │       │   │       │       ├── index_tricks.pyi
    │       │   │       │       ├── lib_function_base.pyi
    │       │   │       │       ├── lib_polynomial.pyi
    │       │   │       │       ├── lib_utils.pyi
    │       │   │       │       ├── lib_version.pyi
    │       │   │       │       ├── linalg.pyi
    │       │   │       │       ├── ma.pyi
    │       │   │       │       ├── matrix.pyi
    │       │   │       │       ├── memmap.pyi
    │       │   │       │       ├── mod.pyi
    │       │   │       │       ├── modules.pyi
    │       │   │       │       ├── multiarray.pyi
    │       │   │       │       ├── nbit_base_example.pyi
    │       │   │       │       ├── ndarray_assignability.pyi
    │       │   │       │       ├── ndarray_conversion.pyi
    │       │   │       │       ├── ndarray_misc.pyi
    │       │   │       │       ├── ndarray_shape_manipulation.pyi
    │       │   │       │       ├── nditer.pyi
    │       │   │       │       ├── nested_sequence.pyi
    │       │   │       │       ├── npyio.pyi
    │       │   │       │       ├── numeric.pyi
    │       │   │       │       ├── numerictypes.pyi
    │       │   │       │       ├── polynomial_polybase.pyi
    │       │   │       │       ├── polynomial_polyutils.pyi
    │       │   │       │       ├── polynomial_series.pyi
    │       │   │       │       ├── random.pyi
    │       │   │       │       ├── rec.pyi
    │       │   │       │       ├── scalars.pyi
    │       │   │       │       ├── shape.pyi
    │       │   │       │       ├── shape_base.pyi
    │       │   │       │       ├── stride_tricks.pyi
    │       │   │       │       ├── strings.pyi
    │       │   │       │       ├── testing.pyi
    │       │   │       │       ├── twodim_base.pyi
    │       │   │       │       ├── type_check.pyi
    │       │   │       │       ├── ufunc_config.pyi
    │       │   │       │       ├── ufunclike.pyi
    │       │   │       │       ├── ufuncs.pyi
    │       │   │       │       └── warnings_and_errors.pyi
    │       │   │       ├── test_isfile.py
    │       │   │       ├── test_runtime.py
    │       │   │       └── test_typing.py
    │       │   ├── version.py
    │       │   └── version.pyi
    │       ├── numpy-2.3.5.dist-info
    │       │   ├── DELVEWHEEL
    │       │   ├── INSTALLER
    │       │   ├── LICENSE.txt
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── entry_points.txt
    │       ├── numpy.libs
    │       │   ├── libscipy_openblas64_-9e3e5a4229c1ca39f10dc82bba9e2b2b.dll
    │       │   └── msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
    │       ├── packaging
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── _elffile.cpython-312.pyc
    │       │   │   ├── _manylinux.cpython-312.pyc
    │       │   │   ├── _musllinux.cpython-312.pyc
    │       │   │   ├── _parser.cpython-312.pyc
    │       │   │   ├── _structures.cpython-312.pyc
    │       │   │   ├── _tokenizer.cpython-312.pyc
    │       │   │   ├── markers.cpython-312.pyc
    │       │   │   ├── metadata.cpython-312.pyc
    │       │   │   ├── requirements.cpython-312.pyc
    │       │   │   ├── specifiers.cpython-312.pyc
    │       │   │   ├── tags.cpython-312.pyc
    │       │   │   ├── utils.cpython-312.pyc
    │       │   │   └── version.cpython-312.pyc
    │       │   ├── _elffile.py
    │       │   ├── _manylinux.py
    │       │   ├── _musllinux.py
    │       │   ├── _parser.py
    │       │   ├── _structures.py
    │       │   ├── _tokenizer.py
    │       │   ├── licenses
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── _spdx.cpython-312.pyc
    │       │   │   └── _spdx.py
    │       │   ├── markers.py
    │       │   ├── metadata.py
    │       │   ├── py.typed
    │       │   ├── requirements.py
    │       │   ├── specifiers.py
    │       │   ├── tags.py
    │       │   ├── utils.py
    │       │   └── version.py
    │       ├── packaging-25.0.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   └── licenses
    │       │       ├── LICENSE
    │       │       ├── LICENSE.APACHE
    │       │       └── LICENSE.BSD
    │       ├── pillow-12.0.0.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   ├── licenses
    │       │   │   └── LICENSE
    │       │   ├── top_level.txt
    │       │   └── zip-safe
    │       ├── pip
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pip-runner__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── __main__.cpython-312.pyc
    │       │   │   └── __pip-runner__.cpython-312.pyc
    │       │   ├── _internal
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── build_env.cpython-312.pyc
    │       │   │   │   ├── cache.cpython-312.pyc
    │       │   │   │   ├── configuration.cpython-312.pyc
    │       │   │   │   ├── exceptions.cpython-312.pyc
    │       │   │   │   ├── main.cpython-312.pyc
    │       │   │   │   ├── pyproject.cpython-312.pyc
    │       │   │   │   ├── self_outdated_check.cpython-312.pyc
    │       │   │   │   └── wheel_builder.cpython-312.pyc
    │       │   │   ├── build_env.py
    │       │   │   ├── cache.py
    │       │   │   ├── cli
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── autocompletion.cpython-312.pyc
    │       │   │   │   │   ├── base_command.cpython-312.pyc
    │       │   │   │   │   ├── cmdoptions.cpython-312.pyc
    │       │   │   │   │   ├── command_context.cpython-312.pyc
    │       │   │   │   │   ├── index_command.cpython-312.pyc
    │       │   │   │   │   ├── main.cpython-312.pyc
    │       │   │   │   │   ├── main_parser.cpython-312.pyc
    │       │   │   │   │   ├── parser.cpython-312.pyc
    │       │   │   │   │   ├── progress_bars.cpython-312.pyc
    │       │   │   │   │   ├── req_command.cpython-312.pyc
    │       │   │   │   │   ├── spinners.cpython-312.pyc
    │       │   │   │   │   └── status_codes.cpython-312.pyc
    │       │   │   │   ├── autocompletion.py
    │       │   │   │   ├── base_command.py
    │       │   │   │   ├── cmdoptions.py
    │       │   │   │   ├── command_context.py
    │       │   │   │   ├── index_command.py
    │       │   │   │   ├── main.py
    │       │   │   │   ├── main_parser.py
    │       │   │   │   ├── parser.py
    │       │   │   │   ├── progress_bars.py
    │       │   │   │   ├── req_command.py
    │       │   │   │   ├── spinners.py
    │       │   │   │   └── status_codes.py
    │       │   │   ├── commands
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── cache.cpython-312.pyc
    │       │   │   │   │   ├── check.cpython-312.pyc
    │       │   │   │   │   ├── completion.cpython-312.pyc
    │       │   │   │   │   ├── configuration.cpython-312.pyc
    │       │   │   │   │   ├── debug.cpython-312.pyc
    │       │   │   │   │   ├── download.cpython-312.pyc
    │       │   │   │   │   ├── freeze.cpython-312.pyc
    │       │   │   │   │   ├── hash.cpython-312.pyc
    │       │   │   │   │   ├── help.cpython-312.pyc
    │       │   │   │   │   ├── index.cpython-312.pyc
    │       │   │   │   │   ├── inspect.cpython-312.pyc
    │       │   │   │   │   ├── install.cpython-312.pyc
    │       │   │   │   │   ├── list.cpython-312.pyc
    │       │   │   │   │   ├── lock.cpython-312.pyc
    │       │   │   │   │   ├── search.cpython-312.pyc
    │       │   │   │   │   ├── show.cpython-312.pyc
    │       │   │   │   │   ├── uninstall.cpython-312.pyc
    │       │   │   │   │   └── wheel.cpython-312.pyc
    │       │   │   │   ├── cache.py
    │       │   │   │   ├── check.py
    │       │   │   │   ├── completion.py
    │       │   │   │   ├── configuration.py
    │       │   │   │   ├── debug.py
    │       │   │   │   ├── download.py
    │       │   │   │   ├── freeze.py
    │       │   │   │   ├── hash.py
    │       │   │   │   ├── help.py
    │       │   │   │   ├── index.py
    │       │   │   │   ├── inspect.py
    │       │   │   │   ├── install.py
    │       │   │   │   ├── list.py
    │       │   │   │   ├── lock.py
    │       │   │   │   ├── search.py
    │       │   │   │   ├── show.py
    │       │   │   │   ├── uninstall.py
    │       │   │   │   └── wheel.py
    │       │   │   ├── configuration.py
    │       │   │   ├── distributions
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── base.cpython-312.pyc
    │       │   │   │   │   ├── installed.cpython-312.pyc
    │       │   │   │   │   ├── sdist.cpython-312.pyc
    │       │   │   │   │   └── wheel.cpython-312.pyc
    │       │   │   │   ├── base.py
    │       │   │   │   ├── installed.py
    │       │   │   │   ├── sdist.py
    │       │   │   │   └── wheel.py
    │       │   │   ├── exceptions.py
    │       │   │   ├── index
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── collector.cpython-312.pyc
    │       │   │   │   │   ├── package_finder.cpython-312.pyc
    │       │   │   │   │   └── sources.cpython-312.pyc
    │       │   │   │   ├── collector.py
    │       │   │   │   ├── package_finder.py
    │       │   │   │   └── sources.py
    │       │   │   ├── locations
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _distutils.cpython-312.pyc
    │       │   │   │   │   ├── _sysconfig.cpython-312.pyc
    │       │   │   │   │   └── base.cpython-312.pyc
    │       │   │   │   ├── _distutils.py
    │       │   │   │   ├── _sysconfig.py
    │       │   │   │   └── base.py
    │       │   │   ├── main.py
    │       │   │   ├── metadata
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _json.cpython-312.pyc
    │       │   │   │   │   ├── base.cpython-312.pyc
    │       │   │   │   │   └── pkg_resources.cpython-312.pyc
    │       │   │   │   ├── _json.py
    │       │   │   │   ├── base.py
    │       │   │   │   ├── importlib
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _compat.cpython-312.pyc
    │       │   │   │   │   │   ├── _dists.cpython-312.pyc
    │       │   │   │   │   │   └── _envs.cpython-312.pyc
    │       │   │   │   │   ├── _compat.py
    │       │   │   │   │   ├── _dists.py
    │       │   │   │   │   └── _envs.py
    │       │   │   │   └── pkg_resources.py
    │       │   │   ├── models
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── candidate.cpython-312.pyc
    │       │   │   │   │   ├── direct_url.cpython-312.pyc
    │       │   │   │   │   ├── format_control.cpython-312.pyc
    │       │   │   │   │   ├── index.cpython-312.pyc
    │       │   │   │   │   ├── installation_report.cpython-312.pyc
    │       │   │   │   │   ├── link.cpython-312.pyc
    │       │   │   │   │   ├── pylock.cpython-312.pyc
    │       │   │   │   │   ├── scheme.cpython-312.pyc
    │       │   │   │   │   ├── search_scope.cpython-312.pyc
    │       │   │   │   │   ├── selection_prefs.cpython-312.pyc
    │       │   │   │   │   ├── target_python.cpython-312.pyc
    │       │   │   │   │   └── wheel.cpython-312.pyc
    │       │   │   │   ├── candidate.py
    │       │   │   │   ├── direct_url.py
    │       │   │   │   ├── format_control.py
    │       │   │   │   ├── index.py
    │       │   │   │   ├── installation_report.py
    │       │   │   │   ├── link.py
    │       │   │   │   ├── pylock.py
    │       │   │   │   ├── scheme.py
    │       │   │   │   ├── search_scope.py
    │       │   │   │   ├── selection_prefs.py
    │       │   │   │   ├── target_python.py
    │       │   │   │   └── wheel.py
    │       │   │   ├── network
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── auth.cpython-312.pyc
    │       │   │   │   │   ├── cache.cpython-312.pyc
    │       │   │   │   │   ├── download.cpython-312.pyc
    │       │   │   │   │   ├── lazy_wheel.cpython-312.pyc
    │       │   │   │   │   ├── session.cpython-312.pyc
    │       │   │   │   │   ├── utils.cpython-312.pyc
    │       │   │   │   │   └── xmlrpc.cpython-312.pyc
    │       │   │   │   ├── auth.py
    │       │   │   │   ├── cache.py
    │       │   │   │   ├── download.py
    │       │   │   │   ├── lazy_wheel.py
    │       │   │   │   ├── session.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── xmlrpc.py
    │       │   │   ├── operations
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── check.cpython-312.pyc
    │       │   │   │   │   ├── freeze.cpython-312.pyc
    │       │   │   │   │   └── prepare.cpython-312.pyc
    │       │   │   │   ├── build
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── build_tracker.cpython-312.pyc
    │       │   │   │   │   │   ├── metadata.cpython-312.pyc
    │       │   │   │   │   │   ├── metadata_editable.cpython-312.pyc
    │       │   │   │   │   │   ├── wheel.cpython-312.pyc
    │       │   │   │   │   │   └── wheel_editable.cpython-312.pyc
    │       │   │   │   │   ├── build_tracker.py
    │       │   │   │   │   ├── metadata.py
    │       │   │   │   │   ├── metadata_editable.py
    │       │   │   │   │   ├── wheel.py
    │       │   │   │   │   └── wheel_editable.py
    │       │   │   │   ├── check.py
    │       │   │   │   ├── freeze.py
    │       │   │   │   ├── install
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   └── wheel.cpython-312.pyc
    │       │   │   │   │   └── wheel.py
    │       │   │   │   └── prepare.py
    │       │   │   ├── pyproject.py
    │       │   │   ├── req
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── constructors.cpython-312.pyc
    │       │   │   │   │   ├── req_dependency_group.cpython-312.pyc
    │       │   │   │   │   ├── req_file.cpython-312.pyc
    │       │   │   │   │   ├── req_install.cpython-312.pyc
    │       │   │   │   │   ├── req_set.cpython-312.pyc
    │       │   │   │   │   └── req_uninstall.cpython-312.pyc
    │       │   │   │   ├── constructors.py
    │       │   │   │   ├── req_dependency_group.py
    │       │   │   │   ├── req_file.py
    │       │   │   │   ├── req_install.py
    │       │   │   │   ├── req_set.py
    │       │   │   │   └── req_uninstall.py
    │       │   │   ├── resolution
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   └── base.cpython-312.pyc
    │       │   │   │   ├── base.py
    │       │   │   │   ├── legacy
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   └── resolver.cpython-312.pyc
    │       │   │   │   │   └── resolver.py
    │       │   │   │   └── resolvelib
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── base.cpython-312.pyc
    │       │   │   │       │   ├── candidates.cpython-312.pyc
    │       │   │   │       │   ├── factory.cpython-312.pyc
    │       │   │   │       │   ├── found_candidates.cpython-312.pyc
    │       │   │   │       │   ├── provider.cpython-312.pyc
    │       │   │   │       │   ├── reporter.cpython-312.pyc
    │       │   │   │       │   ├── requirements.cpython-312.pyc
    │       │   │   │       │   └── resolver.cpython-312.pyc
    │       │   │   │       ├── base.py
    │       │   │   │       ├── candidates.py
    │       │   │   │       ├── factory.py
    │       │   │   │       ├── found_candidates.py
    │       │   │   │       ├── provider.py
    │       │   │   │       ├── reporter.py
    │       │   │   │       ├── requirements.py
    │       │   │   │       └── resolver.py
    │       │   │   ├── self_outdated_check.py
    │       │   │   ├── utils
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _jaraco_text.cpython-312.pyc
    │       │   │   │   │   ├── _log.cpython-312.pyc
    │       │   │   │   │   ├── appdirs.cpython-312.pyc
    │       │   │   │   │   ├── compat.cpython-312.pyc
    │       │   │   │   │   ├── compatibility_tags.cpython-312.pyc
    │       │   │   │   │   ├── datetime.cpython-312.pyc
    │       │   │   │   │   ├── deprecation.cpython-312.pyc
    │       │   │   │   │   ├── direct_url_helpers.cpython-312.pyc
    │       │   │   │   │   ├── egg_link.cpython-312.pyc
    │       │   │   │   │   ├── entrypoints.cpython-312.pyc
    │       │   │   │   │   ├── filesystem.cpython-312.pyc
    │       │   │   │   │   ├── filetypes.cpython-312.pyc
    │       │   │   │   │   ├── glibc.cpython-312.pyc
    │       │   │   │   │   ├── hashes.cpython-312.pyc
    │       │   │   │   │   ├── logging.cpython-312.pyc
    │       │   │   │   │   ├── misc.cpython-312.pyc
    │       │   │   │   │   ├── packaging.cpython-312.pyc
    │       │   │   │   │   ├── retry.cpython-312.pyc
    │       │   │   │   │   ├── subprocess.cpython-312.pyc
    │       │   │   │   │   ├── temp_dir.cpython-312.pyc
    │       │   │   │   │   ├── unpacking.cpython-312.pyc
    │       │   │   │   │   ├── urls.cpython-312.pyc
    │       │   │   │   │   ├── virtualenv.cpython-312.pyc
    │       │   │   │   │   └── wheel.cpython-312.pyc
    │       │   │   │   ├── _jaraco_text.py
    │       │   │   │   ├── _log.py
    │       │   │   │   ├── appdirs.py
    │       │   │   │   ├── compat.py
    │       │   │   │   ├── compatibility_tags.py
    │       │   │   │   ├── datetime.py
    │       │   │   │   ├── deprecation.py
    │       │   │   │   ├── direct_url_helpers.py
    │       │   │   │   ├── egg_link.py
    │       │   │   │   ├── entrypoints.py
    │       │   │   │   ├── filesystem.py
    │       │   │   │   ├── filetypes.py
    │       │   │   │   ├── glibc.py
    │       │   │   │   ├── hashes.py
    │       │   │   │   ├── logging.py
    │       │   │   │   ├── misc.py
    │       │   │   │   ├── packaging.py
    │       │   │   │   ├── retry.py
    │       │   │   │   ├── subprocess.py
    │       │   │   │   ├── temp_dir.py
    │       │   │   │   ├── unpacking.py
    │       │   │   │   ├── urls.py
    │       │   │   │   ├── virtualenv.py
    │       │   │   │   └── wheel.py
    │       │   │   ├── vcs
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── bazaar.cpython-312.pyc
    │       │   │   │   │   ├── git.cpython-312.pyc
    │       │   │   │   │   ├── mercurial.cpython-312.pyc
    │       │   │   │   │   ├── subversion.cpython-312.pyc
    │       │   │   │   │   └── versioncontrol.cpython-312.pyc
    │       │   │   │   ├── bazaar.py
    │       │   │   │   ├── git.py
    │       │   │   │   ├── mercurial.py
    │       │   │   │   ├── subversion.py
    │       │   │   │   └── versioncontrol.py
    │       │   │   └── wheel_builder.py
    │       │   ├── _vendor
    │       │   │   ├── README.rst
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   └── __init__.cpython-312.pyc
    │       │   │   ├── cachecontrol
    │       │   │   │   ├── LICENSE.txt
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _cmd.cpython-312.pyc
    │       │   │   │   │   ├── adapter.cpython-312.pyc
    │       │   │   │   │   ├── cache.cpython-312.pyc
    │       │   │   │   │   ├── controller.cpython-312.pyc
    │       │   │   │   │   ├── filewrapper.cpython-312.pyc
    │       │   │   │   │   ├── heuristics.cpython-312.pyc
    │       │   │   │   │   ├── serialize.cpython-312.pyc
    │       │   │   │   │   └── wrapper.cpython-312.pyc
    │       │   │   │   ├── _cmd.py
    │       │   │   │   ├── adapter.py
    │       │   │   │   ├── cache.py
    │       │   │   │   ├── caches
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── file_cache.cpython-312.pyc
    │       │   │   │   │   │   └── redis_cache.cpython-312.pyc
    │       │   │   │   │   ├── file_cache.py
    │       │   │   │   │   └── redis_cache.py
    │       │   │   │   ├── controller.py
    │       │   │   │   ├── filewrapper.py
    │       │   │   │   ├── heuristics.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── serialize.py
    │       │   │   │   └── wrapper.py
    │       │   │   ├── certifi
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   │   └── core.cpython-312.pyc
    │       │   │   │   ├── cacert.pem
    │       │   │   │   ├── core.py
    │       │   │   │   └── py.typed
    │       │   │   ├── dependency_groups
    │       │   │   │   ├── LICENSE.txt
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   │   ├── _implementation.cpython-312.pyc
    │       │   │   │   │   ├── _lint_dependency_groups.cpython-312.pyc
    │       │   │   │   │   ├── _pip_wrapper.cpython-312.pyc
    │       │   │   │   │   └── _toml_compat.cpython-312.pyc
    │       │   │   │   ├── _implementation.py
    │       │   │   │   ├── _lint_dependency_groups.py
    │       │   │   │   ├── _pip_wrapper.py
    │       │   │   │   ├── _toml_compat.py
    │       │   │   │   └── py.typed
    │       │   │   ├── distlib
    │       │   │   │   ├── LICENSE.txt
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── compat.cpython-312.pyc
    │       │   │   │   │   ├── resources.cpython-312.pyc
    │       │   │   │   │   ├── scripts.cpython-312.pyc
    │       │   │   │   │   └── util.cpython-312.pyc
    │       │   │   │   ├── compat.py
    │       │   │   │   ├── resources.py
    │       │   │   │   ├── scripts.py
    │       │   │   │   ├── t32.exe
    │       │   │   │   ├── t64-arm.exe
    │       │   │   │   ├── t64.exe
    │       │   │   │   ├── util.py
    │       │   │   │   ├── w32.exe
    │       │   │   │   ├── w64-arm.exe
    │       │   │   │   └── w64.exe
    │       │   │   ├── distro
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   │   └── distro.cpython-312.pyc
    │       │   │   │   ├── distro.py
    │       │   │   │   └── py.typed
    │       │   │   ├── idna
    │       │   │   │   ├── LICENSE.md
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── codec.cpython-312.pyc
    │       │   │   │   │   ├── compat.cpython-312.pyc
    │       │   │   │   │   ├── core.cpython-312.pyc
    │       │   │   │   │   ├── idnadata.cpython-312.pyc
    │       │   │   │   │   ├── intranges.cpython-312.pyc
    │       │   │   │   │   ├── package_data.cpython-312.pyc
    │       │   │   │   │   └── uts46data.cpython-312.pyc
    │       │   │   │   ├── codec.py
    │       │   │   │   ├── compat.py
    │       │   │   │   ├── core.py
    │       │   │   │   ├── idnadata.py
    │       │   │   │   ├── intranges.py
    │       │   │   │   ├── package_data.py
    │       │   │   │   ├── py.typed
    │       │   │   │   └── uts46data.py
    │       │   │   ├── msgpack
    │       │   │   │   ├── COPYING
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── exceptions.cpython-312.pyc
    │       │   │   │   │   ├── ext.cpython-312.pyc
    │       │   │   │   │   └── fallback.cpython-312.pyc
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── ext.py
    │       │   │   │   └── fallback.py
    │       │   │   ├── packaging
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── LICENSE.APACHE
    │       │   │   │   ├── LICENSE.BSD
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _elffile.cpython-312.pyc
    │       │   │   │   │   ├── _manylinux.cpython-312.pyc
    │       │   │   │   │   ├── _musllinux.cpython-312.pyc
    │       │   │   │   │   ├── _parser.cpython-312.pyc
    │       │   │   │   │   ├── _structures.cpython-312.pyc
    │       │   │   │   │   ├── _tokenizer.cpython-312.pyc
    │       │   │   │   │   ├── markers.cpython-312.pyc
    │       │   │   │   │   ├── metadata.cpython-312.pyc
    │       │   │   │   │   ├── requirements.cpython-312.pyc
    │       │   │   │   │   ├── specifiers.cpython-312.pyc
    │       │   │   │   │   ├── tags.cpython-312.pyc
    │       │   │   │   │   ├── utils.cpython-312.pyc
    │       │   │   │   │   └── version.cpython-312.pyc
    │       │   │   │   ├── _elffile.py
    │       │   │   │   ├── _manylinux.py
    │       │   │   │   ├── _musllinux.py
    │       │   │   │   ├── _parser.py
    │       │   │   │   ├── _structures.py
    │       │   │   │   ├── _tokenizer.py
    │       │   │   │   ├── licenses
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   └── _spdx.cpython-312.pyc
    │       │   │   │   │   └── _spdx.py
    │       │   │   │   ├── markers.py
    │       │   │   │   ├── metadata.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── requirements.py
    │       │   │   │   ├── specifiers.py
    │       │   │   │   ├── tags.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── version.py
    │       │   │   ├── pkg_resources
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   └── __pycache__
    │       │   │   │       └── __init__.cpython-312.pyc
    │       │   │   ├── platformdirs
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   │   ├── android.cpython-312.pyc
    │       │   │   │   │   ├── api.cpython-312.pyc
    │       │   │   │   │   ├── macos.cpython-312.pyc
    │       │   │   │   │   ├── unix.cpython-312.pyc
    │       │   │   │   │   ├── version.cpython-312.pyc
    │       │   │   │   │   └── windows.cpython-312.pyc
    │       │   │   │   ├── android.py
    │       │   │   │   ├── api.py
    │       │   │   │   ├── macos.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── unix.py
    │       │   │   │   ├── version.py
    │       │   │   │   └── windows.py
    │       │   │   ├── pygments
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   │   ├── console.cpython-312.pyc
    │       │   │   │   │   ├── filter.cpython-312.pyc
    │       │   │   │   │   ├── formatter.cpython-312.pyc
    │       │   │   │   │   ├── lexer.cpython-312.pyc
    │       │   │   │   │   ├── modeline.cpython-312.pyc
    │       │   │   │   │   ├── plugin.cpython-312.pyc
    │       │   │   │   │   ├── regexopt.cpython-312.pyc
    │       │   │   │   │   ├── scanner.cpython-312.pyc
    │       │   │   │   │   ├── sphinxext.cpython-312.pyc
    │       │   │   │   │   ├── style.cpython-312.pyc
    │       │   │   │   │   ├── token.cpython-312.pyc
    │       │   │   │   │   ├── unistring.cpython-312.pyc
    │       │   │   │   │   └── util.cpython-312.pyc
    │       │   │   │   ├── console.py
    │       │   │   │   ├── filter.py
    │       │   │   │   ├── filters
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__
    │       │   │   │   │       └── __init__.cpython-312.pyc
    │       │   │   │   ├── formatter.py
    │       │   │   │   ├── formatters
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   └── _mapping.cpython-312.pyc
    │       │   │   │   │   └── _mapping.py
    │       │   │   │   ├── lexer.py
    │       │   │   │   ├── lexers
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _mapping.cpython-312.pyc
    │       │   │   │   │   │   └── python.cpython-312.pyc
    │       │   │   │   │   ├── _mapping.py
    │       │   │   │   │   └── python.py
    │       │   │   │   ├── modeline.py
    │       │   │   │   ├── plugin.py
    │       │   │   │   ├── regexopt.py
    │       │   │   │   ├── scanner.py
    │       │   │   │   ├── sphinxext.py
    │       │   │   │   ├── style.py
    │       │   │   │   ├── styles
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   └── _mapping.cpython-312.pyc
    │       │   │   │   │   └── _mapping.py
    │       │   │   │   ├── token.py
    │       │   │   │   ├── unistring.py
    │       │   │   │   └── util.py
    │       │   │   ├── pyproject_hooks
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   └── _impl.cpython-312.pyc
    │       │   │   │   ├── _impl.py
    │       │   │   │   ├── _in_process
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   └── _in_process.cpython-312.pyc
    │       │   │   │   │   └── _in_process.py
    │       │   │   │   └── py.typed
    │       │   │   ├── requests
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── __version__.cpython-312.pyc
    │       │   │   │   │   ├── _internal_utils.cpython-312.pyc
    │       │   │   │   │   ├── adapters.cpython-312.pyc
    │       │   │   │   │   ├── api.cpython-312.pyc
    │       │   │   │   │   ├── auth.cpython-312.pyc
    │       │   │   │   │   ├── certs.cpython-312.pyc
    │       │   │   │   │   ├── compat.cpython-312.pyc
    │       │   │   │   │   ├── cookies.cpython-312.pyc
    │       │   │   │   │   ├── exceptions.cpython-312.pyc
    │       │   │   │   │   ├── help.cpython-312.pyc
    │       │   │   │   │   ├── hooks.cpython-312.pyc
    │       │   │   │   │   ├── models.cpython-312.pyc
    │       │   │   │   │   ├── packages.cpython-312.pyc
    │       │   │   │   │   ├── sessions.cpython-312.pyc
    │       │   │   │   │   ├── status_codes.cpython-312.pyc
    │       │   │   │   │   ├── structures.cpython-312.pyc
    │       │   │   │   │   └── utils.cpython-312.pyc
    │       │   │   │   ├── __version__.py
    │       │   │   │   ├── _internal_utils.py
    │       │   │   │   ├── adapters.py
    │       │   │   │   ├── api.py
    │       │   │   │   ├── auth.py
    │       │   │   │   ├── certs.py
    │       │   │   │   ├── compat.py
    │       │   │   │   ├── cookies.py
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── help.py
    │       │   │   │   ├── hooks.py
    │       │   │   │   ├── models.py
    │       │   │   │   ├── packages.py
    │       │   │   │   ├── sessions.py
    │       │   │   │   ├── status_codes.py
    │       │   │   │   ├── structures.py
    │       │   │   │   └── utils.py
    │       │   │   ├── resolvelib
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── providers.cpython-312.pyc
    │       │   │   │   │   ├── reporters.cpython-312.pyc
    │       │   │   │   │   └── structs.cpython-312.pyc
    │       │   │   │   ├── providers.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── reporters.py
    │       │   │   │   ├── resolvers
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── abstract.cpython-312.pyc
    │       │   │   │   │   │   ├── criterion.cpython-312.pyc
    │       │   │   │   │   │   ├── exceptions.cpython-312.pyc
    │       │   │   │   │   │   └── resolution.cpython-312.pyc
    │       │   │   │   │   ├── abstract.py
    │       │   │   │   │   ├── criterion.py
    │       │   │   │   │   ├── exceptions.py
    │       │   │   │   │   └── resolution.py
    │       │   │   │   └── structs.py
    │       │   │   ├── rich
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── __main__.cpython-312.pyc
    │       │   │   │   │   ├── _cell_widths.cpython-312.pyc
    │       │   │   │   │   ├── _emoji_codes.cpython-312.pyc
    │       │   │   │   │   ├── _emoji_replace.cpython-312.pyc
    │       │   │   │   │   ├── _export_format.cpython-312.pyc
    │       │   │   │   │   ├── _extension.cpython-312.pyc
    │       │   │   │   │   ├── _fileno.cpython-312.pyc
    │       │   │   │   │   ├── _inspect.cpython-312.pyc
    │       │   │   │   │   ├── _log_render.cpython-312.pyc
    │       │   │   │   │   ├── _loop.cpython-312.pyc
    │       │   │   │   │   ├── _null_file.cpython-312.pyc
    │       │   │   │   │   ├── _palettes.cpython-312.pyc
    │       │   │   │   │   ├── _pick.cpython-312.pyc
    │       │   │   │   │   ├── _ratio.cpython-312.pyc
    │       │   │   │   │   ├── _spinners.cpython-312.pyc
    │       │   │   │   │   ├── _stack.cpython-312.pyc
    │       │   │   │   │   ├── _timer.cpython-312.pyc
    │       │   │   │   │   ├── _win32_console.cpython-312.pyc
    │       │   │   │   │   ├── _windows.cpython-312.pyc
    │       │   │   │   │   ├── _windows_renderer.cpython-312.pyc
    │       │   │   │   │   ├── _wrap.cpython-312.pyc
    │       │   │   │   │   ├── abc.cpython-312.pyc
    │       │   │   │   │   ├── align.cpython-312.pyc
    │       │   │   │   │   ├── ansi.cpython-312.pyc
    │       │   │   │   │   ├── bar.cpython-312.pyc
    │       │   │   │   │   ├── box.cpython-312.pyc
    │       │   │   │   │   ├── cells.cpython-312.pyc
    │       │   │   │   │   ├── color.cpython-312.pyc
    │       │   │   │   │   ├── color_triplet.cpython-312.pyc
    │       │   │   │   │   ├── columns.cpython-312.pyc
    │       │   │   │   │   ├── console.cpython-312.pyc
    │       │   │   │   │   ├── constrain.cpython-312.pyc
    │       │   │   │   │   ├── containers.cpython-312.pyc
    │       │   │   │   │   ├── control.cpython-312.pyc
    │       │   │   │   │   ├── default_styles.cpython-312.pyc
    │       │   │   │   │   ├── diagnose.cpython-312.pyc
    │       │   │   │   │   ├── emoji.cpython-312.pyc
    │       │   │   │   │   ├── errors.cpython-312.pyc
    │       │   │   │   │   ├── file_proxy.cpython-312.pyc
    │       │   │   │   │   ├── filesize.cpython-312.pyc
    │       │   │   │   │   ├── highlighter.cpython-312.pyc
    │       │   │   │   │   ├── json.cpython-312.pyc
    │       │   │   │   │   ├── jupyter.cpython-312.pyc
    │       │   │   │   │   ├── layout.cpython-312.pyc
    │       │   │   │   │   ├── live.cpython-312.pyc
    │       │   │   │   │   ├── live_render.cpython-312.pyc
    │       │   │   │   │   ├── logging.cpython-312.pyc
    │       │   │   │   │   ├── markup.cpython-312.pyc
    │       │   │   │   │   ├── measure.cpython-312.pyc
    │       │   │   │   │   ├── padding.cpython-312.pyc
    │       │   │   │   │   ├── pager.cpython-312.pyc
    │       │   │   │   │   ├── palette.cpython-312.pyc
    │       │   │   │   │   ├── panel.cpython-312.pyc
    │       │   │   │   │   ├── pretty.cpython-312.pyc
    │       │   │   │   │   ├── progress.cpython-312.pyc
    │       │   │   │   │   ├── progress_bar.cpython-312.pyc
    │       │   │   │   │   ├── prompt.cpython-312.pyc
    │       │   │   │   │   ├── protocol.cpython-312.pyc
    │       │   │   │   │   ├── region.cpython-312.pyc
    │       │   │   │   │   ├── repr.cpython-312.pyc
    │       │   │   │   │   ├── rule.cpython-312.pyc
    │       │   │   │   │   ├── scope.cpython-312.pyc
    │       │   │   │   │   ├── screen.cpython-312.pyc
    │       │   │   │   │   ├── segment.cpython-312.pyc
    │       │   │   │   │   ├── spinner.cpython-312.pyc
    │       │   │   │   │   ├── status.cpython-312.pyc
    │       │   │   │   │   ├── style.cpython-312.pyc
    │       │   │   │   │   ├── styled.cpython-312.pyc
    │       │   │   │   │   ├── syntax.cpython-312.pyc
    │       │   │   │   │   ├── table.cpython-312.pyc
    │       │   │   │   │   ├── terminal_theme.cpython-312.pyc
    │       │   │   │   │   ├── text.cpython-312.pyc
    │       │   │   │   │   ├── theme.cpython-312.pyc
    │       │   │   │   │   ├── themes.cpython-312.pyc
    │       │   │   │   │   ├── traceback.cpython-312.pyc
    │       │   │   │   │   └── tree.cpython-312.pyc
    │       │   │   │   ├── _cell_widths.py
    │       │   │   │   ├── _emoji_codes.py
    │       │   │   │   ├── _emoji_replace.py
    │       │   │   │   ├── _export_format.py
    │       │   │   │   ├── _extension.py
    │       │   │   │   ├── _fileno.py
    │       │   │   │   ├── _inspect.py
    │       │   │   │   ├── _log_render.py
    │       │   │   │   ├── _loop.py
    │       │   │   │   ├── _null_file.py
    │       │   │   │   ├── _palettes.py
    │       │   │   │   ├── _pick.py
    │       │   │   │   ├── _ratio.py
    │       │   │   │   ├── _spinners.py
    │       │   │   │   ├── _stack.py
    │       │   │   │   ├── _timer.py
    │       │   │   │   ├── _win32_console.py
    │       │   │   │   ├── _windows.py
    │       │   │   │   ├── _windows_renderer.py
    │       │   │   │   ├── _wrap.py
    │       │   │   │   ├── abc.py
    │       │   │   │   ├── align.py
    │       │   │   │   ├── ansi.py
    │       │   │   │   ├── bar.py
    │       │   │   │   ├── box.py
    │       │   │   │   ├── cells.py
    │       │   │   │   ├── color.py
    │       │   │   │   ├── color_triplet.py
    │       │   │   │   ├── columns.py
    │       │   │   │   ├── console.py
    │       │   │   │   ├── constrain.py
    │       │   │   │   ├── containers.py
    │       │   │   │   ├── control.py
    │       │   │   │   ├── default_styles.py
    │       │   │   │   ├── diagnose.py
    │       │   │   │   ├── emoji.py
    │       │   │   │   ├── errors.py
    │       │   │   │   ├── file_proxy.py
    │       │   │   │   ├── filesize.py
    │       │   │   │   ├── highlighter.py
    │       │   │   │   ├── json.py
    │       │   │   │   ├── jupyter.py
    │       │   │   │   ├── layout.py
    │       │   │   │   ├── live.py
    │       │   │   │   ├── live_render.py
    │       │   │   │   ├── logging.py
    │       │   │   │   ├── markup.py
    │       │   │   │   ├── measure.py
    │       │   │   │   ├── padding.py
    │       │   │   │   ├── pager.py
    │       │   │   │   ├── palette.py
    │       │   │   │   ├── panel.py
    │       │   │   │   ├── pretty.py
    │       │   │   │   ├── progress.py
    │       │   │   │   ├── progress_bar.py
    │       │   │   │   ├── prompt.py
    │       │   │   │   ├── protocol.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── region.py
    │       │   │   │   ├── repr.py
    │       │   │   │   ├── rule.py
    │       │   │   │   ├── scope.py
    │       │   │   │   ├── screen.py
    │       │   │   │   ├── segment.py
    │       │   │   │   ├── spinner.py
    │       │   │   │   ├── status.py
    │       │   │   │   ├── style.py
    │       │   │   │   ├── styled.py
    │       │   │   │   ├── syntax.py
    │       │   │   │   ├── table.py
    │       │   │   │   ├── terminal_theme.py
    │       │   │   │   ├── text.py
    │       │   │   │   ├── theme.py
    │       │   │   │   ├── themes.py
    │       │   │   │   ├── traceback.py
    │       │   │   │   └── tree.py
    │       │   │   ├── tomli
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _parser.cpython-312.pyc
    │       │   │   │   │   ├── _re.cpython-312.pyc
    │       │   │   │   │   └── _types.cpython-312.pyc
    │       │   │   │   ├── _parser.py
    │       │   │   │   ├── _re.py
    │       │   │   │   ├── _types.py
    │       │   │   │   └── py.typed
    │       │   │   ├── tomli_w
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   └── _writer.cpython-312.pyc
    │       │   │   │   ├── _writer.py
    │       │   │   │   └── py.typed
    │       │   │   ├── truststore
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _api.cpython-312.pyc
    │       │   │   │   │   ├── _macos.cpython-312.pyc
    │       │   │   │   │   ├── _openssl.cpython-312.pyc
    │       │   │   │   │   ├── _ssl_constants.cpython-312.pyc
    │       │   │   │   │   └── _windows.cpython-312.pyc
    │       │   │   │   ├── _api.py
    │       │   │   │   ├── _macos.py
    │       │   │   │   ├── _openssl.py
    │       │   │   │   ├── _ssl_constants.py
    │       │   │   │   ├── _windows.py
    │       │   │   │   └── py.typed
    │       │   │   ├── urllib3
    │       │   │   │   ├── LICENSE.txt
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _collections.cpython-312.pyc
    │       │   │   │   │   ├── _version.cpython-312.pyc
    │       │   │   │   │   ├── connection.cpython-312.pyc
    │       │   │   │   │   ├── connectionpool.cpython-312.pyc
    │       │   │   │   │   ├── exceptions.cpython-312.pyc
    │       │   │   │   │   ├── fields.cpython-312.pyc
    │       │   │   │   │   ├── filepost.cpython-312.pyc
    │       │   │   │   │   ├── poolmanager.cpython-312.pyc
    │       │   │   │   │   ├── request.cpython-312.pyc
    │       │   │   │   │   └── response.cpython-312.pyc
    │       │   │   │   ├── _collections.py
    │       │   │   │   ├── _version.py
    │       │   │   │   ├── connection.py
    │       │   │   │   ├── connectionpool.py
    │       │   │   │   ├── contrib
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _appengine_environ.cpython-312.pyc
    │       │   │   │   │   │   ├── appengine.cpython-312.pyc
    │       │   │   │   │   │   ├── ntlmpool.cpython-312.pyc
    │       │   │   │   │   │   ├── pyopenssl.cpython-312.pyc
    │       │   │   │   │   │   ├── securetransport.cpython-312.pyc
    │       │   │   │   │   │   └── socks.cpython-312.pyc
    │       │   │   │   │   ├── _appengine_environ.py
    │       │   │   │   │   ├── _securetransport
    │       │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   │   ├── bindings.cpython-312.pyc
    │       │   │   │   │   │   │   └── low_level.cpython-312.pyc
    │       │   │   │   │   │   ├── bindings.py
    │       │   │   │   │   │   └── low_level.py
    │       │   │   │   │   ├── appengine.py
    │       │   │   │   │   ├── ntlmpool.py
    │       │   │   │   │   ├── pyopenssl.py
    │       │   │   │   │   ├── securetransport.py
    │       │   │   │   │   └── socks.py
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── fields.py
    │       │   │   │   ├── filepost.py
    │       │   │   │   ├── packages
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   └── six.cpython-312.pyc
    │       │   │   │   │   ├── backports
    │       │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   │   ├── makefile.cpython-312.pyc
    │       │   │   │   │   │   │   └── weakref_finalize.cpython-312.pyc
    │       │   │   │   │   │   ├── makefile.py
    │       │   │   │   │   │   └── weakref_finalize.py
    │       │   │   │   │   └── six.py
    │       │   │   │   ├── poolmanager.py
    │       │   │   │   ├── request.py
    │       │   │   │   ├── response.py
    │       │   │   │   └── util
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── connection.cpython-312.pyc
    │       │   │   │       │   ├── proxy.cpython-312.pyc
    │       │   │   │       │   ├── queue.cpython-312.pyc
    │       │   │   │       │   ├── request.cpython-312.pyc
    │       │   │   │       │   ├── response.cpython-312.pyc
    │       │   │   │       │   ├── retry.cpython-312.pyc
    │       │   │   │       │   ├── ssl_.cpython-312.pyc
    │       │   │   │       │   ├── ssl_match_hostname.cpython-312.pyc
    │       │   │   │       │   ├── ssltransport.cpython-312.pyc
    │       │   │   │       │   ├── timeout.cpython-312.pyc
    │       │   │   │       │   ├── url.cpython-312.pyc
    │       │   │   │       │   └── wait.cpython-312.pyc
    │       │   │   │       ├── connection.py
    │       │   │   │       ├── proxy.py
    │       │   │   │       ├── queue.py
    │       │   │   │       ├── request.py
    │       │   │   │       ├── response.py
    │       │   │   │       ├── retry.py
    │       │   │   │       ├── ssl_.py
    │       │   │   │       ├── ssl_match_hostname.py
    │       │   │   │       ├── ssltransport.py
    │       │   │   │       ├── timeout.py
    │       │   │   │       ├── url.py
    │       │   │   │       └── wait.py
    │       │   │   └── vendor.txt
    │       │   └── py.typed
    │       ├── pip-25.3.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── licenses
    │       │       ├── AUTHORS.txt
    │       │       ├── LICENSE.txt
    │       │       └── src
    │       │           └── pip
    │       │               └── _vendor
    │       │                   ├── cachecontrol
    │       │                   │   └── LICENSE.txt
    │       │                   ├── certifi
    │       │                   │   └── LICENSE
    │       │                   ├── dependency_groups
    │       │                   │   └── LICENSE.txt
    │       │                   ├── distlib
    │       │                   │   └── LICENSE.txt
    │       │                   ├── distro
    │       │                   │   └── LICENSE
    │       │                   ├── idna
    │       │                   │   └── LICENSE.md
    │       │                   ├── msgpack
    │       │                   │   └── COPYING
    │       │                   ├── packaging
    │       │                   │   ├── LICENSE
    │       │                   │   ├── LICENSE.APACHE
    │       │                   │   └── LICENSE.BSD
    │       │                   ├── pkg_resources
    │       │                   │   └── LICENSE
    │       │                   ├── platformdirs
    │       │                   │   └── LICENSE
    │       │                   ├── pygments
    │       │                   │   └── LICENSE
    │       │                   ├── pyproject_hooks
    │       │                   │   └── LICENSE
    │       │                   ├── requests
    │       │                   │   └── LICENSE
    │       │                   ├── resolvelib
    │       │                   │   └── LICENSE
    │       │                   ├── rich
    │       │                   │   └── LICENSE
    │       │                   ├── tomli
    │       │                   │   └── LICENSE
    │       │                   ├── tomli_w
    │       │                   │   └── LICENSE
    │       │                   ├── truststore
    │       │                   │   └── LICENSE
    │       │                   └── urllib3
    │       │                       └── LICENSE.txt
    │       ├── pluggy
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── _callers.cpython-312.pyc
    │       │   │   ├── _hooks.cpython-312.pyc
    │       │   │   ├── _manager.cpython-312.pyc
    │       │   │   ├── _result.cpython-312.pyc
    │       │   │   ├── _tracing.cpython-312.pyc
    │       │   │   ├── _version.cpython-312.pyc
    │       │   │   └── _warnings.cpython-312.pyc
    │       │   ├── _callers.py
    │       │   ├── _hooks.py
    │       │   ├── _manager.py
    │       │   ├── _result.py
    │       │   ├── _tracing.py
    │       │   ├── _version.py
    │       │   ├── _warnings.py
    │       │   └── py.typed
    │       ├── pluggy-1.6.0.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   ├── licenses
    │       │   │   └── LICENSE
    │       │   └── top_level.txt
    │       ├── py.py
    │       ├── pygments
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── __main__.cpython-312.pyc
    │       │   │   ├── cmdline.cpython-312.pyc
    │       │   │   ├── console.cpython-312.pyc
    │       │   │   ├── filter.cpython-312.pyc
    │       │   │   ├── formatter.cpython-312.pyc
    │       │   │   ├── lexer.cpython-312.pyc
    │       │   │   ├── modeline.cpython-312.pyc
    │       │   │   ├── plugin.cpython-312.pyc
    │       │   │   ├── regexopt.cpython-312.pyc
    │       │   │   ├── scanner.cpython-312.pyc
    │       │   │   ├── sphinxext.cpython-312.pyc
    │       │   │   ├── style.cpython-312.pyc
    │       │   │   ├── token.cpython-312.pyc
    │       │   │   ├── unistring.cpython-312.pyc
    │       │   │   └── util.cpython-312.pyc
    │       │   ├── cmdline.py
    │       │   ├── console.py
    │       │   ├── filter.py
    │       │   ├── filters
    │       │   │   ├── __init__.py
    │       │   │   └── __pycache__
    │       │   │       └── __init__.cpython-312.pyc
    │       │   ├── formatter.py
    │       │   ├── formatters
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _mapping.cpython-312.pyc
    │       │   │   │   ├── bbcode.cpython-312.pyc
    │       │   │   │   ├── groff.cpython-312.pyc
    │       │   │   │   ├── html.cpython-312.pyc
    │       │   │   │   ├── img.cpython-312.pyc
    │       │   │   │   ├── irc.cpython-312.pyc
    │       │   │   │   ├── latex.cpython-312.pyc
    │       │   │   │   ├── other.cpython-312.pyc
    │       │   │   │   ├── pangomarkup.cpython-312.pyc
    │       │   │   │   ├── rtf.cpython-312.pyc
    │       │   │   │   ├── svg.cpython-312.pyc
    │       │   │   │   ├── terminal.cpython-312.pyc
    │       │   │   │   └── terminal256.cpython-312.pyc
    │       │   │   ├── _mapping.py
    │       │   │   ├── bbcode.py
    │       │   │   ├── groff.py
    │       │   │   ├── html.py
    │       │   │   ├── img.py
    │       │   │   ├── irc.py
    │       │   │   ├── latex.py
    │       │   │   ├── other.py
    │       │   │   ├── pangomarkup.py
    │       │   │   ├── rtf.py
    │       │   │   ├── svg.py
    │       │   │   ├── terminal.py
    │       │   │   └── terminal256.py
    │       │   ├── lexer.py
    │       │   ├── lexers
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _ada_builtins.cpython-312.pyc
    │       │   │   │   ├── _asy_builtins.cpython-312.pyc
    │       │   │   │   ├── _cl_builtins.cpython-312.pyc
    │       │   │   │   ├── _cocoa_builtins.cpython-312.pyc
    │       │   │   │   ├── _csound_builtins.cpython-312.pyc
    │       │   │   │   ├── _css_builtins.cpython-312.pyc
    │       │   │   │   ├── _googlesql_builtins.cpython-312.pyc
    │       │   │   │   ├── _julia_builtins.cpython-312.pyc
    │       │   │   │   ├── _lasso_builtins.cpython-312.pyc
    │       │   │   │   ├── _lilypond_builtins.cpython-312.pyc
    │       │   │   │   ├── _lua_builtins.cpython-312.pyc
    │       │   │   │   ├── _luau_builtins.cpython-312.pyc
    │       │   │   │   ├── _mapping.cpython-312.pyc
    │       │   │   │   ├── _mql_builtins.cpython-312.pyc
    │       │   │   │   ├── _mysql_builtins.cpython-312.pyc
    │       │   │   │   ├── _openedge_builtins.cpython-312.pyc
    │       │   │   │   ├── _php_builtins.cpython-312.pyc
    │       │   │   │   ├── _postgres_builtins.cpython-312.pyc
    │       │   │   │   ├── _qlik_builtins.cpython-312.pyc
    │       │   │   │   ├── _scheme_builtins.cpython-312.pyc
    │       │   │   │   ├── _scilab_builtins.cpython-312.pyc
    │       │   │   │   ├── _sourcemod_builtins.cpython-312.pyc
    │       │   │   │   ├── _sql_builtins.cpython-312.pyc
    │       │   │   │   ├── _stan_builtins.cpython-312.pyc
    │       │   │   │   ├── _stata_builtins.cpython-312.pyc
    │       │   │   │   ├── _tsql_builtins.cpython-312.pyc
    │       │   │   │   ├── _usd_builtins.cpython-312.pyc
    │       │   │   │   ├── _vbscript_builtins.cpython-312.pyc
    │       │   │   │   ├── _vim_builtins.cpython-312.pyc
    │       │   │   │   ├── actionscript.cpython-312.pyc
    │       │   │   │   ├── ada.cpython-312.pyc
    │       │   │   │   ├── agile.cpython-312.pyc
    │       │   │   │   ├── algebra.cpython-312.pyc
    │       │   │   │   ├── ambient.cpython-312.pyc
    │       │   │   │   ├── amdgpu.cpython-312.pyc
    │       │   │   │   ├── ampl.cpython-312.pyc
    │       │   │   │   ├── apdlexer.cpython-312.pyc
    │       │   │   │   ├── apl.cpython-312.pyc
    │       │   │   │   ├── archetype.cpython-312.pyc
    │       │   │   │   ├── arrow.cpython-312.pyc
    │       │   │   │   ├── arturo.cpython-312.pyc
    │       │   │   │   ├── asc.cpython-312.pyc
    │       │   │   │   ├── asm.cpython-312.pyc
    │       │   │   │   ├── asn1.cpython-312.pyc
    │       │   │   │   ├── automation.cpython-312.pyc
    │       │   │   │   ├── bare.cpython-312.pyc
    │       │   │   │   ├── basic.cpython-312.pyc
    │       │   │   │   ├── bdd.cpython-312.pyc
    │       │   │   │   ├── berry.cpython-312.pyc
    │       │   │   │   ├── bibtex.cpython-312.pyc
    │       │   │   │   ├── blueprint.cpython-312.pyc
    │       │   │   │   ├── boa.cpython-312.pyc
    │       │   │   │   ├── bqn.cpython-312.pyc
    │       │   │   │   ├── business.cpython-312.pyc
    │       │   │   │   ├── c_cpp.cpython-312.pyc
    │       │   │   │   ├── c_like.cpython-312.pyc
    │       │   │   │   ├── capnproto.cpython-312.pyc
    │       │   │   │   ├── carbon.cpython-312.pyc
    │       │   │   │   ├── cddl.cpython-312.pyc
    │       │   │   │   ├── chapel.cpython-312.pyc
    │       │   │   │   ├── clean.cpython-312.pyc
    │       │   │   │   ├── codeql.cpython-312.pyc
    │       │   │   │   ├── comal.cpython-312.pyc
    │       │   │   │   ├── compiled.cpython-312.pyc
    │       │   │   │   ├── configs.cpython-312.pyc
    │       │   │   │   ├── console.cpython-312.pyc
    │       │   │   │   ├── cplint.cpython-312.pyc
    │       │   │   │   ├── crystal.cpython-312.pyc
    │       │   │   │   ├── csound.cpython-312.pyc
    │       │   │   │   ├── css.cpython-312.pyc
    │       │   │   │   ├── d.cpython-312.pyc
    │       │   │   │   ├── dalvik.cpython-312.pyc
    │       │   │   │   ├── data.cpython-312.pyc
    │       │   │   │   ├── dax.cpython-312.pyc
    │       │   │   │   ├── devicetree.cpython-312.pyc
    │       │   │   │   ├── diff.cpython-312.pyc
    │       │   │   │   ├── dns.cpython-312.pyc
    │       │   │   │   ├── dotnet.cpython-312.pyc
    │       │   │   │   ├── dsls.cpython-312.pyc
    │       │   │   │   ├── dylan.cpython-312.pyc
    │       │   │   │   ├── ecl.cpython-312.pyc
    │       │   │   │   ├── eiffel.cpython-312.pyc
    │       │   │   │   ├── elm.cpython-312.pyc
    │       │   │   │   ├── elpi.cpython-312.pyc
    │       │   │   │   ├── email.cpython-312.pyc
    │       │   │   │   ├── erlang.cpython-312.pyc
    │       │   │   │   ├── esoteric.cpython-312.pyc
    │       │   │   │   ├── ezhil.cpython-312.pyc
    │       │   │   │   ├── factor.cpython-312.pyc
    │       │   │   │   ├── fantom.cpython-312.pyc
    │       │   │   │   ├── felix.cpython-312.pyc
    │       │   │   │   ├── fift.cpython-312.pyc
    │       │   │   │   ├── floscript.cpython-312.pyc
    │       │   │   │   ├── forth.cpython-312.pyc
    │       │   │   │   ├── fortran.cpython-312.pyc
    │       │   │   │   ├── foxpro.cpython-312.pyc
    │       │   │   │   ├── freefem.cpython-312.pyc
    │       │   │   │   ├── func.cpython-312.pyc
    │       │   │   │   ├── functional.cpython-312.pyc
    │       │   │   │   ├── futhark.cpython-312.pyc
    │       │   │   │   ├── gcodelexer.cpython-312.pyc
    │       │   │   │   ├── gdscript.cpython-312.pyc
    │       │   │   │   ├── gleam.cpython-312.pyc
    │       │   │   │   ├── go.cpython-312.pyc
    │       │   │   │   ├── grammar_notation.cpython-312.pyc
    │       │   │   │   ├── graph.cpython-312.pyc
    │       │   │   │   ├── graphics.cpython-312.pyc
    │       │   │   │   ├── graphql.cpython-312.pyc
    │       │   │   │   ├── graphviz.cpython-312.pyc
    │       │   │   │   ├── gsql.cpython-312.pyc
    │       │   │   │   ├── hare.cpython-312.pyc
    │       │   │   │   ├── haskell.cpython-312.pyc
    │       │   │   │   ├── haxe.cpython-312.pyc
    │       │   │   │   ├── hdl.cpython-312.pyc
    │       │   │   │   ├── hexdump.cpython-312.pyc
    │       │   │   │   ├── html.cpython-312.pyc
    │       │   │   │   ├── idl.cpython-312.pyc
    │       │   │   │   ├── igor.cpython-312.pyc
    │       │   │   │   ├── inferno.cpython-312.pyc
    │       │   │   │   ├── installers.cpython-312.pyc
    │       │   │   │   ├── int_fiction.cpython-312.pyc
    │       │   │   │   ├── iolang.cpython-312.pyc
    │       │   │   │   ├── j.cpython-312.pyc
    │       │   │   │   ├── javascript.cpython-312.pyc
    │       │   │   │   ├── jmespath.cpython-312.pyc
    │       │   │   │   ├── jslt.cpython-312.pyc
    │       │   │   │   ├── json5.cpython-312.pyc
    │       │   │   │   ├── jsonnet.cpython-312.pyc
    │       │   │   │   ├── jsx.cpython-312.pyc
    │       │   │   │   ├── julia.cpython-312.pyc
    │       │   │   │   ├── jvm.cpython-312.pyc
    │       │   │   │   ├── kuin.cpython-312.pyc
    │       │   │   │   ├── kusto.cpython-312.pyc
    │       │   │   │   ├── ldap.cpython-312.pyc
    │       │   │   │   ├── lean.cpython-312.pyc
    │       │   │   │   ├── lilypond.cpython-312.pyc
    │       │   │   │   ├── lisp.cpython-312.pyc
    │       │   │   │   ├── macaulay2.cpython-312.pyc
    │       │   │   │   ├── make.cpython-312.pyc
    │       │   │   │   ├── maple.cpython-312.pyc
    │       │   │   │   ├── markup.cpython-312.pyc
    │       │   │   │   ├── math.cpython-312.pyc
    │       │   │   │   ├── matlab.cpython-312.pyc
    │       │   │   │   ├── maxima.cpython-312.pyc
    │       │   │   │   ├── meson.cpython-312.pyc
    │       │   │   │   ├── mime.cpython-312.pyc
    │       │   │   │   ├── minecraft.cpython-312.pyc
    │       │   │   │   ├── mips.cpython-312.pyc
    │       │   │   │   ├── ml.cpython-312.pyc
    │       │   │   │   ├── modeling.cpython-312.pyc
    │       │   │   │   ├── modula2.cpython-312.pyc
    │       │   │   │   ├── mojo.cpython-312.pyc
    │       │   │   │   ├── monte.cpython-312.pyc
    │       │   │   │   ├── mosel.cpython-312.pyc
    │       │   │   │   ├── ncl.cpython-312.pyc
    │       │   │   │   ├── nimrod.cpython-312.pyc
    │       │   │   │   ├── nit.cpython-312.pyc
    │       │   │   │   ├── nix.cpython-312.pyc
    │       │   │   │   ├── numbair.cpython-312.pyc
    │       │   │   │   ├── oberon.cpython-312.pyc
    │       │   │   │   ├── objective.cpython-312.pyc
    │       │   │   │   ├── ooc.cpython-312.pyc
    │       │   │   │   ├── openscad.cpython-312.pyc
    │       │   │   │   ├── other.cpython-312.pyc
    │       │   │   │   ├── parasail.cpython-312.pyc
    │       │   │   │   ├── parsers.cpython-312.pyc
    │       │   │   │   ├── pascal.cpython-312.pyc
    │       │   │   │   ├── pawn.cpython-312.pyc
    │       │   │   │   ├── pddl.cpython-312.pyc
    │       │   │   │   ├── perl.cpython-312.pyc
    │       │   │   │   ├── phix.cpython-312.pyc
    │       │   │   │   ├── php.cpython-312.pyc
    │       │   │   │   ├── pointless.cpython-312.pyc
    │       │   │   │   ├── pony.cpython-312.pyc
    │       │   │   │   ├── praat.cpython-312.pyc
    │       │   │   │   ├── procfile.cpython-312.pyc
    │       │   │   │   ├── prolog.cpython-312.pyc
    │       │   │   │   ├── promql.cpython-312.pyc
    │       │   │   │   ├── prql.cpython-312.pyc
    │       │   │   │   ├── ptx.cpython-312.pyc
    │       │   │   │   ├── python.cpython-312.pyc
    │       │   │   │   ├── q.cpython-312.pyc
    │       │   │   │   ├── qlik.cpython-312.pyc
    │       │   │   │   ├── qvt.cpython-312.pyc
    │       │   │   │   ├── r.cpython-312.pyc
    │       │   │   │   ├── rdf.cpython-312.pyc
    │       │   │   │   ├── rebol.cpython-312.pyc
    │       │   │   │   ├── rego.cpython-312.pyc
    │       │   │   │   ├── resource.cpython-312.pyc
    │       │   │   │   ├── ride.cpython-312.pyc
    │       │   │   │   ├── rita.cpython-312.pyc
    │       │   │   │   ├── rnc.cpython-312.pyc
    │       │   │   │   ├── roboconf.cpython-312.pyc
    │       │   │   │   ├── robotframework.cpython-312.pyc
    │       │   │   │   ├── ruby.cpython-312.pyc
    │       │   │   │   ├── rust.cpython-312.pyc
    │       │   │   │   ├── sas.cpython-312.pyc
    │       │   │   │   ├── savi.cpython-312.pyc
    │       │   │   │   ├── scdoc.cpython-312.pyc
    │       │   │   │   ├── scripting.cpython-312.pyc
    │       │   │   │   ├── sgf.cpython-312.pyc
    │       │   │   │   ├── shell.cpython-312.pyc
    │       │   │   │   ├── sieve.cpython-312.pyc
    │       │   │   │   ├── slash.cpython-312.pyc
    │       │   │   │   ├── smalltalk.cpython-312.pyc
    │       │   │   │   ├── smithy.cpython-312.pyc
    │       │   │   │   ├── smv.cpython-312.pyc
    │       │   │   │   ├── snobol.cpython-312.pyc
    │       │   │   │   ├── solidity.cpython-312.pyc
    │       │   │   │   ├── soong.cpython-312.pyc
    │       │   │   │   ├── sophia.cpython-312.pyc
    │       │   │   │   ├── special.cpython-312.pyc
    │       │   │   │   ├── spice.cpython-312.pyc
    │       │   │   │   ├── sql.cpython-312.pyc
    │       │   │   │   ├── srcinfo.cpython-312.pyc
    │       │   │   │   ├── stata.cpython-312.pyc
    │       │   │   │   ├── supercollider.cpython-312.pyc
    │       │   │   │   ├── tablegen.cpython-312.pyc
    │       │   │   │   ├── tact.cpython-312.pyc
    │       │   │   │   ├── tal.cpython-312.pyc
    │       │   │   │   ├── tcl.cpython-312.pyc
    │       │   │   │   ├── teal.cpython-312.pyc
    │       │   │   │   ├── templates.cpython-312.pyc
    │       │   │   │   ├── teraterm.cpython-312.pyc
    │       │   │   │   ├── testing.cpython-312.pyc
    │       │   │   │   ├── text.cpython-312.pyc
    │       │   │   │   ├── textedit.cpython-312.pyc
    │       │   │   │   ├── textfmts.cpython-312.pyc
    │       │   │   │   ├── theorem.cpython-312.pyc
    │       │   │   │   ├── thingsdb.cpython-312.pyc
    │       │   │   │   ├── tlb.cpython-312.pyc
    │       │   │   │   ├── tls.cpython-312.pyc
    │       │   │   │   ├── tnt.cpython-312.pyc
    │       │   │   │   ├── trafficscript.cpython-312.pyc
    │       │   │   │   ├── typoscript.cpython-312.pyc
    │       │   │   │   ├── typst.cpython-312.pyc
    │       │   │   │   ├── ul4.cpython-312.pyc
    │       │   │   │   ├── unicon.cpython-312.pyc
    │       │   │   │   ├── urbi.cpython-312.pyc
    │       │   │   │   ├── usd.cpython-312.pyc
    │       │   │   │   ├── varnish.cpython-312.pyc
    │       │   │   │   ├── verification.cpython-312.pyc
    │       │   │   │   ├── verifpal.cpython-312.pyc
    │       │   │   │   ├── vip.cpython-312.pyc
    │       │   │   │   ├── vyper.cpython-312.pyc
    │       │   │   │   ├── web.cpython-312.pyc
    │       │   │   │   ├── webassembly.cpython-312.pyc
    │       │   │   │   ├── webidl.cpython-312.pyc
    │       │   │   │   ├── webmisc.cpython-312.pyc
    │       │   │   │   ├── wgsl.cpython-312.pyc
    │       │   │   │   ├── whiley.cpython-312.pyc
    │       │   │   │   ├── wowtoc.cpython-312.pyc
    │       │   │   │   ├── wren.cpython-312.pyc
    │       │   │   │   ├── x10.cpython-312.pyc
    │       │   │   │   ├── xorg.cpython-312.pyc
    │       │   │   │   ├── yang.cpython-312.pyc
    │       │   │   │   ├── yara.cpython-312.pyc
    │       │   │   │   └── zig.cpython-312.pyc
    │       │   │   ├── _ada_builtins.py
    │       │   │   ├── _asy_builtins.py
    │       │   │   ├── _cl_builtins.py
    │       │   │   ├── _cocoa_builtins.py
    │       │   │   ├── _csound_builtins.py
    │       │   │   ├── _css_builtins.py
    │       │   │   ├── _googlesql_builtins.py
    │       │   │   ├── _julia_builtins.py
    │       │   │   ├── _lasso_builtins.py
    │       │   │   ├── _lilypond_builtins.py
    │       │   │   ├── _lua_builtins.py
    │       │   │   ├── _luau_builtins.py
    │       │   │   ├── _mapping.py
    │       │   │   ├── _mql_builtins.py
    │       │   │   ├── _mysql_builtins.py
    │       │   │   ├── _openedge_builtins.py
    │       │   │   ├── _php_builtins.py
    │       │   │   ├── _postgres_builtins.py
    │       │   │   ├── _qlik_builtins.py
    │       │   │   ├── _scheme_builtins.py
    │       │   │   ├── _scilab_builtins.py
    │       │   │   ├── _sourcemod_builtins.py
    │       │   │   ├── _sql_builtins.py
    │       │   │   ├── _stan_builtins.py
    │       │   │   ├── _stata_builtins.py
    │       │   │   ├── _tsql_builtins.py
    │       │   │   ├── _usd_builtins.py
    │       │   │   ├── _vbscript_builtins.py
    │       │   │   ├── _vim_builtins.py
    │       │   │   ├── actionscript.py
    │       │   │   ├── ada.py
    │       │   │   ├── agile.py
    │       │   │   ├── algebra.py
    │       │   │   ├── ambient.py
    │       │   │   ├── amdgpu.py
    │       │   │   ├── ampl.py
    │       │   │   ├── apdlexer.py
    │       │   │   ├── apl.py
    │       │   │   ├── archetype.py
    │       │   │   ├── arrow.py
    │       │   │   ├── arturo.py
    │       │   │   ├── asc.py
    │       │   │   ├── asm.py
    │       │   │   ├── asn1.py
    │       │   │   ├── automation.py
    │       │   │   ├── bare.py
    │       │   │   ├── basic.py
    │       │   │   ├── bdd.py
    │       │   │   ├── berry.py
    │       │   │   ├── bibtex.py
    │       │   │   ├── blueprint.py
    │       │   │   ├── boa.py
    │       │   │   ├── bqn.py
    │       │   │   ├── business.py
    │       │   │   ├── c_cpp.py
    │       │   │   ├── c_like.py
    │       │   │   ├── capnproto.py
    │       │   │   ├── carbon.py
    │       │   │   ├── cddl.py
    │       │   │   ├── chapel.py
    │       │   │   ├── clean.py
    │       │   │   ├── codeql.py
    │       │   │   ├── comal.py
    │       │   │   ├── compiled.py
    │       │   │   ├── configs.py
    │       │   │   ├── console.py
    │       │   │   ├── cplint.py
    │       │   │   ├── crystal.py
    │       │   │   ├── csound.py
    │       │   │   ├── css.py
    │       │   │   ├── d.py
    │       │   │   ├── dalvik.py
    │       │   │   ├── data.py
    │       │   │   ├── dax.py
    │       │   │   ├── devicetree.py
    │       │   │   ├── diff.py
    │       │   │   ├── dns.py
    │       │   │   ├── dotnet.py
    │       │   │   ├── dsls.py
    │       │   │   ├── dylan.py
    │       │   │   ├── ecl.py
    │       │   │   ├── eiffel.py
    │       │   │   ├── elm.py
    │       │   │   ├── elpi.py
    │       │   │   ├── email.py
    │       │   │   ├── erlang.py
    │       │   │   ├── esoteric.py
    │       │   │   ├── ezhil.py
    │       │   │   ├── factor.py
    │       │   │   ├── fantom.py
    │       │   │   ├── felix.py
    │       │   │   ├── fift.py
    │       │   │   ├── floscript.py
    │       │   │   ├── forth.py
    │       │   │   ├── fortran.py
    │       │   │   ├── foxpro.py
    │       │   │   ├── freefem.py
    │       │   │   ├── func.py
    │       │   │   ├── functional.py
    │       │   │   ├── futhark.py
    │       │   │   ├── gcodelexer.py
    │       │   │   ├── gdscript.py
    │       │   │   ├── gleam.py
    │       │   │   ├── go.py
    │       │   │   ├── grammar_notation.py
    │       │   │   ├── graph.py
    │       │   │   ├── graphics.py
    │       │   │   ├── graphql.py
    │       │   │   ├── graphviz.py
    │       │   │   ├── gsql.py
    │       │   │   ├── hare.py
    │       │   │   ├── haskell.py
    │       │   │   ├── haxe.py
    │       │   │   ├── hdl.py
    │       │   │   ├── hexdump.py
    │       │   │   ├── html.py
    │       │   │   ├── idl.py
    │       │   │   ├── igor.py
    │       │   │   ├── inferno.py
    │       │   │   ├── installers.py
    │       │   │   ├── int_fiction.py
    │       │   │   ├── iolang.py
    │       │   │   ├── j.py
    │       │   │   ├── javascript.py
    │       │   │   ├── jmespath.py
    │       │   │   ├── jslt.py
    │       │   │   ├── json5.py
    │       │   │   ├── jsonnet.py
    │       │   │   ├── jsx.py
    │       │   │   ├── julia.py
    │       │   │   ├── jvm.py
    │       │   │   ├── kuin.py
    │       │   │   ├── kusto.py
    │       │   │   ├── ldap.py
    │       │   │   ├── lean.py
    │       │   │   ├── lilypond.py
    │       │   │   ├── lisp.py
    │       │   │   ├── macaulay2.py
    │       │   │   ├── make.py
    │       │   │   ├── maple.py
    │       │   │   ├── markup.py
    │       │   │   ├── math.py
    │       │   │   ├── matlab.py
    │       │   │   ├── maxima.py
    │       │   │   ├── meson.py
    │       │   │   ├── mime.py
    │       │   │   ├── minecraft.py
    │       │   │   ├── mips.py
    │       │   │   ├── ml.py
    │       │   │   ├── modeling.py
    │       │   │   ├── modula2.py
    │       │   │   ├── mojo.py
    │       │   │   ├── monte.py
    │       │   │   ├── mosel.py
    │       │   │   ├── ncl.py
    │       │   │   ├── nimrod.py
    │       │   │   ├── nit.py
    │       │   │   ├── nix.py
    │       │   │   ├── numbair.py
    │       │   │   ├── oberon.py
    │       │   │   ├── objective.py
    │       │   │   ├── ooc.py
    │       │   │   ├── openscad.py
    │       │   │   ├── other.py
    │       │   │   ├── parasail.py
    │       │   │   ├── parsers.py
    │       │   │   ├── pascal.py
    │       │   │   ├── pawn.py
    │       │   │   ├── pddl.py
    │       │   │   ├── perl.py
    │       │   │   ├── phix.py
    │       │   │   ├── php.py
    │       │   │   ├── pointless.py
    │       │   │   ├── pony.py
    │       │   │   ├── praat.py
    │       │   │   ├── procfile.py
    │       │   │   ├── prolog.py
    │       │   │   ├── promql.py
    │       │   │   ├── prql.py
    │       │   │   ├── ptx.py
    │       │   │   ├── python.py
    │       │   │   ├── q.py
    │       │   │   ├── qlik.py
    │       │   │   ├── qvt.py
    │       │   │   ├── r.py
    │       │   │   ├── rdf.py
    │       │   │   ├── rebol.py
    │       │   │   ├── rego.py
    │       │   │   ├── resource.py
    │       │   │   ├── ride.py
    │       │   │   ├── rita.py
    │       │   │   ├── rnc.py
    │       │   │   ├── roboconf.py
    │       │   │   ├── robotframework.py
    │       │   │   ├── ruby.py
    │       │   │   ├── rust.py
    │       │   │   ├── sas.py
    │       │   │   ├── savi.py
    │       │   │   ├── scdoc.py
    │       │   │   ├── scripting.py
    │       │   │   ├── sgf.py
    │       │   │   ├── shell.py
    │       │   │   ├── sieve.py
    │       │   │   ├── slash.py
    │       │   │   ├── smalltalk.py
    │       │   │   ├── smithy.py
    │       │   │   ├── smv.py
    │       │   │   ├── snobol.py
    │       │   │   ├── solidity.py
    │       │   │   ├── soong.py
    │       │   │   ├── sophia.py
    │       │   │   ├── special.py
    │       │   │   ├── spice.py
    │       │   │   ├── sql.py
    │       │   │   ├── srcinfo.py
    │       │   │   ├── stata.py
    │       │   │   ├── supercollider.py
    │       │   │   ├── tablegen.py
    │       │   │   ├── tact.py
    │       │   │   ├── tal.py
    │       │   │   ├── tcl.py
    │       │   │   ├── teal.py
    │       │   │   ├── templates.py
    │       │   │   ├── teraterm.py
    │       │   │   ├── testing.py
    │       │   │   ├── text.py
    │       │   │   ├── textedit.py
    │       │   │   ├── textfmts.py
    │       │   │   ├── theorem.py
    │       │   │   ├── thingsdb.py
    │       │   │   ├── tlb.py
    │       │   │   ├── tls.py
    │       │   │   ├── tnt.py
    │       │   │   ├── trafficscript.py
    │       │   │   ├── typoscript.py
    │       │   │   ├── typst.py
    │       │   │   ├── ul4.py
    │       │   │   ├── unicon.py
    │       │   │   ├── urbi.py
    │       │   │   ├── usd.py
    │       │   │   ├── varnish.py
    │       │   │   ├── verification.py
    │       │   │   ├── verifpal.py
    │       │   │   ├── vip.py
    │       │   │   ├── vyper.py
    │       │   │   ├── web.py
    │       │   │   ├── webassembly.py
    │       │   │   ├── webidl.py
    │       │   │   ├── webmisc.py
    │       │   │   ├── wgsl.py
    │       │   │   ├── whiley.py
    │       │   │   ├── wowtoc.py
    │       │   │   ├── wren.py
    │       │   │   ├── x10.py
    │       │   │   ├── xorg.py
    │       │   │   ├── yang.py
    │       │   │   ├── yara.py
    │       │   │   └── zig.py
    │       │   ├── modeline.py
    │       │   ├── plugin.py
    │       │   ├── regexopt.py
    │       │   ├── scanner.py
    │       │   ├── sphinxext.py
    │       │   ├── style.py
    │       │   ├── styles
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _mapping.cpython-312.pyc
    │       │   │   │   ├── abap.cpython-312.pyc
    │       │   │   │   ├── algol.cpython-312.pyc
    │       │   │   │   ├── algol_nu.cpython-312.pyc
    │       │   │   │   ├── arduino.cpython-312.pyc
    │       │   │   │   ├── autumn.cpython-312.pyc
    │       │   │   │   ├── borland.cpython-312.pyc
    │       │   │   │   ├── bw.cpython-312.pyc
    │       │   │   │   ├── coffee.cpython-312.pyc
    │       │   │   │   ├── colorful.cpython-312.pyc
    │       │   │   │   ├── default.cpython-312.pyc
    │       │   │   │   ├── dracula.cpython-312.pyc
    │       │   │   │   ├── emacs.cpython-312.pyc
    │       │   │   │   ├── friendly.cpython-312.pyc
    │       │   │   │   ├── friendly_grayscale.cpython-312.pyc
    │       │   │   │   ├── fruity.cpython-312.pyc
    │       │   │   │   ├── gh_dark.cpython-312.pyc
    │       │   │   │   ├── gruvbox.cpython-312.pyc
    │       │   │   │   ├── igor.cpython-312.pyc
    │       │   │   │   ├── inkpot.cpython-312.pyc
    │       │   │   │   ├── lightbulb.cpython-312.pyc
    │       │   │   │   ├── lilypond.cpython-312.pyc
    │       │   │   │   ├── lovelace.cpython-312.pyc
    │       │   │   │   ├── manni.cpython-312.pyc
    │       │   │   │   ├── material.cpython-312.pyc
    │       │   │   │   ├── monokai.cpython-312.pyc
    │       │   │   │   ├── murphy.cpython-312.pyc
    │       │   │   │   ├── native.cpython-312.pyc
    │       │   │   │   ├── nord.cpython-312.pyc
    │       │   │   │   ├── onedark.cpython-312.pyc
    │       │   │   │   ├── paraiso_dark.cpython-312.pyc
    │       │   │   │   ├── paraiso_light.cpython-312.pyc
    │       │   │   │   ├── pastie.cpython-312.pyc
    │       │   │   │   ├── perldoc.cpython-312.pyc
    │       │   │   │   ├── rainbow_dash.cpython-312.pyc
    │       │   │   │   ├── rrt.cpython-312.pyc
    │       │   │   │   ├── sas.cpython-312.pyc
    │       │   │   │   ├── solarized.cpython-312.pyc
    │       │   │   │   ├── staroffice.cpython-312.pyc
    │       │   │   │   ├── stata_dark.cpython-312.pyc
    │       │   │   │   ├── stata_light.cpython-312.pyc
    │       │   │   │   ├── tango.cpython-312.pyc
    │       │   │   │   ├── trac.cpython-312.pyc
    │       │   │   │   ├── vim.cpython-312.pyc
    │       │   │   │   ├── vs.cpython-312.pyc
    │       │   │   │   ├── xcode.cpython-312.pyc
    │       │   │   │   └── zenburn.cpython-312.pyc
    │       │   │   ├── _mapping.py
    │       │   │   ├── abap.py
    │       │   │   ├── algol.py
    │       │   │   ├── algol_nu.py
    │       │   │   ├── arduino.py
    │       │   │   ├── autumn.py
    │       │   │   ├── borland.py
    │       │   │   ├── bw.py
    │       │   │   ├── coffee.py
    │       │   │   ├── colorful.py
    │       │   │   ├── default.py
    │       │   │   ├── dracula.py
    │       │   │   ├── emacs.py
    │       │   │   ├── friendly.py
    │       │   │   ├── friendly_grayscale.py
    │       │   │   ├── fruity.py
    │       │   │   ├── gh_dark.py
    │       │   │   ├── gruvbox.py
    │       │   │   ├── igor.py
    │       │   │   ├── inkpot.py
    │       │   │   ├── lightbulb.py
    │       │   │   ├── lilypond.py
    │       │   │   ├── lovelace.py
    │       │   │   ├── manni.py
    │       │   │   ├── material.py
    │       │   │   ├── monokai.py
    │       │   │   ├── murphy.py
    │       │   │   ├── native.py
    │       │   │   ├── nord.py
    │       │   │   ├── onedark.py
    │       │   │   ├── paraiso_dark.py
    │       │   │   ├── paraiso_light.py
    │       │   │   ├── pastie.py
    │       │   │   ├── perldoc.py
    │       │   │   ├── rainbow_dash.py
    │       │   │   ├── rrt.py
    │       │   │   ├── sas.py
    │       │   │   ├── solarized.py
    │       │   │   ├── staroffice.py
    │       │   │   ├── stata_dark.py
    │       │   │   ├── stata_light.py
    │       │   │   ├── tango.py
    │       │   │   ├── trac.py
    │       │   │   ├── vim.py
    │       │   │   ├── vs.py
    │       │   │   ├── xcode.py
    │       │   │   └── zenburn.py
    │       │   ├── token.py
    │       │   ├── unistring.py
    │       │   └── util.py
    │       ├── pygments-2.19.2.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── licenses
    │       │       ├── AUTHORS
    │       │       └── LICENSE
    │       ├── pylab.py
    │       ├── pyparsing
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── actions.cpython-312.pyc
    │       │   │   ├── common.cpython-312.pyc
    │       │   │   ├── core.cpython-312.pyc
    │       │   │   ├── exceptions.cpython-312.pyc
    │       │   │   ├── helpers.cpython-312.pyc
    │       │   │   ├── results.cpython-312.pyc
    │       │   │   ├── testing.cpython-312.pyc
    │       │   │   ├── unicode.cpython-312.pyc
    │       │   │   └── util.cpython-312.pyc
    │       │   ├── actions.py
    │       │   ├── common.py
    │       │   ├── core.py
    │       │   ├── diagram
    │       │   │   ├── __init__.py
    │       │   │   └── __pycache__
    │       │   │       └── __init__.cpython-312.pyc
    │       │   ├── exceptions.py
    │       │   ├── helpers.py
    │       │   ├── py.typed
    │       │   ├── results.py
    │       │   ├── testing.py
    │       │   ├── tools
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── cvt_pyparsing_pep8_names.cpython-312.pyc
    │       │   │   └── cvt_pyparsing_pep8_names.py
    │       │   ├── unicode.py
    │       │   └── util.py
    │       ├── pyparsing-3.2.5.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   └── licenses
    │       │       └── LICENSE
    │       ├── pytest
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   └── __main__.cpython-312.pyc
    │       │   └── py.typed
    │       ├── pytest-9.0.2.dist-info
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   ├── licenses
    │       │   │   └── LICENSE
    │       │   └── top_level.txt
    │       ├── python_dateutil-2.9.0.post0.dist-info
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   ├── top_level.txt
    │       │   └── zip-safe
    │       ├── scipy
    │       │   ├── __config__.py
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __config__.cpython-312.pyc
    │       │   │   ├── __init__.cpython-312.pyc
    │       │   │   ├── _distributor_init.cpython-312.pyc
    │       │   │   ├── conftest.cpython-312.pyc
    │       │   │   └── version.cpython-312.pyc
    │       │   ├── _cyutility.cp312-win_amd64.dll.a
    │       │   ├── _cyutility.cp312-win_amd64.pyd
    │       │   ├── _distributor_init.py
    │       │   ├── _lib
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _array_api.cpython-312.pyc
    │       │   │   │   ├── _array_api_compat_vendor.cpython-312.pyc
    │       │   │   │   ├── _array_api_no_0d.cpython-312.pyc
    │       │   │   │   ├── _bunch.cpython-312.pyc
    │       │   │   │   ├── _ccallback.cpython-312.pyc
    │       │   │   │   ├── _disjoint_set.cpython-312.pyc
    │       │   │   │   ├── _docscrape.cpython-312.pyc
    │       │   │   │   ├── _elementwise_iterative_method.cpython-312.pyc
    │       │   │   │   ├── _gcutils.cpython-312.pyc
    │       │   │   │   ├── _pep440.cpython-312.pyc
    │       │   │   │   ├── _sparse.cpython-312.pyc
    │       │   │   │   ├── _testutils.cpython-312.pyc
    │       │   │   │   ├── _threadsafety.cpython-312.pyc
    │       │   │   │   ├── _tmpdirs.cpython-312.pyc
    │       │   │   │   ├── _util.cpython-312.pyc
    │       │   │   │   ├── decorator.cpython-312.pyc
    │       │   │   │   ├── deprecation.cpython-312.pyc
    │       │   │   │   ├── doccer.cpython-312.pyc
    │       │   │   │   └── uarray.cpython-312.pyc
    │       │   │   ├── _array_api.py
    │       │   │   ├── _array_api_compat_vendor.py
    │       │   │   ├── _array_api_no_0d.py
    │       │   │   ├── _bunch.py
    │       │   │   ├── _ccallback.py
    │       │   │   ├── _ccallback_c.cp312-win_amd64.dll.a
    │       │   │   ├── _ccallback_c.cp312-win_amd64.pyd
    │       │   │   ├── _disjoint_set.py
    │       │   │   ├── _docscrape.py
    │       │   │   ├── _elementwise_iterative_method.py
    │       │   │   ├── _fpumode.cp312-win_amd64.dll.a
    │       │   │   ├── _fpumode.cp312-win_amd64.pyd
    │       │   │   ├── _gcutils.py
    │       │   │   ├── _pep440.py
    │       │   │   ├── _sparse.py
    │       │   │   ├── _test_ccallback.cp312-win_amd64.dll.a
    │       │   │   ├── _test_ccallback.cp312-win_amd64.pyd
    │       │   │   ├── _test_deprecation_call.cp312-win_amd64.dll.a
    │       │   │   ├── _test_deprecation_call.cp312-win_amd64.pyd
    │       │   │   ├── _test_deprecation_def.cp312-win_amd64.dll.a
    │       │   │   ├── _test_deprecation_def.cp312-win_amd64.pyd
    │       │   │   ├── _testutils.py
    │       │   │   ├── _threadsafety.py
    │       │   │   ├── _tmpdirs.py
    │       │   │   ├── _uarray
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   └── _backend.cpython-312.pyc
    │       │   │   │   ├── _backend.py
    │       │   │   │   ├── _uarray.cp312-win_amd64.dll.a
    │       │   │   │   └── _uarray.cp312-win_amd64.pyd
    │       │   │   ├── _util.py
    │       │   │   ├── array_api_compat
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   └── _internal.cpython-312.pyc
    │       │   │   │   ├── _internal.py
    │       │   │   │   ├── common
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _aliases.cpython-312.pyc
    │       │   │   │   │   │   ├── _fft.cpython-312.pyc
    │       │   │   │   │   │   ├── _helpers.cpython-312.pyc
    │       │   │   │   │   │   ├── _linalg.cpython-312.pyc
    │       │   │   │   │   │   └── _typing.cpython-312.pyc
    │       │   │   │   │   ├── _aliases.py
    │       │   │   │   │   ├── _fft.py
    │       │   │   │   │   ├── _helpers.py
    │       │   │   │   │   ├── _linalg.py
    │       │   │   │   │   └── _typing.py
    │       │   │   │   ├── cupy
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _aliases.cpython-312.pyc
    │       │   │   │   │   │   ├── _info.cpython-312.pyc
    │       │   │   │   │   │   ├── _typing.cpython-312.pyc
    │       │   │   │   │   │   ├── fft.cpython-312.pyc
    │       │   │   │   │   │   └── linalg.cpython-312.pyc
    │       │   │   │   │   ├── _aliases.py
    │       │   │   │   │   ├── _info.py
    │       │   │   │   │   ├── _typing.py
    │       │   │   │   │   ├── fft.py
    │       │   │   │   │   └── linalg.py
    │       │   │   │   ├── dask
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   └── __init__.cpython-312.pyc
    │       │   │   │   │   └── array
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__
    │       │   │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │   │       │   ├── _aliases.cpython-312.pyc
    │       │   │   │   │       │   ├── _info.cpython-312.pyc
    │       │   │   │   │       │   ├── fft.cpython-312.pyc
    │       │   │   │   │       │   └── linalg.cpython-312.pyc
    │       │   │   │   │       ├── _aliases.py
    │       │   │   │   │       ├── _info.py
    │       │   │   │   │       ├── fft.py
    │       │   │   │   │       └── linalg.py
    │       │   │   │   ├── numpy
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _aliases.cpython-312.pyc
    │       │   │   │   │   │   ├── _info.cpython-312.pyc
    │       │   │   │   │   │   ├── _typing.cpython-312.pyc
    │       │   │   │   │   │   ├── fft.cpython-312.pyc
    │       │   │   │   │   │   └── linalg.cpython-312.pyc
    │       │   │   │   │   ├── _aliases.py
    │       │   │   │   │   ├── _info.py
    │       │   │   │   │   ├── _typing.py
    │       │   │   │   │   ├── fft.py
    │       │   │   │   │   └── linalg.py
    │       │   │   │   └── torch
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── _aliases.cpython-312.pyc
    │       │   │   │       │   ├── _info.cpython-312.pyc
    │       │   │   │       │   ├── _typing.cpython-312.pyc
    │       │   │   │       │   ├── fft.cpython-312.pyc
    │       │   │   │       │   └── linalg.cpython-312.pyc
    │       │   │   │       ├── _aliases.py
    │       │   │   │       ├── _info.py
    │       │   │   │       ├── _typing.py
    │       │   │   │       ├── fft.py
    │       │   │   │       └── linalg.py
    │       │   │   ├── array_api_extra
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _delegation.cpython-312.pyc
    │       │   │   │   │   └── testing.cpython-312.pyc
    │       │   │   │   ├── _delegation.py
    │       │   │   │   ├── _lib
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _at.cpython-312.pyc
    │       │   │   │   │   │   ├── _backends.cpython-312.pyc
    │       │   │   │   │   │   ├── _funcs.cpython-312.pyc
    │       │   │   │   │   │   ├── _lazy.cpython-312.pyc
    │       │   │   │   │   │   └── _testing.cpython-312.pyc
    │       │   │   │   │   ├── _at.py
    │       │   │   │   │   ├── _backends.py
    │       │   │   │   │   ├── _funcs.py
    │       │   │   │   │   ├── _lazy.py
    │       │   │   │   │   ├── _testing.py
    │       │   │   │   │   └── _utils
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__
    │       │   │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │   │       │   ├── _compat.cpython-312.pyc
    │       │   │   │   │       │   ├── _helpers.cpython-312.pyc
    │       │   │   │   │       │   └── _typing.cpython-312.pyc
    │       │   │   │   │       ├── _compat.py
    │       │   │   │   │       ├── _compat.pyi
    │       │   │   │   │       ├── _helpers.py
    │       │   │   │   │       ├── _typing.py
    │       │   │   │   │       └── _typing.pyi
    │       │   │   │   └── testing.py
    │       │   │   ├── cobyqa
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── framework.cpython-312.pyc
    │       │   │   │   │   ├── main.cpython-312.pyc
    │       │   │   │   │   ├── models.cpython-312.pyc
    │       │   │   │   │   ├── problem.cpython-312.pyc
    │       │   │   │   │   └── settings.cpython-312.pyc
    │       │   │   │   ├── framework.py
    │       │   │   │   ├── main.py
    │       │   │   │   ├── models.py
    │       │   │   │   ├── problem.py
    │       │   │   │   ├── settings.py
    │       │   │   │   ├── subsolvers
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── geometry.cpython-312.pyc
    │       │   │   │   │   │   └── optim.cpython-312.pyc
    │       │   │   │   │   ├── geometry.py
    │       │   │   │   │   └── optim.py
    │       │   │   │   └── utils
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── exceptions.cpython-312.pyc
    │       │   │   │       │   ├── math.cpython-312.pyc
    │       │   │   │       │   └── versions.cpython-312.pyc
    │       │   │   │       ├── exceptions.py
    │       │   │   │       ├── math.py
    │       │   │   │       └── versions.py
    │       │   │   ├── decorator.py
    │       │   │   ├── deprecation.py
    │       │   │   ├── doccer.py
    │       │   │   ├── messagestream.cp312-win_amd64.dll.a
    │       │   │   ├── messagestream.cp312-win_amd64.pyd
    │       │   │   ├── pyprima
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   └── __init__.cpython-312.pyc
    │       │   │   │   ├── cobyla
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── cobyla.cpython-312.pyc
    │       │   │   │   │   │   ├── cobylb.cpython-312.pyc
    │       │   │   │   │   │   ├── geometry.cpython-312.pyc
    │       │   │   │   │   │   ├── initialize.cpython-312.pyc
    │       │   │   │   │   │   ├── trustregion.cpython-312.pyc
    │       │   │   │   │   │   └── update.cpython-312.pyc
    │       │   │   │   │   ├── cobyla.py
    │       │   │   │   │   ├── cobylb.py
    │       │   │   │   │   ├── geometry.py
    │       │   │   │   │   ├── initialize.py
    │       │   │   │   │   ├── trustregion.py
    │       │   │   │   │   └── update.py
    │       │   │   │   └── common
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── _bounds.cpython-312.pyc
    │       │   │   │       │   ├── _linear_constraints.cpython-312.pyc
    │       │   │   │       │   ├── _nonlinear_constraints.cpython-312.pyc
    │       │   │   │       │   ├── _project.cpython-312.pyc
    │       │   │   │       │   ├── checkbreak.cpython-312.pyc
    │       │   │   │       │   ├── consts.cpython-312.pyc
    │       │   │   │       │   ├── evaluate.cpython-312.pyc
    │       │   │   │       │   ├── history.cpython-312.pyc
    │       │   │   │       │   ├── infos.cpython-312.pyc
    │       │   │   │       │   ├── linalg.cpython-312.pyc
    │       │   │   │       │   ├── message.cpython-312.pyc
    │       │   │   │       │   ├── powalg.cpython-312.pyc
    │       │   │   │       │   ├── preproc.cpython-312.pyc
    │       │   │   │       │   ├── present.cpython-312.pyc
    │       │   │   │       │   ├── ratio.cpython-312.pyc
    │       │   │   │       │   ├── redrho.cpython-312.pyc
    │       │   │   │       │   └── selectx.cpython-312.pyc
    │       │   │   │       ├── _bounds.py
    │       │   │   │       ├── _linear_constraints.py
    │       │   │   │       ├── _nonlinear_constraints.py
    │       │   │   │       ├── _project.py
    │       │   │   │       ├── checkbreak.py
    │       │   │   │       ├── consts.py
    │       │   │   │       ├── evaluate.py
    │       │   │   │       ├── history.py
    │       │   │   │       ├── infos.py
    │       │   │   │       ├── linalg.py
    │       │   │   │       ├── message.py
    │       │   │   │       ├── powalg.py
    │       │   │   │       ├── preproc.py
    │       │   │   │       ├── present.py
    │       │   │   │       ├── ratio.py
    │       │   │   │       ├── redrho.py
    │       │   │   │       └── selectx.py
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── test__gcutils.cpython-312.pyc
    │       │   │   │   │   ├── test__pep440.cpython-312.pyc
    │       │   │   │   │   ├── test__testutils.cpython-312.pyc
    │       │   │   │   │   ├── test__threadsafety.cpython-312.pyc
    │       │   │   │   │   ├── test__util.cpython-312.pyc
    │       │   │   │   │   ├── test_array_api.cpython-312.pyc
    │       │   │   │   │   ├── test_bunch.cpython-312.pyc
    │       │   │   │   │   ├── test_ccallback.cpython-312.pyc
    │       │   │   │   │   ├── test_config.cpython-312.pyc
    │       │   │   │   │   ├── test_deprecation.cpython-312.pyc
    │       │   │   │   │   ├── test_doccer.cpython-312.pyc
    │       │   │   │   │   ├── test_import_cycles.cpython-312.pyc
    │       │   │   │   │   ├── test_public_api.cpython-312.pyc
    │       │   │   │   │   ├── test_scipy_version.cpython-312.pyc
    │       │   │   │   │   ├── test_tmpdirs.cpython-312.pyc
    │       │   │   │   │   └── test_warnings.cpython-312.pyc
    │       │   │   │   ├── test__gcutils.py
    │       │   │   │   ├── test__pep440.py
    │       │   │   │   ├── test__testutils.py
    │       │   │   │   ├── test__threadsafety.py
    │       │   │   │   ├── test__util.py
    │       │   │   │   ├── test_array_api.py
    │       │   │   │   ├── test_bunch.py
    │       │   │   │   ├── test_ccallback.py
    │       │   │   │   ├── test_config.py
    │       │   │   │   ├── test_deprecation.py
    │       │   │   │   ├── test_doccer.py
    │       │   │   │   ├── test_import_cycles.py
    │       │   │   │   ├── test_public_api.py
    │       │   │   │   ├── test_scipy_version.py
    │       │   │   │   ├── test_tmpdirs.py
    │       │   │   │   └── test_warnings.py
    │       │   │   └── uarray.py
    │       │   ├── cluster
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── hierarchy.cpython-312.pyc
    │       │   │   │   └── vq.cpython-312.pyc
    │       │   │   ├── _hierarchy.cp312-win_amd64.dll.a
    │       │   │   ├── _hierarchy.cp312-win_amd64.pyd
    │       │   │   ├── _optimal_leaf_ordering.cp312-win_amd64.dll.a
    │       │   │   ├── _optimal_leaf_ordering.cp312-win_amd64.pyd
    │       │   │   ├── _vq.cp312-win_amd64.dll.a
    │       │   │   ├── _vq.cp312-win_amd64.pyd
    │       │   │   ├── hierarchy.py
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── hierarchy_test_data.cpython-312.pyc
    │       │   │   │   │   ├── test_disjoint_set.cpython-312.pyc
    │       │   │   │   │   ├── test_hierarchy.cpython-312.pyc
    │       │   │   │   │   └── test_vq.cpython-312.pyc
    │       │   │   │   ├── hierarchy_test_data.py
    │       │   │   │   ├── test_disjoint_set.py
    │       │   │   │   ├── test_hierarchy.py
    │       │   │   │   └── test_vq.py
    │       │   │   └── vq.py
    │       │   ├── conftest.py
    │       │   ├── constants
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _codata.cpython-312.pyc
    │       │   │   │   ├── _constants.cpython-312.pyc
    │       │   │   │   ├── codata.cpython-312.pyc
    │       │   │   │   └── constants.cpython-312.pyc
    │       │   │   ├── _codata.py
    │       │   │   ├── _constants.py
    │       │   │   ├── codata.py
    │       │   │   ├── constants.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_codata.cpython-312.pyc
    │       │   │       │   └── test_constants.cpython-312.pyc
    │       │   │       ├── test_codata.py
    │       │   │       └── test_constants.py
    │       │   ├── datasets
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _download_all.cpython-312.pyc
    │       │   │   │   ├── _fetchers.cpython-312.pyc
    │       │   │   │   ├── _registry.cpython-312.pyc
    │       │   │   │   └── _utils.cpython-312.pyc
    │       │   │   ├── _download_all.py
    │       │   │   ├── _fetchers.py
    │       │   │   ├── _registry.py
    │       │   │   ├── _utils.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   └── test_data.cpython-312.pyc
    │       │   │       └── test_data.py
    │       │   ├── differentiate
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   └── _differentiate.cpython-312.pyc
    │       │   │   ├── _differentiate.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   └── test_differentiate.cpython-312.pyc
    │       │   │       └── test_differentiate.py
    │       │   ├── fft
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _backend.cpython-312.pyc
    │       │   │   │   ├── _basic.cpython-312.pyc
    │       │   │   │   ├── _basic_backend.cpython-312.pyc
    │       │   │   │   ├── _debug_backends.cpython-312.pyc
    │       │   │   │   ├── _fftlog.cpython-312.pyc
    │       │   │   │   ├── _fftlog_backend.cpython-312.pyc
    │       │   │   │   ├── _helper.cpython-312.pyc
    │       │   │   │   ├── _realtransforms.cpython-312.pyc
    │       │   │   │   └── _realtransforms_backend.cpython-312.pyc
    │       │   │   ├── _backend.py
    │       │   │   ├── _basic.py
    │       │   │   ├── _basic_backend.py
    │       │   │   ├── _debug_backends.py
    │       │   │   ├── _fftlog.py
    │       │   │   ├── _fftlog_backend.py
    │       │   │   ├── _helper.py
    │       │   │   ├── _pocketfft
    │       │   │   │   ├── LICENSE.md
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── basic.cpython-312.pyc
    │       │   │   │   │   ├── helper.cpython-312.pyc
    │       │   │   │   │   └── realtransforms.cpython-312.pyc
    │       │   │   │   ├── basic.py
    │       │   │   │   ├── helper.py
    │       │   │   │   ├── pypocketfft.cp312-win_amd64.dll.a
    │       │   │   │   ├── pypocketfft.cp312-win_amd64.pyd
    │       │   │   │   ├── realtransforms.py
    │       │   │   │   └── tests
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── test_basic.cpython-312.pyc
    │       │   │   │       │   └── test_real_transforms.cpython-312.pyc
    │       │   │   │       ├── test_basic.py
    │       │   │   │       └── test_real_transforms.py
    │       │   │   ├── _realtransforms.py
    │       │   │   ├── _realtransforms_backend.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── mock_backend.cpython-312.pyc
    │       │   │       │   ├── test_backend.cpython-312.pyc
    │       │   │       │   ├── test_basic.cpython-312.pyc
    │       │   │       │   ├── test_fftlog.cpython-312.pyc
    │       │   │       │   ├── test_helper.cpython-312.pyc
    │       │   │       │   ├── test_multithreading.cpython-312.pyc
    │       │   │       │   └── test_real_transforms.cpython-312.pyc
    │       │   │       ├── mock_backend.py
    │       │   │       ├── test_backend.py
    │       │   │       ├── test_basic.py
    │       │   │       ├── test_fftlog.py
    │       │   │       ├── test_helper.py
    │       │   │       ├── test_multithreading.py
    │       │   │       └── test_real_transforms.py
    │       │   ├── fftpack
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _basic.cpython-312.pyc
    │       │   │   │   ├── _helper.cpython-312.pyc
    │       │   │   │   ├── _pseudo_diffs.cpython-312.pyc
    │       │   │   │   ├── _realtransforms.cpython-312.pyc
    │       │   │   │   ├── basic.cpython-312.pyc
    │       │   │   │   ├── helper.cpython-312.pyc
    │       │   │   │   ├── pseudo_diffs.cpython-312.pyc
    │       │   │   │   └── realtransforms.cpython-312.pyc
    │       │   │   ├── _basic.py
    │       │   │   ├── _helper.py
    │       │   │   ├── _pseudo_diffs.py
    │       │   │   ├── _realtransforms.py
    │       │   │   ├── basic.py
    │       │   │   ├── convolve.cp312-win_amd64.dll.a
    │       │   │   ├── convolve.cp312-win_amd64.pyd
    │       │   │   ├── helper.py
    │       │   │   ├── pseudo_diffs.py
    │       │   │   ├── realtransforms.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_basic.cpython-312.pyc
    │       │   │       │   ├── test_helper.cpython-312.pyc
    │       │   │       │   ├── test_import.cpython-312.pyc
    │       │   │       │   ├── test_pseudo_diffs.cpython-312.pyc
    │       │   │       │   └── test_real_transforms.cpython-312.pyc
    │       │   │       ├── fftw_double_ref.npz
    │       │   │       ├── fftw_longdouble_ref.npz
    │       │   │       ├── fftw_single_ref.npz
    │       │   │       ├── test.npz
    │       │   │       ├── test_basic.py
    │       │   │       ├── test_helper.py
    │       │   │       ├── test_import.py
    │       │   │       ├── test_pseudo_diffs.py
    │       │   │       └── test_real_transforms.py
    │       │   ├── integrate
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _bvp.cpython-312.pyc
    │       │   │   │   ├── _cubature.cpython-312.pyc
    │       │   │   │   ├── _lebedev.cpython-312.pyc
    │       │   │   │   ├── _ode.cpython-312.pyc
    │       │   │   │   ├── _odepack_py.cpython-312.pyc
    │       │   │   │   ├── _quad_vec.cpython-312.pyc
    │       │   │   │   ├── _quadpack_py.cpython-312.pyc
    │       │   │   │   ├── _quadrature.cpython-312.pyc
    │       │   │   │   ├── _tanhsinh.cpython-312.pyc
    │       │   │   │   ├── dop.cpython-312.pyc
    │       │   │   │   ├── lsoda.cpython-312.pyc
    │       │   │   │   ├── odepack.cpython-312.pyc
    │       │   │   │   ├── quadpack.cpython-312.pyc
    │       │   │   │   └── vode.cpython-312.pyc
    │       │   │   ├── _bvp.py
    │       │   │   ├── _cubature.py
    │       │   │   ├── _dop.cp312-win_amd64.dll.a
    │       │   │   ├── _dop.cp312-win_amd64.pyd
    │       │   │   ├── _ivp
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── base.cpython-312.pyc
    │       │   │   │   │   ├── bdf.cpython-312.pyc
    │       │   │   │   │   ├── common.cpython-312.pyc
    │       │   │   │   │   ├── dop853_coefficients.cpython-312.pyc
    │       │   │   │   │   ├── ivp.cpython-312.pyc
    │       │   │   │   │   ├── lsoda.cpython-312.pyc
    │       │   │   │   │   ├── radau.cpython-312.pyc
    │       │   │   │   │   └── rk.cpython-312.pyc
    │       │   │   │   ├── base.py
    │       │   │   │   ├── bdf.py
    │       │   │   │   ├── common.py
    │       │   │   │   ├── dop853_coefficients.py
    │       │   │   │   ├── ivp.py
    │       │   │   │   ├── lsoda.py
    │       │   │   │   ├── radau.py
    │       │   │   │   ├── rk.py
    │       │   │   │   └── tests
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── test_ivp.cpython-312.pyc
    │       │   │   │       │   └── test_rk.cpython-312.pyc
    │       │   │   │       ├── test_ivp.py
    │       │   │   │       └── test_rk.py
    │       │   │   ├── _lebedev.py
    │       │   │   ├── _lsoda.cp312-win_amd64.dll.a
    │       │   │   ├── _lsoda.cp312-win_amd64.pyd
    │       │   │   ├── _ode.py
    │       │   │   ├── _odepack.cp312-win_amd64.dll.a
    │       │   │   ├── _odepack.cp312-win_amd64.pyd
    │       │   │   ├── _odepack_py.py
    │       │   │   ├── _quad_vec.py
    │       │   │   ├── _quadpack.cp312-win_amd64.dll.a
    │       │   │   ├── _quadpack.cp312-win_amd64.pyd
    │       │   │   ├── _quadpack_py.py
    │       │   │   ├── _quadrature.py
    │       │   │   ├── _rules
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _base.cpython-312.pyc
    │       │   │   │   │   ├── _gauss_kronrod.cpython-312.pyc
    │       │   │   │   │   ├── _gauss_legendre.cpython-312.pyc
    │       │   │   │   │   └── _genz_malik.cpython-312.pyc
    │       │   │   │   ├── _base.py
    │       │   │   │   ├── _gauss_kronrod.py
    │       │   │   │   ├── _gauss_legendre.py
    │       │   │   │   └── _genz_malik.py
    │       │   │   ├── _tanhsinh.py
    │       │   │   ├── _test_multivariate.cp312-win_amd64.dll.a
    │       │   │   ├── _test_multivariate.cp312-win_amd64.pyd
    │       │   │   ├── _test_odeint_banded.cp312-win_amd64.dll.a
    │       │   │   ├── _test_odeint_banded.cp312-win_amd64.pyd
    │       │   │   ├── _vode.cp312-win_amd64.dll.a
    │       │   │   ├── _vode.cp312-win_amd64.pyd
    │       │   │   ├── dop.py
    │       │   │   ├── lsoda.py
    │       │   │   ├── odepack.py
    │       │   │   ├── quadpack.py
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── test__quad_vec.cpython-312.pyc
    │       │   │   │   │   ├── test_banded_ode_solvers.cpython-312.pyc
    │       │   │   │   │   ├── test_bvp.cpython-312.pyc
    │       │   │   │   │   ├── test_cubature.cpython-312.pyc
    │       │   │   │   │   ├── test_integrate.cpython-312.pyc
    │       │   │   │   │   ├── test_odeint_jac.cpython-312.pyc
    │       │   │   │   │   ├── test_quadpack.cpython-312.pyc
    │       │   │   │   │   ├── test_quadrature.cpython-312.pyc
    │       │   │   │   │   └── test_tanhsinh.cpython-312.pyc
    │       │   │   │   ├── test__quad_vec.py
    │       │   │   │   ├── test_banded_ode_solvers.py
    │       │   │   │   ├── test_bvp.py
    │       │   │   │   ├── test_cubature.py
    │       │   │   │   ├── test_integrate.py
    │       │   │   │   ├── test_odeint_jac.py
    │       │   │   │   ├── test_quadpack.py
    │       │   │   │   ├── test_quadrature.py
    │       │   │   │   └── test_tanhsinh.py
    │       │   │   └── vode.py
    │       │   ├── interpolate
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _bary_rational.cpython-312.pyc
    │       │   │   │   ├── _bsplines.cpython-312.pyc
    │       │   │   │   ├── _cubic.cpython-312.pyc
    │       │   │   │   ├── _fitpack2.cpython-312.pyc
    │       │   │   │   ├── _fitpack_impl.cpython-312.pyc
    │       │   │   │   ├── _fitpack_py.cpython-312.pyc
    │       │   │   │   ├── _fitpack_repro.cpython-312.pyc
    │       │   │   │   ├── _interpolate.cpython-312.pyc
    │       │   │   │   ├── _ndbspline.cpython-312.pyc
    │       │   │   │   ├── _ndgriddata.cpython-312.pyc
    │       │   │   │   ├── _pade.cpython-312.pyc
    │       │   │   │   ├── _polyint.cpython-312.pyc
    │       │   │   │   ├── _rbf.cpython-312.pyc
    │       │   │   │   ├── _rbfinterp.cpython-312.pyc
    │       │   │   │   ├── _rgi.cpython-312.pyc
    │       │   │   │   ├── dfitpack.cpython-312.pyc
    │       │   │   │   ├── fitpack.cpython-312.pyc
    │       │   │   │   ├── fitpack2.cpython-312.pyc
    │       │   │   │   ├── interpnd.cpython-312.pyc
    │       │   │   │   ├── interpolate.cpython-312.pyc
    │       │   │   │   ├── ndgriddata.cpython-312.pyc
    │       │   │   │   ├── polyint.cpython-312.pyc
    │       │   │   │   └── rbf.cpython-312.pyc
    │       │   │   ├── _bary_rational.py
    │       │   │   ├── _bsplines.py
    │       │   │   ├── _cubic.py
    │       │   │   ├── _dfitpack.cp312-win_amd64.dll.a
    │       │   │   ├── _dfitpack.cp312-win_amd64.pyd
    │       │   │   ├── _dierckx.cp312-win_amd64.dll.a
    │       │   │   ├── _dierckx.cp312-win_amd64.pyd
    │       │   │   ├── _fitpack.cp312-win_amd64.dll.a
    │       │   │   ├── _fitpack.cp312-win_amd64.pyd
    │       │   │   ├── _fitpack2.py
    │       │   │   ├── _fitpack_impl.py
    │       │   │   ├── _fitpack_py.py
    │       │   │   ├── _fitpack_repro.py
    │       │   │   ├── _interpnd.cp312-win_amd64.dll.a
    │       │   │   ├── _interpnd.cp312-win_amd64.pyd
    │       │   │   ├── _interpolate.py
    │       │   │   ├── _ndbspline.py
    │       │   │   ├── _ndgriddata.py
    │       │   │   ├── _pade.py
    │       │   │   ├── _polyint.py
    │       │   │   ├── _ppoly.cp312-win_amd64.dll.a
    │       │   │   ├── _ppoly.cp312-win_amd64.pyd
    │       │   │   ├── _rbf.py
    │       │   │   ├── _rbfinterp.py
    │       │   │   ├── _rbfinterp_pythran.cp312-win_amd64.dll.a
    │       │   │   ├── _rbfinterp_pythran.cp312-win_amd64.pyd
    │       │   │   ├── _rgi.py
    │       │   │   ├── _rgi_cython.cp312-win_amd64.dll.a
    │       │   │   ├── _rgi_cython.cp312-win_amd64.pyd
    │       │   │   ├── dfitpack.py
    │       │   │   ├── fitpack.py
    │       │   │   ├── fitpack2.py
    │       │   │   ├── interpnd.py
    │       │   │   ├── interpolate.py
    │       │   │   ├── ndgriddata.py
    │       │   │   ├── polyint.py
    │       │   │   ├── rbf.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_bary_rational.cpython-312.pyc
    │       │   │       │   ├── test_bsplines.cpython-312.pyc
    │       │   │       │   ├── test_fitpack.cpython-312.pyc
    │       │   │       │   ├── test_fitpack2.cpython-312.pyc
    │       │   │       │   ├── test_gil.cpython-312.pyc
    │       │   │       │   ├── test_interpnd.cpython-312.pyc
    │       │   │       │   ├── test_interpolate.cpython-312.pyc
    │       │   │       │   ├── test_ndgriddata.cpython-312.pyc
    │       │   │       │   ├── test_pade.cpython-312.pyc
    │       │   │       │   ├── test_polyint.cpython-312.pyc
    │       │   │       │   ├── test_rbf.cpython-312.pyc
    │       │   │       │   ├── test_rbfinterp.cpython-312.pyc
    │       │   │       │   └── test_rgi.cpython-312.pyc
    │       │   │       ├── data
    │       │   │       │   ├── bug-1310.npz
    │       │   │       │   ├── estimate_gradients_hang.npy
    │       │   │       │   └── gcvspl.npz
    │       │   │       ├── test_bary_rational.py
    │       │   │       ├── test_bsplines.py
    │       │   │       ├── test_fitpack.py
    │       │   │       ├── test_fitpack2.py
    │       │   │       ├── test_gil.py
    │       │   │       ├── test_interpnd.py
    │       │   │       ├── test_interpolate.py
    │       │   │       ├── test_ndgriddata.py
    │       │   │       ├── test_pade.py
    │       │   │       ├── test_polyint.py
    │       │   │       ├── test_rbf.py
    │       │   │       ├── test_rbfinterp.py
    │       │   │       └── test_rgi.py
    │       │   ├── io
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _fortran.cpython-312.pyc
    │       │   │   │   ├── _idl.cpython-312.pyc
    │       │   │   │   ├── _mmio.cpython-312.pyc
    │       │   │   │   ├── _netcdf.cpython-312.pyc
    │       │   │   │   ├── harwell_boeing.cpython-312.pyc
    │       │   │   │   ├── idl.cpython-312.pyc
    │       │   │   │   ├── mmio.cpython-312.pyc
    │       │   │   │   ├── netcdf.cpython-312.pyc
    │       │   │   │   └── wavfile.cpython-312.pyc
    │       │   │   ├── _fast_matrix_market
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   └── __init__.cpython-312.pyc
    │       │   │   │   ├── _fmm_core.cp312-win_amd64.dll.a
    │       │   │   │   └── _fmm_core.cp312-win_amd64.pyd
    │       │   │   ├── _fortran.py
    │       │   │   ├── _harwell_boeing
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _fortran_format_parser.cpython-312.pyc
    │       │   │   │   │   └── hb.cpython-312.pyc
    │       │   │   │   ├── _fortran_format_parser.py
    │       │   │   │   ├── hb.py
    │       │   │   │   └── tests
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── test_fortran_format.cpython-312.pyc
    │       │   │   │       │   └── test_hb.cpython-312.pyc
    │       │   │   │       ├── test_fortran_format.py
    │       │   │   │       └── test_hb.py
    │       │   │   ├── _idl.py
    │       │   │   ├── _mmio.py
    │       │   │   ├── _netcdf.py
    │       │   │   ├── _test_fortran.cp312-win_amd64.dll.a
    │       │   │   ├── _test_fortran.cp312-win_amd64.pyd
    │       │   │   ├── arff
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _arffread.cpython-312.pyc
    │       │   │   │   │   └── arffread.cpython-312.pyc
    │       │   │   │   ├── _arffread.py
    │       │   │   │   ├── arffread.py
    │       │   │   │   └── tests
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   └── test_arffread.cpython-312.pyc
    │       │   │   │       ├── data
    │       │   │   │       │   ├── iris.arff
    │       │   │   │       │   ├── missing.arff
    │       │   │   │       │   ├── nodata.arff
    │       │   │   │       │   ├── quoted_nominal.arff
    │       │   │   │       │   ├── quoted_nominal_spaces.arff
    │       │   │   │       │   ├── test1.arff
    │       │   │   │       │   ├── test10.arff
    │       │   │   │       │   ├── test11.arff
    │       │   │   │       │   ├── test2.arff
    │       │   │   │       │   ├── test3.arff
    │       │   │   │       │   ├── test4.arff
    │       │   │   │       │   ├── test5.arff
    │       │   │   │       │   ├── test6.arff
    │       │   │   │       │   ├── test7.arff
    │       │   │   │       │   ├── test8.arff
    │       │   │   │       │   └── test9.arff
    │       │   │   │       └── test_arffread.py
    │       │   │   ├── harwell_boeing.py
    │       │   │   ├── idl.py
    │       │   │   ├── matlab
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _byteordercodes.cpython-312.pyc
    │       │   │   │   │   ├── _mio.cpython-312.pyc
    │       │   │   │   │   ├── _mio4.cpython-312.pyc
    │       │   │   │   │   ├── _mio5.cpython-312.pyc
    │       │   │   │   │   ├── _mio5_params.cpython-312.pyc
    │       │   │   │   │   ├── _miobase.cpython-312.pyc
    │       │   │   │   │   ├── byteordercodes.cpython-312.pyc
    │       │   │   │   │   ├── mio.cpython-312.pyc
    │       │   │   │   │   ├── mio4.cpython-312.pyc
    │       │   │   │   │   ├── mio5.cpython-312.pyc
    │       │   │   │   │   ├── mio5_params.cpython-312.pyc
    │       │   │   │   │   ├── mio5_utils.cpython-312.pyc
    │       │   │   │   │   ├── mio_utils.cpython-312.pyc
    │       │   │   │   │   ├── miobase.cpython-312.pyc
    │       │   │   │   │   └── streams.cpython-312.pyc
    │       │   │   │   ├── _byteordercodes.py
    │       │   │   │   ├── _mio.py
    │       │   │   │   ├── _mio4.py
    │       │   │   │   ├── _mio5.py
    │       │   │   │   ├── _mio5_params.py
    │       │   │   │   ├── _mio5_utils.cp312-win_amd64.dll.a
    │       │   │   │   ├── _mio5_utils.cp312-win_amd64.pyd
    │       │   │   │   ├── _mio_utils.cp312-win_amd64.dll.a
    │       │   │   │   ├── _mio_utils.cp312-win_amd64.pyd
    │       │   │   │   ├── _miobase.py
    │       │   │   │   ├── _streams.cp312-win_amd64.dll.a
    │       │   │   │   ├── _streams.cp312-win_amd64.pyd
    │       │   │   │   ├── byteordercodes.py
    │       │   │   │   ├── mio.py
    │       │   │   │   ├── mio4.py
    │       │   │   │   ├── mio5.py
    │       │   │   │   ├── mio5_params.py
    │       │   │   │   ├── mio5_utils.py
    │       │   │   │   ├── mio_utils.py
    │       │   │   │   ├── miobase.py
    │       │   │   │   ├── streams.py
    │       │   │   │   └── tests
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── test_byteordercodes.cpython-312.pyc
    │       │   │   │       │   ├── test_mio.cpython-312.pyc
    │       │   │   │       │   ├── test_mio5_utils.cpython-312.pyc
    │       │   │   │       │   ├── test_mio_funcs.cpython-312.pyc
    │       │   │   │       │   ├── test_mio_utils.cpython-312.pyc
    │       │   │   │       │   ├── test_miobase.cpython-312.pyc
    │       │   │   │       │   ├── test_pathological.cpython-312.pyc
    │       │   │   │       │   └── test_streams.cpython-312.pyc
    │       │   │   │       ├── data
    │       │   │   │       │   ├── bad_miuint32.mat
    │       │   │   │       │   ├── bad_miutf8_array_name.mat
    │       │   │   │       │   ├── big_endian.mat
    │       │   │   │       │   ├── broken_utf8.mat
    │       │   │   │       │   ├── corrupted_zlib_checksum.mat
    │       │   │   │       │   ├── corrupted_zlib_data.mat
    │       │   │   │       │   ├── debigged_m4.mat
    │       │   │   │       │   ├── japanese_utf8.txt
    │       │   │   │       │   ├── little_endian.mat
    │       │   │   │       │   ├── logical_sparse.mat
    │       │   │   │       │   ├── malformed1.mat
    │       │   │   │       │   ├── miuint32_for_miint32.mat
    │       │   │   │       │   ├── miutf8_array_name.mat
    │       │   │   │       │   ├── nasty_duplicate_fieldnames.mat
    │       │   │   │       │   ├── one_by_zero_char.mat
    │       │   │   │       │   ├── parabola.mat
    │       │   │   │       │   ├── single_empty_string.mat
    │       │   │   │       │   ├── some_functions.mat
    │       │   │   │       │   ├── sqr.mat
    │       │   │   │       │   ├── test3dmatrix_6.1_SOL2.mat
    │       │   │   │       │   ├── test3dmatrix_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── test3dmatrix_7.1_GLNX86.mat
    │       │   │   │       │   ├── test3dmatrix_7.4_GLNX86.mat
    │       │   │   │       │   ├── test_empty_struct.mat
    │       │   │   │       │   ├── test_mat4_le_floats.mat
    │       │   │   │       │   ├── test_skip_variable.mat
    │       │   │   │       │   ├── testbool_8_WIN64.mat
    │       │   │   │       │   ├── testcell_6.1_SOL2.mat
    │       │   │   │       │   ├── testcell_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testcell_7.1_GLNX86.mat
    │       │   │   │       │   ├── testcell_7.4_GLNX86.mat
    │       │   │   │       │   ├── testcellnest_6.1_SOL2.mat
    │       │   │   │       │   ├── testcellnest_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testcellnest_7.1_GLNX86.mat
    │       │   │   │       │   ├── testcellnest_7.4_GLNX86.mat
    │       │   │   │       │   ├── testcomplex_4.2c_SOL2.mat
    │       │   │   │       │   ├── testcomplex_6.1_SOL2.mat
    │       │   │   │       │   ├── testcomplex_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testcomplex_7.1_GLNX86.mat
    │       │   │   │       │   ├── testcomplex_7.4_GLNX86.mat
    │       │   │   │       │   ├── testdouble_4.2c_SOL2.mat
    │       │   │   │       │   ├── testdouble_6.1_SOL2.mat
    │       │   │   │       │   ├── testdouble_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testdouble_7.1_GLNX86.mat
    │       │   │   │       │   ├── testdouble_7.4_GLNX86.mat
    │       │   │   │       │   ├── testemptycell_5.3_SOL2.mat
    │       │   │   │       │   ├── testemptycell_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testemptycell_7.1_GLNX86.mat
    │       │   │   │       │   ├── testemptycell_7.4_GLNX86.mat
    │       │   │   │       │   ├── testfunc_7.4_GLNX86.mat
    │       │   │   │       │   ├── testhdf5_7.4_GLNX86.mat
    │       │   │   │       │   ├── testmatrix_4.2c_SOL2.mat
    │       │   │   │       │   ├── testmatrix_6.1_SOL2.mat
    │       │   │   │       │   ├── testmatrix_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testmatrix_7.1_GLNX86.mat
    │       │   │   │       │   ├── testmatrix_7.4_GLNX86.mat
    │       │   │   │       │   ├── testminus_4.2c_SOL2.mat
    │       │   │   │       │   ├── testminus_6.1_SOL2.mat
    │       │   │   │       │   ├── testminus_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testminus_7.1_GLNX86.mat
    │       │   │   │       │   ├── testminus_7.4_GLNX86.mat
    │       │   │   │       │   ├── testmulti_4.2c_SOL2.mat
    │       │   │   │       │   ├── testmulti_7.1_GLNX86.mat
    │       │   │   │       │   ├── testmulti_7.4_GLNX86.mat
    │       │   │   │       │   ├── testobject_6.1_SOL2.mat
    │       │   │   │       │   ├── testobject_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testobject_7.1_GLNX86.mat
    │       │   │   │       │   ├── testobject_7.4_GLNX86.mat
    │       │   │   │       │   ├── testonechar_4.2c_SOL2.mat
    │       │   │   │       │   ├── testonechar_6.1_SOL2.mat
    │       │   │   │       │   ├── testonechar_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testonechar_7.1_GLNX86.mat
    │       │   │   │       │   ├── testonechar_7.4_GLNX86.mat
    │       │   │   │       │   ├── testscalarcell_7.4_GLNX86.mat
    │       │   │   │       │   ├── testsimplecell.mat
    │       │   │   │       │   ├── testsparse_4.2c_SOL2.mat
    │       │   │   │       │   ├── testsparse_6.1_SOL2.mat
    │       │   │   │       │   ├── testsparse_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testsparse_7.1_GLNX86.mat
    │       │   │   │       │   ├── testsparse_7.4_GLNX86.mat
    │       │   │   │       │   ├── testsparsecomplex_4.2c_SOL2.mat
    │       │   │   │       │   ├── testsparsecomplex_6.1_SOL2.mat
    │       │   │   │       │   ├── testsparsecomplex_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── testsparsecomplex_7.1_GLNX86.mat
    │       │   │   │       │   ├── testsparsecomplex_7.4_GLNX86.mat
    │       │   │   │       │   ├── testsparsefloat_7.4_GLNX86.mat
    │       │   │   │       │   ├── teststring_4.2c_SOL2.mat
    │       │   │   │       │   ├── teststring_6.1_SOL2.mat
    │       │   │   │       │   ├── teststring_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── teststring_7.1_GLNX86.mat
    │       │   │   │       │   ├── teststring_7.4_GLNX86.mat
    │       │   │   │       │   ├── teststringarray_4.2c_SOL2.mat
    │       │   │   │       │   ├── teststringarray_6.1_SOL2.mat
    │       │   │   │       │   ├── teststringarray_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── teststringarray_7.1_GLNX86.mat
    │       │   │   │       │   ├── teststringarray_7.4_GLNX86.mat
    │       │   │   │       │   ├── teststruct_6.1_SOL2.mat
    │       │   │   │       │   ├── teststruct_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── teststruct_7.1_GLNX86.mat
    │       │   │   │       │   ├── teststruct_7.4_GLNX86.mat
    │       │   │   │       │   ├── teststructarr_6.1_SOL2.mat
    │       │   │   │       │   ├── teststructarr_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── teststructarr_7.1_GLNX86.mat
    │       │   │   │       │   ├── teststructarr_7.4_GLNX86.mat
    │       │   │   │       │   ├── teststructnest_6.1_SOL2.mat
    │       │   │   │       │   ├── teststructnest_6.5.1_GLNX86.mat
    │       │   │   │       │   ├── teststructnest_7.1_GLNX86.mat
    │       │   │   │       │   ├── teststructnest_7.4_GLNX86.mat
    │       │   │   │       │   ├── testunicode_7.1_GLNX86.mat
    │       │   │   │       │   ├── testunicode_7.4_GLNX86.mat
    │       │   │   │       │   └── testvec_4_GLNX86.mat
    │       │   │   │       ├── test_byteordercodes.py
    │       │   │   │       ├── test_mio.py
    │       │   │   │       ├── test_mio5_utils.py
    │       │   │   │       ├── test_mio_funcs.py
    │       │   │   │       ├── test_mio_utils.py
    │       │   │   │       ├── test_miobase.py
    │       │   │   │       ├── test_pathological.py
    │       │   │   │       └── test_streams.py
    │       │   │   ├── mmio.py
    │       │   │   ├── netcdf.py
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── test_fortran.cpython-312.pyc
    │       │   │   │   │   ├── test_idl.cpython-312.pyc
    │       │   │   │   │   ├── test_mmio.cpython-312.pyc
    │       │   │   │   │   ├── test_netcdf.cpython-312.pyc
    │       │   │   │   │   ├── test_paths.cpython-312.pyc
    │       │   │   │   │   └── test_wavfile.cpython-312.pyc
    │       │   │   │   ├── data
    │       │   │   │   │   ├── Transparent Busy.ani
    │       │   │   │   │   ├── array_float32_1d.sav
    │       │   │   │   │   ├── array_float32_2d.sav
    │       │   │   │   │   ├── array_float32_3d.sav
    │       │   │   │   │   ├── array_float32_4d.sav
    │       │   │   │   │   ├── array_float32_5d.sav
    │       │   │   │   │   ├── array_float32_6d.sav
    │       │   │   │   │   ├── array_float32_7d.sav
    │       │   │   │   │   ├── array_float32_8d.sav
    │       │   │   │   │   ├── array_float32_pointer_1d.sav
    │       │   │   │   │   ├── array_float32_pointer_2d.sav
    │       │   │   │   │   ├── array_float32_pointer_3d.sav
    │       │   │   │   │   ├── array_float32_pointer_4d.sav
    │       │   │   │   │   ├── array_float32_pointer_5d.sav
    │       │   │   │   │   ├── array_float32_pointer_6d.sav
    │       │   │   │   │   ├── array_float32_pointer_7d.sav
    │       │   │   │   │   ├── array_float32_pointer_8d.sav
    │       │   │   │   │   ├── example_1.nc
    │       │   │   │   │   ├── example_2.nc
    │       │   │   │   │   ├── example_3_maskedvals.nc
    │       │   │   │   │   ├── fortran-3x3d-2i.dat
    │       │   │   │   │   ├── fortran-mixed.dat
    │       │   │   │   │   ├── fortran-sf8-11x1x10.dat
    │       │   │   │   │   ├── fortran-sf8-15x10x22.dat
    │       │   │   │   │   ├── fortran-sf8-1x1x1.dat
    │       │   │   │   │   ├── fortran-sf8-1x1x5.dat
    │       │   │   │   │   ├── fortran-sf8-1x1x7.dat
    │       │   │   │   │   ├── fortran-sf8-1x3x5.dat
    │       │   │   │   │   ├── fortran-si4-11x1x10.dat
    │       │   │   │   │   ├── fortran-si4-15x10x22.dat
    │       │   │   │   │   ├── fortran-si4-1x1x1.dat
    │       │   │   │   │   ├── fortran-si4-1x1x5.dat
    │       │   │   │   │   ├── fortran-si4-1x1x7.dat
    │       │   │   │   │   ├── fortran-si4-1x3x5.dat
    │       │   │   │   │   ├── invalid_pointer.sav
    │       │   │   │   │   ├── null_pointer.sav
    │       │   │   │   │   ├── scalar_byte.sav
    │       │   │   │   │   ├── scalar_byte_descr.sav
    │       │   │   │   │   ├── scalar_complex32.sav
    │       │   │   │   │   ├── scalar_complex64.sav
    │       │   │   │   │   ├── scalar_float32.sav
    │       │   │   │   │   ├── scalar_float64.sav
    │       │   │   │   │   ├── scalar_heap_pointer.sav
    │       │   │   │   │   ├── scalar_int16.sav
    │       │   │   │   │   ├── scalar_int32.sav
    │       │   │   │   │   ├── scalar_int64.sav
    │       │   │   │   │   ├── scalar_string.sav
    │       │   │   │   │   ├── scalar_uint16.sav
    │       │   │   │   │   ├── scalar_uint32.sav
    │       │   │   │   │   ├── scalar_uint64.sav
    │       │   │   │   │   ├── struct_arrays.sav
    │       │   │   │   │   ├── struct_arrays_byte_idl80.sav
    │       │   │   │   │   ├── struct_arrays_replicated.sav
    │       │   │   │   │   ├── struct_arrays_replicated_3d.sav
    │       │   │   │   │   ├── struct_inherit.sav
    │       │   │   │   │   ├── struct_pointer_arrays.sav
    │       │   │   │   │   ├── struct_pointer_arrays_replicated.sav
    │       │   │   │   │   ├── struct_pointer_arrays_replicated_3d.sav
    │       │   │   │   │   ├── struct_pointers.sav
    │       │   │   │   │   ├── struct_pointers_replicated.sav
    │       │   │   │   │   ├── struct_pointers_replicated_3d.sav
    │       │   │   │   │   ├── struct_scalars.sav
    │       │   │   │   │   ├── struct_scalars_replicated.sav
    │       │   │   │   │   ├── struct_scalars_replicated_3d.sav
    │       │   │   │   │   ├── test-1234Hz-le-1ch-10S-20bit-extra.wav
    │       │   │   │   │   ├── test-44100Hz-2ch-32bit-float-be.wav
    │       │   │   │   │   ├── test-44100Hz-2ch-32bit-float-le.wav
    │       │   │   │   │   ├── test-44100Hz-be-1ch-4bytes.wav
    │       │   │   │   │   ├── test-44100Hz-le-1ch-4bytes-early-eof-no-data.wav
    │       │   │   │   │   ├── test-44100Hz-le-1ch-4bytes-early-eof.wav
    │       │   │   │   │   ├── test-44100Hz-le-1ch-4bytes-incomplete-chunk.wav
    │       │   │   │   │   ├── test-44100Hz-le-1ch-4bytes-rf64.wav
    │       │   │   │   │   ├── test-44100Hz-le-1ch-4bytes.wav
    │       │   │   │   │   ├── test-48000Hz-2ch-64bit-float-le-wavex.wav
    │       │   │   │   │   ├── test-8000Hz-be-3ch-5S-24bit.wav
    │       │   │   │   │   ├── test-8000Hz-le-1ch-1byte-ulaw.wav
    │       │   │   │   │   ├── test-8000Hz-le-2ch-1byteu.wav
    │       │   │   │   │   ├── test-8000Hz-le-3ch-5S-24bit-inconsistent.wav
    │       │   │   │   │   ├── test-8000Hz-le-3ch-5S-24bit-rf64.wav
    │       │   │   │   │   ├── test-8000Hz-le-3ch-5S-24bit.wav
    │       │   │   │   │   ├── test-8000Hz-le-3ch-5S-36bit.wav
    │       │   │   │   │   ├── test-8000Hz-le-3ch-5S-45bit.wav
    │       │   │   │   │   ├── test-8000Hz-le-3ch-5S-53bit.wav
    │       │   │   │   │   ├── test-8000Hz-le-3ch-5S-64bit.wav
    │       │   │   │   │   ├── test-8000Hz-le-4ch-9S-12bit.wav
    │       │   │   │   │   ├── test-8000Hz-le-5ch-9S-5bit.wav
    │       │   │   │   │   └── various_compressed.sav
    │       │   │   │   ├── test_fortran.py
    │       │   │   │   ├── test_idl.py
    │       │   │   │   ├── test_mmio.py
    │       │   │   │   ├── test_netcdf.py
    │       │   │   │   ├── test_paths.py
    │       │   │   │   └── test_wavfile.py
    │       │   │   └── wavfile.py
    │       │   ├── linalg
    │       │   │   ├── __init__.pxd
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _basic.cpython-312.pyc
    │       │   │   │   ├── _decomp.cpython-312.pyc
    │       │   │   │   ├── _decomp_cholesky.cpython-312.pyc
    │       │   │   │   ├── _decomp_cossin.cpython-312.pyc
    │       │   │   │   ├── _decomp_ldl.cpython-312.pyc
    │       │   │   │   ├── _decomp_lu.cpython-312.pyc
    │       │   │   │   ├── _decomp_polar.cpython-312.pyc
    │       │   │   │   ├── _decomp_qr.cpython-312.pyc
    │       │   │   │   ├── _decomp_qz.cpython-312.pyc
    │       │   │   │   ├── _decomp_schur.cpython-312.pyc
    │       │   │   │   ├── _decomp_svd.cpython-312.pyc
    │       │   │   │   ├── _expm_frechet.cpython-312.pyc
    │       │   │   │   ├── _matfuncs.cpython-312.pyc
    │       │   │   │   ├── _matfuncs_inv_ssq.cpython-312.pyc
    │       │   │   │   ├── _matfuncs_sqrtm.cpython-312.pyc
    │       │   │   │   ├── _misc.cpython-312.pyc
    │       │   │   │   ├── _procrustes.cpython-312.pyc
    │       │   │   │   ├── _sketches.cpython-312.pyc
    │       │   │   │   ├── _solvers.cpython-312.pyc
    │       │   │   │   ├── _special_matrices.cpython-312.pyc
    │       │   │   │   ├── _testutils.cpython-312.pyc
    │       │   │   │   ├── basic.cpython-312.pyc
    │       │   │   │   ├── blas.cpython-312.pyc
    │       │   │   │   ├── decomp.cpython-312.pyc
    │       │   │   │   ├── decomp_cholesky.cpython-312.pyc
    │       │   │   │   ├── decomp_lu.cpython-312.pyc
    │       │   │   │   ├── decomp_qr.cpython-312.pyc
    │       │   │   │   ├── decomp_schur.cpython-312.pyc
    │       │   │   │   ├── decomp_svd.cpython-312.pyc
    │       │   │   │   ├── interpolative.cpython-312.pyc
    │       │   │   │   ├── lapack.cpython-312.pyc
    │       │   │   │   ├── matfuncs.cpython-312.pyc
    │       │   │   │   ├── misc.cpython-312.pyc
    │       │   │   │   └── special_matrices.cpython-312.pyc
    │       │   │   ├── _basic.py
    │       │   │   ├── _blas_subroutines.h
    │       │   │   ├── _cythonized_array_utils.cp312-win_amd64.dll.a
    │       │   │   ├── _cythonized_array_utils.cp312-win_amd64.pyd
    │       │   │   ├── _cythonized_array_utils.pxd
    │       │   │   ├── _cythonized_array_utils.pyi
    │       │   │   ├── _decomp.py
    │       │   │   ├── _decomp_cholesky.py
    │       │   │   ├── _decomp_cossin.py
    │       │   │   ├── _decomp_interpolative.cp312-win_amd64.dll.a
    │       │   │   ├── _decomp_interpolative.cp312-win_amd64.pyd
    │       │   │   ├── _decomp_ldl.py
    │       │   │   ├── _decomp_lu.py
    │       │   │   ├── _decomp_lu_cython.cp312-win_amd64.dll.a
    │       │   │   ├── _decomp_lu_cython.cp312-win_amd64.pyd
    │       │   │   ├── _decomp_lu_cython.pyi
    │       │   │   ├── _decomp_polar.py
    │       │   │   ├── _decomp_qr.py
    │       │   │   ├── _decomp_qz.py
    │       │   │   ├── _decomp_schur.py
    │       │   │   ├── _decomp_svd.py
    │       │   │   ├── _decomp_update.cp312-win_amd64.dll.a
    │       │   │   ├── _decomp_update.cp312-win_amd64.pyd
    │       │   │   ├── _expm_frechet.py
    │       │   │   ├── _fblas.cp312-win_amd64.dll.a
    │       │   │   ├── _fblas.cp312-win_amd64.pyd
    │       │   │   ├── _flapack.cp312-win_amd64.dll.a
    │       │   │   ├── _flapack.cp312-win_amd64.pyd
    │       │   │   ├── _lapack_subroutines.h
    │       │   │   ├── _linalg_pythran.cp312-win_amd64.dll.a
    │       │   │   ├── _linalg_pythran.cp312-win_amd64.pyd
    │       │   │   ├── _matfuncs.py
    │       │   │   ├── _matfuncs_expm.cp312-win_amd64.dll.a
    │       │   │   ├── _matfuncs_expm.cp312-win_amd64.pyd
    │       │   │   ├── _matfuncs_expm.pyi
    │       │   │   ├── _matfuncs_inv_ssq.py
    │       │   │   ├── _matfuncs_schur_sqrtm.cp312-win_amd64.dll.a
    │       │   │   ├── _matfuncs_schur_sqrtm.cp312-win_amd64.pyd
    │       │   │   ├── _matfuncs_sqrtm.py
    │       │   │   ├── _matfuncs_sqrtm_triu.cp312-win_amd64.dll.a
    │       │   │   ├── _matfuncs_sqrtm_triu.cp312-win_amd64.pyd
    │       │   │   ├── _misc.py
    │       │   │   ├── _procrustes.py
    │       │   │   ├── _sketches.py
    │       │   │   ├── _solve_toeplitz.cp312-win_amd64.dll.a
    │       │   │   ├── _solve_toeplitz.cp312-win_amd64.pyd
    │       │   │   ├── _solvers.py
    │       │   │   ├── _special_matrices.py
    │       │   │   ├── _testutils.py
    │       │   │   ├── basic.py
    │       │   │   ├── blas.py
    │       │   │   ├── cython_blas.cp312-win_amd64.dll.a
    │       │   │   ├── cython_blas.cp312-win_amd64.pyd
    │       │   │   ├── cython_blas.pxd
    │       │   │   ├── cython_blas.pyx
    │       │   │   ├── cython_lapack.cp312-win_amd64.dll.a
    │       │   │   ├── cython_lapack.cp312-win_amd64.pyd
    │       │   │   ├── cython_lapack.pxd
    │       │   │   ├── cython_lapack.pyx
    │       │   │   ├── decomp.py
    │       │   │   ├── decomp_cholesky.py
    │       │   │   ├── decomp_lu.py
    │       │   │   ├── decomp_qr.py
    │       │   │   ├── decomp_schur.py
    │       │   │   ├── decomp_svd.py
    │       │   │   ├── interpolative.py
    │       │   │   ├── lapack.py
    │       │   │   ├── matfuncs.py
    │       │   │   ├── misc.py
    │       │   │   ├── special_matrices.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_basic.cpython-312.pyc
    │       │   │       │   ├── test_batch.cpython-312.pyc
    │       │   │       │   ├── test_blas.cpython-312.pyc
    │       │   │       │   ├── test_cython_blas.cpython-312.pyc
    │       │   │       │   ├── test_cython_lapack.cpython-312.pyc
    │       │   │       │   ├── test_cythonized_array_utils.cpython-312.pyc
    │       │   │       │   ├── test_decomp.cpython-312.pyc
    │       │   │       │   ├── test_decomp_cholesky.cpython-312.pyc
    │       │   │       │   ├── test_decomp_cossin.cpython-312.pyc
    │       │   │       │   ├── test_decomp_ldl.cpython-312.pyc
    │       │   │       │   ├── test_decomp_lu.cpython-312.pyc
    │       │   │       │   ├── test_decomp_polar.cpython-312.pyc
    │       │   │       │   ├── test_decomp_update.cpython-312.pyc
    │       │   │       │   ├── test_extending.cpython-312.pyc
    │       │   │       │   ├── test_fblas.cpython-312.pyc
    │       │   │       │   ├── test_interpolative.cpython-312.pyc
    │       │   │       │   ├── test_lapack.cpython-312.pyc
    │       │   │       │   ├── test_matfuncs.cpython-312.pyc
    │       │   │       │   ├── test_matmul_toeplitz.cpython-312.pyc
    │       │   │       │   ├── test_procrustes.cpython-312.pyc
    │       │   │       │   ├── test_sketches.cpython-312.pyc
    │       │   │       │   ├── test_solve_toeplitz.cpython-312.pyc
    │       │   │       │   ├── test_solvers.cpython-312.pyc
    │       │   │       │   └── test_special_matrices.cpython-312.pyc
    │       │   │       ├── _cython_examples
    │       │   │       │   ├── extending.pyx
    │       │   │       │   └── meson.build
    │       │   │       ├── data
    │       │   │       │   ├── carex_15_data.npz
    │       │   │       │   ├── carex_18_data.npz
    │       │   │       │   ├── carex_19_data.npz
    │       │   │       │   ├── carex_20_data.npz
    │       │   │       │   ├── carex_6_data.npz
    │       │   │       │   └── gendare_20170120_data.npz
    │       │   │       ├── test_basic.py
    │       │   │       ├── test_batch.py
    │       │   │       ├── test_blas.py
    │       │   │       ├── test_cython_blas.py
    │       │   │       ├── test_cython_lapack.py
    │       │   │       ├── test_cythonized_array_utils.py
    │       │   │       ├── test_decomp.py
    │       │   │       ├── test_decomp_cholesky.py
    │       │   │       ├── test_decomp_cossin.py
    │       │   │       ├── test_decomp_ldl.py
    │       │   │       ├── test_decomp_lu.py
    │       │   │       ├── test_decomp_polar.py
    │       │   │       ├── test_decomp_update.py
    │       │   │       ├── test_extending.py
    │       │   │       ├── test_fblas.py
    │       │   │       ├── test_interpolative.py
    │       │   │       ├── test_lapack.py
    │       │   │       ├── test_matfuncs.py
    │       │   │       ├── test_matmul_toeplitz.py
    │       │   │       ├── test_procrustes.py
    │       │   │       ├── test_sketches.py
    │       │   │       ├── test_solve_toeplitz.py
    │       │   │       ├── test_solvers.py
    │       │   │       └── test_special_matrices.py
    │       │   ├── misc
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── common.cpython-312.pyc
    │       │   │   │   └── doccer.cpython-312.pyc
    │       │   │   ├── common.py
    │       │   │   └── doccer.py
    │       │   ├── ndimage
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _delegators.cpython-312.pyc
    │       │   │   │   ├── _filters.cpython-312.pyc
    │       │   │   │   ├── _fourier.cpython-312.pyc
    │       │   │   │   ├── _interpolation.cpython-312.pyc
    │       │   │   │   ├── _measurements.cpython-312.pyc
    │       │   │   │   ├── _morphology.cpython-312.pyc
    │       │   │   │   ├── _ndimage_api.cpython-312.pyc
    │       │   │   │   ├── _ni_docstrings.cpython-312.pyc
    │       │   │   │   ├── _ni_support.cpython-312.pyc
    │       │   │   │   ├── _support_alternative_backends.cpython-312.pyc
    │       │   │   │   ├── filters.cpython-312.pyc
    │       │   │   │   ├── fourier.cpython-312.pyc
    │       │   │   │   ├── interpolation.cpython-312.pyc
    │       │   │   │   ├── measurements.cpython-312.pyc
    │       │   │   │   └── morphology.cpython-312.pyc
    │       │   │   ├── _ctest.cp312-win_amd64.dll.a
    │       │   │   ├── _ctest.cp312-win_amd64.pyd
    │       │   │   ├── _cytest.cp312-win_amd64.dll.a
    │       │   │   ├── _cytest.cp312-win_amd64.pyd
    │       │   │   ├── _delegators.py
    │       │   │   ├── _filters.py
    │       │   │   ├── _fourier.py
    │       │   │   ├── _interpolation.py
    │       │   │   ├── _measurements.py
    │       │   │   ├── _morphology.py
    │       │   │   ├── _nd_image.cp312-win_amd64.dll.a
    │       │   │   ├── _nd_image.cp312-win_amd64.pyd
    │       │   │   ├── _ndimage_api.py
    │       │   │   ├── _ni_docstrings.py
    │       │   │   ├── _ni_label.cp312-win_amd64.dll.a
    │       │   │   ├── _ni_label.cp312-win_amd64.pyd
    │       │   │   ├── _ni_support.py
    │       │   │   ├── _rank_filter_1d.cp312-win_amd64.dll.a
    │       │   │   ├── _rank_filter_1d.cp312-win_amd64.pyd
    │       │   │   ├── _support_alternative_backends.py
    │       │   │   ├── filters.py
    │       │   │   ├── fourier.py
    │       │   │   ├── interpolation.py
    │       │   │   ├── measurements.py
    │       │   │   ├── morphology.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_c_api.cpython-312.pyc
    │       │   │       │   ├── test_datatypes.cpython-312.pyc
    │       │   │       │   ├── test_filters.cpython-312.pyc
    │       │   │       │   ├── test_fourier.cpython-312.pyc
    │       │   │       │   ├── test_interpolation.cpython-312.pyc
    │       │   │       │   ├── test_measurements.cpython-312.pyc
    │       │   │       │   ├── test_morphology.cpython-312.pyc
    │       │   │       │   ├── test_ni_support.cpython-312.pyc
    │       │   │       │   └── test_splines.cpython-312.pyc
    │       │   │       ├── data
    │       │   │       │   ├── label_inputs.txt
    │       │   │       │   ├── label_results.txt
    │       │   │       │   └── label_strels.txt
    │       │   │       ├── dots.png
    │       │   │       ├── test_c_api.py
    │       │   │       ├── test_datatypes.py
    │       │   │       ├── test_filters.py
    │       │   │       ├── test_fourier.py
    │       │   │       ├── test_interpolation.py
    │       │   │       ├── test_measurements.py
    │       │   │       ├── test_morphology.py
    │       │   │       ├── test_ni_support.py
    │       │   │       └── test_splines.py
    │       │   ├── odr
    │       │   │   ├── __init__.py
    │       │   │   ├── __odrpack.cp312-win_amd64.dll.a
    │       │   │   ├── __odrpack.cp312-win_amd64.pyd
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _add_newdocs.cpython-312.pyc
    │       │   │   │   ├── _models.cpython-312.pyc
    │       │   │   │   ├── _odrpack.cpython-312.pyc
    │       │   │   │   ├── models.cpython-312.pyc
    │       │   │   │   └── odrpack.cpython-312.pyc
    │       │   │   ├── _add_newdocs.py
    │       │   │   ├── _models.py
    │       │   │   ├── _odrpack.py
    │       │   │   ├── models.py
    │       │   │   ├── odrpack.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   └── test_odr.cpython-312.pyc
    │       │   │       └── test_odr.py
    │       │   ├── optimize
    │       │   │   ├── __init__.pxd
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _basinhopping.cpython-312.pyc
    │       │   │   │   ├── _bracket.cpython-312.pyc
    │       │   │   │   ├── _chandrupatla.cpython-312.pyc
    │       │   │   │   ├── _cobyla_py.cpython-312.pyc
    │       │   │   │   ├── _cobyqa_py.cpython-312.pyc
    │       │   │   │   ├── _constraints.cpython-312.pyc
    │       │   │   │   ├── _dcsrch.cpython-312.pyc
    │       │   │   │   ├── _differentiable_functions.cpython-312.pyc
    │       │   │   │   ├── _differentialevolution.cpython-312.pyc
    │       │   │   │   ├── _direct_py.cpython-312.pyc
    │       │   │   │   ├── _dual_annealing.cpython-312.pyc
    │       │   │   │   ├── _elementwise.cpython-312.pyc
    │       │   │   │   ├── _hessian_update_strategy.cpython-312.pyc
    │       │   │   │   ├── _isotonic.cpython-312.pyc
    │       │   │   │   ├── _lbfgsb_py.cpython-312.pyc
    │       │   │   │   ├── _linesearch.cpython-312.pyc
    │       │   │   │   ├── _linprog.cpython-312.pyc
    │       │   │   │   ├── _linprog_doc.cpython-312.pyc
    │       │   │   │   ├── _linprog_highs.cpython-312.pyc
    │       │   │   │   ├── _linprog_ip.cpython-312.pyc
    │       │   │   │   ├── _linprog_rs.cpython-312.pyc
    │       │   │   │   ├── _linprog_simplex.cpython-312.pyc
    │       │   │   │   ├── _linprog_util.cpython-312.pyc
    │       │   │   │   ├── _milp.cpython-312.pyc
    │       │   │   │   ├── _minimize.cpython-312.pyc
    │       │   │   │   ├── _minpack_py.cpython-312.pyc
    │       │   │   │   ├── _nnls.cpython-312.pyc
    │       │   │   │   ├── _nonlin.cpython-312.pyc
    │       │   │   │   ├── _numdiff.cpython-312.pyc
    │       │   │   │   ├── _optimize.cpython-312.pyc
    │       │   │   │   ├── _qap.cpython-312.pyc
    │       │   │   │   ├── _remove_redundancy.cpython-312.pyc
    │       │   │   │   ├── _root.cpython-312.pyc
    │       │   │   │   ├── _root_scalar.cpython-312.pyc
    │       │   │   │   ├── _shgo.cpython-312.pyc
    │       │   │   │   ├── _slsqp_py.cpython-312.pyc
    │       │   │   │   ├── _spectral.cpython-312.pyc
    │       │   │   │   ├── _tnc.cpython-312.pyc
    │       │   │   │   ├── _trustregion.cpython-312.pyc
    │       │   │   │   ├── _trustregion_dogleg.cpython-312.pyc
    │       │   │   │   ├── _trustregion_exact.cpython-312.pyc
    │       │   │   │   ├── _trustregion_krylov.cpython-312.pyc
    │       │   │   │   ├── _trustregion_ncg.cpython-312.pyc
    │       │   │   │   ├── _tstutils.cpython-312.pyc
    │       │   │   │   ├── _zeros_py.cpython-312.pyc
    │       │   │   │   ├── cobyla.cpython-312.pyc
    │       │   │   │   ├── elementwise.cpython-312.pyc
    │       │   │   │   ├── lbfgsb.cpython-312.pyc
    │       │   │   │   ├── linesearch.cpython-312.pyc
    │       │   │   │   ├── minpack.cpython-312.pyc
    │       │   │   │   ├── minpack2.cpython-312.pyc
    │       │   │   │   ├── moduleTNC.cpython-312.pyc
    │       │   │   │   ├── nonlin.cpython-312.pyc
    │       │   │   │   ├── optimize.cpython-312.pyc
    │       │   │   │   ├── slsqp.cpython-312.pyc
    │       │   │   │   ├── tnc.cpython-312.pyc
    │       │   │   │   └── zeros.cpython-312.pyc
    │       │   │   ├── _basinhopping.py
    │       │   │   ├── _bglu_dense.cp312-win_amd64.dll.a
    │       │   │   ├── _bglu_dense.cp312-win_amd64.pyd
    │       │   │   ├── _bracket.py
    │       │   │   ├── _chandrupatla.py
    │       │   │   ├── _cobyla_py.py
    │       │   │   ├── _cobyqa_py.py
    │       │   │   ├── _constraints.py
    │       │   │   ├── _dcsrch.py
    │       │   │   ├── _differentiable_functions.py
    │       │   │   ├── _differentialevolution.py
    │       │   │   ├── _direct.cp312-win_amd64.dll.a
    │       │   │   ├── _direct.cp312-win_amd64.pyd
    │       │   │   ├── _direct_py.py
    │       │   │   ├── _dual_annealing.py
    │       │   │   ├── _elementwise.py
    │       │   │   ├── _group_columns.cp312-win_amd64.dll.a
    │       │   │   ├── _group_columns.cp312-win_amd64.pyd
    │       │   │   ├── _hessian_update_strategy.py
    │       │   │   ├── _highspy
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   └── _highs_wrapper.cpython-312.pyc
    │       │   │   │   ├── _core.cp312-win_amd64.dll.a
    │       │   │   │   ├── _core.cp312-win_amd64.pyd
    │       │   │   │   ├── _highs_options.cp312-win_amd64.dll.a
    │       │   │   │   ├── _highs_options.cp312-win_amd64.pyd
    │       │   │   │   └── _highs_wrapper.py
    │       │   │   ├── _isotonic.py
    │       │   │   ├── _lbfgsb.cp312-win_amd64.dll.a
    │       │   │   ├── _lbfgsb.cp312-win_amd64.pyd
    │       │   │   ├── _lbfgsb_py.py
    │       │   │   ├── _linesearch.py
    │       │   │   ├── _linprog.py
    │       │   │   ├── _linprog_doc.py
    │       │   │   ├── _linprog_highs.py
    │       │   │   ├── _linprog_ip.py
    │       │   │   ├── _linprog_rs.py
    │       │   │   ├── _linprog_simplex.py
    │       │   │   ├── _linprog_util.py
    │       │   │   ├── _lsap.cp312-win_amd64.dll.a
    │       │   │   ├── _lsap.cp312-win_amd64.pyd
    │       │   │   ├── _lsq
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── bvls.cpython-312.pyc
    │       │   │   │   │   ├── common.cpython-312.pyc
    │       │   │   │   │   ├── dogbox.cpython-312.pyc
    │       │   │   │   │   ├── least_squares.cpython-312.pyc
    │       │   │   │   │   ├── lsq_linear.cpython-312.pyc
    │       │   │   │   │   ├── trf.cpython-312.pyc
    │       │   │   │   │   └── trf_linear.cpython-312.pyc
    │       │   │   │   ├── bvls.py
    │       │   │   │   ├── common.py
    │       │   │   │   ├── dogbox.py
    │       │   │   │   ├── givens_elimination.cp312-win_amd64.dll.a
    │       │   │   │   ├── givens_elimination.cp312-win_amd64.pyd
    │       │   │   │   ├── least_squares.py
    │       │   │   │   ├── lsq_linear.py
    │       │   │   │   ├── trf.py
    │       │   │   │   └── trf_linear.py
    │       │   │   ├── _milp.py
    │       │   │   ├── _minimize.py
    │       │   │   ├── _minpack.cp312-win_amd64.dll.a
    │       │   │   ├── _minpack.cp312-win_amd64.pyd
    │       │   │   ├── _minpack_py.py
    │       │   │   ├── _moduleTNC.cp312-win_amd64.dll.a
    │       │   │   ├── _moduleTNC.cp312-win_amd64.pyd
    │       │   │   ├── _nnls.py
    │       │   │   ├── _nonlin.py
    │       │   │   ├── _numdiff.py
    │       │   │   ├── _optimize.py
    │       │   │   ├── _pava_pybind.cp312-win_amd64.dll.a
    │       │   │   ├── _pava_pybind.cp312-win_amd64.pyd
    │       │   │   ├── _qap.py
    │       │   │   ├── _remove_redundancy.py
    │       │   │   ├── _root.py
    │       │   │   ├── _root_scalar.py
    │       │   │   ├── _shgo.py
    │       │   │   ├── _shgo_lib
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _complex.cpython-312.pyc
    │       │   │   │   │   └── _vertex.cpython-312.pyc
    │       │   │   │   ├── _complex.py
    │       │   │   │   └── _vertex.py
    │       │   │   ├── _slsqp_py.py
    │       │   │   ├── _slsqplib.cp312-win_amd64.dll.a
    │       │   │   ├── _slsqplib.cp312-win_amd64.pyd
    │       │   │   ├── _spectral.py
    │       │   │   ├── _tnc.py
    │       │   │   ├── _trlib
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   └── __init__.cpython-312.pyc
    │       │   │   │   ├── _trlib.cp312-win_amd64.dll.a
    │       │   │   │   └── _trlib.cp312-win_amd64.pyd
    │       │   │   ├── _trustregion.py
    │       │   │   ├── _trustregion_constr
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── canonical_constraint.cpython-312.pyc
    │       │   │   │   │   ├── equality_constrained_sqp.cpython-312.pyc
    │       │   │   │   │   ├── minimize_trustregion_constr.cpython-312.pyc
    │       │   │   │   │   ├── projections.cpython-312.pyc
    │       │   │   │   │   ├── qp_subproblem.cpython-312.pyc
    │       │   │   │   │   ├── report.cpython-312.pyc
    │       │   │   │   │   └── tr_interior_point.cpython-312.pyc
    │       │   │   │   ├── canonical_constraint.py
    │       │   │   │   ├── equality_constrained_sqp.py
    │       │   │   │   ├── minimize_trustregion_constr.py
    │       │   │   │   ├── projections.py
    │       │   │   │   ├── qp_subproblem.py
    │       │   │   │   ├── report.py
    │       │   │   │   ├── tests
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── test_canonical_constraint.cpython-312.pyc
    │       │   │   │   │   │   ├── test_nested_minimize.cpython-312.pyc
    │       │   │   │   │   │   ├── test_projections.cpython-312.pyc
    │       │   │   │   │   │   ├── test_qp_subproblem.cpython-312.pyc
    │       │   │   │   │   │   └── test_report.cpython-312.pyc
    │       │   │   │   │   ├── test_canonical_constraint.py
    │       │   │   │   │   ├── test_nested_minimize.py
    │       │   │   │   │   ├── test_projections.py
    │       │   │   │   │   ├── test_qp_subproblem.py
    │       │   │   │   │   └── test_report.py
    │       │   │   │   └── tr_interior_point.py
    │       │   │   ├── _trustregion_dogleg.py
    │       │   │   ├── _trustregion_exact.py
    │       │   │   ├── _trustregion_krylov.py
    │       │   │   ├── _trustregion_ncg.py
    │       │   │   ├── _tstutils.py
    │       │   │   ├── _zeros.cp312-win_amd64.dll.a
    │       │   │   ├── _zeros.cp312-win_amd64.pyd
    │       │   │   ├── _zeros_py.py
    │       │   │   ├── cobyla.py
    │       │   │   ├── cython_optimize
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   └── __init__.cpython-312.pyc
    │       │   │   │   ├── _zeros.cp312-win_amd64.dll.a
    │       │   │   │   ├── _zeros.cp312-win_amd64.pyd
    │       │   │   │   ├── _zeros.pxd
    │       │   │   │   └── c_zeros.pxd
    │       │   │   ├── cython_optimize.pxd
    │       │   │   ├── elementwise.py
    │       │   │   ├── lbfgsb.py
    │       │   │   ├── linesearch.py
    │       │   │   ├── minpack.py
    │       │   │   ├── minpack2.py
    │       │   │   ├── moduleTNC.py
    │       │   │   ├── nonlin.py
    │       │   │   ├── optimize.py
    │       │   │   ├── slsqp.py
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── test__basinhopping.cpython-312.pyc
    │       │   │   │   │   ├── test__differential_evolution.cpython-312.pyc
    │       │   │   │   │   ├── test__dual_annealing.cpython-312.pyc
    │       │   │   │   │   ├── test__linprog_clean_inputs.cpython-312.pyc
    │       │   │   │   │   ├── test__numdiff.cpython-312.pyc
    │       │   │   │   │   ├── test__remove_redundancy.cpython-312.pyc
    │       │   │   │   │   ├── test__root.cpython-312.pyc
    │       │   │   │   │   ├── test__shgo.cpython-312.pyc
    │       │   │   │   │   ├── test__spectral.cpython-312.pyc
    │       │   │   │   │   ├── test_bracket.cpython-312.pyc
    │       │   │   │   │   ├── test_chandrupatla.cpython-312.pyc
    │       │   │   │   │   ├── test_cobyla.cpython-312.pyc
    │       │   │   │   │   ├── test_cobyqa.cpython-312.pyc
    │       │   │   │   │   ├── test_constraint_conversion.cpython-312.pyc
    │       │   │   │   │   ├── test_constraints.cpython-312.pyc
    │       │   │   │   │   ├── test_cython_optimize.cpython-312.pyc
    │       │   │   │   │   ├── test_differentiable_functions.cpython-312.pyc
    │       │   │   │   │   ├── test_direct.cpython-312.pyc
    │       │   │   │   │   ├── test_extending.cpython-312.pyc
    │       │   │   │   │   ├── test_hessian_update_strategy.cpython-312.pyc
    │       │   │   │   │   ├── test_isotonic_regression.cpython-312.pyc
    │       │   │   │   │   ├── test_lbfgsb_hessinv.cpython-312.pyc
    │       │   │   │   │   ├── test_lbfgsb_setulb.cpython-312.pyc
    │       │   │   │   │   ├── test_least_squares.cpython-312.pyc
    │       │   │   │   │   ├── test_linear_assignment.cpython-312.pyc
    │       │   │   │   │   ├── test_linesearch.cpython-312.pyc
    │       │   │   │   │   ├── test_linprog.cpython-312.pyc
    │       │   │   │   │   ├── test_lsq_common.cpython-312.pyc
    │       │   │   │   │   ├── test_lsq_linear.cpython-312.pyc
    │       │   │   │   │   ├── test_milp.cpython-312.pyc
    │       │   │   │   │   ├── test_minimize_constrained.cpython-312.pyc
    │       │   │   │   │   ├── test_minpack.cpython-312.pyc
    │       │   │   │   │   ├── test_nnls.cpython-312.pyc
    │       │   │   │   │   ├── test_nonlin.cpython-312.pyc
    │       │   │   │   │   ├── test_optimize.cpython-312.pyc
    │       │   │   │   │   ├── test_quadratic_assignment.cpython-312.pyc
    │       │   │   │   │   ├── test_regression.cpython-312.pyc
    │       │   │   │   │   ├── test_slsqp.cpython-312.pyc
    │       │   │   │   │   ├── test_tnc.cpython-312.pyc
    │       │   │   │   │   ├── test_trustregion.cpython-312.pyc
    │       │   │   │   │   ├── test_trustregion_exact.cpython-312.pyc
    │       │   │   │   │   ├── test_trustregion_krylov.cpython-312.pyc
    │       │   │   │   │   └── test_zeros.cpython-312.pyc
    │       │   │   │   ├── _cython_examples
    │       │   │   │   │   ├── extending.pyx
    │       │   │   │   │   └── meson.build
    │       │   │   │   ├── test__basinhopping.py
    │       │   │   │   ├── test__differential_evolution.py
    │       │   │   │   ├── test__dual_annealing.py
    │       │   │   │   ├── test__linprog_clean_inputs.py
    │       │   │   │   ├── test__numdiff.py
    │       │   │   │   ├── test__remove_redundancy.py
    │       │   │   │   ├── test__root.py
    │       │   │   │   ├── test__shgo.py
    │       │   │   │   ├── test__spectral.py
    │       │   │   │   ├── test_bracket.py
    │       │   │   │   ├── test_chandrupatla.py
    │       │   │   │   ├── test_cobyla.py
    │       │   │   │   ├── test_cobyqa.py
    │       │   │   │   ├── test_constraint_conversion.py
    │       │   │   │   ├── test_constraints.py
    │       │   │   │   ├── test_cython_optimize.py
    │       │   │   │   ├── test_differentiable_functions.py
    │       │   │   │   ├── test_direct.py
    │       │   │   │   ├── test_extending.py
    │       │   │   │   ├── test_hessian_update_strategy.py
    │       │   │   │   ├── test_isotonic_regression.py
    │       │   │   │   ├── test_lbfgsb_hessinv.py
    │       │   │   │   ├── test_lbfgsb_setulb.py
    │       │   │   │   ├── test_least_squares.py
    │       │   │   │   ├── test_linear_assignment.py
    │       │   │   │   ├── test_linesearch.py
    │       │   │   │   ├── test_linprog.py
    │       │   │   │   ├── test_lsq_common.py
    │       │   │   │   ├── test_lsq_linear.py
    │       │   │   │   ├── test_milp.py
    │       │   │   │   ├── test_minimize_constrained.py
    │       │   │   │   ├── test_minpack.py
    │       │   │   │   ├── test_nnls.py
    │       │   │   │   ├── test_nonlin.py
    │       │   │   │   ├── test_optimize.py
    │       │   │   │   ├── test_quadratic_assignment.py
    │       │   │   │   ├── test_regression.py
    │       │   │   │   ├── test_slsqp.py
    │       │   │   │   ├── test_tnc.py
    │       │   │   │   ├── test_trustregion.py
    │       │   │   │   ├── test_trustregion_exact.py
    │       │   │   │   ├── test_trustregion_krylov.py
    │       │   │   │   └── test_zeros.py
    │       │   │   ├── tnc.py
    │       │   │   └── zeros.py
    │       │   ├── signal
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _arraytools.cpython-312.pyc
    │       │   │   │   ├── _czt.cpython-312.pyc
    │       │   │   │   ├── _delegators.cpython-312.pyc
    │       │   │   │   ├── _filter_design.cpython-312.pyc
    │       │   │   │   ├── _fir_filter_design.cpython-312.pyc
    │       │   │   │   ├── _lti_conversion.cpython-312.pyc
    │       │   │   │   ├── _ltisys.cpython-312.pyc
    │       │   │   │   ├── _max_len_seq.cpython-312.pyc
    │       │   │   │   ├── _peak_finding.cpython-312.pyc
    │       │   │   │   ├── _polyutils.cpython-312.pyc
    │       │   │   │   ├── _savitzky_golay.cpython-312.pyc
    │       │   │   │   ├── _short_time_fft.cpython-312.pyc
    │       │   │   │   ├── _signal_api.cpython-312.pyc
    │       │   │   │   ├── _signaltools.cpython-312.pyc
    │       │   │   │   ├── _spectral_py.cpython-312.pyc
    │       │   │   │   ├── _spline_filters.cpython-312.pyc
    │       │   │   │   ├── _support_alternative_backends.cpython-312.pyc
    │       │   │   │   ├── _upfirdn.cpython-312.pyc
    │       │   │   │   ├── _waveforms.cpython-312.pyc
    │       │   │   │   ├── _wavelets.cpython-312.pyc
    │       │   │   │   ├── bsplines.cpython-312.pyc
    │       │   │   │   ├── filter_design.cpython-312.pyc
    │       │   │   │   ├── fir_filter_design.cpython-312.pyc
    │       │   │   │   ├── lti_conversion.cpython-312.pyc
    │       │   │   │   ├── ltisys.cpython-312.pyc
    │       │   │   │   ├── signaltools.cpython-312.pyc
    │       │   │   │   ├── spectral.cpython-312.pyc
    │       │   │   │   ├── spline.cpython-312.pyc
    │       │   │   │   ├── waveforms.cpython-312.pyc
    │       │   │   │   └── wavelets.cpython-312.pyc
    │       │   │   ├── _arraytools.py
    │       │   │   ├── _czt.py
    │       │   │   ├── _delegators.py
    │       │   │   ├── _filter_design.py
    │       │   │   ├── _fir_filter_design.py
    │       │   │   ├── _lti_conversion.py
    │       │   │   ├── _ltisys.py
    │       │   │   ├── _max_len_seq.py
    │       │   │   ├── _max_len_seq_inner.cp312-win_amd64.dll.a
    │       │   │   ├── _max_len_seq_inner.cp312-win_amd64.pyd
    │       │   │   ├── _peak_finding.py
    │       │   │   ├── _peak_finding_utils.cp312-win_amd64.dll.a
    │       │   │   ├── _peak_finding_utils.cp312-win_amd64.pyd
    │       │   │   ├── _polyutils.py
    │       │   │   ├── _savitzky_golay.py
    │       │   │   ├── _short_time_fft.py
    │       │   │   ├── _signal_api.py
    │       │   │   ├── _signaltools.py
    │       │   │   ├── _sigtools.cp312-win_amd64.dll.a
    │       │   │   ├── _sigtools.cp312-win_amd64.pyd
    │       │   │   ├── _sosfilt.cp312-win_amd64.dll.a
    │       │   │   ├── _sosfilt.cp312-win_amd64.pyd
    │       │   │   ├── _spectral_py.py
    │       │   │   ├── _spline.cp312-win_amd64.dll.a
    │       │   │   ├── _spline.cp312-win_amd64.pyd
    │       │   │   ├── _spline.pyi
    │       │   │   ├── _spline_filters.py
    │       │   │   ├── _support_alternative_backends.py
    │       │   │   ├── _upfirdn.py
    │       │   │   ├── _upfirdn_apply.cp312-win_amd64.dll.a
    │       │   │   ├── _upfirdn_apply.cp312-win_amd64.pyd
    │       │   │   ├── _waveforms.py
    │       │   │   ├── _wavelets.py
    │       │   │   ├── bsplines.py
    │       │   │   ├── filter_design.py
    │       │   │   ├── fir_filter_design.py
    │       │   │   ├── lti_conversion.py
    │       │   │   ├── ltisys.py
    │       │   │   ├── signaltools.py
    │       │   │   ├── spectral.py
    │       │   │   ├── spline.py
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _scipy_spectral_test_shim.cpython-312.pyc
    │       │   │   │   │   ├── mpsig.cpython-312.pyc
    │       │   │   │   │   ├── test_array_tools.cpython-312.pyc
    │       │   │   │   │   ├── test_bsplines.cpython-312.pyc
    │       │   │   │   │   ├── test_cont2discrete.cpython-312.pyc
    │       │   │   │   │   ├── test_czt.cpython-312.pyc
    │       │   │   │   │   ├── test_dltisys.cpython-312.pyc
    │       │   │   │   │   ├── test_filter_design.cpython-312.pyc
    │       │   │   │   │   ├── test_fir_filter_design.cpython-312.pyc
    │       │   │   │   │   ├── test_ltisys.cpython-312.pyc
    │       │   │   │   │   ├── test_max_len_seq.cpython-312.pyc
    │       │   │   │   │   ├── test_peak_finding.cpython-312.pyc
    │       │   │   │   │   ├── test_result_type.cpython-312.pyc
    │       │   │   │   │   ├── test_savitzky_golay.cpython-312.pyc
    │       │   │   │   │   ├── test_short_time_fft.cpython-312.pyc
    │       │   │   │   │   ├── test_signaltools.cpython-312.pyc
    │       │   │   │   │   ├── test_spectral.cpython-312.pyc
    │       │   │   │   │   ├── test_splines.cpython-312.pyc
    │       │   │   │   │   ├── test_upfirdn.cpython-312.pyc
    │       │   │   │   │   ├── test_waveforms.cpython-312.pyc
    │       │   │   │   │   ├── test_wavelets.cpython-312.pyc
    │       │   │   │   │   └── test_windows.cpython-312.pyc
    │       │   │   │   ├── _scipy_spectral_test_shim.py
    │       │   │   │   ├── mpsig.py
    │       │   │   │   ├── test_array_tools.py
    │       │   │   │   ├── test_bsplines.py
    │       │   │   │   ├── test_cont2discrete.py
    │       │   │   │   ├── test_czt.py
    │       │   │   │   ├── test_dltisys.py
    │       │   │   │   ├── test_filter_design.py
    │       │   │   │   ├── test_fir_filter_design.py
    │       │   │   │   ├── test_ltisys.py
    │       │   │   │   ├── test_max_len_seq.py
    │       │   │   │   ├── test_peak_finding.py
    │       │   │   │   ├── test_result_type.py
    │       │   │   │   ├── test_savitzky_golay.py
    │       │   │   │   ├── test_short_time_fft.py
    │       │   │   │   ├── test_signaltools.py
    │       │   │   │   ├── test_spectral.py
    │       │   │   │   ├── test_splines.py
    │       │   │   │   ├── test_upfirdn.py
    │       │   │   │   ├── test_waveforms.py
    │       │   │   │   ├── test_wavelets.py
    │       │   │   │   └── test_windows.py
    │       │   │   ├── waveforms.py
    │       │   │   ├── wavelets.py
    │       │   │   └── windows
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── _windows.cpython-312.pyc
    │       │   │       │   └── windows.cpython-312.pyc
    │       │   │       ├── _windows.py
    │       │   │       └── windows.py
    │       │   ├── sparse
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _base.cpython-312.pyc
    │       │   │   │   ├── _bsr.cpython-312.pyc
    │       │   │   │   ├── _compressed.cpython-312.pyc
    │       │   │   │   ├── _construct.cpython-312.pyc
    │       │   │   │   ├── _coo.cpython-312.pyc
    │       │   │   │   ├── _csc.cpython-312.pyc
    │       │   │   │   ├── _csr.cpython-312.pyc
    │       │   │   │   ├── _data.cpython-312.pyc
    │       │   │   │   ├── _dia.cpython-312.pyc
    │       │   │   │   ├── _dok.cpython-312.pyc
    │       │   │   │   ├── _extract.cpython-312.pyc
    │       │   │   │   ├── _index.cpython-312.pyc
    │       │   │   │   ├── _lil.cpython-312.pyc
    │       │   │   │   ├── _matrix.cpython-312.pyc
    │       │   │   │   ├── _matrix_io.cpython-312.pyc
    │       │   │   │   ├── _spfuncs.cpython-312.pyc
    │       │   │   │   ├── _sputils.cpython-312.pyc
    │       │   │   │   ├── base.cpython-312.pyc
    │       │   │   │   ├── bsr.cpython-312.pyc
    │       │   │   │   ├── compressed.cpython-312.pyc
    │       │   │   │   ├── construct.cpython-312.pyc
    │       │   │   │   ├── coo.cpython-312.pyc
    │       │   │   │   ├── csc.cpython-312.pyc
    │       │   │   │   ├── csr.cpython-312.pyc
    │       │   │   │   ├── data.cpython-312.pyc
    │       │   │   │   ├── dia.cpython-312.pyc
    │       │   │   │   ├── dok.cpython-312.pyc
    │       │   │   │   ├── extract.cpython-312.pyc
    │       │   │   │   ├── lil.cpython-312.pyc
    │       │   │   │   ├── sparsetools.cpython-312.pyc
    │       │   │   │   ├── spfuncs.cpython-312.pyc
    │       │   │   │   └── sputils.cpython-312.pyc
    │       │   │   ├── _base.py
    │       │   │   ├── _bsr.py
    │       │   │   ├── _compressed.py
    │       │   │   ├── _construct.py
    │       │   │   ├── _coo.py
    │       │   │   ├── _csc.py
    │       │   │   ├── _csparsetools.cp312-win_amd64.dll.a
    │       │   │   ├── _csparsetools.cp312-win_amd64.pyd
    │       │   │   ├── _csr.py
    │       │   │   ├── _data.py
    │       │   │   ├── _dia.py
    │       │   │   ├── _dok.py
    │       │   │   ├── _extract.py
    │       │   │   ├── _index.py
    │       │   │   ├── _lil.py
    │       │   │   ├── _matrix.py
    │       │   │   ├── _matrix_io.py
    │       │   │   ├── _sparsetools.cp312-win_amd64.dll.a
    │       │   │   ├── _sparsetools.cp312-win_amd64.pyd
    │       │   │   ├── _spfuncs.py
    │       │   │   ├── _sputils.py
    │       │   │   ├── base.py
    │       │   │   ├── bsr.py
    │       │   │   ├── compressed.py
    │       │   │   ├── construct.py
    │       │   │   ├── coo.py
    │       │   │   ├── csc.py
    │       │   │   ├── csgraph
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _laplacian.cpython-312.pyc
    │       │   │   │   │   └── _validation.cpython-312.pyc
    │       │   │   │   ├── _flow.cp312-win_amd64.dll.a
    │       │   │   │   ├── _flow.cp312-win_amd64.pyd
    │       │   │   │   ├── _laplacian.py
    │       │   │   │   ├── _matching.cp312-win_amd64.dll.a
    │       │   │   │   ├── _matching.cp312-win_amd64.pyd
    │       │   │   │   ├── _min_spanning_tree.cp312-win_amd64.dll.a
    │       │   │   │   ├── _min_spanning_tree.cp312-win_amd64.pyd
    │       │   │   │   ├── _reordering.cp312-win_amd64.dll.a
    │       │   │   │   ├── _reordering.cp312-win_amd64.pyd
    │       │   │   │   ├── _shortest_path.cp312-win_amd64.dll.a
    │       │   │   │   ├── _shortest_path.cp312-win_amd64.pyd
    │       │   │   │   ├── _tools.cp312-win_amd64.dll.a
    │       │   │   │   ├── _tools.cp312-win_amd64.pyd
    │       │   │   │   ├── _traversal.cp312-win_amd64.dll.a
    │       │   │   │   ├── _traversal.cp312-win_amd64.pyd
    │       │   │   │   ├── _validation.py
    │       │   │   │   └── tests
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── test_connected_components.cpython-312.pyc
    │       │   │   │       │   ├── test_conversions.cpython-312.pyc
    │       │   │   │       │   ├── test_flow.cpython-312.pyc
    │       │   │   │       │   ├── test_graph_laplacian.cpython-312.pyc
    │       │   │   │       │   ├── test_matching.cpython-312.pyc
    │       │   │   │       │   ├── test_pydata_sparse.cpython-312.pyc
    │       │   │   │       │   ├── test_reordering.cpython-312.pyc
    │       │   │   │       │   ├── test_shortest_path.cpython-312.pyc
    │       │   │   │       │   ├── test_spanning_tree.cpython-312.pyc
    │       │   │   │       │   └── test_traversal.cpython-312.pyc
    │       │   │   │       ├── test_connected_components.py
    │       │   │   │       ├── test_conversions.py
    │       │   │   │       ├── test_flow.py
    │       │   │   │       ├── test_graph_laplacian.py
    │       │   │   │       ├── test_matching.py
    │       │   │   │       ├── test_pydata_sparse.py
    │       │   │   │       ├── test_reordering.py
    │       │   │   │       ├── test_shortest_path.py
    │       │   │   │       ├── test_spanning_tree.py
    │       │   │   │       └── test_traversal.py
    │       │   │   ├── csr.py
    │       │   │   ├── data.py
    │       │   │   ├── dia.py
    │       │   │   ├── dok.py
    │       │   │   ├── extract.py
    │       │   │   ├── lil.py
    │       │   │   ├── linalg
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── _expm_multiply.cpython-312.pyc
    │       │   │   │   │   ├── _interface.cpython-312.pyc
    │       │   │   │   │   ├── _matfuncs.cpython-312.pyc
    │       │   │   │   │   ├── _norm.cpython-312.pyc
    │       │   │   │   │   ├── _onenormest.cpython-312.pyc
    │       │   │   │   │   ├── _special_sparse_arrays.cpython-312.pyc
    │       │   │   │   │   ├── _svdp.cpython-312.pyc
    │       │   │   │   │   ├── dsolve.cpython-312.pyc
    │       │   │   │   │   ├── eigen.cpython-312.pyc
    │       │   │   │   │   ├── interface.cpython-312.pyc
    │       │   │   │   │   ├── isolve.cpython-312.pyc
    │       │   │   │   │   └── matfuncs.cpython-312.pyc
    │       │   │   │   ├── _dsolve
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _add_newdocs.cpython-312.pyc
    │       │   │   │   │   │   └── linsolve.cpython-312.pyc
    │       │   │   │   │   ├── _add_newdocs.py
    │       │   │   │   │   ├── _superlu.cp312-win_amd64.dll.a
    │       │   │   │   │   ├── _superlu.cp312-win_amd64.pyd
    │       │   │   │   │   ├── linsolve.py
    │       │   │   │   │   └── tests
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__
    │       │   │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │   │       │   └── test_linsolve.cpython-312.pyc
    │       │   │   │   │       └── test_linsolve.py
    │       │   │   │   ├── _eigen
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _svds.cpython-312.pyc
    │       │   │   │   │   │   └── _svds_doc.cpython-312.pyc
    │       │   │   │   │   ├── _svds.py
    │       │   │   │   │   ├── _svds_doc.py
    │       │   │   │   │   ├── arpack
    │       │   │   │   │   │   ├── COPYING
    │       │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   │   └── arpack.cpython-312.pyc
    │       │   │   │   │   │   ├── _arpack.cp312-win_amd64.dll.a
    │       │   │   │   │   │   ├── _arpack.cp312-win_amd64.pyd
    │       │   │   │   │   │   ├── arpack.py
    │       │   │   │   │   │   └── tests
    │       │   │   │   │   │       ├── __init__.py
    │       │   │   │   │   │       ├── __pycache__
    │       │   │   │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │       │   └── test_arpack.cpython-312.pyc
    │       │   │   │   │   │       └── test_arpack.py
    │       │   │   │   │   ├── lobpcg
    │       │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   │   └── lobpcg.cpython-312.pyc
    │       │   │   │   │   │   ├── lobpcg.py
    │       │   │   │   │   │   └── tests
    │       │   │   │   │   │       ├── __init__.py
    │       │   │   │   │   │       ├── __pycache__
    │       │   │   │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │       │   └── test_lobpcg.cpython-312.pyc
    │       │   │   │   │   │       └── test_lobpcg.py
    │       │   │   │   │   └── tests
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__
    │       │   │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │   │       │   └── test_svds.cpython-312.pyc
    │       │   │   │   │       └── test_svds.py
    │       │   │   │   ├── _expm_multiply.py
    │       │   │   │   ├── _interface.py
    │       │   │   │   ├── _isolve
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   ├── _gcrotmk.cpython-312.pyc
    │       │   │   │   │   │   ├── iterative.cpython-312.pyc
    │       │   │   │   │   │   ├── lgmres.cpython-312.pyc
    │       │   │   │   │   │   ├── lsmr.cpython-312.pyc
    │       │   │   │   │   │   ├── lsqr.cpython-312.pyc
    │       │   │   │   │   │   ├── minres.cpython-312.pyc
    │       │   │   │   │   │   ├── tfqmr.cpython-312.pyc
    │       │   │   │   │   │   └── utils.cpython-312.pyc
    │       │   │   │   │   ├── _gcrotmk.py
    │       │   │   │   │   ├── iterative.py
    │       │   │   │   │   ├── lgmres.py
    │       │   │   │   │   ├── lsmr.py
    │       │   │   │   │   ├── lsqr.py
    │       │   │   │   │   ├── minres.py
    │       │   │   │   │   ├── tests
    │       │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   ├── __pycache__
    │       │   │   │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   │   │   ├── test_gcrotmk.cpython-312.pyc
    │       │   │   │   │   │   │   ├── test_iterative.cpython-312.pyc
    │       │   │   │   │   │   │   ├── test_lgmres.cpython-312.pyc
    │       │   │   │   │   │   │   ├── test_lsmr.cpython-312.pyc
    │       │   │   │   │   │   │   ├── test_lsqr.cpython-312.pyc
    │       │   │   │   │   │   │   ├── test_minres.cpython-312.pyc
    │       │   │   │   │   │   │   └── test_utils.cpython-312.pyc
    │       │   │   │   │   │   ├── test_gcrotmk.py
    │       │   │   │   │   │   ├── test_iterative.py
    │       │   │   │   │   │   ├── test_lgmres.py
    │       │   │   │   │   │   ├── test_lsmr.py
    │       │   │   │   │   │   ├── test_lsqr.py
    │       │   │   │   │   │   ├── test_minres.py
    │       │   │   │   │   │   └── test_utils.py
    │       │   │   │   │   ├── tfqmr.py
    │       │   │   │   │   └── utils.py
    │       │   │   │   ├── _matfuncs.py
    │       │   │   │   ├── _norm.py
    │       │   │   │   ├── _onenormest.py
    │       │   │   │   ├── _propack
    │       │   │   │   │   ├── _cpropack.cp312-win_amd64.dll.a
    │       │   │   │   │   ├── _cpropack.cp312-win_amd64.pyd
    │       │   │   │   │   ├── _dpropack.cp312-win_amd64.dll.a
    │       │   │   │   │   ├── _dpropack.cp312-win_amd64.pyd
    │       │   │   │   │   ├── _spropack.cp312-win_amd64.dll.a
    │       │   │   │   │   ├── _spropack.cp312-win_amd64.pyd
    │       │   │   │   │   ├── _zpropack.cp312-win_amd64.dll.a
    │       │   │   │   │   └── _zpropack.cp312-win_amd64.pyd
    │       │   │   │   ├── _special_sparse_arrays.py
    │       │   │   │   ├── _svdp.py
    │       │   │   │   ├── dsolve.py
    │       │   │   │   ├── eigen.py
    │       │   │   │   ├── interface.py
    │       │   │   │   ├── isolve.py
    │       │   │   │   ├── matfuncs.py
    │       │   │   │   └── tests
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__
    │       │   │   │       │   ├── __init__.cpython-312.pyc
    │       │   │   │       │   ├── test_expm_multiply.cpython-312.pyc
    │       │   │   │       │   ├── test_interface.cpython-312.pyc
    │       │   │   │       │   ├── test_matfuncs.cpython-312.pyc
    │       │   │   │       │   ├── test_norm.cpython-312.pyc
    │       │   │   │       │   ├── test_onenormest.cpython-312.pyc
    │       │   │   │       │   ├── test_propack.cpython-312.pyc
    │       │   │   │       │   ├── test_pydata_sparse.cpython-312.pyc
    │       │   │   │       │   └── test_special_sparse_arrays.cpython-312.pyc
    │       │   │   │       ├── propack_test_data.npz
    │       │   │   │       ├── test_expm_multiply.py
    │       │   │   │       ├── test_interface.py
    │       │   │   │       ├── test_matfuncs.py
    │       │   │   │       ├── test_norm.py
    │       │   │   │       ├── test_onenormest.py
    │       │   │   │       ├── test_propack.py
    │       │   │   │       ├── test_pydata_sparse.py
    │       │   │   │       └── test_special_sparse_arrays.py
    │       │   │   ├── sparsetools.py
    │       │   │   ├── spfuncs.py
    │       │   │   ├── sputils.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_arithmetic1d.cpython-312.pyc
    │       │   │       │   ├── test_array_api.cpython-312.pyc
    │       │   │       │   ├── test_base.cpython-312.pyc
    │       │   │       │   ├── test_common1d.cpython-312.pyc
    │       │   │       │   ├── test_construct.cpython-312.pyc
    │       │   │       │   ├── test_coo.cpython-312.pyc
    │       │   │       │   ├── test_csc.cpython-312.pyc
    │       │   │       │   ├── test_csr.cpython-312.pyc
    │       │   │       │   ├── test_dok.cpython-312.pyc
    │       │   │       │   ├── test_extract.cpython-312.pyc
    │       │   │       │   ├── test_indexing1d.cpython-312.pyc
    │       │   │       │   ├── test_matrix_io.cpython-312.pyc
    │       │   │       │   ├── test_minmax1d.cpython-312.pyc
    │       │   │       │   ├── test_sparsetools.cpython-312.pyc
    │       │   │       │   ├── test_spfuncs.cpython-312.pyc
    │       │   │       │   └── test_sputils.cpython-312.pyc
    │       │   │       ├── data
    │       │   │       │   ├── csc_py2.npz
    │       │   │       │   └── csc_py3.npz
    │       │   │       ├── test_arithmetic1d.py
    │       │   │       ├── test_array_api.py
    │       │   │       ├── test_base.py
    │       │   │       ├── test_common1d.py
    │       │   │       ├── test_construct.py
    │       │   │       ├── test_coo.py
    │       │   │       ├── test_csc.py
    │       │   │       ├── test_csr.py
    │       │   │       ├── test_dok.py
    │       │   │       ├── test_extract.py
    │       │   │       ├── test_indexing1d.py
    │       │   │       ├── test_matrix_io.py
    │       │   │       ├── test_minmax1d.py
    │       │   │       ├── test_sparsetools.py
    │       │   │       ├── test_spfuncs.py
    │       │   │       └── test_sputils.py
    │       │   ├── spatial
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _geometric_slerp.cpython-312.pyc
    │       │   │   │   ├── _kdtree.cpython-312.pyc
    │       │   │   │   ├── _plotutils.cpython-312.pyc
    │       │   │   │   ├── _procrustes.cpython-312.pyc
    │       │   │   │   ├── _spherical_voronoi.cpython-312.pyc
    │       │   │   │   ├── ckdtree.cpython-312.pyc
    │       │   │   │   ├── distance.cpython-312.pyc
    │       │   │   │   ├── kdtree.cpython-312.pyc
    │       │   │   │   └── qhull.cpython-312.pyc
    │       │   │   ├── _ckdtree.cp312-win_amd64.dll.a
    │       │   │   ├── _ckdtree.cp312-win_amd64.pyd
    │       │   │   ├── _distance_pybind.cp312-win_amd64.dll.a
    │       │   │   ├── _distance_pybind.cp312-win_amd64.pyd
    │       │   │   ├── _distance_wrap.cp312-win_amd64.dll.a
    │       │   │   ├── _distance_wrap.cp312-win_amd64.pyd
    │       │   │   ├── _geometric_slerp.py
    │       │   │   ├── _hausdorff.cp312-win_amd64.dll.a
    │       │   │   ├── _hausdorff.cp312-win_amd64.pyd
    │       │   │   ├── _kdtree.py
    │       │   │   ├── _plotutils.py
    │       │   │   ├── _procrustes.py
    │       │   │   ├── _qhull.cp312-win_amd64.dll.a
    │       │   │   ├── _qhull.cp312-win_amd64.pyd
    │       │   │   ├── _qhull.pyi
    │       │   │   ├── _spherical_voronoi.py
    │       │   │   ├── _voronoi.cp312-win_amd64.dll.a
    │       │   │   ├── _voronoi.cp312-win_amd64.pyd
    │       │   │   ├── _voronoi.pyi
    │       │   │   ├── ckdtree.py
    │       │   │   ├── distance.py
    │       │   │   ├── distance.pyi
    │       │   │   ├── kdtree.py
    │       │   │   ├── qhull.py
    │       │   │   ├── qhull_src
    │       │   │   │   └── COPYING_QHULL.txt
    │       │   │   ├── tests
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── test__plotutils.cpython-312.pyc
    │       │   │   │   │   ├── test__procrustes.cpython-312.pyc
    │       │   │   │   │   ├── test_distance.cpython-312.pyc
    │       │   │   │   │   ├── test_hausdorff.cpython-312.pyc
    │       │   │   │   │   ├── test_kdtree.cpython-312.pyc
    │       │   │   │   │   ├── test_qhull.cpython-312.pyc
    │       │   │   │   │   ├── test_slerp.cpython-312.pyc
    │       │   │   │   │   └── test_spherical_voronoi.cpython-312.pyc
    │       │   │   │   ├── data
    │       │   │   │   │   ├── cdist-X1.txt
    │       │   │   │   │   ├── cdist-X2.txt
    │       │   │   │   │   ├── degenerate_pointset.npz
    │       │   │   │   │   ├── iris.txt
    │       │   │   │   │   ├── pdist-boolean-inp.txt
    │       │   │   │   │   ├── pdist-chebyshev-ml-iris.txt
    │       │   │   │   │   ├── pdist-chebyshev-ml.txt
    │       │   │   │   │   ├── pdist-cityblock-ml-iris.txt
    │       │   │   │   │   ├── pdist-cityblock-ml.txt
    │       │   │   │   │   ├── pdist-correlation-ml-iris.txt
    │       │   │   │   │   ├── pdist-correlation-ml.txt
    │       │   │   │   │   ├── pdist-cosine-ml-iris.txt
    │       │   │   │   │   ├── pdist-cosine-ml.txt
    │       │   │   │   │   ├── pdist-double-inp.txt
    │       │   │   │   │   ├── pdist-euclidean-ml-iris.txt
    │       │   │   │   │   ├── pdist-euclidean-ml.txt
    │       │   │   │   │   ├── pdist-hamming-ml.txt
    │       │   │   │   │   ├── pdist-jaccard-ml.txt
    │       │   │   │   │   ├── pdist-jensenshannon-ml-iris.txt
    │       │   │   │   │   ├── pdist-jensenshannon-ml.txt
    │       │   │   │   │   ├── pdist-minkowski-3.2-ml-iris.txt
    │       │   │   │   │   ├── pdist-minkowski-3.2-ml.txt
    │       │   │   │   │   ├── pdist-minkowski-5.8-ml-iris.txt
    │       │   │   │   │   ├── pdist-seuclidean-ml-iris.txt
    │       │   │   │   │   ├── pdist-seuclidean-ml.txt
    │       │   │   │   │   ├── pdist-spearman-ml.txt
    │       │   │   │   │   ├── random-bool-data.txt
    │       │   │   │   │   ├── random-double-data.txt
    │       │   │   │   │   ├── random-int-data.txt
    │       │   │   │   │   ├── random-uint-data.txt
    │       │   │   │   │   └── selfdual-4d-polytope.txt
    │       │   │   │   ├── test__plotutils.py
    │       │   │   │   ├── test__procrustes.py
    │       │   │   │   ├── test_distance.py
    │       │   │   │   ├── test_hausdorff.py
    │       │   │   │   ├── test_kdtree.py
    │       │   │   │   ├── test_qhull.py
    │       │   │   │   ├── test_slerp.py
    │       │   │   │   └── test_spherical_voronoi.py
    │       │   │   └── transform
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── _rotation_groups.cpython-312.pyc
    │       │   │       │   ├── _rotation_spline.cpython-312.pyc
    │       │   │       │   └── rotation.cpython-312.pyc
    │       │   │       ├── _rigid_transform.cp312-win_amd64.dll.a
    │       │   │       ├── _rigid_transform.cp312-win_amd64.pyd
    │       │   │       ├── _rotation.cp312-win_amd64.dll.a
    │       │   │       ├── _rotation.cp312-win_amd64.pyd
    │       │   │       ├── _rotation_groups.py
    │       │   │       ├── _rotation_spline.py
    │       │   │       ├── rotation.py
    │       │   │       └── tests
    │       │   │           ├── __init__.py
    │       │   │           ├── __pycache__
    │       │   │           │   ├── __init__.cpython-312.pyc
    │       │   │           │   ├── test_rigid_transform.cpython-312.pyc
    │       │   │           │   ├── test_rotation.cpython-312.pyc
    │       │   │           │   ├── test_rotation_groups.cpython-312.pyc
    │       │   │           │   └── test_rotation_spline.cpython-312.pyc
    │       │   │           ├── test_rigid_transform.py
    │       │   │           ├── test_rotation.py
    │       │   │           ├── test_rotation_groups.py
    │       │   │           └── test_rotation_spline.py
    │       │   ├── special
    │       │   │   ├── __init__.pxd
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _add_newdocs.cpython-312.pyc
    │       │   │   │   ├── _basic.cpython-312.pyc
    │       │   │   │   ├── _ellip_harm.cpython-312.pyc
    │       │   │   │   ├── _input_validation.cpython-312.pyc
    │       │   │   │   ├── _lambertw.cpython-312.pyc
    │       │   │   │   ├── _logsumexp.cpython-312.pyc
    │       │   │   │   ├── _mptestutils.cpython-312.pyc
    │       │   │   │   ├── _multiufuncs.cpython-312.pyc
    │       │   │   │   ├── _orthogonal.cpython-312.pyc
    │       │   │   │   ├── _sf_error.cpython-312.pyc
    │       │   │   │   ├── _spfun_stats.cpython-312.pyc
    │       │   │   │   ├── _spherical_bessel.cpython-312.pyc
    │       │   │   │   ├── _support_alternative_backends.cpython-312.pyc
    │       │   │   │   ├── _testutils.cpython-312.pyc
    │       │   │   │   ├── add_newdocs.cpython-312.pyc
    │       │   │   │   ├── basic.cpython-312.pyc
    │       │   │   │   ├── orthogonal.cpython-312.pyc
    │       │   │   │   ├── sf_error.cpython-312.pyc
    │       │   │   │   ├── specfun.cpython-312.pyc
    │       │   │   │   └── spfun_stats.cpython-312.pyc
    │       │   │   ├── _add_newdocs.py
    │       │   │   ├── _basic.py
    │       │   │   ├── _comb.cp312-win_amd64.dll.a
    │       │   │   ├── _comb.cp312-win_amd64.pyd
    │       │   │   ├── _ellip_harm.py
    │       │   │   ├── _ellip_harm_2.cp312-win_amd64.dll.a
    │       │   │   ├── _ellip_harm_2.cp312-win_amd64.pyd
    │       │   │   ├── _gufuncs.cp312-win_amd64.dll.a
    │       │   │   ├── _gufuncs.cp312-win_amd64.pyd
    │       │   │   ├── _input_validation.py
    │       │   │   ├── _lambertw.py
    │       │   │   ├── _logsumexp.py
    │       │   │   ├── _mptestutils.py
    │       │   │   ├── _multiufuncs.py
    │       │   │   ├── _orthogonal.py
    │       │   │   ├── _orthogonal.pyi
    │       │   │   ├── _precompute
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   │   ├── cosine_cdf.cpython-312.pyc
    │       │   │   │   │   ├── expn_asy.cpython-312.pyc
    │       │   │   │   │   ├── gammainc_asy.cpython-312.pyc
    │       │   │   │   │   ├── gammainc_data.cpython-312.pyc
    │       │   │   │   │   ├── hyp2f1_data.cpython-312.pyc
    │       │   │   │   │   ├── lambertw.cpython-312.pyc
    │       │   │   │   │   ├── loggamma.cpython-312.pyc
    │       │   │   │   │   ├── struve_convergence.cpython-312.pyc
    │       │   │   │   │   ├── utils.cpython-312.pyc
    │       │   │   │   │   ├── wright_bessel.cpython-312.pyc
    │       │   │   │   │   ├── wright_bessel_data.cpython-312.pyc
    │       │   │   │   │   ├── wrightomega.cpython-312.pyc
    │       │   │   │   │   └── zetac.cpython-312.pyc
    │       │   │   │   ├── cosine_cdf.py
    │       │   │   │   ├── expn_asy.py
    │       │   │   │   ├── gammainc_asy.py
    │       │   │   │   ├── gammainc_data.py
    │       │   │   │   ├── hyp2f1_data.py
    │       │   │   │   ├── lambertw.py
    │       │   │   │   ├── loggamma.py
    │       │   │   │   ├── struve_convergence.py
    │       │   │   │   ├── utils.py
    │       │   │   │   ├── wright_bessel.py
    │       │   │   │   ├── wright_bessel_data.py
    │       │   │   │   ├── wrightomega.py
    │       │   │   │   └── zetac.py
    │       │   │   ├── _sf_error.py
    │       │   │   ├── _specfun.cp312-win_amd64.dll.a
    │       │   │   ├── _specfun.cp312-win_amd64.pyd
    │       │   │   ├── _special_ufuncs.cp312-win_amd64.dll.a
    │       │   │   ├── _special_ufuncs.cp312-win_amd64.pyd
    │       │   │   ├── _spfun_stats.py
    │       │   │   ├── _spherical_bessel.py
    │       │   │   ├── _support_alternative_backends.py
    │       │   │   ├── _test_internal.cp312-win_amd64.dll.a
    │       │   │   ├── _test_internal.cp312-win_amd64.pyd
    │       │   │   ├── _test_internal.pyi
    │       │   │   ├── _testutils.py
    │       │   │   ├── _ufuncs.cp312-win_amd64.dll.a
    │       │   │   ├── _ufuncs.cp312-win_amd64.pyd
    │       │   │   ├── _ufuncs.pyi
    │       │   │   ├── _ufuncs.pyx
    │       │   │   ├── _ufuncs_cxx.cp312-win_amd64.dll.a
    │       │   │   ├── _ufuncs_cxx.cp312-win_amd64.pyd
    │       │   │   ├── _ufuncs_cxx.pxd
    │       │   │   ├── _ufuncs_cxx.pyx
    │       │   │   ├── _ufuncs_cxx_defs.h
    │       │   │   ├── _ufuncs_defs.h
    │       │   │   ├── add_newdocs.py
    │       │   │   ├── basic.py
    │       │   │   ├── cython_special.cp312-win_amd64.dll.a
    │       │   │   ├── cython_special.cp312-win_amd64.pyd
    │       │   │   ├── cython_special.pxd
    │       │   │   ├── cython_special.pyi
    │       │   │   ├── orthogonal.py
    │       │   │   ├── sf_error.py
    │       │   │   ├── specfun.py
    │       │   │   ├── spfun_stats.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── test_basic.cpython-312.pyc
    │       │   │       │   ├── test_bdtr.cpython-312.pyc
    │       │   │       │   ├── test_boost_ufuncs.cpython-312.pyc
    │       │   │       │   ├── test_boxcox.cpython-312.pyc
    │       │   │       │   ├── test_cdflib.cpython-312.pyc
    │       │   │       │   ├── test_cdft_asymptotic.cpython-312.pyc
    │       │   │       │   ├── test_cephes_intp_cast.cpython-312.pyc
    │       │   │       │   ├── test_cosine_distr.cpython-312.pyc
    │       │   │       │   ├── test_cython_special.cpython-312.pyc
    │       │   │       │   ├── test_data.cpython-312.pyc
    │       │   │       │   ├── test_dd.cpython-312.pyc
    │       │   │       │   ├── test_digamma.cpython-312.pyc
    │       │   │       │   ├── test_ellip_harm.cpython-312.pyc
    │       │   │       │   ├── test_erfinv.cpython-312.pyc
    │       │   │       │   ├── test_exponential_integrals.cpython-312.pyc
    │       │   │       │   ├── test_extending.cpython-312.pyc
    │       │   │       │   ├── test_faddeeva.cpython-312.pyc
    │       │   │       │   ├── test_gamma.cpython-312.pyc
    │       │   │       │   ├── test_gammainc.cpython-312.pyc
    │       │   │       │   ├── test_hyp2f1.cpython-312.pyc
    │       │   │       │   ├── test_hypergeometric.cpython-312.pyc
    │       │   │       │   ├── test_iv_ratio.cpython-312.pyc
    │       │   │       │   ├── test_kolmogorov.cpython-312.pyc
    │       │   │       │   ├── test_lambertw.cpython-312.pyc
    │       │   │       │   ├── test_legendre.cpython-312.pyc
    │       │   │       │   ├── test_log1mexp.cpython-312.pyc
    │       │   │       │   ├── test_loggamma.cpython-312.pyc
    │       │   │       │   ├── test_logit.cpython-312.pyc
    │       │   │       │   ├── test_logsumexp.cpython-312.pyc
    │       │   │       │   ├── test_mpmath.cpython-312.pyc
    │       │   │       │   ├── test_nan_inputs.cpython-312.pyc
    │       │   │       │   ├── test_ndtr.cpython-312.pyc
    │       │   │       │   ├── test_ndtri_exp.cpython-312.pyc
    │       │   │       │   ├── test_orthogonal.cpython-312.pyc
    │       │   │       │   ├── test_orthogonal_eval.cpython-312.pyc
    │       │   │       │   ├── test_owens_t.cpython-312.pyc
    │       │   │       │   ├── test_pcf.cpython-312.pyc
    │       │   │       │   ├── test_pdtr.cpython-312.pyc
    │       │   │       │   ├── test_powm1.cpython-312.pyc
    │       │   │       │   ├── test_precompute_expn_asy.cpython-312.pyc
    │       │   │       │   ├── test_precompute_gammainc.cpython-312.pyc
    │       │   │       │   ├── test_precompute_utils.cpython-312.pyc
    │       │   │       │   ├── test_round.cpython-312.pyc
    │       │   │       │   ├── test_sf_error.cpython-312.pyc
    │       │   │       │   ├── test_sici.cpython-312.pyc
    │       │   │       │   ├── test_specfun.cpython-312.pyc
    │       │   │       │   ├── test_spence.cpython-312.pyc
    │       │   │       │   ├── test_spfun_stats.cpython-312.pyc
    │       │   │       │   ├── test_sph_harm.cpython-312.pyc
    │       │   │       │   ├── test_spherical_bessel.cpython-312.pyc
    │       │   │       │   ├── test_support_alternative_backends.cpython-312.pyc
    │       │   │       │   ├── test_trig.cpython-312.pyc
    │       │   │       │   ├── test_ufunc_signatures.cpython-312.pyc
    │       │   │       │   ├── test_wright_bessel.cpython-312.pyc
    │       │   │       │   ├── test_wrightomega.cpython-312.pyc
    │       │   │       │   └── test_zeta.cpython-312.pyc
    │       │   │       ├── _cython_examples
    │       │   │       │   ├── extending.pyx
    │       │   │       │   └── meson.build
    │       │   │       ├── data
    │       │   │       │   ├── __init__.py
    │       │   │       │   ├── __pycache__
    │       │   │       │   │   └── __init__.cpython-312.pyc
    │       │   │       │   ├── boost.npz
    │       │   │       │   ├── gsl.npz
    │       │   │       │   └── local.npz
    │       │   │       ├── test_basic.py
    │       │   │       ├── test_bdtr.py
    │       │   │       ├── test_boost_ufuncs.py
    │       │   │       ├── test_boxcox.py
    │       │   │       ├── test_cdflib.py
    │       │   │       ├── test_cdft_asymptotic.py
    │       │   │       ├── test_cephes_intp_cast.py
    │       │   │       ├── test_cosine_distr.py
    │       │   │       ├── test_cython_special.py
    │       │   │       ├── test_data.py
    │       │   │       ├── test_dd.py
    │       │   │       ├── test_digamma.py
    │       │   │       ├── test_ellip_harm.py
    │       │   │       ├── test_erfinv.py
    │       │   │       ├── test_exponential_integrals.py
    │       │   │       ├── test_extending.py
    │       │   │       ├── test_faddeeva.py
    │       │   │       ├── test_gamma.py
    │       │   │       ├── test_gammainc.py
    │       │   │       ├── test_hyp2f1.py
    │       │   │       ├── test_hypergeometric.py
    │       │   │       ├── test_iv_ratio.py
    │       │   │       ├── test_kolmogorov.py
    │       │   │       ├── test_lambertw.py
    │       │   │       ├── test_legendre.py
    │       │   │       ├── test_log1mexp.py
    │       │   │       ├── test_loggamma.py
    │       │   │       ├── test_logit.py
    │       │   │       ├── test_logsumexp.py
    │       │   │       ├── test_mpmath.py
    │       │   │       ├── test_nan_inputs.py
    │       │   │       ├── test_ndtr.py
    │       │   │       ├── test_ndtri_exp.py
    │       │   │       ├── test_orthogonal.py
    │       │   │       ├── test_orthogonal_eval.py
    │       │   │       ├── test_owens_t.py
    │       │   │       ├── test_pcf.py
    │       │   │       ├── test_pdtr.py
    │       │   │       ├── test_powm1.py
    │       │   │       ├── test_precompute_expn_asy.py
    │       │   │       ├── test_precompute_gammainc.py
    │       │   │       ├── test_precompute_utils.py
    │       │   │       ├── test_round.py
    │       │   │       ├── test_sf_error.py
    │       │   │       ├── test_sici.py
    │       │   │       ├── test_specfun.py
    │       │   │       ├── test_spence.py
    │       │   │       ├── test_spfun_stats.py
    │       │   │       ├── test_sph_harm.py
    │       │   │       ├── test_spherical_bessel.py
    │       │   │       ├── test_support_alternative_backends.py
    │       │   │       ├── test_trig.py
    │       │   │       ├── test_ufunc_signatures.py
    │       │   │       ├── test_wright_bessel.py
    │       │   │       ├── test_wrightomega.py
    │       │   │       └── test_zeta.py
    │       │   ├── stats
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__
    │       │   │   │   ├── __init__.cpython-312.pyc
    │       │   │   │   ├── _axis_nan_policy.cpython-312.pyc
    │       │   │   │   ├── _binned_statistic.cpython-312.pyc
    │       │   │   │   ├── _binomtest.cpython-312.pyc
    │       │   │   │   ├── _bws_test.cpython-312.pyc
    │       │   │   │   ├── _censored_data.cpython-312.pyc
    │       │   │   │   ├── _common.cpython-312.pyc
    │       │   │   │   ├── _constants.cpython-312.pyc
    │       │   │   │   ├── _continued_fraction.cpython-312.pyc
    │       │   │   │   ├── _continuous_distns.cpython-312.pyc
    │       │   │   │   ├── _correlation.cpython-312.pyc
    │       │   │   │   ├── _covariance.cpython-312.pyc
    │       │   │   │   ├── _crosstab.cpython-312.pyc
    │       │   │   │   ├── _discrete_distns.cpython-312.pyc
    │       │   │   │   ├── _distn_infrastructure.cpython-312.pyc
    │       │   │   │   ├── _distr_params.cpython-312.pyc
    │       │   │   │   ├── _distribution_infrastructure.cpython-312.pyc
    │       │   │   │   ├── _entropy.cpython-312.pyc
    │       │   │   │   ├── _finite_differences.cpython-312.pyc
    │       │   │   │   ├── _fit.cpython-312.pyc
    │       │   │   │   ├── _hypotests.cpython-312.pyc
    │       │   │   │   ├── _kde.cpython-312.pyc
    │       │   │   │   ├── _ksstats.cpython-312.pyc
    │       │   │   │   ├── _mannwhitneyu.cpython-312.pyc
    │       │   │   │   ├── _mgc.cpython-312.pyc
    │       │   │   │   ├── _morestats.cpython-312.pyc
    │       │   │   │   ├── _mstats_basic.cpython-312.pyc
    │       │   │   │   ├── _mstats_extras.cpython-312.pyc
    │       │   │   │   ├── _multicomp.cpython-312.pyc
    │       │   │   │   ├── _multivariate.cpython-312.pyc
    │       │   │   │   ├── _new_distributions.cpython-312.pyc
    │       │   │   │   ├── _odds_ratio.cpython-312.pyc
    │       │   │   │   ├── _page_trend_test.cpython-312.pyc
    │       │   │   │   ├── _probability_distribution.cpython-312.pyc
    │       │   │   │   ├── _qmc.cpython-312.pyc
    │       │   │   │   ├── _qmvnt.cpython-312.pyc
    │       │   │   │   ├── _quantile.cpython-312.pyc
    │       │   │   │   ├── _relative_risk.cpython-312.pyc
    │       │   │   │   ├── _resampling.cpython-312.pyc
    │       │   │   │   ├── _result_classes.cpython-312.pyc
    │       │   │   │   ├── _sampling.cpython-312.pyc
    │       │   │   │   ├── _sensitivity_analysis.cpython-312.pyc
    │       │   │   │   ├── _stats_mstats_common.cpython-312.pyc
    │       │   │   │   ├── _stats_py.cpython-312.pyc
    │       │   │   │   ├── _survival.cpython-312.pyc
    │       │   │   │   ├── _tukeylambda_stats.cpython-312.pyc
    │       │   │   │   ├── _variation.cpython-312.pyc
    │       │   │   │   ├── _warnings_errors.cpython-312.pyc
    │       │   │   │   ├── _wilcoxon.cpython-312.pyc
    │       │   │   │   ├── biasedurn.cpython-312.pyc
    │       │   │   │   ├── contingency.cpython-312.pyc
    │       │   │   │   ├── distributions.cpython-312.pyc
    │       │   │   │   ├── kde.cpython-312.pyc
    │       │   │   │   ├── morestats.cpython-312.pyc
    │       │   │   │   ├── mstats.cpython-312.pyc
    │       │   │   │   ├── mstats_basic.cpython-312.pyc
    │       │   │   │   ├── mstats_extras.cpython-312.pyc
    │       │   │   │   ├── mvn.cpython-312.pyc
    │       │   │   │   ├── qmc.cpython-312.pyc
    │       │   │   │   ├── sampling.cpython-312.pyc
    │       │   │   │   └── stats.cpython-312.pyc
    │       │   │   ├── _ansari_swilk_statistics.cp312-win_amd64.dll.a
    │       │   │   ├── _ansari_swilk_statistics.cp312-win_amd64.pyd
    │       │   │   ├── _axis_nan_policy.py
    │       │   │   ├── _biasedurn.cp312-win_amd64.dll.a
    │       │   │   ├── _biasedurn.cp312-win_amd64.pyd
    │       │   │   ├── _biasedurn.pxd
    │       │   │   ├── _binned_statistic.py
    │       │   │   ├── _binomtest.py
    │       │   │   ├── _bws_test.py
    │       │   │   ├── _censored_data.py
    │       │   │   ├── _common.py
    │       │   │   ├── _constants.py
    │       │   │   ├── _continued_fraction.py
    │       │   │   ├── _continuous_distns.py
    │       │   │   ├── _correlation.py
    │       │   │   ├── _covariance.py
    │       │   │   ├── _crosstab.py
    │       │   │   ├── _discrete_distns.py
    │       │   │   ├── _distn_infrastructure.py
    │       │   │   ├── _distr_params.py
    │       │   │   ├── _distribution_infrastructure.py
    │       │   │   ├── _entropy.py
    │       │   │   ├── _finite_differences.py
    │       │   │   ├── _fit.py
    │       │   │   ├── _hypotests.py
    │       │   │   ├── _kde.py
    │       │   │   ├── _ksstats.py
    │       │   │   ├── _levy_stable
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   └── __init__.cpython-312.pyc
    │       │   │   │   ├── levyst.cp312-win_amd64.dll.a
    │       │   │   │   └── levyst.cp312-win_amd64.pyd
    │       │   │   ├── _mannwhitneyu.py
    │       │   │   ├── _mgc.py
    │       │   │   ├── _morestats.py
    │       │   │   ├── _mstats_basic.py
    │       │   │   ├── _mstats_extras.py
    │       │   │   ├── _multicomp.py
    │       │   │   ├── _multivariate.py
    │       │   │   ├── _new_distributions.py
    │       │   │   ├── _odds_ratio.py
    │       │   │   ├── _page_trend_test.py
    │       │   │   ├── _probability_distribution.py
    │       │   │   ├── _qmc.py
    │       │   │   ├── _qmc_cy.cp312-win_amd64.dll.a
    │       │   │   ├── _qmc_cy.cp312-win_amd64.pyd
    │       │   │   ├── _qmc_cy.pyi
    │       │   │   ├── _qmvnt.py
    │       │   │   ├── _qmvnt_cy.cp312-win_amd64.dll.a
    │       │   │   ├── _qmvnt_cy.cp312-win_amd64.pyd
    │       │   │   ├── _quantile.py
    │       │   │   ├── _rcont
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   └── __init__.cpython-312.pyc
    │       │   │   │   ├── rcont.cp312-win_amd64.dll.a
    │       │   │   │   └── rcont.cp312-win_amd64.pyd
    │       │   │   ├── _relative_risk.py
    │       │   │   ├── _resampling.py
    │       │   │   ├── _result_classes.py
    │       │   │   ├── _sampling.py
    │       │   │   ├── _sensitivity_analysis.py
    │       │   │   ├── _sobol.cp312-win_amd64.dll.a
    │       │   │   ├── _sobol.cp312-win_amd64.pyd
    │       │   │   ├── _sobol.pyi
    │       │   │   ├── _sobol_direction_numbers.npz
    │       │   │   ├── _stats.cp312-win_amd64.dll.a
    │       │   │   ├── _stats.cp312-win_amd64.pyd
    │       │   │   ├── _stats.pxd
    │       │   │   ├── _stats_mstats_common.py
    │       │   │   ├── _stats_py.py
    │       │   │   ├── _stats_pythran.cp312-win_amd64.dll.a
    │       │   │   ├── _stats_pythran.cp312-win_amd64.pyd
    │       │   │   ├── _survival.py
    │       │   │   ├── _tukeylambda_stats.py
    │       │   │   ├── _unuran
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__
    │       │   │   │   │   └── __init__.cpython-312.pyc
    │       │   │   │   ├── unuran_wrapper.cp312-win_amd64.dll.a
    │       │   │   │   ├── unuran_wrapper.cp312-win_amd64.pyd
    │       │   │   │   └── unuran_wrapper.pyi
    │       │   │   ├── _variation.py
    │       │   │   ├── _warnings_errors.py
    │       │   │   ├── _wilcoxon.py
    │       │   │   ├── biasedurn.py
    │       │   │   ├── contingency.py
    │       │   │   ├── distributions.py
    │       │   │   ├── kde.py
    │       │   │   ├── morestats.py
    │       │   │   ├── mstats.py
    │       │   │   ├── mstats_basic.py
    │       │   │   ├── mstats_extras.py
    │       │   │   ├── mvn.py
    │       │   │   ├── qmc.py
    │       │   │   ├── sampling.py
    │       │   │   ├── stats.py
    │       │   │   └── tests
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__
    │       │   │       │   ├── __init__.cpython-312.pyc
    │       │   │       │   ├── common_tests.cpython-312.pyc
    │       │   │       │   ├── test_axis_nan_policy.cpython-312.pyc
    │       │   │       │   ├── test_binned_statistic.cpython-312.pyc
    │       │   │       │   ├── test_censored_data.cpython-312.pyc
    │       │   │       │   ├── test_contingency.cpython-312.pyc
    │       │   │       │   ├── test_continued_fraction.cpython-312.pyc
    │       │   │       │   ├── test_continuous.cpython-312.pyc
    │       │   │       │   ├── test_continuous_basic.cpython-312.pyc
    │       │   │       │   ├── test_continuous_fit_censored.cpython-312.pyc
    │       │   │       │   ├── test_correlation.cpython-312.pyc
    │       │   │       │   ├── test_crosstab.cpython-312.pyc
    │       │   │       │   ├── test_discrete_basic.cpython-312.pyc
    │       │   │       │   ├── test_discrete_distns.cpython-312.pyc
    │       │   │       │   ├── test_distributions.cpython-312.pyc
    │       │   │       │   ├── test_entropy.cpython-312.pyc
    │       │   │       │   ├── test_fast_gen_inversion.cpython-312.pyc
    │       │   │       │   ├── test_fit.cpython-312.pyc
    │       │   │       │   ├── test_hypotests.cpython-312.pyc
    │       │   │       │   ├── test_kdeoth.cpython-312.pyc
    │       │   │       │   ├── test_marray.cpython-312.pyc
    │       │   │       │   ├── test_mgc.cpython-312.pyc
    │       │   │       │   ├── test_morestats.cpython-312.pyc
    │       │   │       │   ├── test_mstats_basic.cpython-312.pyc
    │       │   │       │   ├── test_mstats_extras.cpython-312.pyc
    │       │   │       │   ├── test_multicomp.cpython-312.pyc
    │       │   │       │   ├── test_multivariate.cpython-312.pyc
    │       │   │       │   ├── test_odds_ratio.cpython-312.pyc
    │       │   │       │   ├── test_qmc.cpython-312.pyc
    │       │   │       │   ├── test_quantile.cpython-312.pyc
    │       │   │       │   ├── test_rank.cpython-312.pyc
    │       │   │       │   ├── test_relative_risk.cpython-312.pyc
    │       │   │       │   ├── test_resampling.cpython-312.pyc
    │       │   │       │   ├── test_sampling.cpython-312.pyc
    │       │   │       │   ├── test_sensitivity_analysis.cpython-312.pyc
    │       │   │       │   ├── test_stats.cpython-312.pyc
    │       │   │       │   ├── test_survival.cpython-312.pyc
    │       │   │       │   ├── test_tukeylambda_stats.cpython-312.pyc
    │       │   │       │   └── test_variation.cpython-312.pyc
    │       │   │       ├── common_tests.py
    │       │   │       ├── data
    │       │   │       │   ├── __pycache__
    │       │   │       │   │   ├── _mvt.cpython-312.pyc
    │       │   │       │   │   └── fisher_exact_results_from_r.cpython-312.pyc
    │       │   │       │   ├── _mvt.py
    │       │   │       │   ├── fisher_exact_results_from_r.py
    │       │   │       │   ├── jf_skew_t_gamlss_pdf_data.npy
    │       │   │       │   ├── levy_stable
    │       │   │       │   │   ├── stable-Z1-cdf-sample-data.npy
    │       │   │       │   │   ├── stable-Z1-pdf-sample-data.npy
    │       │   │       │   │   └── stable-loc-scale-sample-data.npy
    │       │   │       │   ├── nist_anova
    │       │   │       │   │   ├── AtmWtAg.dat
    │       │   │       │   │   ├── SiRstv.dat
    │       │   │       │   │   ├── SmLs01.dat
    │       │   │       │   │   ├── SmLs02.dat
    │       │   │       │   │   ├── SmLs03.dat
    │       │   │       │   │   ├── SmLs04.dat
    │       │   │       │   │   ├── SmLs05.dat
    │       │   │       │   │   ├── SmLs06.dat
    │       │   │       │   │   ├── SmLs07.dat
    │       │   │       │   │   ├── SmLs08.dat
    │       │   │       │   │   └── SmLs09.dat
    │       │   │       │   ├── nist_linregress
    │       │   │       │   │   └── Norris.dat
    │       │   │       │   ├── rel_breitwigner_pdf_sample_data_ROOT.npy
    │       │   │       │   └── studentized_range_mpmath_ref.json
    │       │   │       ├── test_axis_nan_policy.py
    │       │   │       ├── test_binned_statistic.py
    │       │   │       ├── test_censored_data.py
    │       │   │       ├── test_contingency.py
    │       │   │       ├── test_continued_fraction.py
    │       │   │       ├── test_continuous.py
    │       │   │       ├── test_continuous_basic.py
    │       │   │       ├── test_continuous_fit_censored.py
    │       │   │       ├── test_correlation.py
    │       │   │       ├── test_crosstab.py
    │       │   │       ├── test_discrete_basic.py
    │       │   │       ├── test_discrete_distns.py
    │       │   │       ├── test_distributions.py
    │       │   │       ├── test_entropy.py
    │       │   │       ├── test_fast_gen_inversion.py
    │       │   │       ├── test_fit.py
    │       │   │       ├── test_hypotests.py
    │       │   │       ├── test_kdeoth.py
    │       │   │       ├── test_marray.py
    │       │   │       ├── test_mgc.py
    │       │   │       ├── test_morestats.py
    │       │   │       ├── test_mstats_basic.py
    │       │   │       ├── test_mstats_extras.py
    │       │   │       ├── test_multicomp.py
    │       │   │       ├── test_multivariate.py
    │       │   │       ├── test_odds_ratio.py
    │       │   │       ├── test_qmc.py
    │       │   │       ├── test_quantile.py
    │       │   │       ├── test_rank.py
    │       │   │       ├── test_relative_risk.py
    │       │   │       ├── test_resampling.py
    │       │   │       ├── test_sampling.py
    │       │   │       ├── test_sensitivity_analysis.py
    │       │   │       ├── test_stats.py
    │       │   │       ├── test_survival.py
    │       │   │       ├── test_tukeylambda_stats.py
    │       │   │       └── test_variation.py
    │       │   └── version.py
    │       ├── scipy-1.16.3-cp312-cp312-win_amd64.whl
    │       ├── scipy-1.16.3.dist-info
    │       │   ├── DELVEWHEEL
    │       │   ├── INSTALLER
    │       │   ├── LICENSE.txt
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   └── WHEEL
    │       ├── scipy.libs
    │       │   └── libscipy_openblas-48c358d105077551cc9cc3ba79387ed5.dll
    │       ├── six-1.17.0.dist-info
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       └── six.py
    ├── Scripts
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.bat
    │   ├── deactivate.bat
    │   ├── f2py.exe
    │   ├── fonttools.exe
    │   ├── numpy-config.exe
    │   ├── pip.exe
    │   ├── pip3.12.exe
    │   ├── pip3.exe
    │   ├── py.test.exe
    │   ├── pyftmerge.exe
    │   ├── pyftsubset.exe
    │   ├── pygmentize.exe
    │   ├── pytest.exe
    │   ├── python.exe
    │   ├── pythonw.exe
    │   └── ttx.exe
    ├── pyvenv.cfg
    └── share
        └── man
            └── man1
                └── ttx.1

```
