import rclpy
from rclpy.node import Node
def main(args=None):
    """
    """
    rclpy.init(args=args)
    node=Node("li4")
    node.get_logger().info("Hello,I'm Li 4.")
    rclpy.spin(node)
    rclpy.shutdown()