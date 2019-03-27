# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_np
#
# Version history:
#   1.1. - Extended to Edit mode
#   1.0. - ZZMove, CCCopy. Object mode


import bpy


class VIEW3D_PT_Np1d_panel(bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_np1d_panel'
    bl_label    = '1D_NP'
    bl_category = '1D_NP'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_region_type = 'HEADER'

    def draw(self, context):
        self.layout.operator("np1d.zzmove", text="ZZ Move")
        self.layout.operator("np1d.cccopy", text="CC Copy")

#def draw_np1d(self, context):
#    self.layout.operator("np1d.zzmove", text="ZZ Move")
#    self.layout.operator("np1d.cccopy", text="CC Copy")

def register():
    bpy.utils.register_class(VIEW3D_PT_Np1d_panel)
    #bpy.types.VIEW3D_HT_header.append(draw_np1d)


def unregister():
    #bpy.types.VIEW3D_HT_header.remove(draw_np1d)
    bpy.utils.unregister_class(VIEW3D_PT_Np1d_panel)
