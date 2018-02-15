# WATTARY Eye:

**This part consists of 2 steps:**
- [x] Extracting faces from an image (Detecting).
- [ ] Recognize faces from a saved data.

**Dependencies:**
- dlib *[requires cmake >= 2.8.13]*.
- sci-kit learn *(skimage)*.

**Results:**
1. Feed the module with an image.

![Input image](imgs/3818.jpg)

2. The returned images after merging:

![Merged output](imgs/merge_from_ofoct.jpg)

3- The provement:

![Detecting Provement](imgs/Screenshot%20from%202018-02-16%2000-37-36.png)


## Step 1: Detecting Faces:

**Note: A face must be more than 100px*100px to be detected.**

**To detect faces from any image use `faceDetector.py`, you can import it in your work by typing:**

```python
import Eye.faceDetector
```
or
```python
from Eye import faceDetector
```

The detector module contains a function called `detectFaces()` which takes a parameters [the path of the image] and it will return the detected faces.


