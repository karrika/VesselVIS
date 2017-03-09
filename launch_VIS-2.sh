#!/bin/bash

gnome-terminal -x bash -c "cd VIS-2; python3 -m swagger_server | tee server.log"
