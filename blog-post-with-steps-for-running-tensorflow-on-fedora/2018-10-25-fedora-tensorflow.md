---
layout: post
title:  "Tensorflow installation guide for Fedora GNU/Linux"
tags:
  - Fedora
  - Linux
  - GNU/Linux
  - Tensorflow
  - AI
  - Machine Learning
  - Artifical Inteligence
  - Google Code-In
hero: uploads/tensorflowfedora.png
overlay: blue
published: true

---
<!–-break-–>
Tensorflow is open-source library used that powers Artifical Inteligence.  It' s originaly developed by Google's  AI Organization, but now it' s used by a lot of companies such as Twitter, Nvidia, Snapchat and many more. 

Tensorflow can be used with python or even JavaScript inside your web browser. It supports NVIDIA CUDA Technology that brings performance to the new level.

In this article we'll talk a little about this library.
## How to install Tensorflow on [Fedora GNU/Linux](https://getfedora.org/)
* Download *virtualenv* by executing ```sudo pip3 install virtualenv```

* As first you have to get 3.6 version of python interpreter. You can do it by executing ```sudo dnf install python36.x86_64```

* Create virtualenv with older python by ```virtualenv --system-site-packages -p /usr/bin/python3.6 ./venv && source ./venv/bin/activate```

* For CPU-Only Tensorflow run: ```pip install tensorflow```

* To execute app designed using tensorflow just run ```python3.6 app.py```

* To go out of virtualenv run ```deactivate```


## Test the installation
* Create test.py
  ```
  import tensorflow as tf

  class SquareTest(tf.test.TestCase):
      def testSquare(self):
        with self.test_session():
            x = tf.square([2, 3])
            self.assertAllEqual(x.eval(), [4, 9])

  if __name__ == '__main__':
      tf.test.main()
  ```

* ```python3.6 test.py```