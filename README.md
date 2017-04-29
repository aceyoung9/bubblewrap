# 🍾 Bubblewrap

An unfortunate OpenCV exploration.

# 🚀 Getting up and running

#### Prerequisites

These instructions assume macOS, with XCode and homebrew already installed.

  * ffmpeg
    * `brew install ffmpeg`
  * OpenCV3
    * `brew install python python3`
```bash
$ brew tap homebrew/science
$ brew install --HEAD opencv3 --with-ffmpeg
$ echo /usr/local/opt/opencv3/lib/python2.7/site-packages >> /usr/local/lib/python2.7/site-packages/opencv3.pth
```

#### Easy Way:
??????

`pip instal -r requirements.txt` probably.

#### Hard Way:
Prerequisites:
  * Python Stable, aka Python 2.7, aka that's right-- I called Python3 fake.
    * I'm on Python 2.7.13 but that's probably not important.
  * virtualenv
  * Please actually make sure you have the [prerequisites](#Prerequisites).

1. `virtualenv bubblewrap-env`
2. `source bubblewrap-env/bin/activate`
3. Here's where you hope I took good notes.  
  `pip install -r requirements.txt`
4. `python Trial1.py` should do it! 💁✨ (Or, right-click running in PyCharm or whatever you're using)
    * To deactivate the virtualenv, run `deactivate`

#### 📹 On Webcams

Sigh. Getting a Logitech c92blah to mount is a very curious matter indeed.

###### The Facts:

* OpenCV does not play nicely with multiple webcams on the same USB hub. The thing with a MacBook,
  however, is that everything is on the same USB Hub, because you're on a portable computer.
* To mount your external Webcam as the default (and only😉) webcam,
    1. Open up the Photo Booth app in Mac.
    2. Plug in your webcam.
    3. Under "Cameras," select your external one. Repeat and toggle steps 1 and 2 until the desired
    webcam is labeled as the "default one."
    4. Test with the Camera Script I wrote in the repository. It returns a live feed in a new window.

# License:
* I'm sorry.
* WTFPL

# Further Reading
* [Guide for installing OpenCV3 with Python 2](http://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/)