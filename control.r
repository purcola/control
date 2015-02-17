library("ggplot2")

control <- read.table("~/control/control.dat", header=TRUE, quote="\"")

pdf("control.pdf")

ggplot(control, aes(x=time, y=v, group=1)) + 
	geom_line() +
	xlab("Time (s)") +
	ylab("Speed (m/s)")

ggplot(control, aes(x=time, y=phi, group=1)) + 
	geom_line() +
	xlab("Time (s)") +
	ylab("Angle (rad)")

ggplot(control, aes(x=time, y=theta, group=1)) + 
	geom_line() +
	xlab("Time (s)") +
	ylab("Orientation (rad)")

ggplot(control, aes(x=x, y=y, group=1)) + 
	geom_line() +
	xlab("x (m)") +
	ylab("y (m)")
