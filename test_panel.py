import bpy
from bpy.types import Panel


class TEST_PT_Panel(Panel):

    bl_idname = "Test_PT_Panel"
    bl_label = "Test Panel"
    bl_category = "Test Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, cotext):
        layout = self.layout 
        row = layout.row()
        row.operator('view3d.cursor_center')