#!/usr/bin/env, python
#-*-coding:-utf-8-*-

#, Sat, Feb, 21, 2015, 15:36:02, GMT-0500, (EST)
#, ---------------------------------------------
#, R/G/B, cubehelix, colour, scheme,
#
#, see, http://www.mrao.cam.ac.uk/~dag/CUBEHELIX/
#----------------------------------------------
#, see, Green, (2011),, BASI,, 39,, 289.,
#
#, start............:, 0.5
#, rotations........:, 1
#, hue..............:, 2.0
#, gamma............:, 0.8
#, number, of, levels.:, 255
#----------------------------------------------
#, Dave, Green:, dag@mrao.cam.ac.uk,
#----------------------------------------------
#, faction, and, R/G/B, values
#
def color_map(val):
  values = [ \
  [ 0.000, 0.000, 0.000, 0.000 ], \
  [ 0.004, 0.018, 0.008, 0.016 ], \
  [ 0.008, 0.033, 0.013, 0.028 ], \
  [ 0.012, 0.047, 0.018, 0.039 ], \
  [ 0.016, 0.060, 0.021, 0.049 ], \
  [ 0.020, 0.074, 0.025, 0.058 ], \
  [ 0.024, 0.087, 0.028, 0.067 ], \
  [ 0.028, 0.100, 0.031, 0.075 ], \
  [ 0.031, 0.113, 0.034, 0.082 ], \
  [ 0.035, 0.126, 0.037, 0.089 ], \
  [ 0.039, 0.139, 0.039, 0.096 ], \
  [ 0.043, 0.151, 0.042, 0.101 ], \
  [ 0.047, 0.164, 0.044, 0.107 ], \
  [ 0.051, 0.176, 0.047, 0.112 ], \
  [ 0.055, 0.188, 0.049, 0.117 ], \
  [ 0.059, 0.201, 0.052, 0.121 ], \
  [ 0.063, 0.213, 0.054, 0.124 ], \
  [ 0.067, 0.225, 0.057, 0.128 ], \
  [ 0.071, 0.237, 0.059, 0.130 ], \
  [ 0.075, 0.248, 0.062, 0.133 ], \
  [ 0.079, 0.260, 0.065, 0.135 ], \
  [ 0.083, 0.271, 0.067, 0.137 ], \
  [ 0.087, 0.283, 0.070, 0.138 ], \
  [ 0.091, 0.294, 0.073, 0.139 ], \
  [ 0.094, 0.305, 0.076, 0.140 ], \
  [ 0.098, 0.315, 0.079, 0.140 ], \
  [ 0.102, 0.326, 0.082, 0.140 ], \
  [ 0.106, 0.336, 0.085, 0.139 ], \
  [ 0.110, 0.346, 0.089, 0.139 ], \
  [ 0.114, 0.356, 0.092, 0.138 ], \
  [ 0.118, 0.366, 0.095, 0.137 ], \
  [ 0.122, 0.375, 0.099, 0.135 ], \
  [ 0.126, 0.384, 0.103, 0.133 ], \
  [ 0.130, 0.393, 0.107, 0.131 ], \
  [ 0.134, 0.402, 0.111, 0.129 ], \
  [ 0.138, 0.410, 0.115, 0.126 ], \
  [ 0.142, 0.418, 0.119, 0.123 ], \
  [ 0.146, 0.426, 0.124, 0.120 ], \
  [ 0.150, 0.434, 0.128, 0.117 ], \
  [ 0.154, 0.441, 0.133, 0.114 ], \
  [ 0.157, 0.448, 0.138, 0.110 ], \
  [ 0.161, 0.455, 0.143, 0.107 ], \
  [ 0.165, 0.461, 0.148, 0.103 ], \
  [ 0.169, 0.467, 0.153, 0.099 ], \
  [ 0.173, 0.473, 0.159, 0.095 ], \
  [ 0.177, 0.478, 0.164, 0.091 ], \
  [ 0.181, 0.484, 0.170, 0.086 ], \
  [ 0.185, 0.488, 0.176, 0.082 ], \
  [ 0.189, 0.493, 0.182, 0.077 ], \
  [ 0.193, 0.497, 0.188, 0.073 ], \
  [ 0.197, 0.501, 0.194, 0.068 ], \
  [ 0.201, 0.505, 0.201, 0.064 ], \
  [ 0.205, 0.508, 0.207, 0.059 ], \
  [ 0.209, 0.511, 0.214, 0.055 ], \
  [ 0.213, 0.513, 0.221, 0.050 ], \
  [ 0.217, 0.515, 0.228, 0.046 ], \
  [ 0.220, 0.517, 0.235, 0.041 ], \
  [ 0.224, 0.519, 0.242, 0.037 ], \
  [ 0.228, 0.520, 0.250, 0.032 ], \
  [ 0.232, 0.521, 0.257, 0.028 ], \
  [ 0.236, 0.522, 0.265, 0.024 ], \
  [ 0.240, 0.522, 0.272, 0.019 ], \
  [ 0.244, 0.522, 0.280, 0.015 ], \
  [ 0.248, 0.521, 0.288, 0.011 ], \
  [ 0.252, 0.521, 0.296, 0.008 ], \
  [ 0.256, 0.520, 0.305, 0.004 ], \
  [ 0.260, 0.519, 0.313, 0.001 ], \
  [ 0.264, 0.517, 0.321, 0.000 ], \
  [ 0.268, 0.515, 0.330, 0.000 ], \
  [ 0.272, 0.513, 0.338, 0.000 ], \
  [ 0.276, 0.511, 0.347, 0.000 ], \
  [ 0.280, 0.508, 0.356, 0.000 ], \
  [ 0.283, 0.505, 0.364, 0.000 ], \
  [ 0.287, 0.502, 0.373, 0.000 ], \
  [ 0.291, 0.498, 0.382, 0.000 ], \
  [ 0.295, 0.495, 0.391, 0.000 ], \
  [ 0.299, 0.491, 0.400, 0.000 ], \
  [ 0.303, 0.487, 0.409, 0.000 ], \
  [ 0.307, 0.482, 0.419, 0.000 ], \
  [ 0.311, 0.478, 0.428, 0.000 ], \
  [ 0.315, 0.473, 0.437, 0.000 ], \
  [ 0.319, 0.468, 0.446, 0.000 ], \
  [ 0.323, 0.463, 0.455, 0.000 ], \
  [ 0.327, 0.458, 0.465, 0.000 ], \
  [ 0.331, 0.452, 0.474, 0.000 ], \
  [ 0.335, 0.446, 0.483, 0.000 ], \
  [ 0.339, 0.441, 0.493, 0.000 ], \
  [ 0.343, 0.435, 0.502, 0.000 ], \
  [ 0.346, 0.429, 0.511, 0.000 ], \
  [ 0.350, 0.422, 0.520, 0.000 ], \
  [ 0.354, 0.416, 0.530, 0.000 ], \
  [ 0.358, 0.410, 0.539, 0.000 ], \
  [ 0.362, 0.403, 0.548, 0.000 ], \
  [ 0.366, 0.397, 0.557, 0.000 ], \
  [ 0.370, 0.390, 0.566, 0.004 ], \
  [ 0.374, 0.383, 0.575, 0.008 ], \
  [ 0.378, 0.377, 0.584, 0.013 ], \
  [ 0.382, 0.370, 0.593, 0.019 ], \
  [ 0.386, 0.363, 0.602, 0.024 ], \
  [ 0.390, 0.357, 0.611, 0.031 ], \
  [ 0.394, 0.350, 0.619, 0.037 ], \
  [ 0.398, 0.343, 0.628, 0.044 ], \
  [ 0.402, 0.336, 0.636, 0.051 ], \
  [ 0.406, 0.330, 0.645, 0.058 ], \
  [ 0.409, 0.323, 0.653, 0.066 ], \
  [ 0.413, 0.316, 0.661, 0.074 ], \
  [ 0.417, 0.310, 0.669, 0.083 ], \
  [ 0.421, 0.304, 0.677, 0.091 ], \
  [ 0.425, 0.297, 0.685, 0.100 ], \
  [ 0.429, 0.291, 0.693, 0.110 ], \
  [ 0.433, 0.285, 0.701, 0.120 ], \
  [ 0.437, 0.279, 0.708, 0.130 ], \
  [ 0.441, 0.273, 0.715, 0.140 ], \
  [ 0.445, 0.267, 0.723, 0.151 ], \
  [ 0.449, 0.262, 0.730, 0.162 ], \
  [ 0.453, 0.256, 0.737, 0.173 ], \
  [ 0.457, 0.251, 0.743, 0.184 ], \
  [ 0.461, 0.246, 0.750, 0.196 ], \
  [ 0.465, 0.241, 0.756, 0.208 ], \
  [ 0.469, 0.236, 0.763, 0.221 ], \
  [ 0.472, 0.232, 0.769, 0.233 ], \
  [ 0.476, 0.228, 0.775, 0.246 ], \
  [ 0.480, 0.224, 0.781, 0.259 ], \
  [ 0.484, 0.220, 0.786, 0.273 ], \
  [ 0.488, 0.216, 0.792, 0.286 ], \
  [ 0.492, 0.213, 0.797, 0.300 ], \
  [ 0.496, 0.210, 0.802, 0.314 ], \
  [ 0.500, 0.207, 0.807, 0.328 ], \
  [ 0.504, 0.204, 0.812, 0.342 ], \
  [ 0.508, 0.202, 0.816, 0.356 ], \
  [ 0.512, 0.200, 0.821, 0.371 ], \
  [ 0.516, 0.198, 0.825, 0.386 ], \
  [ 0.520, 0.197, 0.829, 0.401 ], \
  [ 0.524, 0.196, 0.833, 0.416 ], \
  [ 0.528, 0.195, 0.837, 0.431 ], \
  [ 0.531, 0.194, 0.840, 0.446 ], \
  [ 0.535, 0.194, 0.844, 0.461 ], \
  [ 0.539, 0.194, 0.847, 0.477 ], \
  [ 0.543, 0.195, 0.850, 0.492 ], \
  [ 0.547, 0.195, 0.852, 0.507 ], \
  [ 0.551, 0.196, 0.855, 0.523 ], \
  [ 0.555, 0.198, 0.858, 0.539 ], \
  [ 0.559, 0.199, 0.860, 0.554 ], \
  [ 0.563, 0.201, 0.862, 0.570 ], \
  [ 0.567, 0.203, 0.864, 0.585 ], \
  [ 0.571, 0.206, 0.866, 0.601 ], \
  [ 0.575, 0.209, 0.867, 0.616 ], \
  [ 0.579, 0.212, 0.869, 0.632 ], \
  [ 0.583, 0.216, 0.870, 0.647 ], \
  [ 0.587, 0.220, 0.871, 0.663 ], \
  [ 0.591, 0.224, 0.872, 0.678 ], \
  [ 0.594, 0.228, 0.873, 0.693 ], \
  [ 0.598, 0.233, 0.873, 0.708 ], \
  [ 0.602, 0.238, 0.874, 0.723 ], \
  [ 0.606, 0.244, 0.874, 0.738 ], \
  [ 0.610, 0.250, 0.874, 0.753 ], \
  [ 0.614, 0.256, 0.875, 0.767 ], \
  [ 0.618, 0.262, 0.874, 0.781 ], \
  [ 0.622, 0.269, 0.874, 0.796 ], \
  [ 0.626, 0.276, 0.874, 0.810 ], \
  [ 0.630, 0.283, 0.874, 0.824 ], \
  [ 0.634, 0.291, 0.873, 0.837 ], \
  [ 0.638, 0.298, 0.872, 0.851 ], \
  [ 0.642, 0.306, 0.872, 0.864 ], \
  [ 0.646, 0.315, 0.871, 0.877 ], \
  [ 0.650, 0.323, 0.870, 0.890 ], \
  [ 0.654, 0.332, 0.869, 0.902 ], \
  [ 0.657, 0.341, 0.868, 0.915 ], \
  [ 0.661, 0.351, 0.867, 0.927 ], \
  [ 0.665, 0.360, 0.865, 0.938 ], \
  [ 0.669, 0.370, 0.864, 0.950 ], \
  [ 0.673, 0.380, 0.863, 0.961 ], \
  [ 0.677, 0.390, 0.861, 0.972 ], \
  [ 0.681, 0.400, 0.860, 0.982 ], \
  [ 0.685, 0.411, 0.858, 0.993 ], \
  [ 0.689, 0.422, 0.857, 1.000 ], \
  [ 0.693, 0.433, 0.855, 1.000 ], \
  [ 0.697, 0.444, 0.853, 1.000 ], \
  [ 0.701, 0.455, 0.852, 1.000 ], \
  [ 0.705, 0.466, 0.850, 1.000 ], \
  [ 0.709, 0.478, 0.848, 1.000 ], \
  [ 0.713, 0.489, 0.847, 1.000 ], \
  [ 0.717, 0.501, 0.845, 1.000 ], \
  [ 0.720, 0.513, 0.844, 1.000 ], \
  [ 0.724, 0.525, 0.842, 1.000 ], \
  [ 0.728, 0.537, 0.840, 1.000 ], \
  [ 0.732, 0.549, 0.839, 1.000 ], \
  [ 0.736, 0.561, 0.837, 1.000 ], \
  [ 0.740, 0.573, 0.836, 1.000 ], \
  [ 0.744, 0.585, 0.834, 1.000 ], \
  [ 0.748, 0.597, 0.833, 1.000 ], \
  [ 0.752, 0.609, 0.831, 1.000 ], \
  [ 0.756, 0.621, 0.830, 1.000 ], \
  [ 0.760, 0.634, 0.829, 1.000 ], \
  [ 0.764, 0.646, 0.828, 1.000 ], \
  [ 0.768, 0.658, 0.826, 1.000 ], \
  [ 0.772, 0.670, 0.825, 1.000 ], \
  [ 0.776, 0.682, 0.824, 1.000 ], \
  [ 0.780, 0.694, 0.824, 1.000 ], \
  [ 0.783, 0.705, 0.823, 1.000 ], \
  [ 0.787, 0.717, 0.822, 1.000 ], \
  [ 0.791, 0.729, 0.822, 1.000 ], \
  [ 0.795, 0.740, 0.821, 1.000 ], \
  [ 0.799, 0.752, 0.821, 1.000 ], \
  [ 0.803, 0.763, 0.821, 1.000 ], \
  [ 0.807, 0.774, 0.821, 1.000 ], \
  [ 0.811, 0.785, 0.821, 1.000 ], \
  [ 0.815, 0.796, 0.821, 1.000 ], \
  [ 0.819, 0.806, 0.821, 1.000 ], \
  [ 0.823, 0.817, 0.822, 1.000 ], \
  [ 0.827, 0.827, 0.822, 1.000 ], \
  [ 0.831, 0.837, 0.823, 1.000 ], \
  [ 0.835, 0.847, 0.824, 1.000 ], \
  [ 0.839, 0.856, 0.825, 1.000 ], \
  [ 0.843, 0.866, 0.826, 1.000 ], \
  [ 0.846, 0.875, 0.828, 1.000 ], \
  [ 0.850, 0.884, 0.829, 1.000 ], \
  [ 0.854, 0.893, 0.831, 1.000 ], \
  [ 0.858, 0.901, 0.833, 1.000 ], \
  [ 0.862, 0.909, 0.835, 1.000 ], \
  [ 0.866, 0.917, 0.837, 1.000 ], \
  [ 0.870, 0.924, 0.839, 1.000 ], \
  [ 0.874, 0.932, 0.841, 1.000 ], \
  [ 0.878, 0.939, 0.844, 1.000 ], \
  [ 0.882, 0.945, 0.847, 1.000 ], \
  [ 0.886, 0.952, 0.850, 1.000 ], \
  [ 0.890, 0.958, 0.853, 1.000 ], \
  [ 0.894, 0.964, 0.856, 1.000 ], \
  [ 0.898, 0.969, 0.860, 1.000 ], \
  [ 0.902, 0.974, 0.863, 1.000 ], \
  [ 0.906, 0.979, 0.867, 1.000 ], \
  [ 0.909, 0.984, 0.871, 1.000 ], \
  [ 0.913, 0.988, 0.875, 1.000 ], \
  [ 0.917, 0.992, 0.880, 1.000 ], \
  [ 0.921, 0.995, 0.884, 1.000 ], \
  [ 0.925, 0.998, 0.889, 1.000 ], \
  [ 0.929, 1.000, 0.893, 1.000 ], \
  [ 0.933, 1.000, 0.898, 1.000 ], \
  [ 0.937, 1.000, 0.903, 1.000 ], \
  [ 0.941, 1.000, 0.908, 1.000 ], \
  [ 0.945, 1.000, 0.914, 1.000 ], \
  [ 0.949, 1.000, 0.919, 1.000 ], \
  [ 0.953, 1.000, 0.925, 1.000 ], \
  [ 0.957, 1.000, 0.930, 1.000 ], \
  [ 0.961, 1.000, 0.936, 1.000 ], \
  [ 0.965, 1.000, 0.942, 1.000 ], \
  [ 0.969, 1.000, 0.948, 1.000 ], \
  [ 0.972, 1.000, 0.954, 1.000 ], \
  [ 0.976, 1.000, 0.960, 1.000 ], \
  [ 0.980, 1.000, 0.967, 1.000 ], \
  [ 0.984, 1.000, 0.973, 1.000 ], \
  [ 0.988, 1.000, 0.980, 1.000 ], \
  [ 0.992, 1.000, 0.987, 1.000 ], \
  [ 0.996, 1.000, 0.993, 1.000 ], \
  [ 1.000, 1.000, 1.000, 1.000 ]]

  #print "values[",val,"] = ",values[val]
  return (values[val][3], values[val][2], values[val][1])

