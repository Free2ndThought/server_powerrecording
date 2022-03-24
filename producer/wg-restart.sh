#!/bin/bash

if ping -c 1 -W 2 '10.10.10.1' > /dev/null
    then
        echo "10.10.10.1 is reachable"
        exit 0
    else
        echo "10.10.10.1 is NOT-reachable"
        if nc -z -w 2 bladl-aal.th-deg.de 80 > /dev/null
            then
                echo 'bladl-aal.th-deg.de is reachable'
                systemctl restart wg-quick@wg0.service
            else
                echo 'bladl-aal.th-deg.de is NOT-reachable'
                exit 1
        fi
fi

