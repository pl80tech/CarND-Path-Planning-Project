# **Path Planning Project** 

## Writeup

This is my writeup for the project "Path Planning" of Self Driving Car Nanadegree on Udacity.

---

### Contents

* [About Path Planning Project](#About-Path-Planning-Project)
* [Project code](#Project-code)
* [Rubric Points](#Rubric-Points)
* [Output video](#Output-video)
	* [Final output](#Final-output)
	* [Simulation test](#Simulation-test)
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

Here are the [Rubric Points](https://review.udacity.com/#!/rubrics/1971/view) which need to be addressed to meet the requirements of this project.

---
## Output video

### Final output

| Short version              | Long version               |
|:--------------------------:|:--------------------------:|
| [![alt text][final_short]](https://www.youtube.com/watch?v=LEVu-Uy5Nb0) | [![alt text][final_long]](https://www.youtube.com/watch?v=01b2ZkRlezk) |

### Simulation test

Here are the simulation test videos which were uploaded on Youtube (for easy reference). Click on the thumbnail image to jump to the video on Youtube.

| Filename | Content | Compile flag | Link on Youtube |
|:--------:|:-------:|:------------:|:---------------:|
| [test1.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test1.mp4) | Moving straight at constant velocity | -DTEST1 |[![alt text][animation1]](https://www.youtube.com/watch?v=_qdQqQSLnUI)|
| [test2.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test2.mp4) | Moving in a circle | -DTEST2 |[![alt text][animation2]](https://www.youtube.com/watch?v=qh-NQ2_cI1c)|
| [test3.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test3.mp4) | Moving in a same line | -DTEST3 |[![alt text][animation3]](https://www.youtube.com/watch?v=zmK4KvYfrow)|
| [test4.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test4.mp4) | Moving in a same line with smoother trajectory| -DTEST4 |[![alt text][animation4]](https://www.youtube.com/watch?v=VZFG87Pr-A4)|
| [test5.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test5.mp4) | Slowing down the speed when moving close to another car | -DTEST5 |[![alt text][animation5]](https://www.youtube.com/watch?v=_Wxj_l_im1E)|
| [test6.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test6.mp4) | Speed up and slow down gradually | -DTEST6 |[![alt text][animation6]](https://www.youtube.com/watch?v=r1ohGnhga4E)|
| [test7.mp4](https://github.com/pl80tech/CarND-Path-Planning-Project/blob/master/output/test7.mp4) | Change to left lane when detecting a car moving closely ahead | -DTEST7 |[![alt text][animation7]](https://www.youtube.com/watch?v=t18hE0zdOm4)|

---
## Reference

[1] [Cubic Spline interpolation in C++](https://kluge.in-chemnitz.de/opensource/spline/)