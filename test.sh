#!/bin/bash
title1="roscore"
title2="control node"
title3="vc node"
title4="arduino serial"

cmd1="roscore"
cmd2="rosrun control control"
cmd3="rosrun voice_control vcnode.py"
cmd4="rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=115200"

gnome-terminal --tab --title="$title1" --command="bash -c '$cmd1; $SHELL'" \
               --tab --title="$title2" --command="bash -c '$cmd2; $SHELL'" \
               --tab --title="$title3" --command="bash -c '$cmd3; $SHELL'" \
               --tab --title="$title4" --command="bash -c '$cmd4; $SHELL'"