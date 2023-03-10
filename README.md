# Motion_Capture_Equipment
 Just some bits and bobs that were developed while working in and around motion capture labs for the past few years

## Marker skeleton

Mesh files: marker_holder.stl

![Marker skeleton](https://github.com/Telfer/Motion_Capture_Equipment/blob/main/Marker_skeleton/marker_skeleton.jpg)

After forgeting to put a marker on for the n-th time, I bought a cheap anatomical skeleton, printed these little marker holders, and started using this set up as a way both to store the markers (pre-taped) and show the landmarks where they need to go. We just put the skeleton next to the participant and transfer the markers over one at a time. Usually easy to see if one has been missed. If you use multiple marker sets you could potentially color code or something. 

Designed for ~18mm (3/4 inch) tape. I used short (~12mm) M3 or M4 screws to attach the marker holders to the bones, along with longer ones to hang the marker plates from. Depending on your skeleton, you may also need to make extra plates to attach between bones and stop it swinging around.

## Marker plates

Mesh files: marker_plate_120-72-11.stl, marker_plate_120-80-9.stl, and marker_plate_120-60-6.stl

These do the job and are a lot less expensive than the ones I've seen commericially. The stl files are the plates I use for shank, thigh, and upper arm. These seem to work well but can be easily scaled to generate custom sizes. Be sure to print flat on the build plate for optimal strength. Both PETG and PLA have worked for me. I just superglue markers to each corner.

## Hindfoot wand

Mesh files: HeelPlate.stl, MarkerPlate.stl

Two-part marker plate designed to allow a shoe with a heel window cut in it to be taken on and off during a motion capture study (for example on different types of foot orthoses). Instructions on use in the pdf. Used in [Dose response effects of FOs](https://pubmed.ncbi.nlm.nih.gov/23631857/) and a few other papers.

## Markers with radio-opaque centers

Mesh files: Marker_RO_center_bottom.stl, Marker_RO_center_top.stl

We use these for biplane fluoroscopy studies that also require optical motion capture measurements. The marker is printed in 2 parts, a steel ball bearing is placed in the center and the 2 halves glued together. Finally, cover the marker in reflective 3M tape and you have a marker that can be measured using both biplane and standard motion capture systems. I've included stl files for a sample 9mm marker with for 3mm diameter center bead (we use these for feet), but there is also a quick python script for Rhino to generate custom markers with different hole and overall sizes.

![Marker under fluoroscopy](https://github.com/Telfer/Motion_Capture_Equipment/blob/main/Mocap_RO_Marker/bp_marker_image.jpg)
