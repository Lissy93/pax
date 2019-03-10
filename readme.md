# Pax

 📸 A script which removes flashes from a video stream


## Intro

The aim in developing this module was to use machine vision to detect and eliminate sudden contrast changes, caused mainly by camera speed light. Video footage containing fast flickering images, such as camera flashes is non-accessible for some people with photosensitive epilepsy. It also generally decreases the viewing quality of clips.


## Example

| Before        | After         |
| ------------- |:-------------:|
| ![Demo before running script](docs/before.gif) | ![Demo after running script](docs/after.gif) |
| ![Chart showing luminosity against frame, before](docs/before-chart-grey.png) | ![Chart showing luminosity against frame, after](docs/after-chart-grey.png) |


## Usage Instructions

Once you've cloned and cd'd into the repo, use Python 3 to run the Pax script, for example:

```
$ python3 pax.py -i path/to/your/video.mp4 -o path/to/your/dest.mp4 -c mp4v
```

Where the `--ifile` is your input, `--ofile` is your output, and `--codec` is your chosen, and installed codec


## How It Works

Uses OpenCV to analyse and programmatically adjust frames in a video stream.

![Flow Chart](docs/flow-chart.png) 

It works as a stand-alone module. It should then be able to be used in a Chrome extension, filter for Smart TV, by a broadcasting company, as a mobile app, or on pretty much any other platform.

##About

*Developed by [Oliver Poole](https://github.com/OlliePoole) and [Alicia Sykes](https://aliciasykes.com) at [StartHack 19](https://starthack.ch/). Licensed under [MIT](https://gist.github.com/Lissy93/143d2ee01ccc5c052a17), 2019.*