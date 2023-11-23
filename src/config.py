class config:
	SECRET_KEY = 'VO92s$QfV,^D+_c(-,0v$m'
	


class DevelopmentConfig(config):
	DEBUG=True
	MYSQL_HOST = '172.17.0.1'
	MYSQL_USER = 'root'
	MYSQL_PASSWORD = 'TDHHpnv5IJnRHus'
	MYSQL_DB = 'ProyectoSoftware'

config={
	'development':DevelopmentConfig
}