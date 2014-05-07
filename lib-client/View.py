#!/usr/bin/python

## @file
# Contains class View.

# import avango-guacamole libraries
import avango
import avango.gua
import avango.script
from avango.script import field_has_changed

# import framework libraries
from ClientTrackingReader import *
import ClientPipelineValues


## Internal representation of a standard view on client side.
#
# Creates viewing setup and initializes a tracking sensor in order to avoid latency 
# due to distribution in the network. Refers to a StandardUser on server side.
class View(avango.script.Script):

  ### Fields ###
  sf_head_mat = avango.gua.SFMatrix4()
  sf_head_mat.value = avango.gua.make_identity_mat()


  ## Default constructor.
  def __init__(self):
    self.super(View).__init__()

  ## Custom constructor.
  # @param SCENEGRAPH Reference to the scenegraph to be displayed.
  # @param VIEWER Reference to the viewer to which the created pipeline will be appended to.
  # @param PLATFORM_ID The platform id on which this user is standing on.
  # @param SLOT_ID The identification number of the slot to display.
  # @param DISPLAY_INSTANCE An instance of Display to represent the values.
  # @param SCREEN_NUM The number of the screen node on the platform.
  # @param STEREO Boolean indicating if the view to be constructed is stereo or mono.
  def my_constructor(self, SCENEGRAPH, VIEWER, PLATFORM_ID, SLOT_ID, DISPLAY_INSTANCE, SCREEN_NUM, STEREO):

    ## @var SCENEGRAPH
    # Reference to the scenegraph.
    self.SCENEGRAPH = SCENEGRAPH

    ## @var platform_id
    # The platform id for which this client process is responsible for.
    self.platform_id = PLATFORM_ID

    ## @var slot_id
    # User ID of this user within his or her user group.
    self.slot_id = SLOT_ID

    ## @var screen_num
    # The number of the screen node on the platform.
    self.screen_num = SCREEN_NUM

    ## @var ONLY_TRANSLATION_UPDATE
    # In case this boolean is true, only the translation values will be locally updated from the tracking system.
    self.ONLY_TRANSLATION_UPDATE = False

    # retrieve the needed values from display
    self.display_values = DISPLAY_INSTANCE.register_view()

    # check if no more users allowed at this screen
    if not self.display_values:
      # TODO better handling of this case?
      print 'Error: no more users allowed at display "' + DISPLAY_INSTANCE.name + '"!'
      return

    self.window_size = avango.gua.Vec2ui(DISPLAY_INSTANCE.resolution[0], DISPLAY_INSTANCE.resolution[1]) 

    # create window
    self.window = avango.gua.nodes.Window()
    self.window.Display.value = self.display_values[0] # GPU-ID

    # create camera
    self.camera = avango.gua.nodes.Camera()
    self.camera.SceneGraph.value = SCENEGRAPH.Name.value

    # set render mask for camera
    _render_mask = "!do_not_display_group && !avatar_group_" + str(self.platform_id) + " && !couple_group_" + str(self.platform_id)

    for _i in range(0, 10):
      if _i != self.platform_id:
        _render_mask = _render_mask + " && !platform_group_" + str(_i)

    self.camera.RenderMask.value = _render_mask

    # create pipeline
    self.pipeline = avango.gua.nodes.Pipeline()
    self.pipeline.Enabled.value = True

    if STEREO:

      '''
        Stereo View
      '''

      self.camera.LeftScreen.value = "/net/platform_" + str(self.platform_id) + "/scale/screen_" + str(SCREEN_NUM)
      self.camera.RightScreen.value = "/net/platform_" + str(self.platform_id) + "/scale/screen_" + str(SCREEN_NUM)
      self.camera.LeftEye.value = "/net/platform_" + str(self.platform_id) + "/scale/s" + str(self.screen_num) + "_slot" + str(self.slot_id) + "/eyeL"
      self.camera.RightEye.value = "/net/platform_" + str(self.platform_id) + "/scale/s" + str(self.screen_num) + "_slot" + str(self.slot_id) + "/eyeR"

      self.window.Title.value = "Display: " + str(DISPLAY_INSTANCE.name) + "; Slot: " + str(self.slot_id)
      self.window.LeftResolution.value = self.window_size
      self.window.RightResolution.value = self.window_size

      if DISPLAY_INSTANCE.stereomode == "SIDE_BY_SIDE":
        self.window.Size.value = avango.gua.Vec2ui(self.window_size.x * 2, self.window_size.y)
        self.window.LeftPosition.value = avango.gua.Vec2ui(0, 0)
        self.window.RightPosition.value = avango.gua.Vec2ui(self.window_size.x, 0)
        self.window.StereoMode.value = avango.gua.StereoMode.SIDE_BY_SIDE
      
      elif DISPLAY_INSTANCE.stereomode == "ANAGLYPH_RED_CYAN" or DISPLAY_INSTANCE.stereomode == "CHECKERBOARD":
        self.window.Size.value = self.window_size
        self.window.LeftPosition.value = avango.gua.Vec2ui(0, 0)
        self.window.RightPosition.value = avango.gua.Vec2ui(0, 0)
        
        if DISPLAY_INSTANCE.stereomode == "ANAGLYPH_RED_CYAN":
          #self.window.StereoMode.value = avango.gua.StereoMode.ANAGLYPH_RED_GREEN
          self.window.StereoMode.value = avango.gua.StereoMode.ANAGLYPH_RED_CYAN

        elif DISPLAY_INSTANCE.stereomode == "CHECKERBOARD":
          self.window.StereoMode.value = avango.gua.StereoMode.CHECKERBOARD

      self.pipeline.EnableStereo.value = True
      self.pipeline.LeftResolution.value = self.window.LeftResolution.value
      self.pipeline.RightResolution.value = self.window.RightResolution.value

    else:

      '''
        Mono View
      '''

      self.camera.LeftScreen.value = "/net/platform_" + str(self.platform_id) + "/scale/screen_" + str(SCREEN_NUM)
      self.camera.LeftEye.value = "/net/platform_" + str(self.platform_id) + "/scale/s" + str(self.screen_num) + "_slot" + str(self.slot_id) + "/eye"

      self.window.Title.value = "Display: " + str(DISPLAY_INSTANCE.name) + "; Slot: " + str(self.slot_id)
      self.window.Size.value = self.window_size
      self.window.LeftResolution.value = self.window_size

      self.pipeline.EnableStereo.value = False
      self.pipeline.LeftResolution.value = self.window.LeftResolution.value


    self.pipeline.Window.value = self.window
    self.pipeline.Camera.value = self.camera


    '''
      General user settings
    '''

    # set nice pipeline values
    ClientPipelineValues.set_pipeline_values(self.pipeline)

    # add tracking reader to avoid latency
    self.init_local_tracking_override(None, avango.gua.make_identity_mat(), avango.gua.make_identity_mat())

    # set display string and warpmatrices as given by the display
    if len(self.display_values) > 1:
      self.set_warpmatrices(self.window, self.display_values[1])
    
    # append pipeline to the viewer
    VIEWER.Pipelines.value.append(self.pipeline)


  ### Functions ###
  
  ## Adds a tracking reader to the view instance.
  # @param TRACKING_TARGET_NAME The target name of the tracked object as chosen in daemon.
  # @param TRANSMITTER_OFFSET The transmitter offset to be applied.
  def init_local_tracking_override(self, TRACKING_TARGET_NAME, TRANSMITTER_OFFSET, NO_TRACKING_MAT):
    pass
    '''
    ## @var TRACKING_TARGET_NAME
    # The target name of the tracked object as chosen in daemon.
    self.TRACKING_TARGET_NAME = TRACKING_TARGET_NAME

    ## @var TRANSMITTER_OFFSET
    # The transmitter offset to be applied.
    self.TRANSMITTER_OFFSET = TRANSMITTER_OFFSET

    ## @var NO_TRACKING_MAT
    # Matrix to be applied if no headtracking of the Oculus Rift is available.
    self.NO_TRACKING_MAT = NO_TRACKING_MAT

    ## @var headtracking_reader
    # Instance of a child class of ClientTrackingReader to supply translation input.
    if self.TRACKING_TARGET_NAME != None:
      self.headtracking_reader = ClientTrackingTargetReader()
      self.headtracking_reader.my_constructor(TRACKING_TARGET_NAME)
      self.headtracking_reader.set_transmitter_offset(TRANSMITTER_OFFSET)
      self.headtracking_reader.set_receiver_offset(avango.gua.make_identity_mat())
    '''

  ## Sets the warp matrices if there is a correct amount of them.
  # @param WINDOW The window instance to apply the warp matrices to.
  # @param WARPMATRICES A list of warp matrices to be applied if there are enough of them.
  def set_warpmatrices(self, WINDOW, WARPMATRICES):
    
    if len(WARPMATRICES) == 6:
      WINDOW.WarpMatrixRedRight.value    = WARPMATRICES[0]
      WINDOW.WarpMatrixGreenRight.value  = WARPMATRICES[1]
      WINDOW.WarpMatrixBlueRight.value   = WARPMATRICES[2]
      
      WINDOW.WarpMatrixRedLeft.value     = WARPMATRICES[3]
      WINDOW.WarpMatrixGreenLeft.value   = WARPMATRICES[4]
      WINDOW.WarpMatrixBlueLeft.value    = WARPMATRICES[5]

  
  ### Callbacks ###

  ## Called whenever sf_head_mat changes.
  @field_has_changed(sf_head_mat)
  def sf_head_mat_changed(self):
    pass
    '''
    _node_to_update = self.SCENEGRAPH["/net/platform_" + str(self.platform_id) + "/scale/s" + str(self.screen_num) + "_slot" + str(self.slot_id)]

    # return when scenegraph is not yet present
    if _node_to_update == None:
      return

    _information_node = _node_to_update.Children.value[0]
    _tracking_target_name = _information_node.Name.value

    if _tracking_target_name == "None":
      _tracking_target_name = None

    # create new tracking reader when tracking target changes
    # TODO: when transmitter offset and no tracking mat change, propagate them in the scenegraph
    if _tracking_target_name != self.TRACKING_TARGET_NAME:
      self.init_local_tracking_override(_tracking_target_name, self.TRANSMITTER_OFFSET, self.NO_TRACKING_MAT)

    # when no value is to be updated, stop evaluation
    if self.TRACKING_TARGET_NAME == None:
      return
    
    # update slot node
    # TODO: Consider ONLY_TRANSLATION_UPDATE
    if _node_to_update != None:
      self.sf_head_mat.connect_from(self.headtracking_reader.sf_tracking_mat)
    '''

