# Title: Custom Marker with embedded Radioopaque Beads
# Description: Builds flat bottomed mocap marker ball (2 parts) with 
# radioopaque marker embedded (we used steel ball bearings).  
# Author: Scott Telfer
# Last updated: 2023_02_10


# =============================================================================

## Import modules
import rhinoscriptsyntax as rs


# =============================================================================

def Mocap_RA_marker(marker_radius = 4.5, bead_radius = 1.65, base_cut = 1):
    # check inputs
    if marker_radius < bead_radius:
        raise ValueError('marker_radius must be larger than bead radius')
    
    # Sphere
    sphere = rs.AddSphere((0, 0, marker_radius - base_cut), marker_radius)
    
    ## create flat bottom
    box = rs.AddBox([[50, 50, -100], [-50, 50, -100], [-50, -50, -100], [50, -50, -100], 
                     [50, 50, 0], [-50, 50, 0], [-50, -50, 0], [50, -50, 0]])
    box = rs.MoveObject(box, (0, 0, base_cut))
    marker = rs.BooleanDifference(sphere, box)
    
    # Split marker
    cyl1 = rs.AddCylinder(rs.WorldXYPlane(), (marker_radius * 2) + 5, 
                          (marker_radius * 2) + 5)
    cyl1 = rs.MoveObject(cyl1, [0, 0, marker_radius - base_cut])
    cyl2 = rs.CopyObject(cyl1, [0, 0, ((marker_radius * 2) + 5) * -1])
    top = rs.CopyObject(marker)
    bottom = rs.BooleanDifference(marker, cyl1)
    top = rs.BooleanDifference(top, cyl2)
    
    # Bead hole
    hole1 = rs.AddSphere((0, 0, marker_radius - base_cut), bead_radius)
    hole2 = rs.CopyObject(hole1)
    top = rs.BooleanDifference(top, hole1)
    bottom = rs.BooleanDifference(bottom, hole2)
    

Mocap_RA_marker(marker_radius = 4.5, bead_radius = 1.65, base_cut = 1)