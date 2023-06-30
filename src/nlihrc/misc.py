"""Utility functions"""
from enum import Enum, unique

import numpy as np
from transforms3d._gohlketransforms import quaternion_matrix, euler_matrix, quaternion_from_matrix



CLIPORT_CMDS = [
    "put white box in brown box",
    "put white tape in brown box",
    "put red screwdriver in brown box",
    "put black lego in brown box",
    "put green lego in brown box",
    "pick a white box",
    "put bolt in brown box",
    "put bolt in brown box",
    "put cap in brown box",
    "put piston in brown box",
    "put all bolts in brown box",
    "put all push rods in brown box",
    "give bolt",
    "give push rod",
    "give rocker arm",
    "put bolt in red box",
    "put push rod in red box",
    "put rocker arm in red box",
]

class GoalStatus(Enum):
    PENDING = 0   # The goal has yet to be processed by the action server
    ACTIVE = 1   # The goal is currently being processed by the action server
    PREEMPTED = 2   # The goal received a cancel request after it started executing
                     #   and has since completed its execution (Terminal State)
    SUCCEEDED = 3   # The goal was achieved successfully by the action server (Terminal State)
    ABORTED = 4   # The goal was aborted during execution by the action server due
                  #    to some failure (Terminal State)
    REJECTED = 5   # The goal was rejected by the action server without being processed,
                   #    because the goal was unattainable or invalid (Terminal State)
    PREEMPTING = 6   # The goal received a cancel request after it started executing
                     #    and has not yet completed execution
    RECALLING = 7   # The goal received a cancel request before it started executing,
                    #    but the action server has not yet confirmed that the goal is canceled
    RECALLED = 8   # The goal received a cancel request before it started executing
                   #    and was successfully cancelled (Terminal State)
    LOST = 9   # An action client can determine that a goal is LOST. This should not be
                #    sent over the wire by an action server


class CommandMode(Enum):
    CONTINUOUS = 'continuous'
    STEP = 'step'
    MODEL = 'model'


class MoveDirection(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    FRONT = 'front'
    BACK = 'back'

@unique
class Command(Enum):
    START_ROBOT = 0
    STOP_ROBOT = 1
    SET_MODE_STEP = 2
    SET_MODE_CONTINUOUS = 3
    SET_MODE_MODEL = 4
    MOVE_UP = 5
    MOVE_DOWN = 6
    MOVE_LEFT = 7
    MOVE_RIGHT = 8
    MOVE_BACK = 9
    MOVE_FRONT = 10
    STOP_EXECUTION = 11
    STEP_SIZE = 12
    OPEN_TOOL = 13
    CLOSE_TOOL = 14
    ROTATE_TOOL = 15
    SAVE_POSITION = 16
    LOAD_POSITION = 17
    HOME = 18
    RECOVER = 19
    REPEAT = 20
    PUT_WHITE_BOX_IN_BROWN_BOX = 21
    PUT_WHITE_TAPE_IN_BROWN_BOX = 22
    PUT_RED_SCREWDRIVER_IN_BROWN_BOX = 23
    PUT_BLACK_LEGO_IN_BROWN_BOX = 24
    PUT_GREEN_LEGO_IN_BROWN_BOX = 25
    PICK_A_WHITE_BOX = 26
    PUT_BOLT_IN_BROWN_BOX = 27
    PUT_PUSH_ROD_IN_BROWN_BOX = 28
    PUT_ROCKER_ARM_IN_BROWN_BOX = 29
    PUT_PISTON_IN_BROWN_BOX = 30
    PUT_ALL_BOLTS_IN_BROWN_BOX = 31
    PUT_ALL_PUSH_RODS_IN_BROWN_BOX = 32
    GIVE_BOLT = 33
    GIVE_PUSH_ROD = 34
    GIVE_ROCKER_ARM = 35
    PUT_BOLT_IN_RED_BOX = 36
    PUT_PUSH_ROD_IN_RED_BOX = 37
    PUT_ROCKER_ARM_IN_RED_BOX = 38

class Controller(Enum):
    MOVEIT = "position_joint_trajectory_controller"
    SERVO = "cartesian_controller"

def get_relative_orientation(reference, yaw_rotation):
    """Get orientation relative to reference. Reference is in quaternion (WXYZ) while rotation is given in yaw degrees. Returned orientation is in quaternion (WXYZ)"""
    ref_matrix = quaternion_matrix(reference)
    rel_matrix = euler_matrix(0, 0, np.radians(yaw_rotation), 'sxyz')
    res_matrix = np.dot(rel_matrix, ref_matrix)
    
    return quaternion_from_matrix(res_matrix)
