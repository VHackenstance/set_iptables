# set_iptables
<h3>Set and flush the iptables chain with a script rather than manually.</h3>
<h4>When we are done testing be sure to remove the ip table rules.</h4>
<p>The basic premises is as follows</p>

<p>The script will accept the following arguments</p>
<ul>
    <li><b>-r [VALUE]:</b> --remote.  Set the tables to remote FORWARD, -r TRUE 
        <p>If you do not want this option leave black</p>
    </li>
    <li><b>-l [VALUE]:</b> --local.  Set the tables to local OUTPUT and INPUT, -l TRUE 
        <p>If you do not want this option leave black</p>
    </li>
    <li><b>-n [VALUE]:</b> --number.  Set the queue number
        <p>You cannot leave this field blank</p>
    </li>
    <li><b>-f [VALUE]:</b> --flush.  Flush/delete iptables chain, with -f TRUE
        <p>Leave blank if you do not want to </p>
    </li>
</ul>

<p>The script with automatically show you the chain by running: <b>sudo iptables -L -n</b></p>




<p><b>iptables --flush</b></p>
<p>And there will be zero rules under the chains (headings)</p>
<h4></h4>
<p><b></b>.  <b></b></p>


<p>Run script: <b>sudo python dns_spoof.py</b> in one terminal window.</p>
<p>Run ping: <b>ping -c 1 www.bing.com, </b>in another window.  You should get the following with your IP</p>
![ping_screen_shot.png](assets/ping_screen_shot.png)
<p>So, the target has requested to go to bing.com, but the 
IP we have returned is a spoofed IP and will take it somewhere
else.</p>
<h4>Kali Linux create webserver and your own index page on your IP</h4>
<p>When the user tries to navigate to www.bing.com they will be taken to our local page.</p>
<h3>To Test on a Remote VM.</h3>

