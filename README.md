# Optimizing Traffic Light Detection for AutoRace 2019 Competition Package

This project optimizes the traffic light detection mechanism in the AutoRace 2019 competition by replacing the old **blob detection algorithm** with a **new pixel counting algorithm**. The new algorithm provides more reliable and practical results for detecting the three traffic light colors, significantly improving the autonomous driving performance of the original package.

## Project Overview

- **Objective**: Replace the blob detection algorithm with a pixel counting algorithm to improve traffic light detection.
- **Hardware Platform**: TurtleBot3 Burger.
- **Main Contributions**:
  - Improved traffic light color detection (red, yellow, green).
  - Enhanced the performance of autonomous driving in the AutoRace package.

## Hardware Requirements

- **TurtleBot3 Burger**.
- **Raspberry Pi Camera Type G (Fisheye Lens)**:
  - Ensure the correct mounting of the camera, especially if using conductive materials.
- **Raspberry Pi Camera Mount**.
- **Track structure and accessories**, including:
  - Traffic signs.
  - Traffic lights.
  - Other objects.
## Software Requirements

- **ROS 1 Noetic** on Ubuntu 20.04.
- Dependencies installed for both the **TurtleBot3** and the **remote PC**.
- ROS and dependent packages should be installed both on the robot and the remote PC.



## Getting Started

### Step 1: Install the Optimized AutoRace Packages

Run the following commands on your remote PC:

```bash
$ cd ~/catkin_ws/src/
$ git clone https://github.com/Ibrahim1Hassan/Optimizing-Traffic-Sign-Detection-for-Turtlebot3-ROS-Autonomous-Driving
$ cd ~/catkin_ws && catkin_make
```

### Step 2: Install Dependencies

Run the following commands on your remote PC:

```bash
$ sudo apt-get install ros-noetic-image-transport ros-noetic-cv-bridge ros-noetic-vision-opencv python3-opencv libopencv-dev ros-noetic-image-proc
```
### Step 3: Intrinsic Camera Calibration


1. **Remote PC**: Open a new terminal and start ROS:

    ```bash
    $ roscore
    ```

2. **TurtleBot SBC**: Launch the camera node:

    ```bash
    $ roslaunch turtlebot3_autorace_camera turtlebot3_autorace_camera_pi.launch
    ```

3. **Remote PC**: Use the calibration checkerboard:

    ```bash
    $ export AUTO_IN_CALIB=calibration
    $ roslaunch turtlebot3_autorace_camera turtlebot3_autorace_intrinsic_camera_calibration.launch
    ```

4. **After Calibration**: Overwrite the values of the intrinsic camera calibration file:

    ```bash
    turtlebot3_autorace_camera/calibration/intrinsic_calibration/camerav2_320x240_30fps.yaml
    ```
### Step 4: Extrinsic Camera Calibration

1. **Remote PC**: Start ROS:

    ```bash
    $ roscore
    ```

2. **TurtleBot SBC**: Launch the camera node:

    ```bash
    $ roslaunch turtlebot3_autorace_camera turtlebot3_autorace_camera_pi.launch
    ```

3. **Remote PC**: Start extrinsic calibration:

    ```bash
    $ export AUTO_EX_CALIB=calibration
    $ roslaunch turtlebot3_autorace_camera turtlebot3_autorace_extrinsic_camera_calibration.launch
    ```

4. **Adjust Parameters**: Use `rqt` to tune the parameters:

    ```bash
    $ rosrun rqt_reconfigure rqt_reconfigure
    ```
### Step 5: Traffic Light Calibration

1. Place the robot on the track with the **yellow line on the left** and **white line on the right**.
2. Ensure that the `turtlebot3_robot` node from the `turtlebot3_bringup` package is **not running**.
3. Open a new terminal on the **Remote PC**:

    ```bash
    $ export AUTO_DT_CALIB=calibration
    $ roslaunch turtlebot3_autorace_detect turtlebot3_autorace_detect_traffic_light.launch
    ```

4. Use `rqt_image_view` to monitor the camera feed for red, yellow, and green lights:

    ```bash
    $ rqt
    ```

5. Adjust the traffic light filters using `rqt_reconfigure`:

    ```bash
    $ rosrun rqt_reconfigure rqt_reconfigure
    ```

6. After calibration, overwrite the parameters in `traffic_light.yaml`:

    ```bash
    turtlebot3_autorace_detect/param/traffic_light/traffic_light.yaml
    ```
### Step 6: Running the Traffic Light Challenge

Once calibration is complete, run the challenge with the following command:

```bash
$ export AUTO_DT_CALIB=action
$ roslaunch turtlebot3_autorace_detect turtlebot3_autorace_detect_traffic_light.launch
```
## Additional Notes

This project was part of the **Autonomous Systems** module in the Master’s in Embedded Systems program at Hochschule Anhalt.  
For detailed documentation and a demonstration video, please refer to the `/Technical Report + Demo Video` directory.

For additional information, please refer to the original AutoRace 2019 package guide and documentation:

- [TurtleBot3 Autonomous Driving Guide](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/)
- [TurtleBot3 AutoRace Documentation](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving_autorace/)
