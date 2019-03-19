import bpy
from bpy.types import Operator


class TEST_OT_Operator(Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Simple operator"
    bl_descrition = "Center 3d cursor"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        return {'FINISHED'}