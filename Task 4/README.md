## Task 4 Submission

You can find the ROS package [here](tutorials)

**TF Tutorials**

- Create a nodes and launch directory in ROS package.
- Create the broadcaster and listener files, add them in nodes.
- Create launch file, add it in launch.
- Run using:

```
    roslaunch <ros-pkg> <launch-file>.launch
```

**Creating a Broadcaster**
<img src="Data/tut1.png">

**Creating a Listener**
<img src="Data/tut2.png">

**Adding Frames (Fixed)**
<img src="Data/tut3.png">

**Adding Frames (Dynamic)**
<img src="Data/tut4.png">

**Time Travel using TF**
<img src="Data/tut5.png">

<img src="Data/tut6.png">

**URDF Tutorials**

- Create a urdf and launch directory in ROS package.
- Create the urdf file and add to urdf.
- Create launch files for rviz and gazebo and add to launch.
- Run using:

```
    roslaunch <ros-pkg> <launch-file>.launch model:='$(find <ros-pkg>)/urdf/<urdf-file>.urdf'
```

**URDF Visualization in Rviz**
<img src="Data/tut7.png">

```
    roslaunch <ros-pkg> <gazebo-launch-file>.launch
```

**URDF Visualization in Gazebo**
<img src="Data/tut8.png">
