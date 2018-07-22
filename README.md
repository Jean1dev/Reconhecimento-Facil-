# py_OpenCV

! [alt text] Reconhecimento facial com python

## Quick start on Mac OS X

Quick start options:

git clone https://github.com/Itseez/opencv.git --depth=1
git clone https://github.com/Itseez/opencv_contrib --depth=1
brew install opencv

############ For Python 2 ############
# This is a single line command.
echo /usr/local/opt/opencv/lib/python2.7/site-packages >> 
/usr/local/lib/python2.7/site-packages/opencv3.pth

############ For Python 3 ############
# This is a single line command
echo /usr/local/opt/opencv/lib/python3.6/site-packages >> 
/usr/local/lib/python3.6/site-packages/opencv3.pth


# Install openCV
cd opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D WITH_TBB=ON \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D WITH_V4L=ON \
-D WITH_OPENGL=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules ..
Add -D WITH_QT=ON if needed.
make -j4
sudo make install

# test
import cv2
cv2.__version__
