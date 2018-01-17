# Correlation Flow
Correlation Flow: Robust Optical Flow using Kernel Cross-Correlators

    	Velocity Estimation in 3-D space $v_x, v_y, v_z, \omega_z$

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

# Papers associated with this work:
#### 

[Chen Wang](https://wang-chen.github.io) *, Tete Ji *, Thien-Minh Nguyen, and [Lihua Xie](http://www.ntu.edu.sg/home/elhxie/), "Correlation Flow: Robust Optical Flow Using Kernel Cross-Correlators", accepted by IEEE International Conference on Robotics and Automation (ICRA 2018), 2018 (*Chen Wang and Tete Ji are joint first authors).

[Chen Wang](https://wang-chen.github.io), [Le Zhang](https://sites.google.com/site/zhangleuestc/home), [Lihua Xie](http://www.ntu.edu.sg/home/elhxie/), [Junsong Yuan](http://www.ntu.edu.sg/home/jsyuan/), Kernel Cross-Correlator, In AAAI Conference on Artificial Intelligence (AAAI-18), 2018 ([PDF available here](https://arxiv.org/pdf/1709.05936.pdf))   ([source codes available here](https://github.com/wang-chen/KCC))

The following work applys correlation flow to improve the performance of localization accuracy.

Thien-Minh Nguyen, Abdul Hanif Zaini, [Chen Wang](https://wang-chen.github.io) , Kexin Guo, and [Lihua Xie](http://www.ntu.edu.sg/home/elhxie/), "Robust Target-relative Localization with Ultra-Wideband Ranging and Communication", accepted by IEEE International Conference on Robotics and Automation (ICRA 2018), 2018.

