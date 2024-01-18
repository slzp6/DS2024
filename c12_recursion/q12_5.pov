// q12-5.pov (v1.24.00)

#include "colors.inc"      

#declare pt1 = <cos(90.0*pi/180.0),sin(90.0*pi/180.0),0>;
#declare pt2 = <cos(210.0*pi/180.0),sin(210.0*pi/180.0),0>;
#declare pt3 = <cos(330.0*pi/180.0),sin(330.0*pi/180.0),0>;

#declare sierpinski = object{
  polygon { 4, pt1, pt2, pt3, pt1} 
  texture {
    pigment{Blue}
  } 
};                       

background { color White }

camera {         
  direction <-1,0,0>        
  right     x*image_width/image_height
  location  <0,0,3>
  look_at   <0,0,0>
}

light_source {
  <0,0,5> 
  color White
}

#declare counter=1;
#while(counter < 6)
  #declare sierpinski=union{
    object{sierpinski scale 0.5 translate 0.5*pt1}
    object{sierpinski scale 0.5 translate 0.5*pt2}
    object{sierpinski scale 0.5 translate 0.5*pt3}
}
  #declare counter=counter+1;
#end

sierpinski
