from .add_node import SimpleAddNode

# 必须的变量名，ComfyUI 会读取这个字典来注册节点
NODE_CLASS_MAPPINGS = {
    "Simple Add Node": SimpleAddNode,
}

# 可选：如果要添加前端交互（JS），可以指定 WEB_DIRECTORY
WEB_DIRECTORY = "./js"

# 必须的变量名，用于导出
__all__ = ['NODE_CLASS_MAPPINGS', 'WEB_DIRECTORY']