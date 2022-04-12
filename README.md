# ROS2_modeling
This is a task to test your ability to learn and implement a simple ROS simulation using given robot CAD model.   
Show that robot can be moved via teleoperation and navigate from point A to point B within the virtual environment.  
To start, please ensure source the environment  
Open a terminal under workplace, and type  
```bash
. install/setup.bash
```
Don't forget to do this process when creating a new terminal!  
## Structure
└── farmbot  
    ├── config  
    ├── farmbot    
    ├── launch     
    ├── meshes  
    ├── models  
    ├── resource  
    ├── test  
    └── world  
## Environment
ROS2 foxy  
Gazebo  
python3  
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
