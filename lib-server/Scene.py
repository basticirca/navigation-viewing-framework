#!/usr/bin/python

## @file
# Contains classes SceneManager, TimedMaterialUniformUpdate and TimedRotationUpdate.

# import avango-guacamole libraries
import avango

# import framework libraries
from Objects import *

# import python libraries
# ...


class Passat(SceneObject):

  # dummy testing scene with just the passat object

  # constructor
  def __init__(self, SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE):
    SceneObject.__init__(self, "Passat", SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE) # call base class constructor

    _mat = avango.gua.make_trans_mat(-1.99, 0.0, -3) * \
           avango.gua.make_rot_mat(-90.0,1,0,0) * \
           avango.gua.make_rot_mat(90.0,0,0,1) * \
           avango.gua.make_scale_mat(0.04)
    self.init_geometry("passat", "data/objects/passat/passat.obj", _mat, None, True, True, self.scene_root) 

    self.background_texture = "data/textures/skymap.png"


class SceneMedievalTown(SceneObject):

  # constructor
  def __init__(self, SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE):
    SceneObject.__init__(self, "MedievalTown", SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE) # call base class constructor

    # navigation parameters
    # nice navigation starting mat is avango.gua.make_trans_mat(0.0, 0.0, 22.0)

    # geometry
    _mat = avango.gua.make_scale_mat(7.5)
    self.init_geometry("town", "data/objects/demo_models/medieval_harbour/town.obj", _mat, None, True, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    
    _mat = avango.gua.make_trans_mat(0, -3.15, 0) * avango.gua.make_scale_mat(1000.0)
    self.init_geometry("water", "data/objects/plane.obj", _mat, 'data/materials/Water.gmd', True, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG,
  
    #_mat = avango.gua.make_trans_mat(0.0, 0.0, 20.0)
    #self.init_kinect("kinect1", "/opt/kinect-resources/shot_steppo_animation_distributed_daedalos.ks", _mat, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, PARENT_NODE    
    #self.init_kinect("kinect1", "/opt/kinect-resources/kinect_surface_K_23_24_25.ks", _mat, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, PARENT_NODE
     
    # lights
    _mat = avango.gua.make_rot_mat(72.0, -1.0, 0, 0) * avango.gua.make_rot_mat(-30.0, 0, 1, 0)
    self.init_light(TYPE = 0, NAME = "sun_light", COLOR = avango.gua.Color(0.75,0.75,0.75), MATRIX = _mat, PARENT_NODE = self.scene_root, ENABLE_SHADOW = False, RENDER_GROUP = "main_scene") # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE
    
    #_mat = avango.gua.make_trans_mat(0.0, 35.0, 20.0) * avango.gua.make_rot_mat(-65.0,1,0,0)
    #self.init_light(TYPE = 2, NAME = "spot_light", COLOR = avango.gua.Color(1.0, 1.0, 1.0), MATRIX = _mat, PARENT_NODE = self.scene_root, MANIPULATION_PICK_FLAG = True, RENDER_GROUP = "main_scene", ENABLE_SHADOW = True, LIGHT_DIMENSIONS = avango.gua.Vec3(300.0,300.0,150.0) ) # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE

    # render pipeline parameters
    self.enable_backface_culling = False
    self.enable_frustum_culling = True
    self.enable_ssao = False
    self.enable_fxaa = True


class ScenePitoti(SceneObject):

  # constructor
  def __init__(self, SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE):
    SceneObject.__init__(self, "ScenePitotiTest", SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE) # call base class constructor

    # navigation parameters
    # nice navigation starting mat is avango.gua.make_trans_mat(0.092, 4.922, 22.049)

    # geometry
    _mat = avango.gua.make_identity_mat()
    self.init_point_cloud("spacemonkey", "/mnt/pitoti/KDN_LOD/PITOTI_KDN_LOD/Spacemonkey_new.kdn", _mat, self.scene_root, "main_scene")
          
    # lights
    _mat = avango.gua.make_rot_mat(72.0, -1.0, 0, 0) * avango.gua.make_rot_mat(-30.0, 0, 1, 0)
    self.init_light(TYPE = 0, NAME = "sun_light", COLOR = avango.gua.Color(0.5, 0.5, 0.5), MATRIX = _mat, PARENT_NODE = self.scene_root, ENABLE_SHADOW = True) # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE


class SceneVianden(SceneObject):

  # constructor
  def __init__(self, SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE):
    SceneObject.__init__(self, "SceneVianden", SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE) # call base class constructor

    # nice navigation starting mat is avango.gua.make_trans_mat(72.730, -5.571, -51.930)  

    # geometry
    _mat = avango.gua.make_rot_mat(90.0,-1,0,0)
    #self.init_geometry("vianden_out", "data/objects/demo_models/Arctron/Vianden/Aussen_gesamt/VIANDEN.obj", _mat, None, True, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    #self.init_geometry("vianden_in", "data/objects/demo_models/Arctron/Vianden/Innen_gesamt/Innenraeume_Gesamt.obj", _mat, None, True, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_geometry("vianden_out", "/mnt/ssd_pitoti/Vianden/Aussen_gesamt/VIANDEN.obj", _mat, None, True, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_geometry("vianden_in", "/mnt/ssd_pitoti/Vianden/Innen_gesamt/Innenraeume_Gesamt.obj", _mat, None, True, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE

          
    # lights
    _mat = avango.gua.make_rot_mat(72.0, -1.0, 0, 0) * avango.gua.make_rot_mat(-30.0, 0, 1, 0)
    self.init_light(TYPE = 0, NAME = "sun_light", COLOR = avango.gua.Color(1.0, 1.0, 1.0), MATRIX = _mat, PARENT_NODE = self.scene_root, ENABLE_SHADOW = False, SHADOW_MAP_SIZE = 256, ENABLE_GODRAYS = False) # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE

    '''
    _mat = avango.gua.make_trans_mat(50.0, 100.0, -50.0) * \
           avango.gua.make_rot_mat(-90.0, 1.0, 0.0, 0.0)

    self.init_light(TYPE = 2, 
                    NAME = "spot_light",
                    COLOR = avango.gua.Color(1.0, 1.0, 1.0), 
                    MATRIX = _mat, 
                    PARENT_NODE = self.scene_root,
                    RENDER_GROUP = "main_scene", 
                    MANIPULATION_PICK_FLAG = True, 
                    ENABLE_SHADOW = True, 
                    LIGHT_DIMENSIONS = avango.gua.Vec3(900.0,900.0,300.0),
                    SHADOW_MAP_SIZE = 2048)
    '''


    # render pipeline parameters
    self.enable_backface_culling = False
    self.enable_frustum_culling = True
    self.enable_ssao = False
    self.enable_fxaa = True
    self.enable_fog = False
    self.ambient_color = avango.gua.Color(0.25, 0.25, 0.25)
    #self.background_texture = "/opt/guacamole/resources/skymaps/DH221SN.png"
    self.background_texture = "/opt/guacamole/resources/skymaps/cycles_island2.jpg"

 
class SceneMonkey(SceneObject):

  # constructor
  def __init__(self, SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE):
    SceneObject.__init__(self, "Monkey", SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE) # call base class constructor

    # nice navigation starting mat is avango.gua.make_trans_mat(0.0, 0.0, 1.0)

    _mat = avango.gua.make_identity_mat()
    self.init_group("group", _mat, False, True, self.scene_root, "main_scene")

    _parent_object = self.get_object("group")

    _mat = avango.gua.make_trans_mat(0.0,1.2,0.0) * avango.gua.make_scale_mat(0.1)
    self.init_geometry("monkey1", "data/objects/monkey.obj", _mat, "data/materials/SimplePhongWhite.gmd", False, True, _parent_object, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE, RENDER_GROUP

    _mat = avango.gua.make_trans_mat(-0.25,1.2,0.0) * avango.gua.make_scale_mat(0.05)
    self.init_geometry("monkey2", "data/objects/monkey.obj", _mat, "data/materials/AvatarBlue.gmd", False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE

    _mat = avango.gua.make_trans_mat(0.25,1.2,0.0) * avango.gua.make_scale_mat(0.05)
    self.init_geometry("monkey3", "data/objects/monkey.obj", _mat, "data/materials/AvatarBlue.gmd", False, True, _parent_object, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE

    _mat = avango.gua.make_trans_mat(0.0, 1.0, 0.0) * avango.gua.make_scale_mat(2.0)
    self.init_geometry("plane", "data/objects/plane.obj", _mat, 'data/materials/ComplexPhongTiles.gmd', False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
  
    
    # lights
    _mat = avango.gua.make_rot_mat(72.0, -1.0, 0, 0) * avango.gua.make_rot_mat(-30.0, 0, 1, 0)
    self.init_light(TYPE = 0, NAME = "sun_light", COLOR = avango.gua.Color(0.5, 0.5, 0.5), MATRIX = _mat, PARENT_NODE = self.scene_root, ENABLE_SHADOW = True, RENDER_GROUP = "main_scene") # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE

    _mat = avango.gua.make_trans_mat(-0.3, 1.4, 0.0)
    self.init_light(TYPE = 1, NAME = "point_light", COLOR = avango.gua.Color(0.0, 1.0, 0.0), MATRIX = _mat, PARENT_NODE = self.scene_root, MANIPULATION_PICK_FLAG = True, RENDER_GROUP = "main_scene") # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE

    _mat = avango.gua.make_trans_mat(0.0, 1.55, 0.0) * avango.gua.make_rot_mat(90.0,-1,0,0)
    self.init_light(TYPE = 2, NAME = "spot_light", COLOR = avango.gua.Color(1.0, 0.25, 0.25), MATRIX = _mat, PARENT_NODE = self.scene_root, MANIPULATION_PICK_FLAG = True, ENABLE_SHADOW = True, LIGHT_DIMENSIONS = avango.gua.Vec3(2.0,2.0,1.0), RENDER_GROUP = "main_scene") # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE



class ScenePLOD(SceneObject):

  # constructor
  def __init__(self, SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE):
    SceneObject.__init__(self, "PLOD", SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE) # call base class constructor

    # nice navigation starting mat is avango.gua.make_trans_mat(0.0, 0.0, 1.0)

    _mat = avango.gua.make_trans_mat(0.0,1.2,0.0) * avango.gua.make_scale_mat(0.25)
    self.init_plod("pig", "/opt/3d_models/point_based/plod/pig.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE

    #_mat = avango.gua.make_trans_mat(1.0,2.5,0.0) * avango.gua.make_scale_mat(3.0)
    #self.init_plod("pitoti", "/mnt/pitoti/KDN_LOD/PITOTI_KDN_LOD/Spacemonkey_new.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE    

    #_mat = avango.gua.make_trans_mat(1.0,2.5,0.0) * avango.gua.make_scale_mat(3.0)
    #self.init_plod("pitoti", "/mnt/pitoti/XYZ_ALL/new_pitoti_sampling/Area_4_hunter_with_bow.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE    

    #_mat = avango.gua.make_identity_mat()
    #self.init_plod("pitoti", "/mnt/pitoti/XYZ_ALL/new_pitoti_sampling/TLS_Seradina_Rock-12C.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE    

    _mat = avango.gua.make_trans_mat(0.0, 1.0, 0.0) * avango.gua.make_scale_mat(3.0)
    self.init_geometry("plane", "data/objects/plane.obj", _mat, 'data/materials/ComplexPhongTiles.gmd', False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
  
    _mat = avango.gua.make_trans_mat(-1.1,1.3,0.0) * avango.gua.make_scale_mat(0.25)
    self.init_geometry("monkey2", "data/objects/monkey.obj", _mat, "data/materials/AvatarBlue.gmd", False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    
    # lights
    _mat = avango.gua.make_trans_mat(0.0, 1.55, 0.0)
    self.init_light(TYPE = 1, NAME = "point_light", COLOR = avango.gua.Color(0.0, 1.0, 0.0), MATRIX = _mat, PARENT_NODE = self.scene_root, MANIPULATION_PICK_FLAG = True, LIGHT_DIMENSIONS = avango.gua.Vec3(3.0,3.0,3.0)) # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE

    #_mat = avango.gua.make_trans_mat(0.0, 1.55, 0.0)
    #self.init_light(TYPE = 2, NAME = "spot_light", COLOR = avango.gua.Color(1.0, 0.25, 0.25), MATRIX = _mat, PARENT_NODE = self.scene_root, MANIPULATION_PICK_FLAG = True, ENABLE_SHADOW = True, LIGHT_DIMENSIONS = avango.gua.Vec3(2.0,2.0,1.0), RENDER_GROUP = "main_scene") # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE
      
class SceneValcamonicaTest(SceneObject):

  # constructor
  def __init__(self, SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE):
    SceneObject.__init__(self, "ValcamonicaTest", SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE) # call base class constructor

    self.starting_matrix = avango.gua.make_trans_mat(15.736, -12.518, 13.413)
    self.starting_scale = 0.022

    ### valley
    #_mat = avango.gua.make_trans_mat(-473.909*2, 377.739*2, -399.864*2) * \
    #        avango.gua.make_scale_mat(60.0, -60.0, -60.0)

    # seradina flyover
    _mat = avango.gua.make_scale_mat(1.0, -1.0, -1.0)
    
    #_path = "/mnt/pitoti/Seradina_FULL_SCAN/sera_fixed/"
    _path = "/mnt/ssd_pitoti/pitoti/valley/seradina_flyover/" # pitoti ssd path
    
    self.init_plod("valley1", _path + "sera_part_01.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    
    self.init_plod("valley2", _path + "sera_part_02.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley3", _path + "sera_part_03.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley4", _path + "sera_part_04.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley5", _path + "sera_part_05.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley6", _path + "sera_part_06.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley7", _path + "sera_part_07.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley8", _path + "sera_part_08.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley9", _path + "sera_part_09.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley10", _path + "sera_part_10.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley11", _path + "sera_part_11.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley12", _path + "sera_part_12.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley13", _path + "sera_part_13.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley14", _path + "sera_part_14.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley15", _path + "sera_part_15.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
    self.init_plod("valley16", _path + "sera_part_16.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
 
    # foppe di nadro flyover
    #_path = "/mnt/pitoti/Foppe_di_Nadro_FULL_SCAN/"
    _path = "/mnt/ssd_pitoti/pitoti/valley/nadro_flyover/" # pitoti ssd path    

    _mat = avango.gua.make_identity_mat()
    _mat.set_element(0,0,-0.0184506)
    _mat.set_element(0,1, 0.0273582)
    _mat.set_element(0,2, 0.000322056)
    _mat.set_element(0,3,-53.0709)
    _mat.set_element(1,0,-0.000856462)
    _mat.set_element(1,1,-0.000965775)
    _mat.set_element(1,2, 0.0329747)
    _mat.set_element(1,3, 4.59356)
    _mat.set_element(2,0, 0.0273467)
    _mat.set_element(2,1, 0.0184281)
    _mat.set_element(2,2, 0.00125001)
    _mat.set_element(2,3, 5.75228)
 
    self.init_plod("valley17", _path + "foppe_di_nadro_const.kdn", _mat, False, True, self.scene_root, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE
 

    ### rocks
    
    # seradina 12c
    _mat = avango.gua.make_identity_mat()
    _mat.set_element(0,0,-0.01020285)
    _mat.set_element(0,1,0.05133345)
    _mat.set_element(0,2,-0.0041307)
    _mat.set_element(0,3,-4.360018767)
    _mat.set_element(1,0,0.0030513)
    _mat.set_element(1,1,0.0048069)
    _mat.set_element(1,2,0.05219025)
    _mat.set_element(1,3,-17.288150233)
    _mat.set_element(2,0,0.05140905)
    _mat.set_element(2,1,0.00990255)
    _mat.set_element(2,2,-0.00391755)
    _mat.set_element(2,3,10.845176942)
 

    self.init_group("seradina_12c_group", _mat, False, True, self.scene_root, "main_scene")

    _parent_object = self.get_interactive_object("seradina_12c_group")
    _mat = avango.gua.make_identity_mat()
    
    #_path = "/mnt/pitoti/XYZ_ALL/new_pitoti_sampling/" # opt path    
    #_path = "/media/SSD_500GB/Pitoti_Resampled/" # ssd path
    _path = "/mnt/ssd_pitoti/pitoti/seradina_12c/rock/" # pitoti ssd path

    self.init_plod("seradina_12c_rock", _path + "TLS_Seradina_Rock-12C.kdn", _mat, False, True, _parent_object, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE    


    # seradina motives
    _path = "/mnt/ssd_pitoti/pitoti/seradina_12c/motives/" # pitoti ssd path

    self.init_plod("seradina_motive1", _path + "Area-1_Warrior-scene_P01-1.kdn", _mat, False, False, _parent_object, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE    
    self.init_plod("seradina_motive2", _path + "Area-1_Warrior-scene_P01-2.kdn", _mat, False, False, _parent_object, "main_scene") # parameters: NAME, FILENAME, MATRIX, MATERIAL, GROUNDFOLLOWING_PICK_FLAG, MANIPULATION_PICK_FLAG, PARENT_NODE    



class SceneWeimar(SceneObject):

  # constructor
  def __init__(self, SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE):
    SceneObject.__init__(self, "Weimar", SCENE_MANAGER, SCENEGRAPH, NET_TRANS_NODE) # call base class constructor

    # nice navigation starting mat is avango.gua.make_trans_mat(42.0, 0.1, -5.8)
    
    self.enable_ssao = True
    self.ssao_radius = 2.0
    self.ssao_intensity = 2.0
    self.enable_fog = False
    self.ambient_color.value = avango.gua.Color(0.0, 0.0, 0.0)
    #self.ambient_color.value = avango.gua.Color(1.0, 0.0, 0.0)
    self.far_clip = 2000.0

    self.background_texture = "data/textures/bright_sky.jpg"

    _mat = avango.gua.make_scale_mat(0.5)
    #self.init_geometry("weimar", "data/objects/demo_models/weimar_stadtmodell_29.08.12/weimar_stadtmodell_final.obj", _mat, "data/materials/SimplePhongWhite.gmd", True, False, self.scene_root, "main_scene")
    self.init_geometry("weimar", "data/objects/demo_models/weimar_stadtmodell_29.08.12/weimar_stadtmodell_final.obj", _mat, None, True, False, self.scene_root, "main_scene")

    _mat = avango.gua.make_trans_mat(0.0, 200.0, 60.0) * \
           avango.gua.make_rot_mat(-45.0, 1.0, 0.0, 0.0)
    self.init_light(TYPE = 2, NAME = "spot_light", COLOR = avango.gua.Color(1.0, 1.0, 1.0), MATRIX = _mat, PARENT_NODE = self.scene_root, MANIPULATION_PICK_FLAG = True, ENABLE_SHADOW = False, LIGHT_DIMENSIONS = avango.gua.Vec3(1000.0,1000.0,300.0), FALLOFF = 0.009, SOFTNESS = 0.003, SHADOW_MAP_SIZE = 2048, ENABLE_SPECULAR_SHADING = True)

    #_mat = avango.gua.make_rot_mat(72.0, -1.0, 0, 0) * avango.gua.make_rot_mat(-30.0, 0, 1, 0)
    #self.init_light(TYPE = 0, NAME = "sun_light", COLOR = avango.gua.Color(0.5, 0.5, 0.5), MATRIX = _mat, PARENT_NODE = self.scene_root, ENABLE_SHADOW = True, SHADOW_MAP_SIZE = 2048) # parameters TYPE (0 = sun light), NAME, COLOR, MATRIX, PARENT_NODE
    
    
