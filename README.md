# set_iptables
<h3>Set and flush the iptables chain with a script rather than manually.</h3>
<h4>When we are done testing be sure to remove the ip table rules.</h4>
<p>The basic premises is as follows</p>

<p>The script will accept the following arguments</p>
<ul>
    <li><b>-r [VALUE]:</b> --remote.  Set the tables to remote FORWARD, -r TRUE 
        <p>If you do not want this option leave black</p>
        <p>eg,$ sudo python set_iptables.py -r True -n 0</p>
    </li>
    <li><b>-l [VALUE]:</b> --local.  Set the tables to local OUTPUT and INPUT, -l TRUE 
        <p>If you do not want this option leave black</p>
        <p>eg,$ sudo python set_iptables.py -l True -n 0</p>
    </li>
    <li><b>-n [VALUE]:</b> --number.  Set the queue number
        <p>You cannot leave this field blank</p>
        <p>eg,$ sudo python set_iptables.py -l True -n 0</p>
    </li>
    <li><b>-f [VALUE]:</b> --flush.  Flush/delete iptables chain, with -f TRUE
        <p>Leave blank if you do not want to </p>
        <p>eg,$ sudo python set_iptables.py -f True</p>
    </li>
</ul>

<p>The script with automatically show you the chain by running: <b>sudo iptables -L -n</b></p>
<p>And there will be zero rules under the chains (headings)</p>

