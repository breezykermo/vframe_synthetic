import sys
import importlib
import time

# sys.path.append('/home/fa-researcher/code/sandbox/vframe/vframe_synthetic/cli')
# ----------------------------------------------------------------------
from app.blender.operators import (
    preferences,
    render,
    fileio,
    camera,
    world,
    ground,
    static_system,
    particle_system,
)
from app.utils import file_utils, log_utils  # reload

importlib.reload(file_utils)
importlib.reload(log_utils)

# Create logger
log_utils.Logger.create()
log = log_utils.Logger.getLogger()


class Boss:
    def __init__(self, fp_cfg):

        cfg = file_utils.load_yml(fp_cfg)

        self.prefs = preferences.PreferenceManager(cfg)
        self.render = render.RenderManager(cfg)
        self.fileio = fileio.FileIOManager(cfg)
        self.camera = camera.CameraManager(cfg)
        self.world = world.WorldManager(cfg)
        self.ground = ground.GroundManager(cfg)
        self.object_system = static_system.StaticSystem(cfg)
        self.object_system = particle_system.ParticleSystemManager(cfg)
        self.fileio.annos_to_csv(self.object_system.get_annotation_meta())

    def unmask(self):
        self.render.set_engine_real()
        self.world.unmask()
        self.ground.unmask()
        self.object_system.unmask()

    def mask(self):
        self.render.set_engine_mask()
        self.world.mask()
        self.ground.mask()
        self.object_system.mask()

    def cleanup(self):
        """Relays cleanup command to sub managers"""
        self.prefs.cleanup()
        self.render.cleanup()
        self.fileio.cleanup()
        self.world.cleanup()
        self.ground.cleanup()
        self.camera.cleanup()
        self.object_system.clear_real()
        self.object_system.cleanup()
