<VirtualHost *>
	DocumentRoot GPP_SERVICE_DIR 
	ServerName GPP_HOSTNAME
	ErrorLog /var/log/apache2/error.log
 
        LogLevel warn
 
        CustomLog /var/log/apache2/access.log combined
        ServerSignature On
 
        # Allow directory listings so that people can browse the repository from their browser too
        <Directory "GPP_SERVICE_DIR">
                Options Indexes FollowSymLinks MultiViews
                DirectoryIndex index.html
                AllowOverride Options
                Order allow,deny
                allow from all
        </Directory>
 
        # Hide the conf/ directory for all repositories
        <Directory "GPP_SERVICE_DIR/*/conf">
                Order allow,deny
                Deny from all
                Satisfy all
        </Directory>
 
        # Hide the db/ directory for all repositories
        <Directory "GPP_SERVICE_DIR/*/db">
                Order allow,deny
                Deny from all
                Satisfy all
        </Directory>
</VirtualHost>
