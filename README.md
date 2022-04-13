# ROS2_modeling
This is a task to test your ability to learn and implement a simple ROS simulation using given robot CAD model.   
Show that robot can be moved via teleoperation and navigate from point A to point B within the virtual environment.  
To start, please ensure source the environment  
Open a terminal under workplace, and type  
```bash
. install/setup.bash
```
Don't forget to do this process when creating a new terminal!  
Furthermore, please export the path under bashrc  
```bash
gedit ~/.bashrc
```
and add the path under your_workspace/src  
For example, path to your model: home/your_user_name/your_workspace/src/farmbot/meshes
```
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:<path to your model>
```
Finally, in order to make sure model components can be read by Gazebo  
Copy the package under the gazebo default path  
Open the terminal under your_workspace/src, and type  
```bash
cp -r farmbot ~/.gazebo/models
```
## Structure
```
└── farmbot      #package name
    ├── config   #rviz file
    ├── farmbot  
    ├── launch   
    ├── meshes   #model components
    ├── models   #urdf file
    ├── resource  
    ├── test  
    └── world    #gazebo world file
```
## Environment
Ubuntu20.04
ROS2 foxy  
Gazebo11  
python3  
##### Dependencies
Please make sure the environment include dependencies below  
```
ros-foxy-robot-localization  
ros-foxy-ros2-control  
ros-foxy-ros2-controllers
```
## Teleop
This step is to control the model with keyboard.  
The main idea is to connect the model with "/cmd_vel" and "/odom", which can allow builtin teleop to control.  
To run the code, please type  
```bash
ros2 launch farmbot teleop_launch.py
```
It will start Gazebo with a model in it.    
Then open another terminal, and type  
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
Now the model can be controlled by "i"(up), "j"(turn left), "l"(turn right), and ","(down)  
For other functions, they will show on terminal.  
Result  
[![Watch the video](https://img.youtube.com/vi/CR262LVR7MQ/maxresdefault.jpg)](https://youtu.be/CR262LVR7MQ)

## Move to certain position
This step is to move the model to the certain position   
The main idea is to subscribe /odom to get the model pose and publish speed to /cmd_vel.  
The calculation is simple. When the theta of the model is more than 0.1 to the goal theta, the model will spin.  
Otherwise, the model will go straight.  
When achieving the goal, the model will spin at the position.  
To run the code, please type  
```bash
ros2 launch farmbot teleop_launch.py
```
It will start Gazebo with a model in it.    
Then open another terminal, and type  
```bash
ros2 run farmbot move
```
ps. Don't forget to source the terminal  
Result  
[![Watch the video](https://img.youtube.com/vi/_cX2DPGpzag/maxresdefault.jpg)](https://youtu.be/_cX2DPGpzag)
