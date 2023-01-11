# CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpass';
# create database database_name with owner your_user_name
sudo -u postgres psql -c "CREATE USER sammy WITH ENCRYPTED PASSWORD 'root1234' ;"\
&& sudo -u postgres psql -c "create database test2 with owner sammy ;" \
&& sudo -u postgres psql -c "grant all privileges on database test2 to sammy ;" \
&& sudo -u postgres psql test2 < dump.sql \
&& sudo -u postgres psql -c "ALTER DATABASE test2 OWNER TO sammy ;"

