# Correlation Flow

# Steps to run the demo-

1. Clone the repository
```
cd catkin_ws/src
git clone https://github.com/akathpal/correlation_flow
```

2. Install Dependencies as mentioned.
3. Compile the ROS workspace using catkin_make
4. Give permissions to py files.
```
cd catkin_ws/src/correlation_flow/script
chmod u+x imagepub_video.py
chmod u+x imagepub_2frames.py
```

5. Run correlation flow launch file 
```
roslaunch correlation_flow correlation_flow.launch
```

6. To run the video from a camera, 
```
rosrun correlation_flow imagepub_video.py
```
7. To view the optical flow output using 2 frames, 
```
rosrun correlation_flow imagepub_2frames.py
```


Correlation Flow: Robust Optical Flow using Kernel Cross-Correlators

    	Velocity Estimation in 3-D space $v_x, v_y, v_z, \omega_z$

This repo contains source codes for the following paper, which is accepted by ICRA-18:

[Chen Wang](https://wang-chen.github.io) *, Tete Ji *, Thien-Minh Nguyen, and [Lihua Xie](http://www.ntu.edu.sg/home/elhxie/), "Correlation Flow: Robust Optical Flow Using Kernel Cross-Correlators", IEEE International Conference on Robotics and Automation (ICRA), 2018.

# Platform
  Codes have been tested on Ubuntu 16.04 with ROS kinetic.
  
# Install Dependencies:
  1. Install FFT library: 
	```
	sudo apt-get install libfftw3-dev libfftw3-doc
	```

# Install Intel Math Kernel Library (MKL) （optional）:

  1. Download MKL from Intel website
  2. Extract downloaded file 
  	```
  	tar -zxvf [name_of_downloaded_file]
  	```
  3. Go to extracted folder, give permission: 
  	```
  	sudo chmod +x install.sh
  	```
  4. Run installation 
	```
  	./install.sh
  	```
  5. Link library, add to .bashrc: 
  	```
  	source /opt/intel/bin/compilervars.sh intel64
  	```
  6. Try compile in ROS workspace

# If this repo is useful for your projects, you may cite it as:
    
	@inproceedings{wang2018correlation,
	  title={{Correlation Flow: Robust Optical Flow using Kernel Cross-Correlators}},
	  author={Wang, Chen and Ji, Tete and Nguyen, Thien-Minh and Xie, Lihua},
	  booktitle={International Conference on Robotics and Automation (ICRA)},
	  year={2018},
	  organization={IEEE}
	}
     
# Correlation Flow is built on following work: 

[Chen Wang](https://wang-chen.github.io), [Le Zhang](https://sites.google.com/site/zhangleuestc/home), [Lihua Xie](http://www.ntu.edu.sg/home/elhxie/), [Junsong Yuan](http://www.ntu.edu.sg/home/jsyuan/), Kernel Cross-Correlator, In AAAI Conference on Artificial Intelligence (AAAI-18), 2018 ([PDF available here](https://arxiv.org/pdf/1709.05936.pdf))   ([source codes available here](https://github.com/wang-chen/KCC))

# Works using Correlation Flow


Thien-Minh Nguyen, Abdul Hanif Zaini, [Chen Wang](https://wang-chen.github.io) , Kexin Guo, and [Lihua Xie](http://www.ntu.edu.sg/home/elhxie/), "Robust Target-relative Localization with Ultra-Wideband Ranging and Communication", IEEE International Conference on Robotics and Automation (ICRA 2018), 2018. ([Video available here](https://youtu.be/ZkxFDGdB0hQ))

*The above work applys correlation flow to improve the performance of localization accuracy.


