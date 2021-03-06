# **Path Planning Project** 
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

---
## Writeup

This is my writeup for the project "Path Planning" of Self Driving Car Nanadegree on Udacity.

---

### Contents

* [About Path Planning Project](#About-Path-Planning-Project)
* [Project code](#Project-code)
* [Rubric Points](#Rubric-Points)
* [Code compilation](#Code-compilation)
* [Valid Trajectories](#Valid-Trajectories)
* [Reflection](#Reflection)
	* [Path generation and planning](#Path-generation-and-planning)
	* [Further improvement](#Further-improvement)
* [Output video](#Output-video)
	* [Final output](#Final-output)
	* [Simulation test](#Simulation-test)
* [Test code](#Test-code)
* [Reference](#Reference)

[//]: # (Image References)

[animation1]: ./output/test1.gif "Animated gif of simulation video (test1)"
[animation2]: ./output/test2.gif "Animated gif of simulation video (test2)"
[animation3]: ./output/test3.gif "Animated gif of simulation video (test3)"
[animation4]: ./output/test4.gif "Animated gif of simulation video (test4)"
[animation5]: ./output/test5.gif "Animated gif of simulation video (test5)"
[animation6]: ./output/test6.gif "Animated gif of simulation video (test6)"
[animation7]: ./output/test7.gif "Animated gif of simulation video (test7)"

[final_short]: ./output/final_short.gif "Animated gif of final output video (short version)"
[final_long]: ./output/final_long.gif "Animated gif of final output video (long version)"
[final_left]: ./output/final_ChangeLeft.gif "Animated gif of final output video (change left)"
[final_slow]: ./output/final_SlowDown.gif "Animated gif of final output video (slow down)"
[final_right]: ./output/final_ChangeRight.gif "Animated gif of final output video (change right)"

---
## About Path Planning Project

The goals / steps of this project are the following:

* The goal of this project is to build a path planner that creates smooth, safe trajectories for the car to follow. The highway track has other vehicles, all going different speeds, but approximately obeying the 50 MPH speed limit. The car transmits its location, along with its sensor fusion data, which estimates the location of all the vehicles on the same side of the road.
* More detail explanation can be found in [README](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/README.md)

---
## Project code

Here is my working repository for this project:

https://github.com/pl80tech/CarND-Path-Planning-Project.git

It is imported and frequently updated (cherry-pick or merge) from below original repository:

https://github.com/udacity/CarND-Path-Planning-Project.git

---
## Rubric Points

Here are the [Rubric Points](https://review.udacity.com/#!/rubrics/1971/view) which need to be addressed to meet the requirements of this project. Each point/criteria is explained in next sections.

---
## Code compilation

The final solution is implemented in [/src/main.cpp](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/src/main.cpp) and it can be compiled successfully with **cmake** and **make** (as explained in [README](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/README.md)).

```shell
$ cmake ..
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done

$ make
Scanning dependencies of target path_planning
[ 50%] Building CXX object CMakeFiles/path_planning.dir/src/main.cpp.o
[100%] Linking CXX executable path_planning
[100%] Built target path_planning
```

Some tests (test1 ~ test7) are implemented in [main_test.cpp](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/src/main_test.cpp) with correspondent compile definition **-DTEST1** ~ **-DTEST7**. It can be compile by adding the definition and specifying the target source code in [CMakeLists.txt](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/CMakeLists.txt) as below:

```cmake
add_definitions(-DTEST1)

set(sources src/main_test.cpp)
```

After adding the compile options in [CMakeLists.txt](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/CMakeLists.txt) (by [following commit](https://github.com/pl80tech/CarND-Path-Planning-Project/commit/585c4093a5cd2af960f1264786ccf061c413dedb)), each test can be enabled by simply specifying the option when running cmake as below:

```shell
$ cmake -DTEST1=ON ..
$ make
```

---
## Valid Trajectories

As shown on [Output video](#Output-video), the trajectories generated by final solution are valid and can meet all the required specifications.

* The car is able to drive more than 7 miles without incident
* The car drives according to the speed limit (moving as fast as possible but always less than 50mph)
* Max Acceleration and Jerk are not exceeded (no red warning)
* Car does not have collisions
* The car stays in its lane, except for the time between changing lanes
* The car is able to change lanes when necessary

---
## Reflection

## Path generation and planning

The main code to generate the trajectory, control the velocity & decide the driving lane is implemented in *main()* function on [main.cpp](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/src/main.cpp) (line 294 ~ line 474) with detail comment for each process. Here are some main points of the implemention:

* Get the data from sensor fusion and use below functions to detect the cars moving in each lane for further processing (line 309 ~ line 345)
	* *getLane():* get lane of other car from d information
	* *isAhead():* check whether other car is moving ahead in close range or not
	* *isClose():* check whether other car is in close range or not
	* *isTarget():* check whether other car is a target for further checking
* Use below flags (set in above process) to decide the lane and velocity for next trajectory (line 347 ~ line 368)
	* *isCarAhead*: whether there is a car moving closely ahead
	* *isCarLeft*: whether there is a car moving closely on left lane
	* *isCarRight*: whether there is a car moving closely on right lane
* Use the points from previous trajectory and some new poinst generated by spline open source library (mentioned in [Reference](#Reference)) to create the next trajectory when moving forward or changing to left/right lane (line 370 ~ line 474)

## Further improvement

Here are some ideas which may help to improve the performance of current solution.

* Take into account the speed of the cars moving on left or right lane to avoid potential collision in some specific cases (for example when the cars in other lanes change the speed very fastly while lane changing is being executed, etc)
* Dynamically change the safe distance correspondent to the reference velocity (need to be optimized) instead of using a constant  (SAFE_DISTANCE = 30) in current solution.

---
## Output video

### Final output

Here are the final output videos uploaded on Youtube for easy reference. Click on the thumbnail image to jump to the video on Youtube. Click on the hyperlink to download the video from Google Drive (big size).

| [Short version](https://drive.google.com/open?id=1jxRWFcxBBjQk0v3BHh-obfSjYeunmjJZ) (4.47 miles) | [Long version](https://drive.google.com/open?id=1f8PO1-CLHWBGUC5TcWsCpG6K8amXM0e7) (7.13 miles)  |
|:--------------------------:|:--------------------------:|
| [![alt text][final_short]](https://www.youtube.com/watch?v=LEVu-Uy5Nb0) | [![alt text][final_long]](https://www.youtube.com/watch?v=01b2ZkRlezk) |

Here are some animated images from final output video showing the behavior of the car when keeping or changing lane.

| Change left             | Keep lane and slow down | Change right             |
|:-----------------------:|:-----------------------:|:------------------------:|
| ![alt text][final_left] | ![alt text][final_slow] | ![alt text][final_right] |

### Simulation test

Here are the simulation videos of some tests which are implemented under correspondent compile definitions (TEST1 ~ TEST7). Refer to section [Code compilation](#Code-compilation) on how to compile the code for each test. Click on the thumbnail image to jump to the video on Youtube.

| Filename | Content | Compile definition | Link on Youtube |
|:--------:|:-------:|:------------------:|:---------------:|
| [test1.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test1.mp4) | Moving straight at constant velocity | -DTEST1 | [![alt text][animation1]](https://www.youtube.com/watch?v=_qdQqQSLnUI) |
| [test2.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test2.mp4) | Moving in a circle | -DTEST2 | [![alt text][animation2]](https://www.youtube.com/watch?v=qh-NQ2_cI1c) |
| [test3.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test3.mp4) | Moving in a same line | -DTEST3 | [![alt text][animation3]](https://www.youtube.com/watch?v=zmK4KvYfrow) |
| [test4.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test4.mp4) | Moving in a same line with smoother trajectory| -DTEST4 | [![alt text][animation4]](https://www.youtube.com/watch?v=VZFG87Pr-A4) |
| [test5.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test5.mp4) | Slowing down the speed when moving close to another car | -DTEST5 | [![alt text][animation5]](https://www.youtube.com/watch?v=_Wxj_l_im1E) |
| [test6.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test6.mp4) | Speed up and slow down gradually | -DTEST6 | [![alt text][animation6]](https://www.youtube.com/watch?v=r1ohGnhga4E) |
| [test7.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test7.mp4) | Change to left lane when detecting a car moving closely ahead | -DTEST7 | [![alt text][animation7]](https://www.youtube.com/watch?v=t18hE0zdOm4)|
---
## Test code

Folder [/test_code/](https://github.com/pl80tech/CarND-Path-Planning-Project/tree/master/test_code) includes the code (Jupyter notebook, C++) for the quiz on lesson 8 ~ 11. Refer to the description on [runtest.sh](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/test_code/runtest.sh) about how to compile and run the C++ code.

---
## Reference

[1] [Cubic Spline interpolation in C++](https://kluge.in-chemnitz.de/opensource/spline/)