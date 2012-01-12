<html>
	<body>
		<h1>Welcome to the veltzer.net APT repository</h1>
		<p>
		I hold various packages here for my own usage and you are welcome to use them too.
		My packages are for GPP_CODENAME/GPP_ID only. It may also work on debian but this is not guaranteed.
		If you want to use my repository you have to add it to your system as a source of packages.
		Here is how you do that.
		<ul>
			<li>
				Add my key to your apt-key keyring.
				My key id is <b>GPP_KEY</b>.
				You can get it from <a href="http://GPP_HOSTNAME/GPP_FOLDER/GPP_KEYNAME">here</a>.
				<pre style="font-weight:bold;">
wget http://GPP_HOSTNAME/GPP_FOLDER/GPP_KEYNAME
sudo apt-key add GPP_KEYNAME
				</pre>
			</li>
			<li>
				After doing this should see my key in your apt-key keyring using:
				<pre style="font-weight:bold;">
sudo apt-key list
				</pre>
			</li>
			<li>
				Add the next lines in your /etc/apt/sources.list file
				or add a file like /etc/apt/sources.list.d/veltzer.net.list containing them. You do have to
				call the file .list (I don't know why...).
				<pre style="font-weight:bold;">
# GPP_HOSTNAME APT repository
deb http://GPP_HOSTNAME/GPP_FOLDER GPP_CODENAME GPP_COMPONENT
deb-src http://GPP_HOSTNAME/GPP_FOLDER GPP_CODENAME GPP_COMPONENT
				</pre>
			</li>
			<li>
				Now you need to update your package repository:
				<pre style="font-weight:bold;">
sudo apt-get update
				</pre>
			</li>
			<li>
				You can now starting installing my packages. For example:
				<pre style="font-weight:bold;">
sudo apt-get install python-pdmt
				</pre>
			</li>
		</ul>
		</p>
		<p>
		Another option for using my packages is to just browse the <a href="http://veltzer.net/apt/pool">repository</a> and download the ones you want
		and then install them using <b>dpkg --install [package name]</b>.
		<h1>An uptodate list of packages in my repository:</h1>
		<?php
			function getDirectoryRec($path,$level,&$arr) {
				$ignore=array('.','..');
				if(!is_dir($path)) {
					return;
				}
				$dh=opendir($path);
				while(false!==($file=readdir($dh))) {
					if(in_array($file,$ignore)) {
						break;
					}
					$current=$path.'/'.$file;
					if(is_dir($current)) {
						getDirectoryRec($current,$level+1,$arr);
					}
					if(is_file($current)) {
						$arr[]=$file;
					}
				}
				closedir($dh);
			}
			function getDirectory($path='.',$level=0) {
				$arr=array();
				getDirectoryRec($path,$level,$arr);
				return $arr;
			}
			$arr=getDirectory($path='GPP_SERVICE_DIR/pool');
			echo '<ul>';
			foreach($arr as $x) {
				echo '<li>'.$x.'</li>';
			}
			echo '</ul>';
		?>
		<h1>Why should you want any of these packages ?</h1>
		<p>
		I once had a brand new 2.6.38 kernel made for ubuntu 10.10 (maverick).
		Yes - you could download this from ubuntu daily but they are compiling using a compiler that you do not have
		and cannot install and so you will not be able to install third party modules for your kernel. You <b>will</b>
		be able to do that with my kernels. I also have a -pae version of the kernel which will allow you to use 4G
		or more on 32 bit boards (ubuntu do not supply that either for 10.10). Update: If you upgraded to ubuntu 11.04 (natty)
		then you do not need my kernels and ubuntu do supply quite a reasonable -pae kernel for natty as well.
		You will still need the old firewire stack (see below). If you are in 11.10 then you don't need the firewire stack.
		If you are using a 37/38 kernel on a system and feel the urge for an old firewire stack I supply it <a href="https://github.com/veltzer/ieee1394">here</a>. Why would you want this? Well, many reasons but the best one is audio production (this is what I did it for). This you cannot find anywhere (or at least that is what google says).
		</p>
		<p>
		I have my new PDMT tool here. It is still very much alpha.
		</p>
		<p>
		I will add more packages in the future.
		</p>
		<p>
			Mark Veltzer, 2011
		</p>
	</body>
</html>
