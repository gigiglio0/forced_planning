#!/usr/bin/env pyhton3
import rclpy
from rclpy.node import Node




class MyNode(Node):
    def __init__(self):
        super().__init__("motor_controller")
        self.get_logger().info("Avvio i motori!")



def main(args=None):
    rclpy.init(args=args)  

    node = MyNode()
    rclpy.spin(node) #it continues to run until you kill it form the keyboard

    rclpy.shutdown()




if __name__ == '__main__':
    main()




