# Projet Finale ROS


### Partie 1 - URDF
L'urdf de la premiere partie se trouve dans le package udm_spider/urdf/mesh_part1.urdf
Pour le visualizer: roslaunch udm_spider visualize_urdf_part1.launch

L'urdf de la 2eme partie se trouve dans le package udm_spider/urdf/mesh.urdf
Pour le visualizer: roslaunch udm_spider visualize_urdf.launch


### Partie 2 - Moveit
Pour visualizer sur moveit: roslaunch udm_project_moveitconfig demo.launch

### Partie 3 - cinematique direct et indirect

Lancer d'abord le robot sur moveit: roslaunch udm_project_moveitconfig demo.launch
Dans un 2eme terminal:
Pour lancer le robot en cinematique direct: roslaunch udm_project_control direct.launch
Pour lancer le robot en cinematique indirect: roslaunch udm_project_control indirect.launch


### Partie 3 - Configurations

Changer le solver: J’ai remplacer par TRAC-IK Kinematics Solver

Pour l'installer, lancer: sudo apt-get install ros-melodic-trac-ik-kinematics-plugin

Dans le repertoire udm_project_moveitconfig/config, j’ai modifier kinematics_solver et kinematics_solver_search_resolution dans  le kinematics.yaml:

leg1:
  kinematics_solver: trac_ik_kinematics_plugin/TRAC_IKKinematicsPlugin
  kinematics_solver_search_resolution: 0.0001
  kinematics_solver_timeout: 0.005
leg2:
  kinematics_solver: trac_ik_kinematics_plugin/TRAC_IKKinematicsPlugin
  kinematics_solver_search_resolution: 0.0001
  kinematics_solver_timeout: 0.005
leg3:
  kinematics_solver: trac_ik_kinematics_plugin/TRAC_IKKinematicsPlugin
  kinematics_solver_search_resolution: 0.0001
  kinematics_solver_timeout: 0.005
leg4:
  kinematics_solver: trac_ik_kinematics_plugin/TRAC_IKKinematicsPlugin
  kinematics_solver_search_resolution: 0.0001
  kinematics_solver_timeout: 0.005
ee1:
  kinematics_solver: trac_ik_kinematics_plugin/TRAC_IKKinematicsPlugin
  kinematics_solver_search_resolution: 0.0001
  kinematics_solver_timeout: 0.005
ee2:
  kinematics_solver: trac_ik_kinematics_plugin/TRAC_IKKinematicsPlugin
  kinematics_solver_search_resolution: 0.0001
  kinematics_solver_timeout: 0.005
ee3:
  kinematics_solver: trac_ik_kinematics_plugin/TRAC_IKKinematicsPlugin
  kinematics_solver_search_resolution: 0.0001
  kinematics_solver_timeout: 0.005
ee4:
  kinematics_solver: trac_ik_kinematics_plugin/TRAC_IKKinematicsPlugin
  kinematics_solver_search_resolution: 0.0001
  kinematics_solver_timeout: 0.005

Dans joint_limits.yaml, j'ai changer les configurations pour le max_acceleration et max_velocity, et min_position:

joint_limits:
  leaf_link_1_joint:
    has_velocity_limits: true
    max_velocity: 2
    has_acceleration_limits: true
    max_acceleration: 0.4
    min_position: 0

Résultat: Quand j’ai lancer moveit, dans le tab joints, je vois que le minimum limite de leaf_link_1 est passer de -0.5 à 0 degré..


