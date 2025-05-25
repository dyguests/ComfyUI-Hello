import torch
from comfy.model_management import get_torch_device

print("Loading Custom Node...")  # Debug print

class CustomNode:
    """
    自定义节点示例
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": ("STRING", {"default": "Hello World"}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "custom"

    def process(self, input):
        # 在这里处理输入并返回结果
        return (input,)

# 节点注册
NODE_CLASS_MAPPINGS = {
    "CustomNode": CustomNode
}

# 节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "CustomNode": "Custom Node"
}

print("Custom Node registered:", NODE_CLASS_MAPPINGS)  # Debug print 