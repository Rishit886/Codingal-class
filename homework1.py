import math

angle_degrees = float(input("Enter the angle in degrees: "))

angle_radians = math.radians(angle_degrees)

sin_val = math.sin(angle_radians)
cos_val = math.cos(angle_radians)
tan_val = math.tan(angle_radians)

print(f"Angle: {angle_degrees} degrees")
print(f"Sine: {sin_val:.4f}")
print(f"Cosine: {cos_val:.4f}")
print(f"Tangent: {tan_val:.4f}")