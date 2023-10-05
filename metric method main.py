import math

# Function to calculate the similarity ratio of two triangles
def triangle_similarity(triangle1, triangle2):
    # Calculate the ratios of corresponding sides
    side_ratio1 = triangle1[0] / triangle2[0]
    side_ratio2 = triangle1[1] / triangle2[1]
    side_ratio3 = triangle1[2] / triangle2[2]

    # Check if the ratios of corresponding sides are approximately equal
    side_ratios_equal = math.isclose(side_ratio1, side_ratio2) and math.isclose(side_ratio1, side_ratio3)

    # Check if the angles are approximately equal (in degrees)
    angle1_ratio = math.isclose(triangle1[3], triangle2[3], rel_tol=1e-5)
    angle2_ratio = math.isclose(triangle1[4], triangle2[4], rel_tol=1e-5)
    angle3_ratio = math.isclose(triangle1[5], triangle2[5], rel_tol=1e-5)

    # Determine if the triangles are geometrically similar
    if side_ratios_equal and angle1_ratio and angle2_ratio and angle3_ratio:
        return True
    else:
        return False

# Define two triangles as (side1, side2, side3, angle1, angle2, angle3) in degrees
triangle1 = (6, 8, 10, 90, 45, 45)
triangle2 = (3, 4, 5, 90, 45, 45)

# Check if the triangles are geometrically similar
if triangle_similarity(triangle1, triangle2):
    print("The triangles are geometrically similar.")
else:
    print("The triangles are not geometrically similar.")