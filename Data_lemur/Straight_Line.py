def on_straight_line(points):
  if points[1][0] - points[0][0] == 0:
    slope1 = float('inf')  # Using infinity to represent the slope of a vertical line
  else:
    slope1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])

  # Check for vertical lines between points 1 and 2
  if points[2][0] - points[1][0] == 0:
    slope2 = float('inf')
  else:
    slope2 = (points[2][1] - points[1][1]) / (points[2][0] - points[1][0])

  # Check for vertical lines between points 2 and 0
  if points[2][0] - points[0][0] == 0:
    slope3 = float('inf')
  else:
    slope3 = (points[2][1] - points[0][1]) / (points[2][0] - points[0][0])
    
  if slope1 == slope2 == slope3:
    return True
  else:
    return False
  