# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/1d_np

import bpy


class Np1d_panel(bpy.types.Panel):
    bl_idname = 'np1d.panel'
    bl_label = 'NP_1D_Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = '1D'

    def draw(self, context):
        self.layout.operator("replica.replica", text="Replica")


def register():
    bpy.utils.register_class(Np1d_panel)


def unregister():
    bpy.utils.unregister_class(Np1d_panel)
