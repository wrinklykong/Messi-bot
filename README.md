# Messi-bot
Soccer playing robot that locates a ball and scores a goal. Programmed on TETRIX Prizm and Raspberry Pi.

//////////////

Programmed for my Embedded Systems class during Fall 2022

Authors: John Jones, Adrian Carranza

Goals of this project: To achieve the goal of kicking the ball into the goal, we utilized the color sensor to
outline where the bounds are on the field, as well as highlight where the ball is on the
field. The robot could not enter the field-goal area or go out of bounds. In order to return
the ball, we turn the robot around the ball and push it forward. While the robot is
controlling the ball, we checked to make sure that it did not push it out of bounds; if the
robot pushed the ball out of bounds then we would rotate the robot to push the ball back
into the bounds.

Features: This project features precise turning with an on-board gyro-sensor and senses the boundaries of the area
with a color sensor.
