#!/bin/bash
title1="launch_file"
title2="control node"
title3="vc node"
title4="arduino serial"

cmd1="source devel/setup.bash;roslaunch navstack_pub spark.launch"
cmd3="source devel/setup.bash;rosrun vel_trans translate.py"
cmd2="sudo chmod 666 /dev/ttyACM0;rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=115200"

gnome-terminal --tab --title="$title1" --command="bash -c '$cmd1; $SHELL'" \
               --tab --title="$title2" --command="bash -c '$cmd2; $SHELL'" \
               --tab --title="$title3" --command="bash -c '$cmd3; $SHELL'" 