from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Joint State Publisher node
        Node(
            package='your_custom_package',
            executable='joint_state_publisher.py',
            name='joint_state_publisher',
            output='screen'
        ),

        # Servo Controller node
        Node(
            package='your_custom_package',
            executable='servo_controller.py',
            name='servo_controller',
            output='screen'
        ),

        # Optional: Include MoveIt2 demo (adjust package and launch file names)
        # Node(
        #     package='moveit2_tutorials',
        #     executable='demo.launch.py',
        #     name='moveit2_demo',
        #     output='screen'
        # )
    ])
