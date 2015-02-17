import numpy

class Robot:
	def __init__(self, L, x=0.0, y=0.0, theta=0.0):
		self.L = L
		self.x = x
		self.y = y
		self.theta = theta

	def __repr__(self):
		return "{} {} {}".format(self.x, self.y, self.theta)

	def k(self, phi):
		return numpy.tan(phi)/self.L

	def move(self, v, phi, t): 
		k = self.k(phi)
		next_theta = self.theta + v * t * k
		if abs(phi) < 1e-3:
			self.x += v * t * numpy.cos(self.theta)
			self.y += v * t * numpy.sin(self.theta)
		else:
			self.x += (numpy.sin(next_theta) - numpy.sin(self.theta))/k
			self.y += -(numpy.cos(next_theta) - numpy.cos(self.theta))/k
		self.theta = next_theta

	def distance(self, point):
		return numpy.sqrt((self.x - point[0])**2 + (self.y - point[1])**2)

	def relative(self, point):
		dx = point[0] - self.x
		dy = point[1] - self.y

		return (dx * numpy.cos(self.theta) + dy * numpy.sin(self.theta),
				-dx * numpy.sin(self.theta) + dy * numpy.cos(self.theta))

			
def sin_control(robot, goal):
	d = robot.distance(goal)
	v = 1.0 - numpy.exp(-d)
	r_goal = robot.relative(goal)
	phi = r_goal[1]/d
	return v, phi

def tan_control(robot, goal):
	d = robot.distance(goal)
	v = 1.0 - numpy.exp(-d)
	r_goal = robot.relative(goal)
	phi = numpy.arctan2(r_goal[1], r_goal[0])
	return v, phi

def tan_L_control(robot, goal):
	d = robot.distance(goal)
	v = 1.0 - numpy.exp(-d)
	r_goal = robot.relative(goal)
	phi = numpy.arctan2(r_goal[1], r_goal[0] - robot.L)
	return v, phi


if __name__ == '__main__':
	L = 1.2
	max_phi = 0.4
	max_v = 1.0
	dt = 0.01

	x0 = 20.0
	y0 = -20.0
	theta0 = numpy.pi/2

	goal = (0.0, 0.0)
	control = sin_control

	eva = Robot(L, x0, y0, theta0)
	
	t = 0.0
	print "time v phi x y theta"	
	print t, 0.0, 0.0, eva
	while eva.distance(goal) > 1e-1:
		v, phi = control(eva, goal)
		v *= max_v
		phi *= max_phi
		eva.move(v, phi, dt)
		t += dt
		print t, v, phi, eva
	 
