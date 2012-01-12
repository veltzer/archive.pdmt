<VirtualHost *>
	DocumentRoot ${pdmt.config.ns_apt.p_abs_dir} 
	ServerName ${pdmt.config.ns_distrib.p_domain}
	ErrorLog /var/log/apache2/error.log
 
        LogLevel warn
 
        CustomLog /var/log/apache2/access.log combined
        ServerSignature On
 
        # Allow directory listings so that people can browse the repository from their browser too
        <Directory "${pdmt.config.ns_apt.p_abs_dir}">
                Options Indexes FollowSymLinks MultiViews
                DirectoryIndex index.html
                AllowOverride Options
                Order allow,deny
                allow from all
        </Directory>
 
        # Hide the conf/ directory for all repositories
        <Directory "${pdmt.config.ns_apt.p_abs_dir}/*/conf">
                Order allow,deny
                Deny from all
                Satisfy all
        </Directory>
 
        # Hide the db/ directory for all repositories
        <Directory "${pdmt.config.ns_apt.p_abs_dir}/*/db">
                Order allow,deny
                Deny from all
                Satisfy all
        </Directory>
</VirtualHost>
