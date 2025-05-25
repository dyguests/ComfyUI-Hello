import torch
from server import PromptServer  # ComfyUI 的服务端API


class SimpleAddNode:
    """
    最简单的自定义节点：输入一个数字，输出该数字 +1
    """

    # 定义节点在 UI 中的分类（会出现在菜单里）
    CATEGORY = "Simple Nodes"

    # 定义节点的功能名称（调用方法）
    FUNCTION = "add_one"

    # 定义输出类型（这里返回一个浮点数）
    RETURN_TYPES = ("FLOAT",)

    @classmethod
    def INPUT_TYPES(cls):
        """
        定义输入参数：
        - number: 浮点数输入，默认值 0.0，范围 0~100，步长 0.1
        """
        return {
            "required": {
                "number": ("FLOAT", {
                    "default": 0.0,
                    "min": 0.0,
                    "max": 100.0,
                    "step": 0.1
                }),
            },
        }

    def add_one(self, number):
        """
        节点逻辑：输入数字 +1
        """
        result = number + 1.0
        return (result,)