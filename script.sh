#!/bin/bash
title1="roscore"
title2="control node"
title3="vc node"
title4="arduino serial"
title5="voice control"
title6="initial sound_play"
title7="text2speech"


cmd1="roscore"
cmd2="rosrun control control"
cmd3="rosrun voice_control vcnode.py"
cmd4="rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=115200"
cmd5="roslaunch roboticarts_voice_control voice_control.launch" 
cmd6="rosrun sound_play soundplay_node.py"
cmd7="rosrun sound_play say.py 'Hello I'm Spark from the Innovation lab Sofrecom Tunisia'"

gnome-terminal --tab --title="$title1" --command="bash -c '$cmd1; $SHELL'" \
               --tab --title="$title2" --command="bash -c '$cmd2; $SHELL'" \
               --tab --title="$title3" --command="bash -c '$cmd3; $SHELL'" \
               --tab --title="$title4" --command="bash -c '$cmd4; $SHELL'" \
               --tab --title="$title5" --command="bash -c '$cmd5; $SHELL'" \
               --tab --title="$title5" --command="bash -c '$cmd6; $SHELL'" \
               --tab --title="$title7" --command="bash -c '$cmd7; $SHELL'"

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
               
