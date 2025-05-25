import torch
from comfy.model_management import get_torch_device

print("Loading Custom Node...")  # Debug print

class NumberIncrementNode:
    """
    数字加1节点
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "number": ("INT", {"default": 0, "min": -1000000, "max": 1000000}),
            },
        }
    
    RETURN_TYPES = ("INT", "STRING")
    RETURN_NAMES = ("number", "display")
    FUNCTION = "increment"
    CATEGORY = "custom"

    def increment(self, number):
        # 数字加1
        result = number + 1
        return (result, f"输入: {number} -> 输出: {result}")

# 节点注册
NODE_CLASS_MAPPINGS = {
    "NumberIncrement": NumberIncrementNode
}

# 节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "NumberIncrement": "Number +1"
}

print("Custom Node registered:", NODE_CLASS_MAPPINGS)  # Debug print 