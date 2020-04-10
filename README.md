# Robotics book code

This repo accompanies the text [ricopic.one/robotics](http://ricopic.one/robotics). It is organized into packages, one for each chapter. 

## Requirements

The text assumes the use of ROS Melodic Morenia and Ubuntu 18.04.4 LTS (Bionic Beaver). Instructions for installing this development environment are included in the text.

## Installation

To make the chapter packages available to your ROS distribution, complete the following steps.

1. Create a ROS workspace with a `src` directory.
2. Download and unzip or (fork! and) clone this repository to the `src` directory.
```bash
git clone https://github.com/ricopicone/robotics-book-code.git
```
3. In the workspace, make.
```bash
catkin_make
```
4. Source your workspace.
```bash
source devel/setup.bash
```

The chapter packages are now available to your ROS distribution. If you have `rosbash` installed (and you should), the chapter packages should appear to `roscd` and `rosls`.

## Organization

Due to the developing nature of the text and code, chapter numbers are omitted and instead are identified by abbreviated name. For instance, the chapter _ROS topics_ is abbreviated `rico_topics`. The prefix `rico_` is included to differentiate the textbook packages.

## Origins

This repository began as a fork of the sample code [repository](https://github.com/gbiggs/ros_book_sample_code) that accompanies the excellent text _Programming Robots with ROS_, by Morgan Quigley, Brian Gerkey and William D. Smart (O'Reilly Media, Inc., 2015). The original repository was distributed under the Apache 2.0 license. Differences in ROS and Ubuntu software versions, book organizational structure, and code details suggested moving from fork to distinct project, but I express my significant debt to this original repository and gratitude to its authors.
