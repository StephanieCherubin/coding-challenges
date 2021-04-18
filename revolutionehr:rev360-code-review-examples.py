# class ConversionAstigatism:
    # """
    # Conversion: To convert from minus-cylinder notation to plus-cylinder notation or from plus-cylinder to minus-cylinder, add the Cylinder power to the Sphere power, negate the Cylinder power, and rotate the Axis by 90 degrees (add or subtract 90 degrees to the Axis).
    
    # Example: +1.50 -1.25 x080 - the Cylinder power is negative, so this is a minus-cylinder refraction. The equivalent refraction in plus-cylinder notation would be +0.25 +1.25 x170.
    # """
    # def __init__(self, cylinder, sphere, axis):
    #     self.cylinder = cylinder
    #     self.sphere = sphere
    #     self.axis = axis
    
    # def convertCylinder(self, cylinder): 
    #     return [ -i for i in cylinder ]
import numpy as np
def convertCylinder(cylinder): 
    cylinder = np.array(cylinder) 
    return list(-cylinder)  
        
    # def convertSphere(sphere):
    #     pass
    
    # def convertAxis(axis):
    #     "Axis less than 001 or greater than 180"
    #     pass
    
# if __name__ == '__main__':
#     convert = ConversionAstigatism(1.50, -1.25, 80)
#     print(convert.convertCylinder(1.50))
    # print(convert.convertSphere())
    # print(convert.convertAxis())
print(convertCylinder(1))
# print(conversionAstigatism([1.50, -1.25, 80]))
# Output: [0.25,1.25,170]
# Output: [+0.25 +1.25 'x170']
